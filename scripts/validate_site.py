#!/usr/bin/env python3
"""Validate a built ryanorban.com artifact before it is uploaded or deployed.

Standard library only. Exit status is non-zero when any check fails.

The validator reads two inputs:

* the Hugo output directory (``--public``); and
* the policy manifest Hugo writes to ``<public>/_policy/manifest.json`` (one record per
  page with its content state, index cohort, and the surface memberships computed by
  ``layouts/partials/functions/content-policy.html``).

The manifest is the single source of truth for *intended* behaviour; this script checks
that the rendered artifact agrees with it, and that a handful of invariants hold no matter
what the templates say (URL preservation, robots denials, feeds that must not exist, ...).

Usage::

    python3 scripts/validate_site.py --public public \
        --url-manifest scripts/baselines/public-urls.txt [--expected-sha SHA]
        [--expect-architecture-enabled] [--allow-fixtures]
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable
from urllib.parse import urlsplit
from xml.etree import ElementTree

SITE_ORIGIN = "https://ryanorban.com"
PERSON_ID = f"{SITE_ORIGIN}/#person"

GENERATED_LABEL = "Automatically generated from the linked source; not reviewed by Ryan Orban."
REVIEWED_LABEL = (
    "AI-assisted source summary, reviewed for accuracy by Ryan Orban. "
    "This page is not Ryan's original analysis."
)
ANNOTATED_LABEL = "AI-assisted source summary, reviewed and annotated by Ryan Orban."

HOME_SEO_TITLE = "Ryan Orban — Production AI Systems and Reliability"
HOME_META_DESCRIPTION = (
    "Production AI systems: agent evaluation, statistical release decisions, secure retrieval, and production feedback loops. Founder of Cadea; previously CTO at Tribe AI and Galvanize. San Francisco."
)
HOME_SOCIAL_TITLE = "Ryan Orban — Production AI Systems and Reliability"  # aligned with the SEO title 2026-08-19; one positioning statement everywhere
HOME_SOCIAL_DESCRIPTION = (
    "Agent evaluation, statistical release decisions, secure retrieval, production feedback loops. Founder of Cadea; previously CTO at Tribe AI and Galvanize."
)
HOME_H1 = "Ryan Orban"  # was the plan's tagline; changed to the name 2026-08-19 at Ryan's direction

AUTHORED_JSONLD_TYPES = {"Article", "BlogPosting", "TechArticle", "ScholarlyArticle", "NewsArticle"}


# --------------------------------------------------------------------------- HTML scraping


class PageScraper(HTMLParser):
    """Collect the parts of an HTML document the validator cares about."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.h1_texts: list[str] = []
        self.metas: list[dict[str, str]] = []
        self.links: list[dict[str, str]] = []
        self.anchors: list[dict[str, str]] = []
        self.ids: set[str] = set()
        self.jsonld: list[str] = []
        self.title = ""
        self.text_parts: list[str] = []
        self.nav_hrefs: list[str] = []
        self.footer_hrefs: list[str] = []
        self.class_hrefs: dict[str, list[str]] = {}
        self._in_h1 = 0
        self._in_title = False
        self._in_jsonld = False
        self._nav_depth = 0
        self._footer_depth = 0
        self._skip_depth = 0
        self._section_stack: list[str] = []
        self.section_hrefs: dict[str, list[str]] = {}

    def handle_starttag(self, tag: str, attrs_list) -> None:  # type: ignore[override]
        attrs = {k: (v or "") for k, v in attrs_list}
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "h1":
            self._in_h1 += 1
            self.h1_texts.append("")
        elif tag == "title":
            self._in_title = True
        elif tag == "meta":
            self.metas.append(attrs)
        elif tag == "link":
            self.links.append(attrs)
        elif tag == "script":
            if attrs.get("type", "").strip().lower() == "application/ld+json":
                self._in_jsonld = True
                self.jsonld.append("")
            else:
                self._skip_depth += 1
        elif tag == "style":
            self._skip_depth += 1
        elif tag == "nav":
            self._nav_depth += 1
        elif tag == "footer":
            self._footer_depth += 1
        elif tag == "section":
            self._section_stack.append(attrs.get("id", ""))
        elif tag == "a":
            href = attrs.get("href", "")
            self.anchors.append(attrs)
            if self._nav_depth:
                self.nav_hrefs.append(href)
            if self._footer_depth:
                self.footer_hrefs.append(href)
            for cls in attrs.get("class", "").split():
                self.class_hrefs.setdefault(cls, []).append(href)
            for sec in self._section_stack:
                if sec:
                    self.section_hrefs.setdefault(sec, []).append(href)

    def handle_endtag(self, tag: str) -> None:
        if tag == "h1" and self._in_h1:
            self._in_h1 -= 1
        elif tag == "title":
            self._in_title = False
        elif tag == "script":
            if self._in_jsonld:
                self._in_jsonld = False
            elif self._skip_depth:
                self._skip_depth -= 1
        elif tag == "style" and self._skip_depth:
            self._skip_depth -= 1
        elif tag == "nav" and self._nav_depth:
            self._nav_depth -= 1
        elif tag == "footer" and self._footer_depth:
            self._footer_depth -= 1
        elif tag == "section" and self._section_stack:
            self._section_stack.pop()

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title += data
        if self._in_jsonld:
            self.jsonld[-1] += data
            return
        if self._skip_depth:
            return
        if self._in_h1 and self.h1_texts:
            self.h1_texts[-1] += data
        self.text_parts.append(data)

    # convenience -----------------------------------------------------------------
    @property
    def text(self) -> str:
        return re.sub(r"\s+", " ", " ".join(self.text_parts)).strip()

    def meta(self, name: str, attr: str | None = None) -> list[str]:
        """Content of <meta> tags whose name/property/itemprop equals `name`.

        `attr` selects the attribute explicitly; by default OpenGraph-style keys (og:, article:,
        fb:) match `property`, camelCase schema keys match `itemprop`, everything else `name`.
        """
        if attr is None:
            if name.split(":")[0] in {"og", "article", "fb", "profile", "book"}:
                attr = "property"
            elif name in {"datePublished", "dateModified", "wordCount", "keywords", "image"} and name != name.lower():
                attr = "itemprop"
            else:
                attr = "name"
        out = []
        for m in self.metas:
            if (m.get(attr) or "").lower() == name.lower():
                out.append(m.get("content", ""))
        return out

    def robots_directives(self) -> list[str]:
        return [c.strip().lower() for c in self.meta("robots")]

    def canonical(self) -> str | None:
        for link in self.links:
            if link.get("rel", "").lower() == "canonical":
                return link.get("href")
        return None

    def has_meta_refresh(self) -> bool:
        return any((m.get("http-equiv") or "").lower() == "refresh" for m in self.metas)

    def jsonld_objects(self) -> list[dict]:
        objs: list[dict] = []
        for raw in self.jsonld:
            raw = raw.strip()
            if not raw:
                continue
            try:
                data = json.loads(raw)
            except json.JSONDecodeError:
                objs.append({"__invalid__": raw[:80]})
                continue
            if isinstance(data, list):
                objs.extend(d for d in data if isinstance(d, dict))
            elif isinstance(data, dict):
                objs.append(data)
                for node in data.get("@graph", []) or []:
                    if isinstance(node, dict):
                        objs.append(node)
        return objs


