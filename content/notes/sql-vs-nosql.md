---
title: SQL vs. NoSQL
date: 2012-09-04
categories:
  - databases
  - sql
  - nosql
  - architecture
  - data-engineering
description: Linux Journal's SQL vs. NoSQL comparison from the height of the NoSQL hype cycle — a useful grounding piece that distinguished the different NoSQL categories (document, key-value, column-family, graph) and when each made sense. The pendulum has since swung back toward SQL for most use cases.
params:
  source: pinboard
  sourceUrl: http://www.linuxjournal.com/article/10770?page=0,0
---

## Summary

This Linux Journal piece appeared during the peak of NoSQL hype — the period (roughly 2010–2013) when MongoDB, Cassandra, Redis, CouchDB, and HBase were being positioned as replacements for relational databases rather than complements. The article took the more measured position: different database models exist because different data access patterns have genuinely different requirements.

The NoSQL movement had emerged from two separate pressures. One was scale: relational databases struggled to scale horizontally, and web companies like Amazon (Dynamo), Google (Bigtable), and Facebook (Cassandra) had built new database architectures to handle their workloads. The second was schema flexibility: relational databases require predefined schemas, which creates friction in fast-moving development where data shapes aren't fully known upfront. Document databases like MongoDB removed the schema requirement.

The piece distinguished the NoSQL categories that were often conflated: key-value stores (Redis, DynamoDB) for simple lookup by key; document databases (MongoDB, CouchDB) for schema-flexible JSON-like documents; column-family stores (Cassandra, HBase) for write-heavy, time-series-like workloads at scale; graph databases (Neo4j) for relationship-centric queries. These have different strengths and the choice should be driven by access patterns, not by which database had the best conference talk. The Google Spanner paper (saved the same week) was simultaneous evidence that strong consistency at scale was achievable — the NoSQL assumption that you had to give up ACID to scale was being challenged.

## Key points

- NoSQL categories are distinct: key-value (Redis), document (MongoDB), column-family (Cassandra), graph (Neo4j) — each optimizes for different access patterns
- Horizontal scaling and schema flexibility were the two main NoSQL value propositions, not a single unified advantage
- CAP theorem (Brewer): consistency, availability, partition tolerance — pick two. NoSQL systems typically chose availability + partition tolerance
- The BASE model (basically available, soft state, eventual consistency) vs. ACID is the fundamental tradeoff
- By 2015–2020 the pendulum swung back: PostgreSQL's JSON support, CockroachDB, Cloud Spanner showed relational + scale was achievable

[Original](http://www.linuxjournal.com/article/10770?page=0,0)
