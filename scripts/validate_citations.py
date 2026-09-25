#!/usr/bin/env python3
"""Resolve every arXiv and DOI citation in the posts and check the link text matches.

The failure this catches is specific and it has already happened twice on this
site: a link whose text names one paper while the identifier points at another.
Paper nicknames collide -- there are two unrelated projects called SWE-Dev and
two called DeepSWE -- so a plausible-looking arXiv ID next to a plausible-looking
name is not evidence they are the same work. Only resolution is.

Each citation is fetched from the authority (arXiv's export API, doi.org content
negotiation) and the link text is checked against the resolved title and author
list. A nickname link like [Math-Shepherd](...) must have its distinctive tokens
in the title; an author-style link like [Namkoong et al.](...) must match a
surname. Anything that resolves to nothing is a hard failure.

    python3 scripts/validate_citations.py                  # every post
    python3 scripts/validate_citations.py content/posts/x.md
    python3 scripts/validate_citations.py --verbose        # print every match

Network access is required. Offline, this exits 2 rather than passing silently:
a check that cannot run has not passed.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "content" / "posts"

ARXIV_API = "http://export.arxiv.org/api/query?id_list={}"
DOI_API = "https://doi.org/{}"
USER_AGENT = "ryanorban.com citation validator (+https://ryanorban.com)"

LINK_RE = re.compile(r"\[([^\[\]]+)\]\((https?://[^)\s]+)\)")
ARXIV_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/([0-9]{4}\.[0-9]{4,5})(?:v\d+)?")
DOI_RE = re.compile(r"doi\.org/(10\.[^\s)]+)")

# Words too common to carry identity. "Verify" alone must not match a title
# just because the title happens to contain it.
STOPWORDS = {
    "a", "an", "and", "the", "of", "for", "to", "in", "on", "with", "by",
    "is", "are", "at", "as", "from", "via", "et", "al", "s", "when", "who",
    "step", "let", "lets", "it", "its", "this", "that",
}

# An author-style link: "Namkoong et al.", "Oberst & Sontag's ...". Matched
# against the author list rather than the title.
AUTHOR_LINK_RE = re.compile(r"\bet al\b|&|\band\b")


@dataclass
class Citation:
    file: Path
    line: int
    text: str
    url: str
    ident: str
    kind: str  # "arxiv" | "doi"


@dataclass
class Resolved:
    title: str
    authors: list[str]
    abstract: str = ""

    @property
    def searchable(self) -> str:
        """Title plus abstract.

        A nickname usually appears in the title, but plenty of papers introduce
        their acronym only in the abstract -- COMA, OmegaPRM and RLFDC all do.
        Searching both still separates a real citation from a name collision,
        because a different paper's abstract will not contain the nickname.
        """
        return f"{self.title} {self.abstract}"


def _display(path: Path) -> str:
    """Repo-relative when possible; absolute for a file passed from elsewhere."""
    try:
        return str(path.resolve().relative_to(ROOT))
    except ValueError:
        return str(path)


def find_citations(path: Path) -> list[Citation]:
    out = []
    for lineno, line in enumerate(path.read_text().splitlines(), start=1):
        for text, url in LINK_RE.findall(line):
            if m := ARXIV_RE.search(url):
                out.append(Citation(path, lineno, text, url, m.group(1), "arxiv"))
            elif m := DOI_RE.search(url):
                out.append(Citation(path, lineno, text, url, m.group(1), "doi"))
    return out


def _get(url: str, accept: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": accept})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read()


class _NoDTDParser(ET.XMLParser):
    """Reject any document carrying a DTD.

    ElementTree expands internal entities, so a hostile or compromised response
    could bill-of-laughs this script. arXiv's Atom feed has no DTD, so refusing
    one outright costs nothing and removes the class.
    """

    def doctype(self, name, _pubid, _system):  # ET calls this on <!DOCTYPE>
        raise ET.ParseError(f"refusing a response with a DTD ({name})")


def resolve_arxiv(ident: str) -> Resolved | None:
    """Query the arXiv export API. A withdrawn or nonexistent ID returns no entry."""
    body = _get(ARXIV_API.format(ident), "application/atom+xml")
    ns = {"a": "http://www.w3.org/2005/Atom"}
    entry = ET.fromstring(body, parser=_NoDTDParser()).find("a:entry", ns)
    if entry is None:
        return None
    title = entry.findtext("a:title", default="", namespaces=ns)
    # arXiv returns "Error" entries for bad IDs with the id set to the api docs.
    if entry.findtext("a:id", default="", namespaces=ns).endswith("api/errors"):
        return None
    authors = [
        a.findtext("a:name", default="", namespaces=ns)
        for a in entry.findall("a:author", ns)
    ]
    abstract = entry.findtext("a:summary", default="", namespaces=ns)
    return Resolved(" ".join(title.split()), authors, " ".join(abstract.split()))


def resolve_doi(ident: str) -> Resolved | None:
    """Content-negotiate CSL JSON from doi.org. Unregistered DOIs 404."""
    body = _get(DOI_API.format(ident), "application/vnd.citationstyles.csl+json")
    data = json.loads(body)
    title = data.get("title") or ""
    if isinstance(title, list):
        title = title[0] if title else ""
    authors = [
        " ".join(filter(None, (a.get("given"), a.get("family"))))
        for a in data.get("author", [])
    ]
    return Resolved(" ".join(title.split()), authors, data.get("abstract") or "")


def tokens(s: str) -> set[str]:
    return {t for t in re.findall(r"[a-z0-9]+", s.lower()) if t not in STOPWORDS}


def check_match(cite: Citation, got: Resolved) -> str | None:
    """Return a failure reason, or None when the link text is consistent."""
    link = tokens(cite.text)
    if not link:
        return None  # nothing distinctive to check against

    if AUTHOR_LINK_RE.search(cite.text):
        surnames = tokens(" ".join(got.authors))
        if link & (surnames | tokens(got.title)):
            return None
        who = ", ".join(got.authors[:3]) or "(no authors listed)"
        return f"names no author of the resolved work (authors: {who})"

    # Nickname link. Hyphenated names resolve to their parts, so require the
    # whole set rather than any single token: "SWE-Gym" must not pass on "SWE".
    haystack = tokens(got.searchable)
    if link <= haystack:
        return None
    # An acronym written solid in the link but spaced in the paper, or vice
    # versa: "OmegaPRM" against "Omega PRM".
    squashed = re.sub(r"[^a-z0-9]", "", got.searchable.lower())
    if re.sub(r"[^a-z0-9]", "", cite.text.lower()) in squashed:
        return None
    missing = ", ".join(sorted(link - haystack))
    return f"link text appears nowhere in the paper (missing: {missing})"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("paths", nargs="*", type=Path)
    ap.add_argument("--verbose", action="store_true", help="print every resolved citation")
    args = ap.parse_args()

    paths = args.paths or sorted(POSTS.glob("*.md"))
    cites = [c for p in paths for c in find_citations(p)]
    if not cites:
        print("no arXiv or DOI citations found")
        return 0

    # One fetch per identifier, not per occurrence.
    cache: dict[str, Resolved | None] = {}
    failures: list[str] = []

    print(f"resolving {len({c.ident for c in cites})} identifiers "
          f"across {len(cites)} citations\n")

    for cite in cites:
        where = f"{_display(cite.file)}:{cite.line}"
        if cite.ident not in cache:
            resolver = resolve_arxiv if cite.kind == "arxiv" else resolve_doi
            try:
                cache[cite.ident] = resolver(cite.ident)
            except urllib.error.HTTPError as e:
                if e.code == 404:
                    cache[cite.ident] = None
                else:
                    print(f"  network error on {cite.ident}: {e}", file=sys.stderr)
                    return 2
            except (urllib.error.URLError, TimeoutError, ET.ParseError) as e:
                print(f"  cannot reach the resolver for {cite.ident}: {e}", file=sys.stderr)
                return 2
            time.sleep(0.5)  # arXiv asks for one request every 3s; be polite-ish

        got = cache[cite.ident]
        if got is None:
            failures.append(f"FAIL {where}\n     [{cite.text}] -> {cite.ident} does not resolve")
            continue

        if reason := check_match(cite, got):
            failures.append(
                f"FAIL {where}\n"
                f"     [{cite.text}] -> {cite.ident}\n"
                f"     resolves to: {got.title}\n"
                f"     {reason}"
            )
        elif args.verbose:
            print(f"  ok  [{cite.text}] -> {got.title}")

    print()
    if failures:
        print("\n".join(failures))
        print(f"\n{len(failures)} citation failure(s)")
        return 1
    print(f"{len(cites)} citations resolve and match their link text")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