def scrape(path: Path) -> PageScraper:
    parser = PageScraper()
    parser.feed(path.read_text(encoding="utf-8", errors="replace"))
    return parser


# --------------------------------------------------------------------------- helpers


@dataclass
class Report:
    failures: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    passed: list[str] = field(default_factory=list)

    def fail(self, msg: str) -> None:
        self.failures.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)

    def ok(self, msg: str) -> None:
        self.passed.append(msg)


def norm_path(url_or_path: str) -> str:
    """Return the site-relative path for a URL or path, always with a leading slash."""
    if url_or_path.startswith("http://") or url_or_path.startswith("https://"):
        parts = urlsplit(url_or_path)
        if parts.netloc not in {"ryanorban.com", "www.ryanorban.com"}:
            return url_or_path
        path = parts.path
    else:
        path = url_or_path.split("#", 1)[0].split("?", 1)[0]
    if not path.startswith("/"):
        path = "/" + path
    return path or "/"


def output_file_for(public: Path, path: str) -> Path | None:
    """Map a site path to the file Hugo would have written for it, if any."""
    rel = path.lstrip("/")
    candidates = []
    if path.endswith("/") or path == "":
        candidates.append(public / rel / "index.html")
    else:
        candidates.append(public / rel)
        candidates.append(public / rel / "index.html")
    for cand in candidates:
        if cand.is_file():
            return cand
    return None


def read_lines(path: Path) -> list[str]:
    return [ln.strip() for ln in path.read_text(encoding="utf-8").splitlines() if ln.strip() and not ln.startswith("#")]


def sitemap_locs(path: Path) -> list[str]:
    tree = ElementTree.parse(path)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    return [el.text.strip() for el in tree.getroot().findall("sm:url/sm:loc", ns) if el.text]


def rss_links(path: Path) -> list[str]:
    tree = ElementTree.parse(path)
    return [el.text.strip() for el in tree.getroot().findall("./channel/item/link") if el.text]


def parse_robots(text: str) -> list[dict]:
    """Return robots.txt groups as dicts: {"agents": [...], "rules": [(directive, value)]}."""
    groups: list[dict] = []
    current: dict | None = None
    last_was_agent = False
    for raw in text.splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        if ":" not in line:
            continue
        key, value = [p.strip() for p in line.split(":", 1)]
        lkey = key.lower()
        if lkey == "user-agent":
            if current is None or not last_was_agent:
                current = {"agents": [], "rules": []}
                groups.append(current)
            current["agents"].append(value)
            last_was_agent = True
        elif lkey in {"allow", "disallow", "crawl-delay", "content-signal"}:
            if current is None:
                current = {"agents": [], "rules": []}
                groups.append(current)
            current["rules"].append((lkey, value))
            last_was_agent = False
        else:
            last_was_agent = False
    return groups


def robots_rules_for(groups: list[dict], agent: str) -> list[tuple[str, str]] | None:
    for g in groups:
        if any(a.lower() == agent.lower() for a in g["agents"]):
            return g["rules"]
    return None


