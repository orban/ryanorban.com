---
title: Facebook Seeks Next-Generation Big Data Tools
date: 2012-09-29
categories:
  - facebook
  - big-data
  - hadoop
  - infrastructure
  - data-engineering
description: InformationWeek's 2012 report on Facebook's efforts to move beyond Hadoop for its next-generation big data infrastructure — one of the first major signals that the tech industry's heaviest Hadoop user was already looking past it.
params:
  source: pinboard
  sourceUrl: http://www.informationweek.com/software/business-intelligence/facebook-seeks-next-generation-big-data/240008120
---

## Summary

This InformationWeek piece from late 2012 reported that Facebook was actively seeking tools to move beyond its existing Hadoop-based data infrastructure. Coming from one of the world's heaviest Hadoop users — Facebook had been a major contributor to the Hadoop ecosystem and had deployed it at a scale that few others had reached — this was a significant signal about the limits of the MapReduce model.

Facebook's data infrastructure in 2012 was processing hundreds of terabytes daily through Hive on top of Hadoop, but the batch nature of the system created fundamental latency problems. Product teams asking questions about user behavior often waited hours for query results, limiting how quickly product decisions could be made. The company was also running into operational complexity at scale — managing enormous HDFS clusters with thousands of nodes required significant engineering overhead.

The article previewed what would become Facebook's Presto project (a distributed SQL query engine for interactive analytics that would be open-sourced in 2013) and pointed toward the broader trend of disaggregating the Hadoop stack. Instead of one system doing everything, the next generation would use specialized tools: Presto for interactive queries, Apache Spark for iterative computation, Apache Kafka for stream processing. This architectural decomposition — the post-Hadoop era — became the dominant infrastructure pattern by 2015.

## Key points

- Facebook's signal: one of Hadoop's biggest users was looking past it — a leading indicator for the broader industry's trajectory.
- Batch processing latency was the core problem: Hive queries taking hours prevented real-time product iteration.
- Precursor to Presto: Facebook was building interactive SQL on top of their distributed storage to replace slow Hive jobs.
- The disaggregation trend: instead of one Hadoop system for everything, specialized tools for each workload type.
- HDFS operational complexity at scale was also a growing cost — the management overhead of large clusters was significant.

[Original](http://www.informationweek.com/software/business-intelligence/facebook-seeks-next-generation-big-data/240008120)
