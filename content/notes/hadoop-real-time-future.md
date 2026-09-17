---
title: 5 Reasons Why the Future of Hadoop Is Real-Time
date: 2013-03-07
categories:
  - hadoop
  - real-time
  - stream-processing
  - apache-storm
  - big-data
description: GigaOM's 2013 argument for why Hadoop was evolving toward real-time processing — covering YARN, Storm, and in-memory frameworks as the drivers. A snapshot of the moment when batch-only Hadoop started feeling inadequate.
params:
  source: pinboard
  sourceUrl: http://gigaom.com/2013/03/07/5-reasons-why-the-future-of-hadoop-is-real-time-relatively-speaking/
---

![5 Reasons Why the Future of Hadoop Is Real-Time](/images/notes/hadoop-real-time-future.png)

## Summary

In early 2013, Hadoop's reputation as a batch processing system was becoming a liability. The original MapReduce model was designed for jobs that could run for hours — not for use cases that needed answers in seconds or minutes. GigaOM's piece made the case that Hadoop's ecosystem was evolving to close this gap, and identified five forces driving that evolution.

The key drivers: YARN (in beta, releasing later that year) decoupled cluster resource management from MapReduce, enabling real-time frameworks to share cluster resources. Apache Storm, Twitter's open-sourced stream processing system, could run alongside Hadoop jobs and process individual events as they arrived. Apache Spark (just released publicly) was showing that in-memory computation could run iterative algorithms and interactive queries orders of magnitude faster than disk-based MapReduce. And HBase, the Hadoop ecosystem's key-value store, enabled random read/write access to data in HDFS — providing the random access pattern that batch MapReduce lacked.

The broader observation was that real-time in 2013 meant relative improvement over overnight batch jobs — processing latency measured in minutes or seconds, not milliseconds. True sub-millisecond streaming (Apache Flink, Kafka Streams) would come later. But the direction was clear: the ecosystem was adding layers of faster computation on top of HDFS as durable storage, moving away from MapReduce as the only compute model.

## Key points

- YARN was the architectural prerequisite for real-time on Hadoop — by separating resource management from MapReduce, it allowed streaming frameworks on the same cluster.
- Apache Storm (Twitter-developed, open-sourced 2011) was the leading stream processor in 2013 — processing individual events rather than batch files.
- Apache Spark 0.7 was showing in-memory iterative computation 10–100x faster than disk-based MapReduce for the right workloads.
- HBase provided random access to HDFS data, enabling serving layer queries that MapReduce couldn't support.
- In retrospect: Apache Flink and Kafka Streams solved true streaming better than Storm; Spark Streaming became the interim solution before those matured.

[Original](http://gigaom.com/2013/03/07/5-reasons-why-the-future-of-hadoop-is-real-time-relatively-speaking/)
