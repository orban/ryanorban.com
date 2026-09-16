---
title: New Tools Simplify the Power of Hadoop
date: 2012-09-18
categories:
  - hadoop
  - big-data
  - tools
  - ecosystem
  - data-engineering
description: InformationWeek's 2012 survey of tools making Hadoop more approachable for enterprise practitioners — the abstraction layers (Hive, Pig, HBase) and commercial distributions (Cloudera, Hortonworks) that were papering over Hadoop's low-level complexity. Captures the ecosystem's maturation moment.
params:
  source: pinboard
  sourceUrl: http://www.informationweek.com/big-data/news/big-data-analytics/240007462/new-tools-simplify-power-of-hadoop
---

![New Tools Simplify the Power of Hadoop](/images/notes/hadoop-ecosystem-tools.png)

## Summary

By September 2012, Apache Hadoop had established itself as the reference big data platform, but its raw complexity was limiting enterprise adoption. Most organizations couldn't staff Java-fluent engineers who could write MapReduce jobs from scratch. The ecosystem response was a proliferation of abstraction layers — tools that let analysts and engineers work with Hadoop at a higher level of abstraction without touching Java or MapReduce directly.

InformationWeek surveyed the major tools making Hadoop more accessible: Apache Hive (SQL-like queries translated to MapReduce jobs, created at Facebook), Apache Pig (dataflow scripting language with high-level operations), HCatalog (metadata table management), and Apache Sqoop (bulk data transfer between RDBMS and HDFS). On the commercial side, Cloudera and Hortonworks were packaging these tools into managed distributions with enterprise support, simplified installation, and management interfaces.

The piece also covered the emerging real-time and streaming tools trying to address Hadoop's batch-only limitation. Apache HBase provided random-access reads and writes on HDFS, enabling lower-latency queries. Apache Storm was beginning to provide stream processing. This was the early version of the lambda architecture pattern — combining Hadoop's batch layer with faster systems for stream processing. The implicit critique of Hadoop: it was a batch system wearing a general-purpose outfit, and the ecosystem was compensating for its limitations rather than fixing them.

## Key points

- Apache Hive (originally Facebook): SQL-to-MapReduce translation — the single most important Hadoop accessibility tool for analysts
- Apache Pig: dataflow scripting language (Pig Latin) for ETL operations — more flexible than SQL, less verbose than raw MapReduce
- Cloudera and Hortonworks as commercial distributions: enterprise packaging, support, and management UI on top of open-source components
- Lambda architecture emerging: batch layer (Hadoop) + speed layer (Storm, later Spark Streaming) — addressing Hadoop's batch-only limitation
- The sophistication required even with these tools was high — the simplification was relative, not absolute

[Original](http://www.informationweek.com/big-data/news/big-data-analytics/240007462/new-tools-simplify-power-of-hadoop)