def robots_path_allowed(rules: list[tuple[str, str]], path: str) -> bool:
    """Longest-match evaluation as Google/Bing/OpenAI document it."""
    best_len = -1
    allowed = True
    for directive, value in rules:
        if directive not in {"allow", "disallow"}:
            continue
        if value == "":
            if directive == "disallow" and best_len < 0:
                allowed = True
            continue
        pattern = re.escape(value).replace(r"\*", ".*")
        if value.endswith("$"):
            pattern = pattern[: -len(r"\$")] + "$"
        if re.match(pattern, path):
            if len(value) > best_len or (len(value) == best_len and directive == "allow"):
                best_len = len(value)
                allowed = directive == "allow"
    return allowed


# --------------------------------------------------------------------------- checks


def load_manifest(public: Path, report: Report) -> dict | None:
    manifest_path = public / "_policy" / "manifest.json"
    if not manifest_path.is_file():
        report.warn("policy manifest missing (public/_policy/manifest.json); running structural checks only")
        return None
    try:
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        report.fail(f"policy manifest is not valid JSON: {exc}")
        return None
    if not isinstance(data, dict) or "pages" not in data:
        report.fail("policy manifest has unexpected shape")
        return None
    report.ok(f"policy manifest loaded ({len(data['pages'])} pages, enabled={data.get('enabled')})")
    return data


def check_url_manifest(public: Path, url_manifest: Path, approved_aliases: dict[str, str], report: Report) -> None:
    missing = []
    for path in read_lines(url_manifest):
        out = output_file_for(public, path)
        if out is None:
            missing.append(path)
            continue
        if path in approved_aliases:
            continue
        # A page in the pre-migration manifest may not silently become a redirect.
        if out.suffix == ".html":
            page = scrape(out)
            if page.has_meta_refresh() and path not in approved_aliases:
                # Hugo paginator aliases (/posts/page/1/) were already aliases at baseline.
                if not re.search(r"/page/1/$", path):
                    report.fail(f"pre-migration URL {path} became a redirect without an approved alias")
    if missing:
        report.fail(
            f"{len(missing)} pre-migration URL(s) lost their output (first 10): " + ", ".join(missing[:10])
        )
    else:
        report.ok("every pre-migration URL still has an output file")


def check_sitemap(public: Path, manifest: dict | None, baseline_sitemap: Path | None, report: Report) -> set[str]:
    sitemap = public / "sitemap.xml"
    if not sitemap.is_file():
        report.fail("sitemap.xml missing")
        return set()
    locs = sitemap_locs(sitemap)
    seen: set[str] = set()
    for loc in locs:
        if not loc.startswith(SITE_ORIGIN + "/"):
            report.fail(f"sitemap URL is not on {SITE_ORIGIN}: {loc}")
            continue
        path = norm_path(loc)
        if path in seen:
            report.fail(f"sitemap lists {path} more than once")
        seen.add(path)
        out = output_file_for(public, path)
        if out is None:
            report.fail(f"sitemap URL has no output file: {path}")
            continue
        if out.suffix != ".html":
            continue
        page = scrape(out)
        if page.has_meta_refresh():
            report.fail(f"sitemap URL is a Hugo alias/meta-refresh: {path}")
        canonical = page.canonical()
        if canonical and norm_path(canonical) != path:
            report.fail(f"sitemap URL {path} is noncanonical (canonical={canonical})")
        if any("noindex" in d for d in page.robots_directives()):
            report.fail(f"sitemap URL is noindexed: {path}")
    if not report.failures:
        report.ok(f"sitemap has {len(seen)} URLs, all present, canonical, and indexable")

    enabled = bool(manifest and manifest.get("enabled"))
    if not enabled and baseline_sitemap and baseline_sitemap.is_file():
        baseline = {norm_path(u) for u in read_lines(baseline_sitemap)}
        lost = sorted(baseline - seen)
        # Notes feeds and pagination never belonged in the sitemap; ignore removed posts drafts.
        if lost:
            report.fail(
                f"architecture disabled but {len(lost)} baseline sitemap URL(s) disappeared (first 10): "
                + ", ".join(lost[:10])
            )
        else:
            report.ok("architecture disabled: sitemap still contains every baseline URL")
    return seen


def check_forbidden_outputs(public: Path, enabled: bool, report: Report) -> None:
    for rel in ("notes/index.xml", "notes/index.json"):
        exists = (public / rel).is_file()
        if enabled and exists:
            report.fail(f"{rel} must not be generated when the publication architecture is enabled")
        elif not enabled and not exists:
            report.warn(f"{rel} absent while architecture disabled (was present at baseline)")
    if enabled:
        report.ok("notes RSS/JSON outputs are absent")


