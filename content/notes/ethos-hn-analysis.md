---
title: "Ethos: Hacker News analysis with vector embeddings"
date: 2026-02-13
categories:
  - tools
  - hacker-news
  - nlp
  - sentiment-analysis
  - open-source
description: Ethos analyzes Hacker News discussions using vector embeddings to surface concepts, entities, sentiment, and discourse patterns. Open-source, from devrupt.io.
params:
  source: pinboard
  sourceUrl: https://ethos.devrupt.io/
---

![Ethos: Hacker News analysis with vector embeddings](/images/notes/ethos-hn-analysis.png)

## Summary

Ethos is a web-based analysis tool for Hacker News discussions, created by devrupt.io and available as open source. The tagline: understand \what HN is really thinking\ — semantic analysis beyond keyword matching.

The tool uses vector embeddings to understand relationships between posts and comments semantically. The analysis surfaces six views: a Dashboard overview, Concepts (key ideas being discussed), Entities (important people, companies, topics), Sentiment (emotional tone), Discourse (discussion patterns), and Search. Each is a different lens on the same underlying HN data.

This sits in a small category of tools that treat HN as a structured data source worth analyzing deeply. HN discussions have a distinct character — technically sophisticated, often contrarian, reflecting the views of people building technology — so understanding the patterns in HN discourse has some signal value for tracking emerging technical ideas. Vector embeddings as the core analytical approach makes this more semantic than keyword-based trend tools.

## Key points

- Vector embeddings over Hacker News data for semantic analysis.
- Six analysis views: Dashboard, Concepts, Entities, Sentiment, Discourse, Search.
- Goes beyond keyword matching to find semantic relationships between posts/comments.
- Open source, created by devrupt.io.

[Original](https://ethos.devrupt.io/)
