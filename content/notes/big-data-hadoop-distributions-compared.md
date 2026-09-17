---
title: "Big Data: Hadoop Distributions Compared"
date: 2013-03-17
categories:
  - hadoop
  - big-data
  - cloudera
  - hortonworks
  - mapr
  - distributions
description: Comparison of the main commercial Hadoop distributions in 2013 — Cloudera CDH, Hortonworks HDP, and MapR — when the market was consolidating around a handful of vendors each taking different bets on what enterprises needed.
params:
  source: pinboard
  sourceUrl: http://blog.blazeclan.com/252/
---

## Summary

By early 2013, the commercial Hadoop ecosystem had consolidated around three main distributions: Cloudera CDH (Cloudera Distribution of Hadoop), Hortonworks HDP (Hortonworks Data Platform), and MapR. Each took a different approach to what enterprise Hadoop meant, and choosing between them was a real procurement decision for organizations investing in big data infrastructure.

Cloudera was first to market and led with proprietary management tooling — Cloudera Manager provided a polished UI for cluster operations, monitoring, and configuration management that the open-source ecosystem lacked. Cloudera also invested heavily in Impala, its own SQL-on-Hadoop engine that bypassed MapReduce entirely for interactive queries. Hortonworks took the opposite philosophical position: fully open-source, nothing proprietary, all contributions pushed back to Apache. This made HDP attractive to organizations concerned about vendor lock-in. MapR differentiated on the storage layer — replacing HDFS with their own MapR-FS that offered better random read/write performance, NFS mounting, and no single-point-of-failure NameNode.

The distribution wars reflected genuine engineering tradeoffs. Organizations with strong open-source commitments gravitated to Hortonworks. Those that wanted the best out-of-box operational experience chose Cloudera. Workloads with mixed analytics and operational use cases — where HDFS's append-only model was a bottleneck — considered MapR.

## Key points

- Three main distributions in 2013: Cloudera CDH, Hortonworks HDP, MapR — each with different tradeoffs on openness vs. features.
- Cloudera added proprietary tooling (Cloudera Manager, Impala) on top of open-source Hadoop — strongest management UX.
- Hortonworks was fully open-source with everything contributed back to Apache — good for avoiding vendor lock-in.
- MapR replaced HDFS with its own distributed filesystem supporting random I/O and NFS mounting — targeted mixed analytics/operational use cases.
- All three distributions have since been consolidated: Cloudera acquired Hortonworks in 2019; MapR was acquired by HPE in 2019.

[Original](http://blog.blazeclan.com/252/)
