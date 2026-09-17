---
title: 5 Trends That Are Changing How We Do Big Data
date: 2012-11-03
categories:
  - big-data
  - hadoop
  - real-time
  - nosql
  - data-engineering
description: "GigaOM's 2012 survey of five trends reshaping big data: real-time processing rising against batch, NoSQL maturity, cloud-based data platforms, open-source ecosystem growth, and the shift from data collection to data monetization. A useful snapshot of where the field was heading at Hadoop's peak."
params:
  source: pinboard
  sourceUrl: http://gigaom.com/2012/11/03/5-trends-that-are-changing-how-we-do-big-data/
---

![5 Trends That Are Changing How We Do Big Data](/images/notes/5-big-data-trends.png)

## Summary

This GigaOM piece from November 2012 surveyed the major shifts underway in big data practice and infrastructure. In late 2012, Hadoop was the dominant framework for batch processing at scale, but several trends were beginning to expose its limitations and push the ecosystem in new directions. The piece captured this inflection — after Hadoop's success in batch ETL, the community was asking what came next.

The dominant trend was the push toward real-time or near-real-time processing. Apache Storm (which Twitter had open-sourced earlier that year) and nascent versions of Apache Spark were challenging the assumption that large-scale data processing required long-running batch jobs. Organizations that had built Hadoop clusters for overnight jobs were now being asked to provide results in seconds or minutes. This created the lambda architecture discussion — how to combine batch and streaming layers — that would dominate big data architecture thinking for the following three years.

The other major trends were NoSQL database maturity (with Cassandra, HBase, and MongoDB each finding distinct niches), the movement of data infrastructure to the cloud (early Amazon EMR, Redshift, and the beginning of what became the modern cloud data warehouse), and the shift in emphasis from data collection and storage to analytics and monetization. By 2012, many organizations had built large data lakes and discovered that having the data wasn't the bottleneck — extracting value from it was.

## Key points

- Real-time processing emerging alongside batch: Apache Storm and early Apache Spark pushed against the assumption that large-scale analytics required overnight jobs.
- NoSQL maturation: Cassandra, HBase, and MongoDB found distinct use cases rather than competing head-to-head — wide-column vs. document vs. key-value.
- Cloud data infrastructure beginning: early Amazon EMR and Redshift signaled the path to managed data infrastructure that would dominate by 2018.
- Data lakes hitting the value problem: organizations had collected data, now needed to extract insight — the analytics bottleneck replaced the storage bottleneck.
- Open-source ecosystem growth: 2012 saw the proliferation of tools around Hadoop (Hive, Pig, Sqoop, Flume) making it more accessible to non-Hadoop-expert engineers.

[Original](http://gigaom.com/2012/11/03/5-trends-that-are-changing-how-we-do-big-data/)
