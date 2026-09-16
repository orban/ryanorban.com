---
title: Facebook Unveils Presto for 250 PB Data Warehouse
date: 2013-06-07
categories:
  - facebook
  - presto
  - big-data
  - sql-on-hadoop
  - distributed-systems
description: GigaOm's coverage of Facebook unveiling Presto, their distributed SQL query engine for interactive queries against a 250 petabyte data warehouse. Presto addressed the core limitation of Hive — batch latency — by using a pipelined execution model that avoided writing intermediate results to disk.
params:
  source: pinboard
  sourceUrl: http://gigaom.com/2013/06/06/facebook-unveils-presto-engine-for-querying-250-pb-data-warehouse/
---

## Summary

Facebook announced Presto in 2013 — a distributed SQL query engine built to run interactive queries against their 250 petabyte Hadoop-based data warehouse. This was a significant milestone: at the time, Hive was the standard way to query HDFS data, but Hive translated SQL to MapReduce jobs, which required multiple disk write cycles and took minutes to hours for common analytical queries. Presto addressed this directly.

Presto uses a pipelined, in-memory execution model: data flows between query stages without intermediate disk writes, and the engine keeps data in memory across the query plan rather than flushing to HDFS between stages. This reduces query latency from minutes (Hive/MapReduce) to seconds for many queries. Facebook engineers were running thousands of queries per day against petabyte-scale tables using Presto by the time they announced it.

This announcement was part of a broader wave — Cloudera Impala launched around the same time, and Apache Drill and Apache Tez were also in development. The shared insight: MapReduce was the wrong execution model for interactive SQL, and a new generation of engines was needed. Presto was later open-sourced and eventually became Trino.

## Key points

- Presto queries HDFS data via a pipelined, in-memory execution engine — no intermediate disk writes, unlike Hive
- Facebook's warehouse was 250 PB across multiple Hadoop clusters in 2013
- Latency: seconds (Presto) vs. minutes/hours (Hive + MapReduce)
- Presto supports standard ANSI SQL — analysts didn't need to learn new syntax
- Competes with Cloudera Impala (same era, similar approach), Apache Spark SQL (later)
- Eventually open-sourced; rebranded as Trino in 2020 when community forked from Facebook's stewardship
- Represented a critical inflection: the SQL-on-Hadoop problem forced a new wave of query engine design

[Original](http://gigaom.com/2013/06/06/facebook-unveils-presto-engine-for-querying-250-pb-data-warehouse/)
