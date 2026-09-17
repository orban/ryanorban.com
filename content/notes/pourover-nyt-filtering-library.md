---
title: The PourOver Book — NYT's In-Browser Filtering Library
date: 2014-04-17
categories:
  - javascript
  - data-visualization
  - filtering
  - nyt
  - open-source
description: PourOver is an NYT-open-sourced JavaScript library for fast in-browser filtering and sorting of large collections. Built for news apps that need to let users slice thousands of items without server round-trips.
params:
  source: pinboard
  sourceUrl: http://nytimes.github.io/pourover/
---

## Summary

PourOver is a JavaScript library for fast, composable filtering and sorting of large collections in the browser, open-sourced by The New York Times. The design goal was interactive news apps: you have thousands of records (election results, restaurant inspections, crime data) and want users to filter and sort them instantly without server round-trips.

The library uses a set-based approach: filters are represented as bitsets over the collection, and combining filters (AND, OR, NOT) is a set operation rather than a linear scan. This makes multi-filter queries fast even on large client-side collections — O(n/64) with bit manipulation rather than O(n) per filter.

PourOver reflects the NYT's broader investment in D3.js-era open source tools for data journalism. The Times released several influential JavaScript tools during this period for building interactive graphics, including tools for map rendering and chart animation. The premise was that good interactive data visualization required libraries built specifically for editorial and data journalism use cases — not just generic charting tools.

## Key points

- Bitset-based filtering: each filter is a set of matching indices, combined via bit operations for speed.
- Designed for news apps: thousands of items, multi-dimensional filtering, instant feedback required.
- Open-sourced by The New York Times as part of their data journalism tooling investment.
- Composable: filters combine with AND/OR/NOT without linear scans through the full collection.
- Reflects the era when D3.js and custom JavaScript tools were standard for data journalism.

[Original](http://nytimes.github.io/pourover/) → GitHub
