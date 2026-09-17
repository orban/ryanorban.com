---
title: PoWA — PostgreSQL Workload Analyzer
date: 2014-08-22
categories:
  - postgresql
  - databases
  - performance
  - monitoring
  - devops
description: PoWA (PostgreSQL Workload Analyzer) is a real-time statistics and workload analysis tool for PostgreSQL — collects query statistics, visualizes slow queries, and helps identify index and configuration improvements. A targeted alternative to generic APM tools for Postgres-specific performance work.
params:
  source: pinboard
  sourceUrl: https://dalibo.github.io/powa/
---

## Summary

PoWA (PostgreSQL Workload Analyzer) is an open-source performance monitoring and analysis tool for PostgreSQL, developed by Dalibo (a French PostgreSQL consulting company). It collects query statistics from PostgreSQL's `pg_stat_statements` extension, stores historical snapshots, and presents them in a web UI for trend analysis.

The core use case: identifying which queries are consuming the most time, how execution plans change over time, and where indexes are missing or underused. PostgreSQL ships with `pg_stat_statements` built in (since 9.2), which tracks execution count, total time, rows, and I/O per query. PoWA wraps this with historical tracking and visualization — `pg_stat_statements` alone only shows cumulative totals, not trends.

The architecture: a background worker polls `pg_stat_statements` at a configurable interval (default: every 5 minutes) and stores snapshots in dedicated PostgreSQL tables. A separate web UI renders charts of query performance over time, identifies regressions, and allows drilling into execution plans. This is PostgreSQL-native observability — purpose-built for the database rather than a generic APM overlay.

## Key points

- PoWA: PostgreSQL performance monitoring built on `pg_stat_statements` with historical snapshots and web UI.
- Identifies top time-consuming queries, missing indexes, and plan regressions over time.
- `pg_stat_statements`: built-in PostgreSQL extension tracking per-query execution stats — the foundation.
- Background worker polls stats at intervals, enabling trend analysis rather than just point-in-time snapshots.
- Dalibo (Paris) is one of the leading PostgreSQL consulting firms in Europe.
- Alternative to generic APM tools like Datadog or New Relic for deep Postgres-specific query analysis.

[Original](https://dalibo.github.io/powa/) → GitHub
