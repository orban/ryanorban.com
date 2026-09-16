---
title: Apache Hadoop 2 Is Now GA
date: 2013-10-16
categories:
  - hadoop
  - big-data
  - yarn
  - distributed-systems
  - open-source
description: Hortonworks announcement that Apache Hadoop 2 reached general availability in October 2013 — introducing YARN as the cluster resource manager. A landmark release that decoupled compute from MapReduce and made Hadoop a general-purpose cluster platform.
params:
  source: pinboard
  sourceUrl: http://hortonworks.com/blog/apache-hadoop-2-is-ga/
---

![Apache Hadoop 2 Is Now GA](/images/notes/apache-hadoop-2-ga.png)

## Summary

Apache Hadoop 2.0 reaching general availability in October 2013 was a significant milestone in big data infrastructure. The headline addition was YARN (Yet Another Resource Negotiator) — a cluster resource management layer that decoupled Hadoop's compute capabilities from the MapReduce programming model. This was architecturally significant: before YARN, Hadoop clusters could only run MapReduce jobs. After YARN, other processing frameworks — including Apache Spark — could run on the same cluster, competing for resources alongside MapReduce.

Hortonworks, co-founded by former Yahoo engineers who had built much of the original Hadoop at Yahoo, was one of the primary commercial contributors to Hadoop 2. The GA announcement marked the end of a long development cycle and validated the investment enterprises had made in Hadoop clusters — their hardware would be usable for Spark, Tez, and other next-generation frameworks without a forklift upgrade.

HDFS improvements in Hadoop 2 also added HDFS Federation (multiple NameNodes, removing the single-node bottleneck) and HDFS High Availability (standby NameNode for failover). These addressed the two most serious reliability concerns with Hadoop 1 at scale.

## Key points

- YARN decoupled resource management from MapReduce — Hadoop clusters became a general platform, not just a MapReduce platform.
- Apache Spark, Tez, and other frameworks could now co-exist on YARN clusters alongside MapReduce workloads.
- HDFS improvements: Federation (multiple NameNodes) and High Availability (standby NameNode) — critical for production reliability.
- Released by Hortonworks (former Yahoo Hadoop team) in October 2013, coordinated with the broader Apache community.
- Milestone context: Apache Spark had been released earlier in 2013 and would become the dominant YARN application within 2 years.

[Original](http://hortonworks.com/blog/apache-hadoop-2-is-ga/)