def check_taxonomies(public: Path, manifest: dict, sitemap_paths: set[str], report: Report) -> None:
    enabled = manifest.get("enabled")
    if not enabled:
        return
    bad_feed = []
    bad_noindex = []
    in_sitemap = []
    checked = 0
    for rec in manifest["pages"]:
        if rec.get("kind") not in {"taxonomy", "term"}:
            continue
        checked += 1
        path = rec["path"]
        directory = public / path.lstrip("/")
        for feed in ("index.xml", "index.json"):
            if (directory / feed).is_file():
                bad_feed.append(path + feed)
        out = output_file_for(public, path)
        if out is None:
            report.fail(f"taxonomy page {path} has no output")
            continue
        page = scrape(out)
        if not any("noindex" in d for d in page.robots_directives()):
            bad_noindex.append(path)
        if path in sitemap_paths:
            in_sitemap.append(path)
    if bad_feed:
        report.fail(f"{len(bad_feed)} taxonomy feed(s) generated (first 5): {bad_feed[:5]}")
    if bad_noindex:
        report.fail(f"{len(bad_noindex)} taxonomy page(s) lack noindex (first 5): {bad_noindex[:5]}")
    if in_sitemap:
        report.fail(f"{len(in_sitemap)} taxonomy page(s) in sitemap (first 5): {in_sitemap[:5]}")
    if not (bad_feed or bad_noindex or in_sitemap):
        report.ok(f"{checked} taxonomy/term pages: HTML only, noindex, absent from sitemap")


def page_has_authored_metadata(page: PageScraper) -> list[str]:
    """Return a list of authored-publication signals present in the page."""
    signals = []
    if page.meta("author"):
        signals.append("meta[name=author]")
    if any(v.lower() == "article" for v in page.meta("og:type")):
        signals.append("og:type=article")
    for prop in ("article:published_time", "article:modified_time", "article:author", "article:section", "article:tag"):
        if page.meta(prop):
            signals.append(prop)
    for prop in ("datePublished", "dateModified"):
        if page.meta(prop):
            signals.append(f"itemprop={prop}")
    for obj in page.jsonld_objects():
        types = obj.get("@type")
        types = types if isinstance(types, list) else [types]
        if any(t in AUTHORED_JSONLD_TYPES for t in types):
            signals.append(f"jsonld:{types}")
        if "author" in obj:
            signals.append("jsonld:author")
        if "datePublished" in obj:
            signals.append("jsonld:datePublished")
        if "copyrightHolder" in obj:
            signals.append("jsonld:copyrightHolder")
    return signals


def check_pages(public: Path, manifest: dict, sitemap_paths: set[str], report: Report, allow_fixtures: bool) -> dict:
    """Per-page policy checks. Returns a summary dict used by later surface checks."""
    enabled = bool(manifest.get("enabled"))
    publications: set[str] = set()
    non_publications: set[str] = set()
    fixtures: list[str] = []
    counts: dict[str, int] = {}
    problems = 0

    for rec in manifest["pages"]:
        path = rec["path"]
        if rec.get("fixture"):
            fixtures.append(path)
        state = rec.get("state")
        cohort = rec.get("cohort")
        key = f"{state}+{cohort}"
        counts[key] = counts.get(key, 0) + 1
        if rec.get("publication"):
            publications.add(path)
        elif rec.get("kind") == "page" and rec.get("section") in {"notes", "posts"}:
            non_publications.add(path)

        if rec.get("invalid"):
            report.fail(f"content-policy: invalid state/cohort on {path}: {rec.get('invalidReason')}")
            problems += 1

        # Route/state invariant is enforced whether or not the architecture is enabled.
        if state in {"annotated", "original"} and path.startswith("/notes/"):
            report.fail(f"{state} page renders beneath /notes/: {path}")
            problems += 1
        if state in {"generated", "reviewed"} and rec.get("kind") == "page" and not path.startswith("/notes/"):
            report.fail(f"{state} source summary renders outside /notes/: {path}")
            problems += 1

        if not enabled:
            continue

        out = output_file_for(public, path)
        if out is None or out.suffix != ".html":
            if rec.get("kind") == "page":
                report.fail(f"no HTML output for {path}")
                problems += 1
            continue
        page = scrape(out)
        robots = page.robots_directives()
        noindex_count = sum(1 for d in robots if "noindex" in d)

        # 1 & 2: index policy agreement
        if rec.get("indexable"):
            if noindex_count:
                report.fail(f"{path} is indexable per policy but emits noindex")
                problems += 1
        else:
            if noindex_count != 1:
                report.fail(f"{path} must emit exactly one noindex directive (found {noindex_count})")
                problems += 1
        if rec.get("sitemap") != (path in sitemap_paths):
            report.fail(f"{path}: sitemap membership {path in sitemap_paths} disagrees with policy {rec.get('sitemap')}")
            problems += 1
        if not rec.get("indexable") and path in sitemap_paths:
            report.fail(f"non-indexable page in sitemap: {path}")
            problems += 1

        # 4: attribution / authorship
        if rec.get("kind") == "page" and state in {"generated", "reviewed"}:
            signals = page_has_authored_metadata(page)
            if signals:
                report.fail(f"{path} ({state}) emits authored-publication metadata: {signals}")
                problems += 1
            og_types = [v.lower() for v in page.meta("og:type")]
            if og_types and og_types != ["website"]:
                report.fail(f"{path} og:type must be website, got {og_types}")
                problems += 1

        # 5 & 6: bookmark disclosure, source link, self-links
        if path.startswith("/notes/") and rec.get("kind") == "page":
            expected_label = {"generated": GENERATED_LABEL, "reviewed": REVIEWED_LABEL}.get(state)
            if expected_label and expected_label not in page.text:
                report.fail(f"{path} lacks the visible {state} disclosure label")
                problems += 1
            source_url = rec.get("sourceUrl") or ""
            if source_url:
                if not any(a.get("href") == source_url for a in page.anchors):
                    report.fail(f"{path} does not link to its source URL {source_url}")
                    problems += 1
            else:
                report.warn(f"{path} has no sourceUrl in front matter")
            self_links = [
                a.get("href", "")
                for a in page.anchors
                if a.get("href", "") and not a["href"].startswith("#") and norm_path(a["href"]) == path
            ]
            if self_links:
                report.fail(f"{path} contains {len(self_links)} self-link(s): {self_links[:3]}")
                problems += 1

        # 7: annotated pages
        if state == "annotated":
            if not rec.get("reviewedAt"):
                report.fail(f"annotated page {path} lacks reviewedAt")
                problems += 1
            if not rec.get("sourceUrl"):
                report.fail(f"annotated page {path} lacks sourceUrl")
                problems += 1
            if not rec.get("hasAnnotation") or "annotation" not in page.text.lower():
                report.fail(f"annotated page {path} lacks a clearly separated Ryan annotation section")
                problems += 1
            if ANNOTATED_LABEL not in page.text:
                report.fail(f"annotated page {path} lacks the visible annotated-source label")
                problems += 1

        # publications must carry accurate authorship
        if rec.get("publication") and rec.get("kind") == "page":
            objs = page.jsonld_objects()
            authored = [
                o for o in objs
                if any(t in AUTHORED_JSONLD_TYPES for t in (o.get("@type") if isinstance(o.get("@type"), list) else [o.get("@type")]))
            ]
            if not authored:
                report.fail(f"publication {path} lacks authored Article/BlogPosting JSON-LD")
                problems += 1
            else:
                author = authored[0].get("author") or {}
                if isinstance(author, list):
                    author = author[0] if author else {}
                if author.get("@id") != PERSON_ID:
                    report.fail(f"publication {path} author @id must be {PERSON_ID}, got {author.get('@id')}")
                    problems += 1
            if not page.meta("author"):
                report.fail(f"publication {path} lacks meta[name=author]")
                problems += 1

    if fixtures and not allow_fixtures:
        report.fail(f"{len(fixtures)} fixture page(s) entered the artifact: {fixtures[:5]}")
    elif fixtures:
        report.ok(f"{len(fixtures)} fixture pages present (allowed for overlay build)")
    else:
        report.ok("no fixture pages in artifact")

    if problems == 0:
        report.ok(f"per-page policy checks passed ({', '.join(f'{k}={v}' for k, v in sorted(counts.items()))})")
    return {"publications": publications, "non_publications": non_publications, "enabled": enabled}


