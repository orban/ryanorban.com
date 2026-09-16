---
title: MySQL INSERT Speed Optimization
date: 2014-10-07
categories:
  - mysql
  - databases
  - performance
  - sql
description: MySQL 5.0 reference manual section on optimizing INSERT performance — covering bulk inserts, transaction batching, and buffer sizing. The reference for squeezing write throughput out of MySQL when ingestion speed matters.
params:
  source: pinboard
  sourceUrl: http://dev.mysql.com/doc/refman/5.0/en/insert-speed.html
---

## Summary

MySQL's reference manual section on INSERT speed covers the practical levers for improving write throughput — relevant when ingesting large volumes of data through a MySQL database. The core techniques have remained consistent across MySQL versions: batch inserts, transaction grouping, and buffer tuning.

The most impactful optimization is **bulk inserts**: using `INSERT INTO t VALUES (a,b), (c,d), (e,f)` instead of separate single-row INSERTs. A single multi-row INSERT amortizes the network round-trip and index update overhead across many rows. MySQL's `LOAD DATA INFILE` is even faster — it's a dedicated bulk load path that bypasses much of the normal row-insertion machinery.

Transaction grouping matters especially for InnoDB: every autocommitted INSERT flushes the InnoDB redo log to disk (if `innodb_flush_log_at_trx_commit=1`), so 1000 single-row INSERTs mean 1000 fsync calls. Wrapping them in a single explicit transaction drops this to one fsync. This is the single biggest performance gain available without schema changes.

Buffer tuning: `innodb_buffer_pool_size` controls how much data InnoDB keeps in memory. On a dedicated database server, setting this to 70-80% of RAM means indexes and recently written data stay in memory, dramatically reducing I/O during write-heavy workloads.

## Key points

- Multi-row `INSERT INTO t VALUES (...), (...), (...)`: amortizes network + index overhead — often 10-50x faster than single-row inserts.
- `LOAD DATA INFILE`: fastest bulk load path — bypasses normal insert machinery, processes CSV files directly.
- Transaction batching: wrap 100-1000 INSERTs in one explicit transaction to reduce fsync calls (critical for InnoDB).
- `innodb_buffer_pool_size`: set to 70-80% of RAM on dedicated servers — keeps hot data in memory.
- `innodb_flush_log_at_trx_commit=2`: reduces durability guarantee but can double write throughput (loses last second of data on crash).
- Context: shared in response to someone asking about MySQL write throughput — standard performance engineering.

[Original](http://dev.mysql.com/doc/refman/5.0/en/insert-speed.html)
