---
title: Cleaning Up Your Postgres Database
date: 2021-03-06
categories:
  - postgresql
  - database
  - maintenance
  - performance
  - devops
description: Crunchy Data's guide to PostgreSQL database maintenance — identifying bloat, reclaiming space with VACUUM, finding unused indexes, and cleaning up dead connections. Practical operations reference for keeping a Postgres database healthy.
params:
  source: pinboard
  sourceUrl: http://blog.crunchydata.com/blog/cleaning-up-your-postgres-database
---

![Cleaning Up Your Postgres Database](/images/notes/cleaning-postgres-database.png)

## Summary

Crunchy Data's guide covers the maintenance tasks that keep a PostgreSQL database healthy over time — the things that get neglected until they cause performance problems or disk exhaustion. The focus is on operations that are easy to forget because PostgreSQL mostly handles itself, until it doesn't.

Key areas: VACUUM and AUTOVACUUM for reclaiming space from dead tuples left by MVCC (Multi-Version Concurrency Control) — PostgreSQL doesn't overwrite old row versions immediately, it marks them dead and reclaims space lazily. When autovacuum falls behind (on tables with very high write volume), bloat accumulates. `pg_stat_user_tables` shows bloat; `VACUUM ANALYZE` forces cleanup and updates query planner statistics.

Unused indexes are another common source of overhead — they consume disk space and slow down writes without benefiting any query. `pg_stat_user_indexes` shows index scan counts; zero-scan indexes over a long period are candidates for removal. The guide also covers finding long-running queries (`pg_stat_activity`), idle-in-transaction connections that hold locks, and `pg_bloat` extension for measuring table and index bloat.

## Key points

- VACUUM / AUTOVACUUM: reclaims dead tuples from MVCC overhead — bloat accumulates when autovacuum falls behind on high-write tables.
- `pg_stat_user_indexes`: find indexes with zero scans — candidates for removal to recover write performance.
- `pg_stat_activity`: identify long-running queries and idle-in-transaction connections holding locks.
- `ANALYZE` updates query planner statistics — run after major data changes for accurate query plans.
- By Crunchy Data — a PostgreSQL professional services company, so advice is operationally grounded.

[Original](http://blog.crunchydata.com/blog/cleaning-up-your-postgres-database)
