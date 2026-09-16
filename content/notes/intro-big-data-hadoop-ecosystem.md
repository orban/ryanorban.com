---
title: Introduction to Big Data and Hadoop Ecosystem
date: 2013-03-17
categories:
  - hadoop
  - big-data
  - hdfs
  - mapreduce
  - ecosystem
description: A beginner's introduction to the Apache Hadoop ecosystem cataloguing all major components — HDFS, MapReduce, Hive, HBase, Pig, Mahout, Sqoop, ZooKeeper, and more. A useful taxonomy of the 2012-era Hadoop stack.
params:
  source: pinboard
  sourceUrl: https://pramanicks.wordpress.com/2012/07/31/introduction-to-big-data-and-hadoop-ecosystem-for-beginners-41/
---

![Introduction to Big Data and Hadoop Ecosystem](/images/notes/intro-big-data-hadoop-ecosystem.png)

## Summary

This WordPress post from Pramanick provides a systematic taxonomy of the Apache Hadoop ecosystem as it stood in mid-2012, bookmarked in early 2013 when this knowledge was actively useful for practitioners evaluating the stack. The post defines big data through the lens of the 4 Vs — Velocity, Volume, Variety, and Value — and then catalogs the ecosystem components.

The Hadoop ecosystem in 2012-2013 was not a single product but a constellation of Apache projects, each solving a specific problem in large-scale data pipelines. HDFS handled distributed storage with rack-aware replication across commodity hardware. MapReduce provided the fault-tolerant parallel compute model. Above that layer: Hive added SQL-like querying, Pig provided a dataflow scripting language (Pig Latin), and Mahout brought machine learning algorithms like clustering and collaborative filtering. HBase offered low-latency random read/write access on top of HDFS for cases where MapReduce's batch model was too slow.

Supporting infrastructure included ZooKeeper for distributed coordination and leader election, Sqoop for RDBMS-to-Hadoop data transfer, Chukwa for log collection, and Avro for data serialization. The variety and number of components was a practical challenge: assembling a working pipeline required understanding how each piece fit together.

## Key points

- HDFS: rack-aware replication, petabyte-scale storage across commodity hardware — the foundation everything else builds on
- MapReduce: parallel batch compute with automatic fault tolerance via speculative execution and task retry
- Hive + Pig Latin: SQL and dataflow abstractions over MapReduce for analysts who didn't write Java
- HBase: random read/write access on HDFS — fills the gap between batch MapReduce and low-latency lookups
- Mahout: distributed machine learning on Hadoop — collaborative filtering, clustering, classification at scale
- ZooKeeper: distributed synchronization service — the coordination substrate for HBase, Kafka, and others
- Sqoop + Flume: data ingest connectors — RDBMS and log streaming respectively

[Original](https://pramanicks.wordpress.com/2012/07/31/introduction-to-big-data-and-hadoop-ecosystem-for-beginners-41/)
