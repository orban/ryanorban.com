---
title: Hacker News Books
date: 2021-08-29
categories:
  - books
  - hacker-news
  - reading
  - tools
  - discovery
description: Hacker News Books extracts and ranks book recommendations from HN comments — a crowd-sourced reading list from technically sophisticated readers. Useful for finding what books the HN community actually recommends, beyond bestseller lists.
params:
  source: pinboard
  sourceUrl: https://hackernewsbooks.com/
---

## Summary

[Hacker News Books](/notes/hacker-news-books/) is a simple tool that scrapes Hacker News comment threads for book mentions and recommendations, then aggregates them into a ranked list. The premise: HN's Ask HN: What are you reading? threads and other book-recommendation threads are a rich source of curated technical and intellectual reading, but that signal is buried in threaded comments and hard to aggregate across time.

The output is a de-duplicated, popularity-ranked list of books that appear frequently in HN comments. This is valuable as a discovery mechanism: it surfaces books that are genuinely valued by a technically sophisticated, intellectually curious community rather than the algorithm-optimized lists on Amazon or Goodreads. Books like Gödel, Escher, Bach, The Art of Problem Solving, and various math/CS texts consistently surface because they're what HN commenters actually recommend, not what gets marketed to readers.

The tool sits alongside tools like Goodreads and [StoryGraph](/notes/storygraph/) but with a fundamentally different curation mechanism — crowd intelligence from a specific community rather than explicit ratings.

## Key points

- Aggregates book mentions and recommendations from Hacker News comments — community-curated rather than algorithm-curated.
- Surfaces books that HN's technical/intellectual community genuinely recommends, including niche titles that wouldn't surface elsewhere.
- Simple scraping + aggregation approach; the value is entirely from the source community's signal quality.
- Useful for finding adjacent and surprising reads outside the mainstream reading lists.

[Original](https://hackernewsbooks.com/)
