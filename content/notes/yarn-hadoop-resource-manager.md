---
title: "YARN: Yet Another Resource Negotiator"
date: 2013-03-19
categories:
  - yarn
  - hadoop
  - distributed-systems
  - resource-management
  - apache
description: Apache YARN (Yet Another Resource Negotiator) is the cluster resource management layer introduced in Hadoop 2 — the architectural change that turned Hadoop from a MapReduce system into a general-purpose distributed compute platform.
params:
  source: pinboard
  sourceUrl: https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/YARN.html
---

## Summary

YARN is the resource management framework introduced in Apache Hadoop 2.0 that fundamentally changed what Hadoop clusters could do. Before YARN, Hadoop clusters ran exactly one type of workload: MapReduce jobs. YARN decoupled the cluster resource management layer from the MapReduce programming model, making the cluster a general-purpose compute platform that multiple frameworks could share.

The architecture has three components: the **ResourceManager** (global cluster resource authority — one per cluster, tracks available CPU and memory across nodes), **NodeManagers** (per-machine agents that launch and monitor containers), and **ApplicationMasters** (per-application processes that negotiate resources from the ResourceManager and coordinate tasks within a container). Each application running on YARN provides its own ApplicationMaster — MapReduce has one, Apache Spark has one, Apache Tez has one.

This separation is what made YARN significant. Before it, if you wanted to run Spark on the same hardware as your Hadoop cluster, you needed separate clusters. With YARN, Spark became a YARN application and could co-exist with MapReduce jobs on the same cluster, competing for the same pool of CPU and memory. HDFS remained shared storage; YARN became the shared compute scheduler.

## Key points

- YARN separates resource management (ResourceManager + NodeManagers) from application logic (ApplicationMasters) — the core architectural insight.
- Any framework can run on YARN by implementing an ApplicationMaster: MapReduce, Apache Spark, Apache Tez, Apache Storm, HBase region servers.
- Container model: resources are allocated as CPU + memory containers on specific nodes; ApplicationMasters request containers and run tasks inside them.
- HDFS data locality still works under YARN — the ResourceManager tracks which nodes have which HDFS blocks and prefers local container placement.
- Released as part of Apache Hadoop 2.0 GA in October 2013; this bookmark predates that release, suggesting the docs were consulted during the 2.0 beta period.

[Original](https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/YARN.html) → AI agent
