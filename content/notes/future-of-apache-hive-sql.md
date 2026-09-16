---
title: Future of Apache Hive — SQL PASS BA 2013
date: 2013-04-16
categories:
  - hadoop
  - hive
  - sql
  - big-data
  - data-warehousing
description: Carter Shanklin's 2013 talk on the future of Apache Hive — covering the push to make Hive's HiveQL a proper SQL dialect with ACID semantics, better query planning, and sub-second latency. A snapshot of the war between SQL-on-Hadoop and traditional data warehouses.
params:
  source: pinboard
  sourceUrl: https://speakerdeck.com/cartershanklin/future-of-apache-hive-sql-pass-ba-2013
---

## Summary

In 2013, Apache Hive was the dominant query layer for Apache Hadoop — but it had serious limitations as an analytic platform. HiveQL was SQL-ish but not ANSI-compliant, queries took minutes even for simple aggregations, and it lacked ACID semantics for updates and deletes. Carter Shanklin's talk at SQL PASS BA 2013 laid out the roadmap for Hive to become a genuine SQL data warehouse, not just a batch query tool bolted onto HDFS.

The key initiatives at the time: Stinger Initiative (led by Hortonworks) aimed to make Hive 100x faster through ORC file format, query vectorization, and Tez execution instead of MapReduce; HCatalog unified the metadata layer so Hive, Pig, and other tools could share table definitions; and support for ACID transactions was on the roadmap to handle streaming updates from tools like Sqoop and Flume. The argument was that YARN (then coming in Hadoop 2.0) would give Hive the resource management it needed to coexist with real-time workloads.

This talk sat at the intersection of two competing visions for enterprise analytics: the incumbents (Teradata, Vertica, Netezza) defended the proprietary data warehouse, while the Hadoop ecosystem argued that commodity hardware + open formats would win on economics. The SQL compatibility push was Hive's answer to the warehouse vendors' strongest argument — that Hadoop was fine for ETL but couldn't replace a real query engine.

## Key points

- Apache Hive in 2013: functional but slow — minutes for queries that Impala or Presto would later handle in seconds.
- Stinger Initiative: Hortonworks-led effort to make Hive 100x faster via ORC format, vectorized execution, and Apache Tez (instead of MapReduce).
- ACID transactions: planned support for update/delete on Hive tables — closing the biggest semantic gap with traditional warehouses.
- HiveQL vs SQL: push toward ANSI SQL compliance so existing BI tools (Tableau, MicroStrategy) could connect without modification.
- The broader competition: Cloudera Impala, Facebook Presto, and Apache Drill all launched around this time as faster SQL-on-Hadoop alternatives.

[Original](https://speakerdeck.com/cartershanklin/future-of-apache-hive-sql-pass-ba-2013)
