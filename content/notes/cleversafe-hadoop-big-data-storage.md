---
title: "Cleversafe and Hadoop: Combining Next Generation Storage with Big Data Analytics"
date: 2012-07-10
categories:
  - cleversafe
  - hadoop
  - distributed-storage
  - object-storage
  - big-data
description: Cleversafe's 2012 integration with Hadoop connected dispersed object storage (using information dispersal algorithms rather than replication) to the Hadoop analytics ecosystem. Later acquired by IBM and became IBM Cloud Object Storage.
params:
  source: pinboard
  sourceUrl: http://techcrunch.com/2012/07/09/cleversafe-and-hadoop-combining-next-generation-storage-with-big-data-analytics/
---

![Cleversafe and Hadoop: Combining Next Generation Storage with Big Data Analytics](/images/notes/cleversafe-hadoop-big-data-storage.png)

## Summary

Cleversafe was a Chicago-based company building dispersed storage using information dispersal algorithms (IDA) — a technique from cryptography where data is split into fragments such that any subset of fragments (e.g., 8 of 16) can reconstruct the original. Unlike RAID or replication, IDA-based storage provides configurable durability without storing full copies. Cleversafe's 2012 Hadoop integration made this storage architecture accessible to analytics workloads through a standard HDFS interface.

The technical differentiation mattered for certain workloads. At the time, the dominant Hadoop storage pattern was HDFS with 3x replication — meaning a 1PB dataset required 3PB of raw storage. Cleversafe offered comparable durability (configurable for higher than 3-replica reliability) at approximately 1.2-1.5x storage overhead. For organizations storing truly massive datasets, that economics difference was substantial. The tradeoff was CPU overhead for the encoding/decoding operations and higher latency compared to local HDFS.

The product positioning: use Cleversafe for cold/warm storage of large datasets, run Hadoop analytics against it via the integration. This separated the storage economics from the compute layer — a pattern that has since become standard (S3 + compute, GCS + BigQuery, Azure Data Lake + HDInsight). Cleversafe was ahead of the decoupled storage/compute model that Snowflake and others later built businesses on. It was acquired by IBM in 2015 and became IBM Cloud Object Storage.

## Key points

- Information dispersal algorithm (IDA): data split into N fragments, any K recover the original — provides higher durability than replication at lower storage overhead.
- Storage efficiency: 1.2-1.5x overhead vs. 3x for HDFS 3-replica — significant at petabyte scale.
- HDFS API compatibility: Hadoop jobs see Cleversafe as standard HDFS — no application changes needed.
- Early implementation of decoupled storage/compute architecture — separated the storage economics from the analytical engine, anticipating cloud data warehouse patterns.
- Acquired by IBM in 2015, became IBM Cloud Object Storage — now used in enterprise cloud workloads where erasure coding economics matter.

[Original](http://techcrunch.com/2012/07/09/cleversafe-and-hadoop-combining-next-generation-storage-with-big-data-analytics/)
