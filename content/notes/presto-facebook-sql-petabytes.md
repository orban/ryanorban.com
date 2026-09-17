---
title: "Presto: Interacting with Petabytes of Data at Facebook"
date: 2013-11-11
categories:
  - presto
  - facebook
  - sql
  - big-data
  - distributed-systems
description: Hacker News discussion on Facebook's newly open-sourced Presto SQL engine, capable of querying petabytes of data interactively. A watershed moment — before Presto, interactive SQL at Facebook scale wasn't possible.
params:
  source: pinboard
  sourceUrl: https://news.ycombinator.com/item?id=6684318
---

## Summary

Presto is a distributed SQL query engine built by Facebook to solve a specific problem: Hive queries over HDFS data took hours, which made ad hoc data exploration impractical. Analysts needed answers in seconds or minutes, not hours. Presto was built from scratch as a massively parallel processing (MPP) query engine that could return results from petabyte-scale datasets interactively.

The 2013 HN discussion captured the excitement around Facebook's decision to open-source Presto. The engine's architecture was novel: no MapReduce, no writing intermediate results to disk between stages, fully pipelined execution. This made it fundamentally different from Hive running on Hadoop — closer to Google's Dremel paper (which later became BigQuery) than to traditional MapReduce-based systems.

Presto used a federated connector model that let it query not just HDFS but multiple data sources — including Cassandra, relational databases, and custom connectors. This made it a query layer across Facebook's entire data infrastructure rather than just a faster Hive.

## Key points

- Presto solved interactive query latency at petabyte scale — something Hive on Hadoop MapReduce couldn't do (hours vs. seconds).
- Fully pipelined, in-memory execution with no disk writes between stages — architecturally closer to MPP databases than MapReduce.
- Open-sourced by Facebook in late 2013; became the foundation for Trino (after the original maintainers left Facebook).
- Federated connector model: query HDFS, Cassandra, MySQL, and other sources with the same SQL interface.
- Influenced the broader SQL-on-Hadoop category: Spark SQL, Impala, Drill all followed similar interactive query patterns.

[Original](https://news.ycombinator.com/item?id=6684318)
