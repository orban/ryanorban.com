---
title: "YARN: Hadoop NextGen MapReduce"
date: 2012-07-07
categories:
  - hadoop
  - big-data
  - distributed-systems
  - yarn
  - mapreduce
description: YARN's official documentation from 2012 — the architecture that decoupled Hadoop cluster resource management from MapReduce. By separating resource negotiation into its own layer, YARN turned Hadoop from a MapReduce platform into a general-purpose cluster OS.
params:
  source: pinboard
  sourceUrl: https://hadoop.apache.org/common/docs/r0.23.0/hadoop-yarn/hadoop-yarn-site/YARN.html
---

![YARN: Hadoop NextGen MapReduce](/images/notes/yarn-hadoop-next-gen-mapreduce.png)

## Summary

YARN (Yet Another Resource Negotiator) was the architectural redesign of Apache Hadoop's resource management layer, separating cluster resource scheduling from the MapReduce programming model. In Hadoop 1.x, the JobTracker handled both resource management (what resources are available, which tasks run where) and MapReduce job scheduling — they were fused into one component. This coupling meant only MapReduce workloads could run on a Hadoop cluster. YARN split this into two parts: a global ResourceManager that allocates cluster resources, and per-application ApplicationMaster processes that negotiate with the ResourceManager on behalf of specific frameworks.

The architectural consequence was significant: any distributed computing framework could now run on a Hadoop cluster by implementing the ApplicationMaster interface. Apache Spark, Apache Storm, Apache Tez, and others could co-exist on the same cluster, competing for resources via YARN rather than requiring separate infrastructure. This transformed Hadoop from "the MapReduce platform" into a more general cluster operating system — a common substrate for heterogeneous workloads.

YARN shipped in Apache Hadoop 0.23 (2012) and became GA with Hadoop 2.0 in 2013. The 2012 documentation bookmark reflects the early period when YARN was still in the preview/incubator phase but already attracting significant interest as the path to multi-framework Hadoop clusters. In retrospect, YARN was a necessary stepping stone: it extended Hadoop's operational life by making it a viable substrate for Spark, delaying (but not preventing) the eventual shift to cloud-native compute over HDFS.

## Key points

- YARN decouples resource management from computation: ResourceManager allocates cluster resources; per-framework ApplicationMaster negotiates for them.
- Enables any framework (Apache Spark, Apache Tez, Apache Storm) to run on a Hadoop cluster — not just MapReduce.
- Ships in Hadoop 0.23 (2012); GA in Apache Hadoop 2.0 (2013).
- JobTracker split into ResourceManager (global) + ApplicationMaster (per-job) — removes the single point of failure and the MapReduce coupling.
- Makes Hadoop a cluster OS rather than a MapReduce engine — the foundation for heterogeneous workload execution.
- HDFS Federation added alongside YARN: multiple NameNodes remove the single-node storage bottleneck.

[Original](https://hadoop.apache.org/common/docs/r0.23.0/hadoop-yarn/hadoop-yarn-site/YARN.html)