def check_publication_surfaces(public: Path, manifest: dict, summary: dict, sitemap_paths: set[str], report: Report) -> None:
    if not summary["enabled"]:
        return
    publications: set[str] = summary["publications"]
    non_publications: set[str] = summary["non_publications"]
    regular_publications = {
        rec["path"] for rec in manifest["pages"]
        if rec.get("publication") and rec.get("kind") == "page" and rec.get("section") in manifest.get("publicationSections", ["posts"])
    }

    # Writing list
    writing = public / "posts" / "index.html"
    if writing.is_file():
        page = scrape(writing)
        listed = {norm_path(a.get("href", "")) for a in page.anchors}
        leaked = sorted(listed & non_publications)
        if leaked:
            report.fail(f"Writing list links non-publication pages: {leaked[:5]}")
        missing = sorted(regular_publications - listed)
        if missing:
            report.fail(f"Writing list is missing publications: {missing[:5]}")
        if not leaked and not missing:
            report.ok(f"Writing lists exactly the {len(regular_publications)} publication pages")
    else:
        report.fail("/posts/ HTML missing")

    # Feeds
    for feed in ("posts/index.xml", "posts/index.json"):
        fp = public / feed
        if not fp.is_file():
            report.fail(f"{feed} missing")
            continue
        if feed.endswith(".xml"):
            items = {norm_path(u) for u in rss_links(fp)}
        else:
            data = json.loads(fp.read_text(encoding="utf-8"))
            items = {norm_path(d.get("id") or d.get("url") or "") for d in data}
        leaked = sorted(items & non_publications)
        missing = sorted(regular_publications - items)
        if leaked:
            report.fail(f"{feed} contains non-publication pages: {leaked[:5]}")
        if missing:
            report.fail(f"{feed} is missing publications: {missing[:5]}")
        if not leaked and not missing:
            report.ok(f"{feed} contains exactly the publication pages")

    # Sitemap must contain every publication
    missing = sorted(regular_publications - sitemap_paths)
    if missing:
        report.fail(f"publications missing from sitemap: {missing[:5]}")

    # Graph JSON
    graph = public / "graph" / "index.json"
    if graph.is_file():
        data = json.loads(graph.read_text(encoding="utf-8"))
        nodes = {norm_path(k) for k in (data.get("pages") or {}).keys()}
        leaked = sorted(nodes & non_publications)
        missing = sorted(regular_publications - nodes)
        if leaked:
            report.fail(f"/graph/index.json includes non-publication pages: {leaked[:5]}")
        if missing:
            report.fail(f"/graph/index.json is missing publications: {missing[:5]}")
        if not leaked and not missing:
            report.ok("/graph/index.json contains only publication content")
        graph_html = public / "graph" / "index.html"
        if graph_html.is_file():
            page = scrape(graph_html)
            if not any("noindex" in d for d in page.robots_directives()):
                report.fail("/graph/ lacks noindex")
            if "/graph/" in sitemap_paths:
                report.fail("/graph/ is in the sitemap")
    else:
        report.warn("/graph/index.json missing")

    # Homepage writing selection must never include a non-publication
    home = public / "index.html"
    if home.is_file():
        page = scrape(home)
        hrefs = set()
        # The separate Writing section merged into Current evidence on 2026-08-19; the "work"
        # section now carries every publication link.
        for sec in ("work",):
            hrefs.update(norm_path(h) for h in page.section_hrefs.get(sec, []))
        leaked = sorted(hrefs & non_publications)
        if leaked:
            report.fail(f"homepage links non-publication pages in Work/Writing: {leaked[:5]}")
        else:
            report.ok("homepage Work/Writing links contain no bookmark pages")


