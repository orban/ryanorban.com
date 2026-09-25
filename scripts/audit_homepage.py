#!/usr/bin/env python3
"""Build and audit the homepage against its evidence-first contract.

The audit asserts behaviour of the *built* site wherever it can. Factual claims
are not checked by looking for a literal in the template — they are extracted
from the linked source of truth and compared against the rendered page, so a
number that drifts away from its own essay fails here.
"""

from __future__ import annotations

import re
import subprocess
import tempfile
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = ROOT / "content" / "_index.md"
ABOUT_PATH = ROOT / "content" / "about.md"
TEMPLATE_PATH = ROOT / "layouts" / "_default" / "home.html"
BASEOF_PATH = ROOT / "layouts" / "_default" / "baseof.html"
CSS_PATH = ROOT / "static" / "css" / "home.css"
MOIRAI_POST = ROOT / "content" / "posts" / "what-stochastic-variation-reveals.md"

EXPECTED_TITLE = "Ryan Orban — Agent evaluation and reliability"
EXPECTED_H1 = ["Ryan Orban"]
REQUIRED_H2 = {
    "The record",
    "Built",
    "What I’m looking for",
}
REQUIRED_NAV = {"Record", "Work", "Contact"}
# Writing is omitted wholesale when every published post is pinned into "Building
# now". Heading, nav item, anchor and list travel together, so one derived answer
# to "should Writing exist on this build?" drives all four.
WRITING = {"list": "record-writing-list", "h2": "Writing", "nav": "Writing", "id": "writing"}
REQUIRED_IMAGES = {
    "/images/ryan-orban.jpg",
}
# Art-directed narrow crops, referenced from <source> rather than <img>. None since the
# 2026-09-04 pass: the portrait is the only raster on the page.
REQUIRED_NARROW_SOURCES: set[str] = set()
# Below-fold artefacts must not compete with the hero for bandwidth.
LAZY_IMAGES: set[str] = set()
# Fonts are self-hosted; the homepage must not fetch type from a third party.
THIRD_PARTY_FONT_HOSTS = ("fonts.googleapis.com", "fonts.gstatic.com", "cdn.jsdelivr.net/npm/geist")
# list-style: none strips list semantics in Safari/VoiceOver without role="list".
# One entry per list *instance*, not per class name, and compared by name and count
# rather than against a total floor -- a floor can be silently lowered by shrinking
# the constant, an exact comparison cannot.
REQUIRED_LISTS = (
    "record-rows",  # The record
    "record-rows",  # Built
    "record-rows",  # Other projects
)
OPTIONAL_LISTS = ("record-writing-list",)  # Writing, only when an unpinned post exists

# Every Moirai figure on the homepage is derived from the essay it links to.
# The homepage label is the key; the essay is the only authority for the value.
# "Preference pairs" was retired here on 2026-09-25 alongside the metric itself in
# layouts/partials/record/data.html. The literal "11,006 preference pairs" still appears
# in the essay inside a fenced code block, so this entry would have gone on passing --
# the contract checks that a rendered figure agrees with its source, not that the claim
# the figure encodes is one the essay still makes. The essay's September update reports
# the pairs predict nothing on held-out runs.
MOIRAI_CONTRACT = {
    "Runs analyzed": r"([\d,]+) runs total",
    "Mixed-outcome tasks": r"attempts ([\d,]+) software engineering tasks",
}
# Claims the homepage shares with the About page, which is their source here.
ABOUT_CLAIMS = ("$1M", "150+", "$100M+", "91%")

BANNED_COPY = re.compile(
    r"(?i)\b(?:"
    r"passionate about|leveraging|empowering|delivering value|end-to-end|"
    r"world-class|innovative solutions?|transformative|groundbreaking|"
    r"category-defining|cutting-edge|fractional cto|ai consultant|"
    r"llm expert|startup advisor|i help (?:companies|organizations)"
    r")\b"
)

FAILURES: list[str] = []


class HomepageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: list[str] = []
        self.aria_refs: list[str] = []
        self.links: list[str] = []
        self.images: dict[str, str] = {}
        self.image_attrs: list[dict[str, str]] = []
        self.sources: list[dict[str, str]] = []
        self.h1: list[str] = []
        self.h2: list[str] = []
        self.meta: dict[str, str] = {}
        self.meta_props: dict[str, str] = {}
        self.nav_items: list[str] = []
        self.metrics: dict[str, str] = {}
        self.lists: list[tuple[tuple[str, ...], str]] = []
        self.writing_items = 0
        self.title = ""
        self.body_classes: list[str] = []
        self._heading: tuple[str, list[str]] | None = None
        self._title_open = False
        self._nav_depth = 0
        self._nav_link_text: list[str] | None = None
        self._metric_term: list[str] | None = None
        self._metric_value: list[str] | None = None
        self._pending_term = ""
        self._metrics_depth = 0
        self._writing_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = {key: value or "" for key, value in attrs}
        classes = attributes.get("class", "").split()
        if element_id := attributes.get("id"):
            self.ids.append(element_id)
        if aria_labelledby := attributes.get("aria-labelledby"):
            self.aria_refs.extend(aria_labelledby.split())
        if tag == "a":
            self.links.append(attributes.get("href", ""))
            if self._nav_depth:
                self._nav_link_text = []
        if tag == "img":
            self.images[attributes.get("src", "")] = attributes.get("alt", "")
            self.image_attrs.append(attributes)
        if tag == "source":
            self.sources.append(attributes)
        if tag == "meta":
            if name := attributes.get("name"):
                self.meta[name] = attributes.get("content", "")
            if prop := attributes.get("property"):
                self.meta_props[prop] = attributes.get("content", "")
        if tag in {"h1", "h2"}:
            self._heading = (tag, [])
        if tag == "title":
            self._title_open = True
        if tag == "nav":
            self._nav_depth += 1
        if tag == "body":
            self.body_classes = classes
        if tag in {"ul", "ol"}:
            self.lists.append((tuple(classes), attributes.get("role", "")))
            if "record-writing-list" in classes:
                self._writing_depth = 1
        if tag == "dl" and "record-metrics" in classes:
            self._metrics_depth = 1
        if self._metrics_depth and tag == "dt":
            self._metric_term = []
        if self._metrics_depth and tag == "dd":
            self._metric_value = []
        if self._writing_depth and tag == "li":
            self.writing_items += 1

    def handle_endtag(self, tag: str) -> None:
        if self._heading and tag == self._heading[0]:
            heading_tag, fragments = self._heading
            text = normalize_text("".join(fragments))
            (self.h1 if heading_tag == "h1" else self.h2).append(text)
            self._heading = None
        if tag == "title":
            self._title_open = False
        if tag == "a" and self._nav_link_text is not None:
            text = normalize_text("".join(self._nav_link_text))
            if text:
                self.nav_items.append(text)
            self._nav_link_text = None
        if tag == "nav":
            self._nav_depth -= 1
        if tag == "dt" and self._metric_term is not None:
            self._pending_term = normalize_text("".join(self._metric_term))
            self._metric_term = None
        if tag == "dd" and self._metric_value is not None:
            self.metrics[self._pending_term] = normalize_text("".join(self._metric_value))
            self._metric_value = None
        if tag == "dl":
            self._metrics_depth = 0
        if tag == "ol" and self._writing_depth:
            self._writing_depth = 0

    def handle_data(self, data: str) -> None:
        if self._heading:
            self._heading[1].append(data)
        if self._title_open:
            self.title += data
        if self._nav_link_text is not None:
            self._nav_link_text.append(data)
        if self._metric_term is not None:
            self._metric_term.append(data)
        if self._metric_value is not None:
            self._metric_value.append(data)


def normalize_text(value: str) -> str:
    return " ".join(value.split())


def parse_color_variables(css: str) -> dict[str, str]:
    return dict(re.findall(r"--([\w-]+):\s*(#[0-9a-fA-F]{6})", css))


def luminance(value: str) -> float:
    value = value.lstrip("#")
    channels = tuple(int(value[index : index + 2], 16) / 255 for index in (0, 2, 4))
    linear = tuple(
        channel / 12.92
        if channel <= 0.04045
        else ((channel + 0.055) / 1.055) ** 2.4
        for channel in channels
    )
    return sum(weight * channel for weight, channel in zip((0.2126, 0.7152, 0.0722), linear))


