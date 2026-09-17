---
title: "Running Elasticsearch: Fun & Profit"
date: 2021-01-06
categories:
  - elasticsearch
  - search
  - operations
  - distributed-systems
  - open-source
description: A free online book on running Elasticsearch in production — cluster sizing, index design, mapping, query optimization, and operational concerns like snapshots and upgrades. Practitioner-focused with real-world configuration guidance rather than API documentation.
params:
  source: pinboard
  sourceUrl: https://fdv.github.io/running-elasticsearch-fun-profit/
---

## Summary

*Running Elasticsearch: Fun & Profit* by Frédéric de Villamil is a free online book for practitioners running Elasticsearch clusters in production. It covers the full operational surface: cluster sizing, shard allocation strategies, index design, mapping configuration, query optimization, snapshot management, rolling upgrades, and monitoring. This is distinct from Elastic's official documentation — it's opinionated guidance from someone who has run ES at scale.

The book's value is the gap it fills between "I can run the getting-started tutorial and I understand why my cluster is behaving this way." Topics like shard sizing (more shards = more overhead, fewer shards = less parallelism — there's a sweet spot), mapping explosion (when dynamically mapped fields blow up index size), and fielddata vs doc_values (a distinction that matters for aggregation performance) are the kinds of things you only learn by running into problems.

Elasticsearch as a technology sits at the intersection of full-text search, log aggregation (ELK stack), and analytics. The book is most useful for engineering teams that run their own ES clusters rather than using managed services like Elastic Cloud or Amazon OpenSearch. For teams already on managed services, the operational chapters are less relevant, but the index design and query optimization sections apply regardless.

## Key points

- Covers production operations beyond the docs: shard sizing, mapping explosion prevention, snapshot configuration, rolling upgrades.
- Shard sizing guidance: the sweet spot principle — too many shards add overhead, too few limit parallelism.
- Mapping discipline: dynamic mapping is convenient but can blow up index sizes; explicit mapping is the production standard.
- Query optimization: filter context vs query context (filters are cached, queries are scored — use filters for yes/no conditions).
- Applies to self-managed Elasticsearch, OpenSearch, and adjacent tools like Solr for conceptual understanding.

[Original](https://fdv.github.io/running-elasticsearch-fun-profit/) → GitHub
