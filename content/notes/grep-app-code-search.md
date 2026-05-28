---
title: grep.app — Fast Code Search Across GitHub
date: 2020-09-01
categories:
  - tools
  - code-search
  - developer-tools
  - github
  - open-source
description: grep.app is a fast regex code search engine across public GitHub repositories — half a million repos indexed, results in milliseconds. Useful for finding real-world usage examples of APIs, patterns, and idioms that GitHub's own search can't handle.
params:
  source: pinboard
  sourceUrl: https://grep.app/
---

![grep.app — Fast Code Search Across GitHub](/images/notes/grep-app-code-search.png)

## Summary

grep.app is a regex-capable code search engine indexing public GitHub repositories. Where GitHub's native search is limited (no regex, slow for code-level queries, poor for finding exact patterns), grep.app handles full regular expression search across ~500,000 repositories with results in under a second.

The practical use case: you want to find real-world examples of how a library function is used, find all open-source implementations of a specific algorithm, check how others handle a particular API call, or verify whether a pattern is common or idiosyncratic. GitHub's own code search is improving (they've been building a separate code search product), but grep.app was significantly ahead at the time it launched.

The interface is intentionally minimal — a search box and a list of code matches with repository context. Regex support is the key differentiator: `find.*\bpath\b.*join` will find code that uses path joining in specific ways that keyword search can't.

## Key points

- Regex support is the core value add over GitHub search — enables searching for patterns, not just keywords.
- Useful for: finding library usage examples, checking idiomatic patterns in a language, finding implementations of specific algorithms, discovering projects that use a particular API.
- ~500,000 repositories indexed — large enough for most searches, smaller than GitHub's full corpus (hundreds of millions of repos).
- Alternatives: Sourcegraph (more comprehensive, enterprise focus), GitHub Code Search (improved significantly after this was bookmarked), CS.github.com.
- Speed comes from offline indexing — results are fast because the corpus is pre-indexed, not searched live.

[Original](https://grep.app/)