def contrast_ratio(first: str, second: str) -> float:
    high, low = sorted((luminance(first), luminance(second)), reverse=True)
    return (high + 0.05) / (low + 0.05)


def check(name: str, condition: bool, detail: str = "") -> bool:
    if condition:
        print(f"PASS {name}")
        return True
    suffix = f": {detail}" if detail else ""
    print(f"FAIL {name}{suffix}")
    FAILURES.append(f"{name}{suffix}")
    return False


def extract_sourced_facts(post: str) -> dict[str, str]:
    """Pull the Moirai figures out of the essay the homepage links to."""
    facts: dict[str, str] = {}
    for label, pattern in MOIRAI_CONTRACT.items():
        match = re.search(pattern, post)
        if match:
            facts[label] = match.group(1)
        else:
            check(f"source of truth for {label!r}", False, f"pattern not found: {pattern}")
    return facts


def output_path_for(output: Path, link: str) -> Path:
    target = link.split("#", 1)[0].split("?", 1)[0]
    relative = target.lstrip("/")
    if target.endswith("/") or not relative:
        return output / relative / "index.html"
    return output / relative


def main() -> None:
    source = SOURCE_PATH.read_text()
    about = ABOUT_PATH.read_text()
    template = TEMPLATE_PATH.read_text()
    baseof = BASEOF_PATH.read_text()
    css = CSS_PATH.read_text()
    post = MOIRAI_POST.read_text()

    with tempfile.TemporaryDirectory(prefix="ryanorban-homepage-") as output_dir:
        subprocess.run(
            [
                "hugo",
                "--source",
                str(ROOT),
                "--destination",
                output_dir,
                "--cleanDestinationDir",
                "--minify",
            ],
            check=True,
            cwd=ROOT,
        )
        output = Path(output_dir)
        html = (output / "index.html").read_text()
        posts_index = (output / "posts" / "index.html").read_text()
        parser = HomepageParser()
        parser.feed(html)

        for image_path in REQUIRED_IMAGES | REQUIRED_NARROW_SOURCES:
            check(
                f"asset published {image_path}",
                (output / image_path.lstrip("/")).is_file(),
            )

        check("non-home page rendered", (output / "about" / "index.html").is_file())

        # Every internal link the homepage emits must resolve in the real output.
        internal = sorted(
            {
                link
                for link in parser.links
                if link.startswith("/") and not link.startswith("//")
            }
        )
        unresolved = [link for link in internal if not output_path_for(output, link).exists()]
        check(
            "internal links resolve",
            not unresolved,
            f"{unresolved} of {len(internal)} checked",
        )

        # Notes must be reachable by a human, not only by sitemap.xml.
        notes_index = output / "notes" / "index.html"
        # --minify strips attribute quotes, so match the href tolerantly.
        notes_href = re.compile(r"""href=["']?/notes/""")
        home_link = bool(notes_href.search(html))
        about_link = bool(notes_href.search((output / "about" / "index.html").read_text()))
        check("notes section is built", notes_index.is_file())
        check(
            "notes has a human navigation path",
            home_link and about_link,
            f"homepage={home_link} non-home={about_link}",
        )

    # --- factual contract -------------------------------------------------
    sourced = extract_sourced_facts(post)
    for label, value in sourced.items():
        check(
            f"homepage figure matches source: {label}",
            parser.metrics.get(label) == value,
            f"homepage={parser.metrics.get(label)!r} source={value!r}",
        )
    if {"Mixed-outcome tasks", "Preference pairs"} <= sourced.keys():
        tasks = sourced["Mixed-outcome tasks"]
        pairs = sourced["Preference pairs"]
        check(
            "source labels its task count as mixed-outcome",
            f"{tasks} mixed-outcome tasks" in post,
            f"expected '{tasks} mixed-outcome tasks' in the linked analysis",
        )
        check(
            "preference pairs share the task denominator",
            f"{pairs} preference pairs from {tasks} tasks" in post,
            f"expected '{pairs} preference pairs from {tasks} tasks' in the linked analysis",
        )
    for claim in ABOUT_CLAIMS:
        check(f"claim {claim} is corroborated by /about/", claim in about and claim in template)
    # The ledger leads with real, dated work. A synthetic illustration must never
    # reappear as the opening claim, so the page carries no seeded demo at all.
    check(
        "no synthetic demo on the page",
        not re.search(
            r"""class=["']?is-(?:pass|fail)|synthetic and seeded|not a real system""",
            html,
        ),
    )
    # Figures may only appear where a source of truth vouches for them, so an
    # unsourced metric cannot be added without failing the contract above.
    check(
        "no unsourced figures",
        set(parser.metrics) == set(MOIRAI_CONTRACT),
        repr(sorted(set(parser.metrics) ^ set(MOIRAI_CONTRACT))),
    )
    # The record's own rows only. "Built" and the writing list reuse the row
    # class, and the writing count moves with the post data.
    ledger = re.search(r"<ol[^>]*class=[\"']?record-rows.*?</ol>", html, re.DOTALL)
    rows = re.findall(
        r"<li[^>]*class=[\"']?[^\">]*record-row[^>]*>(.*?)</li>",
        ledger.group(0) if ledger else "",
        re.DOTALL,
    )
    check("ledger rows present", len(rows) >= 7, f"{len(rows)} rows")
    # Every ledger row is dated, so the record can be checked rather than believed.
    undated = [n for n, row in enumerate(rows, 1) if "<time datetime" not in row]
    check("every ledger row is dated", not undated, f"rows {undated} carry no <time datetime>")
    check("direction contract survives the build", "THESIS:" in html and "FINISH:" in html)
    check(
        "no third-party font requests on the homepage",
        not any(host in html for host in THIRD_PARTY_FONT_HOSTS),
    )

    # --- document contract ------------------------------------------------
    # "Should Writing exist on this build?" answered once, from the post data
    # rather than from the markup under test. A published post that "Built"
    # has not pinned is a post Writing must list. Every conditional check below
    # compares rendered markup against this expectation, never against itself.
    published = set(re.findall(r"""href=["']?(/posts/[^"'\s>]+/)""", posts_index))
    work_section = re.search(r"""<section[^>]*id=["']?work\b.*?</section>""", html, re.DOTALL)
    pinned = set(
        re.findall(
            r"""href=["']?(/posts/[^"'\s>]+/)""",
            work_section.group(0) if work_section else "",
        )
    )
    writing_expected = bool(published - pinned)
    seen = sorted(" ".join(classes) for classes, _ in parser.lists)
    check("seo title", normalize_text(parser.title) == EXPECTED_TITLE, parser.title)
    description = parser.meta.get("description", "")
    check("seo description present", bool(description))
    check(
        "seo description fits a search result",
        len(description) <= 160,
        f"{len(description)} characters",
    )
    check("working record body class", "working-record-site" in parser.body_classes)
    check("single exact h1", parser.h1 == EXPECTED_H1, repr(parser.h1))
    expected_h2 = REQUIRED_H2 | ({WRITING["h2"]} if writing_expected else set())
    check(
        "required sections present",
        expected_h2 <= set(parser.h2),
        repr(sorted(expected_h2 - set(parser.h2))),
    )
    check(
        "no orphan section heading",
        (WRITING["h2"] in set(parser.h2)) == writing_expected,
        f"heading={WRITING['h2'] in set(parser.h2)} expected={writing_expected}",
    )
    check("unique ids", len(parser.ids) == len(set(parser.ids)), repr(parser.ids))
    check(
        "aria references resolve",
        set(parser.aria_refs).issubset(set(parser.ids)),
        repr(sorted(set(parser.aria_refs) - set(parser.ids))),
    )
    check("skip link", "#maincontent" in parser.links)
    anchors = ["record", "work", "contact"] + ([WRITING["id"]] if writing_expected else [])
    for anchor in anchors:
        check(f"{anchor} anchor", anchor in parser.ids)
    # Nav, heading, anchor and section appear and disappear together: a nav item
    # pointing at a section that did not render is a dead link.
    fragments = {link[1:] for link in parser.links if link.startswith("#") and len(link) > 1}
    dangling = sorted(fragment for fragment in fragments if fragment not in parser.ids)
    check("fragment links resolve", not dangling, repr(dangling))
    check("email link", "mailto:me@ryanorban.com" in parser.links)
    expected_nav = REQUIRED_NAV | ({WRITING["nav"]} if writing_expected else set())
    check(
        "primary navigation",
        expected_nav <= set(parser.nav_items),
        repr(parser.nav_items),
    )
    check(
        "no nav item for an absent section",
        (WRITING["nav"] in set(parser.nav_items)) == writing_expected,
        repr(parser.nav_items),
    )
    check(
        "documentary images present",
        REQUIRED_IMAGES <= set(parser.images),
        repr(sorted(REQUIRED_IMAGES - set(parser.images))),
    )
    check("all images have alt text", all(parser.images.values()), repr(parser.images))

    # --- art direction, semantics, loading --------------------------------
    narrow = {source_.get("srcset", "") for source_ in parser.sources}
    check(
        "narrow crops are art-directed",
        REQUIRED_NARROW_SOURCES <= narrow,
        repr(sorted(REQUIRED_NARROW_SOURCES - narrow)),
    )
    check(
        "narrow crops declare intrinsic size",
        all(
            source_.get("width") and source_.get("height")
            for source_ in parser.sources
            if source_.get("srcset") in REQUIRED_NARROW_SOURCES
        ),
        repr(parser.sources),
    )
    check(
        "images declare intrinsic size",
        all(image.get("width") and image.get("height") for image in parser.image_attrs),
        repr([image.get("src") for image in parser.image_attrs if not image.get("width")]),
    )
    eager = [
        image.get("src")
        for image in parser.image_attrs
        if image.get("src") in LAZY_IMAGES and image.get("loading") != "lazy"
    ]
    check("below-fold artefacts are lazy", not eager, repr(eager))
    # Every list on this page is styled list-style: none, so every list on this
    # page needs role="list" to survive Safari/VoiceOver.
    unrolled = [classes for classes, role in parser.lists if role != "list"]
    check("lists keep list semantics", not unrolled, repr(unrolled))
    expected_lists = sorted(REQUIRED_LISTS + (OPTIONAL_LISTS if writing_expected else ()))
    check(
        "all homepage lists were seen",
        seen == expected_lists,
        f"saw {seen}, expected {expected_lists} (published={len(published)} pinned={len(pinned)})",
    )
    check(
        "writing list is populated exactly when an unpinned post exists",
        parser.writing_items > 0 if writing_expected else parser.writing_items == 0,
        f"items={parser.writing_items} expected={writing_expected}",
    )

    # --- sharing metadata --------------------------------------------------
    check("social preview image", bool(parser.meta_props.get("og:image")), repr(parser.meta_props))
    check(
        "large-image twitter card",
        parser.meta.get("twitter:card") == "summary_large_image",
        repr(parser.meta.get("twitter:card")),
    )

    check("analytics preserved", "plausible.srv.ryo.wtf/js/script.js" in html)
    check("homepage CSS is emitted", ".record-rows" in html)
    # Screened against the rendered page, so copy arriving via post descriptions
    # is covered too — not just the strings hardcoded in the template.
    banned = BANNED_COPY.search(html) or BANNED_COPY.search(template + baseof)
    check("marketing language absent", not banned, banned.group(0) if banned else "")

    # --- CSS invariants ----------------------------------------------------
    check("no specificity overrides", "!important" not in css)
    check("no parent-selector dependency", ":has(" not in css)
    check("no card shadows", "box-shadow" not in css)
    check("no decorative gradients", "gradient(" not in css)
    check("responsive rules present", css.count("@media (max-width:") >= 2)
    check("focus is styled", ":focus-visible" in css)
    check("reduced motion respected", "prefers-reduced-motion" in css)

    variables = parse_color_variables(css)
    for name in ("record-ink", "record-mid", "record-muted", "record-accent", "record-accent-dark"):
        ratio = contrast_ratio(variables[name], variables["record-bg"])
        check(f"{name} contrast", ratio >= 4.5, f"{ratio:.2f}:1")

    body = source.split("---", 2)[-1].strip()
    check("content file is metadata only", not body, repr(body[:120]))

    if FAILURES:
        raise SystemExit(f"Homepage audit failed ({len(FAILURES)}):\n  " + "\n  ".join(FAILURES))
    print("Homepage audit passed.")


if __name__ == "__main__":
    main()