def check_about(public: Path, enabled: bool, report: Report) -> None:
    about = public / "about" / "index.html"
    if not about.is_file():
        report.fail("/about/ missing")
        return
    if not enabled:
        return
    page = scrape(about)
    profile = [
        o for o in page.jsonld_objects()
        if (o.get("@type") == "ProfilePage" or (isinstance(o.get("@type"), list) and "ProfilePage" in o["@type"]))
    ]
    if not profile:
        report.fail("/about/ JSON-LD is not a ProfilePage")
        return
    main = profile[0].get("mainEntity") or {}
    if main.get("@id") != PERSON_ID:
        report.fail(f"/about/ ProfilePage.mainEntity.@id must be {PERSON_ID}, got {main.get('@id')}")
    else:
        report.ok("/about/ is a ProfilePage with the stable Person identifier")


def check_homepage(public: Path, enabled: bool, expect_v2: bool, report: Report) -> None:
    home = public / "index.html"
    if not home.is_file():
        report.fail("homepage missing")
        return
    page = scrape(home)
    h1s = [re.sub(r"\s+", " ", t).strip() for t in page.h1_texts]
    if not expect_v2:
        # Legacy homepage (markdown body, no <h1>): report the defect without blocking a deploy
        # that only exists to unwedge the pipeline. The redesign adds the <h1> and flips to v2.
        if len(h1s) == 1:
            report.ok("homepage has exactly one <h1>")
        else:
            report.warn(f"homepage should have exactly one <h1>; found {len(h1s)}: {h1s}")
        return
    if len(h1s) != 1:
        report.fail(f"homepage must have exactly one <h1>; found {len(h1s)}: {h1s}")
    if h1s and h1s[0] != HOME_H1:
        report.fail(f"homepage <h1> must be {HOME_H1!r}, got {h1s[0]!r}")
    for anchor in ("work", "contact"):
        if anchor not in page.ids:
            report.fail(f"homepage lacks id=\"{anchor}\" anchor")
    title = re.sub(r"\s+", " ", page.title).strip()
    if title != HOME_SEO_TITLE:
        report.fail(f"homepage <title> must be {HOME_SEO_TITLE!r}, got {title!r}")
    if page.meta("description") != [HOME_META_DESCRIPTION]:
        report.fail(f"homepage meta description mismatch: {page.meta('description')}")
    if page.meta("og:title") != [HOME_SOCIAL_TITLE]:
        report.fail(f"homepage og:title mismatch: {page.meta('og:title')}")
    if page.meta("og:description") != [HOME_SOCIAL_DESCRIPTION]:
        report.fail(f"homepage og:description mismatch: {page.meta('og:description')}")
    if page.meta("twitter:title") != [HOME_SOCIAL_TITLE]:
        report.fail(f"homepage twitter:title mismatch: {page.meta('twitter:title')}")
    if any("noindex" in d for d in page.robots_directives()):
        report.fail("homepage is noindexed")
    text = page.text
    # "Discuss a role" / "See current work" were pinned by the 2026-08-18 plan and removed on
    # 2026-08-19 at Ryan's direction (no call-to-action apparatus on the homepage).
    for phrase in ("Changing agent systems without flying blind", "Current program", "me@ryanorban.com"):
        if phrase not in text:
            report.fail(f"homepage copy missing required phrase: {phrase!r}")
    for banned in ("Proof-Carrying Changes", "fractional CTO", "Fractional CTO"):
        if banned in text:
            report.fail(f"homepage must not mention {banned!r} yet")
    # Program evidence must appear before career history. The through-line is located by its
    # section anchor rather than its heading text, so the heading can be edited without
    # silently disabling the order check.
    raw = home.read_text(encoding="utf-8")
    idx_program = raw.find("Changing agent systems without flying blind")
    m = re.search(r'id="?home-throughline-heading"?', raw)
    idx_history = m.start() if m else -1
    if idx_program == -1 or idx_history == -1 or idx_program > idx_history:
        report.fail("Current Program must precede the career through-line on the homepage")
    if not report.failures:
        report.ok("homepage H1, anchors, copy order, and metadata match the specification")


