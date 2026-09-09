#!/usr/bin/env python3
"""Validate the Cloudflare-fronted production site after a deployment.

Standard library only. Checks public status, redirects, canonical targets, metadata, and the
edge-served crawler policy for a representative set of URLs. It cannot prove behaviour that
Cloudflare reserves for verified crawler source networks (WAF/IP-list rules); audit those in
the Cloudflare dashboard/API separately.

Usage::

    python3 scripts/validate_live.py --base-url https://ryanorban.com \
        --expected-sha "$GITHUB_SHA" --url-manifest scripts/baselines/public-urls.txt
"""
from __future__ import annotations

import argparse
import json
import random
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_site import (  # noqa: E402
    PageScraper,
    Report,
    parse_robots,
    read_lines,
    robots_path_allowed,
    robots_rules_for,
)

USER_AGENT = "ryanorban-live-validator/1.0 (+https://ryanorban.com/)"


def fetch(url: str, timeout: float = 20.0) -> tuple[int, dict[str, str], bytes, str]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Cache-Control": "no-cache"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:  # noqa: S310
            return resp.status, {k.lower(): v for k, v in resp.headers.items()}, resp.read(), resp.geturl()
    except urllib.error.HTTPError as exc:
        return exc.code, {k.lower(): v for k, v in exc.headers.items()}, exc.read() or b"", url
    except (urllib.error.URLError, TimeoutError) as exc:
        return 0, {}, str(exc).encode(), url


def scrape_bytes(body: bytes) -> PageScraper:
    p = PageScraper()
    p.feed(body.decode("utf-8", errors="replace"))
    return p


def wait_for_sha(base: str, expected: str, wait_seconds: int, report: Report) -> None:
    deadline = time.time() + wait_seconds
    last = None
    while True:
        status, _, body, _ = fetch(f"{base}/build.json")
        if status == 200:
            try:
                last = json.loads(body).get("sha")
            except json.JSONDecodeError:
                last = None
            if last == expected:
                report.ok(f"/build.json sha matches {expected[:12]}")
                return
        if time.time() > deadline:
            report.fail(f"/build.json did not report {expected[:12]} within {wait_seconds}s (status={status}, last={last})")
            return
        time.sleep(15)


