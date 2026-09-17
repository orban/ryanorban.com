---
title: Apache HBase
date: 2012-07-07
categories:
  - hadoop
  - big-data
  - nosql
  - distributed-systems
  - apache
description: "Apache HBase's homepage from 2012 — the open-source implementation of Google Bigtable that added random-read/write access to Hadoop's otherwise write-once HDFS. HBase filled the gap MapReduce couldn't: low-latency lookups on data stored across a distributed cluster."
params:
  source: pinboard
  sourceUrl: https://hbase.apache.org/
---

![Apache HBase](/images/notes/apache-hbase-homepage.png)

## Summary

Apache HBase is a distributed, column-oriented NoSQL database built on top of HDFS — the open-source implementation of Google Bigtable. The fundamental gap it fills: HDFS is optimized for sequential writes (append-only) and full-scan reads. MapReduce batch jobs work well with this, but any use case requiring low-latency random reads or updates — looking up a single user's data, incrementing a counter, serving a recommendation in real-time — is impossible with HDFS alone. HBase adds a key-value store layer over HDFS that enables random reads and writes at millisecond latency.

The data model is sparse, distributed, and sorted by row key. Each row can have an arbitrary number of columns organized into column families (defined at table creation time). Rows are stored sorted by row key, enabling efficient range scans. A single HBase table can hold billions of rows and millions of columns. The architecture uses a master/region server model: a Master server manages cluster metadata and region assignment; RegionServers handle read/write requests for their assigned row ranges. ZooKeeper coordinates distributed state between them.

In the 2012 Hadoop ecosystem, HBase was the answer whenever real-time access to data stored in Hadoop was needed. Facebook used HBase for its Messages product (storing hundreds of billions of messages). Twitter used it for ad targeting. RSVP and other applications needing both Hadoop batch processing and low-latency online serving used HBase as the serving layer. The system worked, but the operational complexity — tuning ZooKeeper, region server memory, compaction — was high. Later alternatives like Apache Cassandra (more operationally tractable) and cloud-native services (Amazon DynamoDB, Google Cloud Bigtable) displaced HBase in many use cases.

## Key points

- Apache HBase = open-source Google Bigtable: random read/write at millisecond latency on data stored in HDFS.
- Column-family model: sparse, sorted by row key, billions of rows and millions of columns possible per table.
- RegionServer architecture: rows partitioned by key range into regions; each RegionServer handles a subset of regions.
- ZooKeeper for distributed coordination — metadata, leader election, region assignment state.
- Primary use case: the online serving layer for data ingested via MapReduce batch pipelines — the read path to Hadoop's write path.
- Used in production by Facebook (Messages), Twitter (ad targeting) in 2012; later displaced by Cassandra and managed cloud alternatives in many settings.

[Original](https://hbase.apache.org/)