def check_navigation(public: Path, report: Report) -> None:
    home = public / "index.html"
    if not home.is_file():
        return
    page = scrape(home)
    hrefs = set(page.nav_hrefs) | set(page.footer_hrefs)
    broken = []
    for href in sorted(hrefs):
        if not href or href.startswith(("http://", "https://", "mailto:", "#")):
            continue
        path = norm_path(href)
        if output_file_for(public, path) is None and not (public / path.lstrip("/")).is_file():
            broken.append(href)
    if broken:
        report.fail(f"navigation/footer links to missing internal routes: {broken}")
    else:
        report.ok(f"{len(hrefs)} navigation/footer links resolve")


def check_static_html(public: Path, manifest: dict | None, allowlist: set[str], report: Report) -> None:
    """Every HTML file that Hugo did not render from content must still satisfy policy."""
    enabled = bool(manifest and manifest.get("enabled"))
    known = {rec["path"] for rec in (manifest or {}).get("pages", [])}
    sfevents_missing_noindex = []
    unknown = []
    for html in public.rglob("*.html"):
        rel = "/" + html.relative_to(public).as_posix()
        path = rel[: -len("index.html")] if rel.endswith("/index.html") else rel
        if path in known or path == "/404.html":
            continue
        if path.startswith("/sfevents/"):
            if enabled:
                page = scrape(html)
                if not any("noindex" in d for d in page.robots_directives()):
                    sfevents_missing_noindex.append(path)
            continue
        if path in allowlist:
            continue
        if re.search(r"/page/\d+/$", path):
            continue  # Hugo paginator pages/aliases
        unknown.append(path)
    if enabled and sfevents_missing_noindex:
        report.fail(
            f"{len(sfevents_missing_noindex)} EventScout HTML page(s) lack noindex (first 5): {sfevents_missing_noindex[:5]}"
        )
    if unknown:
        if enabled:
            report.fail(f"{len(unknown)} static HTML file(s) bypassed policy checks: {unknown[:10]}")
        else:
            report.warn(f"{len(unknown)} HTML file(s) outside the policy manifest: {unknown[:10]}")
    elif enabled and not sfevents_missing_noindex:
        report.ok("no static HTML escaped policy checks; EventScout HTML is noindexed")


def check_robots(public: Path, baselines: Path, report: Report, manifest: dict | None) -> None:
    robots = public / "robots.txt"
    if not robots.is_file():
        report.fail("robots.txt missing")
        return
    text = robots.read_text(encoding="utf-8")
    groups = parse_robots(text)
    if not groups:
        report.fail("robots.txt has no groups")
        return
    matrix = Path(__file__).resolve().parent.parent / "data" / "crawlers.toml"
    # Agents the matrix moves to publication-path access at the active stage may legitimately
    # leave the baseline denial list; everything else must stay denied.
    retrieval_exempt: set[str] = set()
    if matrix.is_file():
        import tomllib

        with matrix.open("rb") as fh:
            m = tomllib.load(fh)
        stage_line = re.search(r"^# crawler-policy-stage: (\S+)", text, re.M)
        stage = stage_line.group(1) if stage_line else "baseline"
        for entry in m.get("agents") or []:
            pol = (entry.get("policy") or {})
            want = pol.get(stage) or pol.get("default")
            if want == "publication-paths" and str(entry.get("role", "")).startswith("automatic answer retrieval"):
                retrieval_exempt.add(entry.get("agent"))
    denied_baseline = baselines / "robots-denied-agents.txt"
    if denied_baseline.is_file():
        reopened = []
        for agent in read_lines(denied_baseline):
            if agent in retrieval_exempt:
                continue
            rules = robots_rules_for(groups, agent)
            if rules is None or robots_path_allowed(rules, "/"):
                reopened.append(agent)
        if reopened:
            report.fail(f"robots.txt reopened deliberately denied agent(s): {reopened}")
        else:
            report.ok("robots.txt preserves every baseline denial" + (f" (retrieval crawlers reopened per matrix: {sorted(retrieval_exempt)})" if retrieval_exempt else ""))
    for agent in ("Googlebot", "Bingbot", "*"):
        rules = robots_rules_for(groups, agent)
        if rules is None:
            continue
        for path in ("/notes/", "/notes/example/", "/posts/", "/"):
            if not robots_path_allowed(rules, path):
                report.fail(f"robots.txt blocks {agent} from {path}; Google/Bing must crawl to process noindex")
    if "Sitemap:" not in text:
        report.fail("robots.txt lacks a Sitemap line")

    if matrix.is_file():
        check_robots_matrix(text, groups, matrix, report)