def check_page(base: str, path: str, report: Report, *, expect_noindex: bool | None = None, expect_status: int = 200) -> PageScraper | None:
    status, headers, body, final = fetch(base + path)
    if status != expect_status:
        report.fail(f"{path}: HTTP {status} (expected {expect_status})")
        return None
    if final.rstrip("/") != (base + path).rstrip("/") and not path.endswith(".json"):
        report.fail(f"{path}: redirected to {final}")
    ctype = headers.get("content-type", "")
    if "html" not in ctype:
        report.ok(f"{path}: {status} {ctype}")
        return None
    page = scrape_bytes(body)
    canonical = page.canonical()
    if canonical and canonical.rstrip("/") != (base + path).rstrip("/"):
        report.fail(f"{path}: canonical points to {canonical}")
    noindex = any("noindex" in d for d in page.robots_directives())
    if expect_noindex is True and not noindex:
        report.fail(f"{path}: expected noindex, none served")
    if expect_noindex is False and noindex:
        report.fail(f"{path}: unexpectedly noindexed")
    report.ok(f"{path}: {status}, noindex={noindex}")
    return page


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base-url", default="https://ryanorban.com")
    ap.add_argument("--expected-sha")
    ap.add_argument("--url-manifest", type=Path)
    ap.add_argument("--wait-seconds", type=int, default=0)
    ap.add_argument("--sample", type=int, default=25, help="random sample size from the URL manifest")
    ap.add_argument("--architecture-enabled", action="store_true",
                    help="assert the Release B behaviours (noindex on bookmarks/taxonomies, feeds absent)")
    args = ap.parse_args()
    base = args.base_url.rstrip("/")
    report = Report()

    if args.expected_sha:
        wait_for_sha(base, args.expected_sha, args.wait_seconds, report)
    else:
        status, _, body, _ = fetch(f"{base}/build.json")
        if status == 200:
            report.ok(f"/build.json present: {body[:120]!r}")
        else:
            report.warn(f"/build.json returned HTTP {status}")

    # robots.txt as served by the edge
    status, _, body, _ = fetch(f"{base}/robots.txt")
    if status != 200:
        report.fail(f"/robots.txt HTTP {status}")
    else:
        text = body.decode("utf-8", errors="replace")
        groups = parse_robots(text)
        baselines = args.url_manifest.parent if args.url_manifest else Path("scripts/baselines")
        denied = baselines / "robots-denied-agents.txt"
        if denied.is_file():
            reopened = []
            for agent in read_lines(denied):
                rules = robots_rules_for(groups, agent)
                if rules is None or robots_path_allowed(rules, "/"):
                    reopened.append(agent)
            if reopened:
                report.fail(f"edge robots.txt reopened denied agent(s): {reopened}")
            else:
                report.ok("edge robots.txt preserves baseline denials")
        for agent in ("Googlebot", "Bingbot", "*"):
            rules = robots_rules_for(groups, agent)
            if rules is not None and not robots_path_allowed(rules, "/notes/"):
                report.fail(f"edge robots.txt blocks {agent} from /notes/")
        if "BEGIN Cloudflare Managed content" in text:
            report.warn("Cloudflare managed robots.txt content is being prepended at the edge (release plan requires it disabled or matched)")
        stage = re.search(r"^# crawler-policy-stage: (\S+)", text, re.M)
        report.ok(f"edge robots.txt stage marker: {stage.group(1) if stage else 'absent (pre-migration file)'}")

    # sitemap
    status, _, body, _ = fetch(f"{base}/sitemap.xml")
    if status != 200:
        report.fail(f"/sitemap.xml HTTP {status}")
    else:
        locs = re.findall(r"<loc>([^<]+)</loc>", body.decode("utf-8", errors="replace"))
        report.ok(f"/sitemap.xml has {len(locs)} URLs")

    # Representative pages
    check_page(base, "/", report, expect_noindex=False)
    check_page(base, "/about/", report, expect_noindex=False)
    check_page(base, "/posts/", report, expect_noindex=False)
    for feed in ("/posts/index.xml", "/posts/index.json"):
        status, _, _, _ = fetch(base + feed)
        (report.ok if status == 200 else report.fail)(f"{feed}: HTTP {status}")
    check_page(base, "/notes/", report, expect_noindex=True if args.architecture_enabled else None)
    for feed in ("/notes/index.xml", "/notes/index.json"):
        status, _, _, _ = fetch(base + feed)
        if args.architecture_enabled:
            (report.ok if status == 404 else report.fail)(f"{feed}: HTTP {status} (must be absent)")
        else:
            report.ok(f"{feed}: HTTP {status}")
    check_page(base, "/graph/", report, expect_noindex=True if args.architecture_enabled else None)
    status, _, _, _ = fetch(f"{base}/graph/index.json")
    report.ok(f"/graph/index.json: HTTP {status}")
    for path in ("/advising/", "/office-hours/"):
        check_page(base, path, report, expect_noindex=True if args.architecture_enabled else None)
    check_page(base, "/categories/", report, expect_noindex=True if args.architecture_enabled else None)
    check_page(base, "/sfevents/", report, expect_noindex=True if args.architecture_enabled else None)
    status, _, _, _ = fetch(f"{base}/sfevents/api/events.json")
    report.ok(f"/sfevents/api/events.json: HTTP {status}")

    # Random sample from the pre-migration manifest must still resolve
    if args.url_manifest and args.url_manifest.is_file():
        urls = read_lines(args.url_manifest)
        rng = random.Random(42)
        sample = rng.sample(urls, min(args.sample, len(urls)))
        broken = []
        for path in sample:
            status, _, _, _ = fetch(base + path)
            if status != 200:
                broken.append((path, status))
        if broken:
            report.fail(f"{len(broken)} sampled pre-migration URL(s) do not return 200: {broken[:5]}")
        else:
            report.ok(f"{len(sample)} sampled pre-migration URLs return 200")

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
