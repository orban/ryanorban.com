---
title: Is There Room for SSDs in the Hadoop Framework?
date: 2013-05-14
categories:
  - ssd
  - hadoop
  - storage
  - performance
  - infrastructure
description: StorageTuning blog's technical assessment of where SSDs fit in Hadoop's storage hierarchy — evaluating specific bottlenecks (NameNode metadata, shuffle I/O, random reads) where flash storage provides measurable gains over spinning disk.
params:
  source: pinboard
  sourceUrl: http://storagetuning.wordpress.com/2011/10/19/is-there-room-for-solid-state-disks-in-the-hadoop-framework/
---

![Is There Room for SSDs in the Hadoop Framework?](/images/notes/ssd-in-hadoop-framework.png)

## Summary

This StorageTuning post gave a more technical assessment of SSD placement in Hadoop clusters, moving beyond the cost-per-GB debate to specific architectural bottlenecks where flash storage provides measurable gains. The key distinction: not all Hadoop I/O is equal, and knowing which operations are latency-sensitive vs. throughput-sensitive determines where SSD investment pays off.

The three primary candidates for SSD in Hadoop: the NameNode (stores all HDFS metadata in memory + journals to disk — SSD reduces journal write latency), the shuffle/sort temporary data directory (intermediate MapReduce data written and read back quickly — high random I/O), and OS and log directories (noisy neighbors that can saturate spinning disk bandwidth during heavy cluster activity).

The analysis prefigured the YARN era's more sophisticated resource isolation — in Hadoop 1.0, these I/O paths competed on the same spindles, so isolating NameNode metadata and shuffle data on SSD was a manual tuning recommendation rather than a configurable platform feature.

## Key points

- NameNode journal writes: latency-sensitive, small writes — high SSD benefit
- Shuffle/sort: `mapreduce.cluster.local.dir` — temporary data between map and reduce phases; heavy random I/O
- Separating OS, logs, and HDFS data onto separate spindles (or SSD vs. HDD) prevents I/O contention
- HDFS data blocks themselves: large sequential I/O — spinning disk competitive, SSD less critical
- By Hadoop 2.0 / YARN, per-node resource isolation improved; HDFS tiered storage added in Hadoop 2.6
- The post reads as a 2011 tuning guide — prescient about where SSD would eventually become standard

[Original](http://storagetuning.wordpress.com/2011/10/19/is-there-room-for-solid-state-disks-in-the-hadoop-framework/)
