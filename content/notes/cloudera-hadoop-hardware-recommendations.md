---
title: Cloudera's Support Team Shares Some Basic Hardware Recommendations
date: 2013-02-14
categories:
  - hadoop
  - hardware
  - cloudera
  - infrastructure
  - big-data
description: Cloudera's 2010 hardware recommendations for Hadoop clusters — still relevant in 2013 when bookmarked. The canonical guidance on disk, RAM, and CPU specs for commodity Hadoop nodes before cloud deployments became dominant.
params:
  source: pinboard
  sourceUrl: http://blog.cloudera.com/blog/2010/03/clouderas-support-team-shares-some-basic-hardware-recommendations/
---

![Cloudera's Support Team Shares Some Basic Hardware Recommendations](/images/notes/cloudera-hadoop-hardware-recommendations.png)

## Summary

Cloudera's support team published these hardware recommendations in 2010, but they remained widely referenced in 2013 when bookmarked — because Hadoop hardware choices were still predominantly on-premises and the guidance had aged well. The core principle: Hadoop is designed for commodity hardware, but commodity has a specific meaning.

The recommendations were shaped by Hadoop's architecture: data locality (the NameNode routes compute to where data lives), sequential disk I/O (MapReduce reads and writes large files sequentially, so many commodity SATA spindles beat fewer expensive SCSI/SAS drives), and fault tolerance (replication factor 3 means hardware failure is expected and handled, so ECC DRAM and RAID are less critical than in traditional databases).

Typical 2010-2013 Hadoop worker node specs: 12-24 cores (for running multiple MapReduce tasks concurrently), 24-48GB RAM, 12 direct-attached SATA drives (no RAID — let HDFS handle replication), 1Gb NIC. The NameNode (metadata server) got more RAM and potentially SSDs because all filesystem metadata was held in memory. Network was 1Gb with 10Gb uplinks — most traffic was local after data locality, but shuffles crossed the network.

## Key points

- **Direct-attached SATA** over SAN: HDFS replication provides fault tolerance; RAID adds cost without benefit; SAN adds latency
- **Many cores**: MapReduce task parallelism benefits from 12-24 cores per node — more concurrent tasks mean better utilization
- **NameNode sizing**: all HDFS metadata held in JVM heap — production clusters needed 64-128GB+ RAM on the NameNode
- **No RAID**: controversial guidance — HDFS handles redundancy at the filesystem layer, making per-disk RAID redundant overhead
- Amazon EMR (2009) and Google Dataproc would eventually displace on-premises Hadoop for most workloads, making these hardware decisions obsolete for new deployments

[Original](http://blog.cloudera.com/blog/2010/03/clouderas-support-team-shares-some-basic-hardware-recommendations/)
