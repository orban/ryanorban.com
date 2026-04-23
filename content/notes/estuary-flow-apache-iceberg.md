---
title: "Estuary Flow: Apache Iceberg Materialization Connector"
date: 2025-05-29
categories:
  - data-engineering
  - apache-iceberg
  - estuary-flow
  - streaming
  - data-lakehouse
description: Estuary Flow's Apache Iceberg materialization connector writes streaming Flow collections into Iceberg tables on object storage — bridging real-time CDC streams into the open lakehouse table format. A key integration for streaming-to-lakehouse pipelines.
params:
  source: pinboard
  sourceUrl: https://docs.estuary.dev/reference/Connectors/materialization-connectors/apache-iceberg/
---

![Estuary Flow: Apache Iceberg Materialization Connector](/images/notes/estuary-flow-apache-iceberg.png)

## Summary

Estuary Flow is a real-time CDC (Change Data Capture) and data pipeline platform that captures, transforms, and materializes data streams. The Apache Iceberg connector materializes Flow collections — Estuary's abstraction for streaming data — into Apache Iceberg tables stored on object storage (S3-compatible).

This is a bridge between the streaming world and the data lakehouse ecosystem. You can continuously capture changes from databases (PostgreSQL, MySQL, MongoDB) via CDC into Estuary collections, then materialize those streams as Iceberg tables that Spark, Trino, DuckDB, or Mooncake can read. The result: real-time CDC feeds a queryable, open-format table without custom transformation code.

Apache Iceberg as a materialization target is significant because of its interoperability. Unlike writing to a proprietary format, Iceberg tables are readable by any engine that speaks the format — giving you flexibility to swap query engines without re-ingesting data. Combined with Estuary Flow's continuous streaming, you get a lakehouse with sub-minute freshness rather than nightly batch loads.

## Key points

- Estuary Flow → Apache Iceberg: materializes streaming collections into open-format lakehouse tables.
- CDC source → Iceberg output: database changes flow continuously into queryable Iceberg tables.
- Object storage backend: S3-compatible, cost-efficient at scale.
- Interoperable: Iceberg tables readable by Spark, Trino, DuckDB, Mooncake, and others.
- Enables near-real-time freshness in the lakehouse — not overnight batch.
- Complements tools like Mooncake (Postgres-native Iceberg analytics) in the lakehouse ecosystem.

[Original](https://docs.estuary.dev/reference/Connectors/materialization-connectors/apache-iceberg/)