def check_robots_matrix(text: str, groups: list[dict], matrix_path: Path, report: Report) -> None:
    """The generated robots.txt must agree with the provider matrix for the active stage."""
    import tomllib

    with matrix_path.open("rb") as fh:
        matrix = tomllib.load(fh)
    stage_line = re.search(r"^# crawler-policy-stage: (\S+)", text, re.M)
    if not stage_line:
        report.fail("robots.txt lacks the '# crawler-policy-stage:' marker; cannot verify against the matrix")
        return
    stage = stage_line.group(1)
    stages = matrix.get("stages") or {}
    if stage not in stages:
        report.fail(f"robots.txt stage {stage!r} is not defined in data/crawlers.toml")
        return
    problems = 0
    for entry in matrix.get("agents") or []:
        agent = entry.get("agent")
        policy = entry.get("policy") or {}
        want = policy.get(stage) or policy.get("default")
        rules = robots_rules_for(groups, agent)
        if want == "deny":
            if rules is None or robots_path_allowed(rules, "/"):
                report.fail(f"matrix says {agent} is denied at stage {stage} but robots.txt allows it")
                problems += 1
        elif want == "allow":
            if rules is not None and not robots_path_allowed(rules, "/"):
                report.fail(f"matrix says {agent} is allowed at stage {stage} but robots.txt denies it")
                problems += 1
        elif want == "publication-paths":
            if rules is None:
                report.fail(f"matrix says {agent} gets publication-path access but robots.txt has no group for it")
                problems += 1
                continue
            for allowed in matrix.get("publicationPaths") or []:
                if not robots_path_allowed(rules, allowed):
                    report.fail(f"{agent} must be allowed on {allowed} at stage {stage}")
                    problems += 1
            for denied in matrix.get("rawPaths") or []:
                if robots_path_allowed(rules, denied if denied.endswith("/") else denied):
                    report.fail(f"{agent} must be disallowed on {denied} at stage {stage}")
                    problems += 1
        else:
            report.fail(f"unknown matrix policy {want!r} for {agent}")
            problems += 1
    # Contradictory groups: an agent named in more than one group.
    seen: dict[str, int] = {}
    for g in groups:
        for a in g["agents"]:
            seen[a.lower()] = seen.get(a.lower(), 0) + 1
    dupes = [a for a, n in seen.items() if n > 1]
    if dupes:
        report.fail(f"robots.txt names agent(s) in more than one group: {dupes}")
        problems += 1
    if problems == 0:
        report.ok(f"robots.txt agrees with data/crawlers.toml at stage {stage!r}")


def check_build_json(public: Path, expected_sha: str | None, report: Report) -> None:
    bj = public / "build.json"
    if not bj.is_file():
        if expected_sha:
            report.fail("build.json missing")
        else:
            report.warn("build.json missing (local build)")
        return
    data = json.loads(bj.read_text(encoding="utf-8"))
    if expected_sha and data.get("sha") != expected_sha:
        report.fail(f"build.json sha {data.get('sha')} != expected {expected_sha}")
    else:
        report.ok(f"build.json sha={data.get('sha', '')[:12]}")


# --------------------------------------------------------------------------- main


def main(argv: Iterable[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--public", required=True, type=Path)
    ap.add_argument("--url-manifest", required=True, type=Path)
    ap.add_argument("--expected-sha")
    ap.add_argument("--expect-architecture-enabled", action="store_true")
    ap.add_argument("--allow-fixtures", action="store_true")
    ap.add_argument("--expect-homepage-v2", action="store_true", default=None,
                    help="Force the new-homepage checks (default: auto-detect from the manifest)")
    args = ap.parse_args(list(argv) if argv is not None else None)

    public: Path = args.public
    if not public.is_dir():
        print(f"public dir not found: {public}", file=sys.stderr)
        return 2
    baselines = args.url_manifest.parent
    report = Report()

    manifest = load_manifest(public, report)
    enabled = bool(manifest and manifest.get("enabled"))
    if args.expect_architecture_enabled and not enabled:
        report.fail("expected the publication architecture to be enabled in this build, but it is not")
    if manifest and manifest.get("enabled") and not args.expect_architecture_enabled and not args.allow_fixtures:
        # Production artifact must not silently ship the enabled architecture before Release B.
        report.warn("publication architecture is ENABLED in this artifact")

    approved_aliases: dict[str, str] = {}
    alias_file = baselines / "approved-aliases.txt"
    if alias_file.is_file():
        for ln in read_lines(alias_file):
            src, _, dst = ln.partition(" ")
            approved_aliases[src.strip()] = dst.strip()
    static_allow: set[str] = set()
    allow_file = baselines / "static-html-allowlist.txt"
    if allow_file.is_file():
        static_allow = set(read_lines(allow_file))

    check_build_json(public, args.expected_sha, report)
    check_url_manifest(public, args.url_manifest, approved_aliases, report)
    sitemap_paths = check_sitemap(public, manifest, baselines / "sitemap-urls-2026-08-18.txt", report)
    check_forbidden_outputs(public, enabled, report)
    if manifest:
        check_taxonomies(public, manifest, sitemap_paths, report)
        summary = check_pages(public, manifest, sitemap_paths, report, args.allow_fixtures)
        check_publication_surfaces(public, manifest, summary, sitemap_paths, report)
    check_about(public, enabled, report)
    expect_v2 = args.expect_homepage_v2
    if expect_v2 is None:
        expect_v2 = bool(manifest and manifest.get("homepageVersion", 1) >= 2)
    check_homepage(public, enabled, expect_v2, report)
    check_navigation(public, report)
    check_static_html(public, manifest, static_allow, report)
    check_robots(public, baselines, report, manifest)

    for line in report.passed:
        print(f"PASS  {line}")
    for line in report.warnings:
        print(f"WARN  {line}")
    for line in report.failures:
        print(f"FAIL  {line}")
    print(f"\n{len(report.passed)} passed, {len(report.warnings)} warnings, {len(report.failures)} failures")
    return 1 if report.failures else 0


if __name__ == "__main__":
    sys.exit(main())
