---
title: Obsidian Omnisearch
date: 2022-10-16
categories:
  - obsidian
  - search
  - pkm
  - plugins
  - open-source
description: Omnisearch is an Obsidian plugin that replaces the native search with full-text search that 'just works' — ranking results intelligently based on match quality, note size, and recency. Solves Obsidian's long-standing weak native search with BM25-style relevance scoring.
params:
  source: pinboard
  sourceUrl: https://github.com/scambier/obsidian-omnisearch
---

## Summary

Omnisearch is a community plugin for Obsidian that replaces the built-in search with a significantly more capable full-text search engine. The native Obsidian search is basic — it finds text matches but doesn't rank results by relevance. Omnisearch uses minisearch under the hood to apply BM25-style relevance scoring, so the best matches surface first rather than appearing in arbitrary order.

The just works tagline refers to the out-of-box experience: install, and you have meaningfully better search without configuration. Results are ranked by how well they match the query, with adjustments for note length (avoiding bias toward long notes) and match position. There's also a Vim-style navigation mode and fuzzy matching for typo tolerance.

For heavy Obsidian users with large vaults, search quality becomes a genuine bottleneck. Omnisearch directly addresses this — it's one of the most downloaded community plugins precisely because the native search is so limited relative to the vault sizes people build up. Complements semantic search plugins (like those using local embeddings) by being fast and exact-match-capable.

## Key points

- Full-text search for Obsidian with relevance ranking — replaces weak native search.
- BM25-style scoring via minisearch library — matches ranked by quality, not just presence.
- Fuzzy matching handles typos; length normalization prevents bias toward long notes.
- One of the most-downloaded Obsidian community plugins.
- Works on desktop and mobile Obsidian.
- Open-source under GNU GPL v3.

[Original](https://github.com/scambier/obsidian-omnisearch) → GitHub
