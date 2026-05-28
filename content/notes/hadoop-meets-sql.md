---
title: Hadoop Meets SQL
date: 2013-07-30
categories:
  - hadoop
  - sql
  - hive
  - impala
  - data-warehouse
description: IBM Big Data Hub's overview of SQL-on-Hadoop approaches in 2013 — Hive, Impala, and the broader push to make Hadoop queryable by the vast majority of analysts who knew SQL but not MapReduce. The SQL interface became the primary adoption driver for Hadoop in the enterprise.
params:
  source: pinboard
  sourceUrl: http://www.ibmbigdatahub.com/blog/hadoop-meets-sql
---

![Hadoop Meets SQL](/images/notes/hadoop-meets-sql.png)

## Summary

By mid-2013, the central challenge facing Hadoop adoption in enterprises was clear: most analysts knew SQL, not Java MapReduce. Hive (Facebook's SQL-on-Hadoop layer, open-sourced to Apache) had addressed this partially, but it generated slow MapReduce jobs unsuitable for interactive queries. This IBM Big Data Hub post surveyed the emerging SQL-on-Hadoop landscape: Hive, Cloudera Impala, Facebook Presto, Apache Drill, and IBM's BigSQL — each taking a different architectural approach to giving SQL users access to data in HDFS.

Cloudera Impala was the most aggressive bet: an MPP (massively parallel processing) SQL engine that ran as daemons on each Hadoop node, bypassing MapReduce entirely and querying HDFS data in seconds rather than minutes. Presto (being built at Facebook but not yet open-sourced) took a similar approach. Apache Drill aimed for a more schema-free JSON-native experience. Hive was adding Tez as a faster execution engine to compete.

The SQL interface on Hadoop race was driven by the same insight: the BI analyst workforce spoke SQL; making Hadoop speak SQL back was the only realistic enterprise adoption path. This race essentially ended when Apache Spark SQL absorbed most of the market and cloud data warehouses (Amazon Redshift, Snowflake, BigQuery) made the question moot for most organizations.

## Key points

- Hive: SQL translated to MapReduce jobs — correct but slow (minutes to hours); the standard enterprise-grade SQL-on-Hadoop in 2013.
- Cloudera Impala: MPP SQL engine bypassing MapReduce entirely — interactive query speeds (seconds) but required its own daemon infrastructure.
- Presto (Facebook): similar MPP architecture to Impala; open-sourced later in 2013 — evolved into Trino and became dominant in federated query scenarios.
- Apache Drill: aimed for schema-free SQL across JSON, Parquet, and HDFS — lower adoption than Impala but interesting for heterogeneous data.
- Tez project: Apache project to replace MapReduce as Hive's execution engine with a general DAG-based execution model — Hive on Tez was significantly faster.
- Long-term winner: Spark SQL and cloud data warehouses made most SQL-on-Hadoop projects obsolete by 2018.

[Original](http://www.ibmbigdatahub.com/blog/hadoop-meets-sql)
