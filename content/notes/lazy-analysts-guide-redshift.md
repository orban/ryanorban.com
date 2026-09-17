---
title: The Lazy Analyst's Guide to Amazon Redshift
date: 2015-09-11
categories:
  - amazon-redshift
  - sql
  - data-warehouse
  - analytics
  - periscope
description: Periscope Data's practical guide to Amazon Redshift — covering the distribution and sort key mechanics that determine query performance, plus common gotchas for analysts who know SQL but not columnar databases. Still one of the clearest explanations of why Redshift behaves differently from Postgres.
params:
  source: pinboard
  sourceUrl: https://www.periscope.io/amazon-redshift-guide
---

## Summary

This guide from Periscope Data (later acquired by Sisense) bridges the gap between knowing SQL and actually getting good performance out of Amazon Redshift. Redshift is built on a columnar storage architecture distributed across multiple compute nodes (slices), which means it has two categories of query behavior that surprise analysts coming from PostgreSQL or MySQL: excellent performance on aggregate queries across many rows, and poor performance on queries that trigger cross-node data movement.

The key Redshift-specific concepts are distribution keys (DISTKEY) and sort keys (SORTKEY). The distribution key determines how rows are spread across slices — if you join two tables without a shared distribution key, Redshift has to shuffle data across the network, which is expensive. The sort key determines how data is physically stored within each slice — range queries on the sort key skip large chunks of data, dramatically reducing I/O. Getting these wrong leads to queries that look fine in a small dataset and are catastrophically slow at production scale.

The "lazy" framing is the guide's strength: it focuses on the minimum a working analyst needs to understand to write queries that don't embarrass them in production, rather than the full distributed systems theory. The VACUUM and ANALYZE commands (maintaining sort order and statistics), the COPY command for bulk loading, and column encoding are the other major analyst-facing concepts.

## Key points

- Columnar storage + MPP architecture means aggregate queries are fast, ad-hoc point queries are not.
- Distribution key (DISTKEY) controls data placement across nodes — bad DISTKEY → expensive redistribution on joins.
- Sort key (SORTKEY) controls physical storage order — range queries on sort key skip huge data blocks.
- VACUUM reclaims space from deletes/updates; ANALYZE updates query planner statistics — both are maintenance requirements.
- Column encoding (compression) reduces storage and I/O — set automatically during COPY or must be set manually.
- Redshift ≈ PostgreSQL SQL dialect but behaves completely differently at scale — PostgreSQL intuitions don't transfer.

[Original](https://www.periscope.io/amazon-redshift-guide)
