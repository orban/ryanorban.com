---
title: Querying Live Crypto Trades with SQL in Real-Time
date: 2022-04-14
categories:
  - time-series
  - databases
  - crypto
  - sql
  - real-time
description: QuestDB tutorial showing how to query live cryptocurrency trade data in real-time with SQL — ingesting from Coinbase's WebSocket feed into QuestDB and running time-series queries. A practical demo of time-series SQL for financial market data.
params:
  source: pinboard
  sourceUrl: https://questdb.io/blog/2022/04/12/query-live-crypto-trades-with-sql-in-real-time/
---

## Summary

This QuestDB tutorial demonstrates ingesting real-time cryptocurrency trade data from Coinbase's WebSocket feed into QuestDB and querying it with SQL as trades arrive. QuestDB is a high-performance time-series database that exposes a standard SQL interface — you write familiar SQL, but with time-series-specific extensions (`SAMPLE BY`, `LATEST ON`, `ASOF JOIN`) that make temporal queries concise and fast.

The architecture is straightforward: a process subscribes to the Coinbase WebSocket feed (which streams every trade), writes each trade to QuestDB over its PostgreSQL wire protocol, and then arbitrary SQL queries can run against the live data. The `SAMPLE BY` clause aggregates trades into OHLCV bars (open/high/low/close/volume) for any time interval in a single query line — what would require a multi-step window function in standard SQL is one clause in QuestDB's dialect. `LATEST ON` gives the last record per partition (the current price per symbol) efficiently.

The broader point the tutorial makes is about time-series databases as a category: financial market data, sensor data, and logs all have the same structure — a timestamp plus a value — and general-purpose databases handle it poorly. QuestDB stores time-ordered data in columnar append-only partitions, processes SIMD-accelerated aggregations over time ranges natively, and achieves ingestion rates in the millions of rows per second on commodity hardware. The SQL interface means you don't need to learn a new query language; the architecture means you get performance that PostgreSQL or MySQL can't match for temporal workloads.

## Key points

- QuestDB: time-series database with SQL interface + time-specific extensions (`SAMPLE BY`, `LATEST ON`, `ASOF JOIN`).
- Real-time ingestion from Coinbase WebSocket feed — trades land in the database as they happen.
- `SAMPLE BY` builds OHLCV bars for any interval in one line — equivalent of multi-step window functions in standard SQL.
- PostgreSQL wire protocol compatibility: any Postgres client works, standard tooling applies.
- Time-series databases as a category: append-only columnar storage + SIMD aggregations = orders of magnitude faster than RDBMS for temporal queries.
- Competes with InfluxDB, TimescaleDB (Postgres extension), ClickHouse in the time-series analytics space.

[Original](https://questdb.io/blog/2022/04/12/query-live-crypto-trades-with-sql-in-real-time/)
