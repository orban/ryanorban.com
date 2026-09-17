---
title: "Mooncake: Analytics Database Inside Postgres"
date: 2025-05-29
categories:
  - postgres
  - analytics
  - timeseries
  - iceberg
  - object-storage
description: Mooncake is an analytics layer inside Postgres — fast columnar timeseries and analytics built on object storage and Apache Iceberg, no ETL required. Brings data warehouse performance to Postgres without leaving it.
params:
  source: pinboard
  sourceUrl: https://mooncake.dev
---

![Mooncake: Analytics Database Inside Postgres](/images/notes/mooncake-postgres-analytics.png)

## Summary

Mooncake extends Postgres with a fast analytics engine for timeseries and OLAP workloads, built on object storage and Apache Iceberg as the table format. The positioning is "bring the data warehouse into Postgres" rather than the traditional approach of ETLing data out to a separate analytics system.

The architectural bet is that Apache Iceberg's open table format plus cloud object storage (S3-compatible) gives you near-warehouse performance at warehouse-like scale, but without the operational overhead of a separate cluster. Your operational and analytical queries share the same Postgres endpoint — no separate ClickHouse or BigQuery to maintain, no ETL pipeline to break.

This connects to a broader trend of Postgres extensions doing things that used to require dedicated systems: pgvector for vector search, TimescaleDB for timeseries, and now Mooncake for analytics. The pattern suggests Postgres is becoming a platform, not just a database. The Apache Iceberg integration is particularly interesting since it enables interop with the broader data lakehouse ecosystem — data written by Mooncake can be read by Spark, Trino, or other Iceberg-compatible tools.

## Key points

- Analytics database built into Postgres — no ETL to a separate system.
- Built on Apache Iceberg (open table format) + object storage — interoperable with lakehouse tools.
- Targets timeseries and OLAP workloads that traditionally required dedicated engines.
- Follows the pattern of pgvector, TimescaleDB: Postgres as a platform with specialized extensions.
- Single endpoint for operational and analytical queries.
- Potential for columnar storage advantages (compression, scan speed) within Postgres.

[Original](https://mooncake.dev)
