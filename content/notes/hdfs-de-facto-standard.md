---
title: "HDFS Has Won: De Facto Standard for Centralized Data Storage"
date: 2012-11-17
categories:
  - big-data
  - hadoop
  - hdfs
  - distributed-systems
  - data-engineering
description: A 2012 claim that HDFS had emerged as the de facto standard for centralized big data storage — a snapshot of a moment when Hadoop's dominance seemed settled. Written just before the data lake era that HDFS would define, and before object storage (S3) would eventually displace it.
params:
  source: pinboard
  sourceUrl: http://mark.chmarny.com/2012/11/hdfs-has-won-now-de-facto-standard-for.html
---

## Summary

In November 2012, Mark Chmarny declared that HDFS (the Hadoop Distributed File System) had emerged as the de facto standard for large-scale centralized data storage — the settled substrate on which big data analytics tools would run. The claim was reasonable given the landscape: Apache Hive, Apache Pig, Apache HBase, Apache Spark, and dozens of other tools had converged on HDFS as their storage layer.

The historical context is interesting. HDFS was designed after Google's GFS ([Google File System](/notes/google-file-system/)) paper and implemented as the storage layer for Apache Hadoop. By 2012, enterprises were building data lakes on HDFS — replacing siloed data warehouses with centralized Hadoop clusters. Cloudera, Hortonworks, and MapR had built businesses around it.

The post looks prescient in one dimension and wrong in another. HDFS-based architectures did define enterprise data infrastructure from 2012–2018. But by 2018, Amazon S3 and similar object storage services displaced HDFS for most use cases — lower cost, simpler operations, decoupled storage and compute. The data lakehouse on Delta Lake, Apache Iceberg, and Apache Hudi sits atop object storage today. HDFS "won" the 2012 battle but lost the longer war.

## Key points

- HDFS achieved ecosystem lock-in: Hive, Pig, HBase, Spark, Impala all assumed HDFS as storage
- 2012 data lake concept: one large HDFS cluster replacing multiple domain-specific data warehouses
- Major vendors: Cloudera, Hortonworks, MapR — all building on Hadoop/HDFS
- The HDFS won claim aged poorly: Amazon S3 object storage displaced HDFS after ~2016
- The compute/storage separation enabled by S3 + Spark made the HDFS coupling a liability

[Original](http://mark.chmarny.com/2012/11/hdfs-has-won-now-de-facto-standard-for.html)
