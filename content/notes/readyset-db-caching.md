---
title: "ReadySet: Transparent Database Caching Layer"
date: 2024-02-21
categories:
  - database
  - caching
  - postgres
  - mysql
  - rust
  - open-source
description: ReadySet is a Rust-built wire-compatible caching proxy for MySQL and PostgreSQL that sits between your app and database, incrementally maintaining cached query results via the replication stream. Drop-in deployment with no application code changes.
params:
  source: pinboard
  sourceUrl: https://github.com/readysettech/readyset
---

![ReadySet: Transparent Database Caching Layer](/images/notes/readyset-db-caching.png)

## Summary

ReadySet is a Rust-built caching proxy that sits between applications and existing MySQL or PostgreSQL databases. It intercepts queries, caches the results of designated SELECT statements, and incrementally updates those cached results as the underlying data changes by monitoring the database's replication stream. The result is performance approaching an in-memory key-value store without the manual cache invalidation work.

The key technical distinction from simpler caching approaches: ReadySet uses a **dataflow architecture** with materialized query views. When source data changes, the dataflow system propagates those changes incrementally to all affected cached views — so cached results stay consistent without needing explicit invalidation logic in application code. This works even for complex SQL queries.

Wire compatibility means existing PostgreSQL and MySQL clients and ORMs work without modification. It's a drop-in proxy — point your connection string at ReadySet instead of the database directly. ReadySet handles query routing, serving cached results for instrumented queries and passing others through to the real database.

## Key points

- Wire-compatible proxy for MySQL and PostgreSQL — no application code changes required.
- Incremental cache updates via database replication stream — no manual cache invalidation.
- Dataflow architecture with materialized query views keeps cached results consistent.
- Complex SQL queries supported — not just simple key lookups.
- Horizontal read scaling by distributing cached query load across nodes.
- Built in Rust for performance. Open-source.

[Original](https://github.com/readysettech/readyset) → GitHub
