---
title: "Shark: Real-time Queries and Analytics for Big Data"
date: 2012-11-29
categories:
  - big-data
  - spark
  - sql
  - distributed-systems
  - data-engineering
description: O'Reilly Strata article on Shark — the precursor to Spark SQL that brought real-time interactive queries to Hadoop/Spark in 2012. Part of the wave of tools (Impala, Shark, Drill) that challenged Hive's batch-query dominance.
params:
  source: pinboard
  sourceUrl: http://strata.oreilly.com/2012/11/shark-real-time-queries-and-analytics-for-big-data.html
---

## Summary

Shark was a SQL-on-Spark query engine developed at UC Berkeley's AMPLab in 2012, designed to bring interactive query speeds to data stored in HDFS. It ran on top of early Apache Spark and provided a SQL interface orders of magnitude faster than Apache Hive for analytical queries — by keeping data in memory across queries rather than materializing intermediate results to disk.

The 2012 context: Hive had become the standard way to query data in Hadoop clusters, but it was slow — batch-oriented, writing every stage to disk. Google Dremel (and its open-source analog Apache Drill) had demonstrated that interactive query was possible at scale. Cloudera Impala (announced November 2012) was another direct response. Shark was Berkeley's answer, built on top of the Spark execution engine that the same lab had created.

Shark was eventually superseded by Spark SQL, introduced in Spark 1.0 (2014), which replaced Shark's approach of modifying Hive's execution engine with a native Spark query planner. Shark is historically important as an early demonstration of in-memory computing applied to SQL analytics — the approach that Databricks and Snowflake would build major companies around.

## Key points

- Shark built on Apache Spark to deliver interactive SQL queries vs. Hive's batch model
- Key innovation: intermediate results stay in memory rather than writing to HDFS between stages
- 2012 competition: Shark (Berkeley), Impala (Cloudera), Drill (MapR/Apache) — all attacking Hive latency
- Shark was eventually replaced by Spark SQL in 2014, which rewrote the query planner natively
- Part of the AMPLab ecosystem at Berkeley that produced Spark, Mesos, and Alluxio

[Original](http://strata.oreilly.com/2012/11/shark-real-time-queries-and-analytics-for-big-data.html)
