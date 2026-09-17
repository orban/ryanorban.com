---
title: "Hadoop 2.0 & YARN: The Big Data Breakthrough"
date: 2013-05-24
categories:
  - hadoop
  - yarn
  - big-data
  - distributed-systems
  - mapreduce
description: ReadWrite's accessible overview of Hadoop 2.0 and YARN, explaining why the resource manager redesign was a bigger deal than an incremental release — it turned Hadoop from a MapReduce platform into a general-purpose cluster resource manager.
params:
  source: pinboard
  sourceUrl: http://readwrite.com/2013/05/24/hadoop-20-yarn-bid-data-mapreduce
---

![Hadoop 2.0 & YARN: The Big Data Breakthrough](/images/notes/hadoop-2-yarn-breakthrough.png)

## Summary

ReadWrite's coverage explained why Hadoop 2.0 and YARN (Yet Another Resource Negotiator) represented a fundamental architectural shift rather than just an incremental upgrade. Hadoop 1.0's JobTracker was both a resource manager and a MapReduce job scheduler — meaning Hadoop clusters could only run MapReduce jobs. YARN decoupled these concerns: a generic ResourceManager handles cluster-wide resource allocation, and ApplicationMasters handle per-application scheduling.

The consequence: any computation framework could run on a YARN cluster alongside MapReduce. Apache Spark, Apache Tez, Apache Storm, and HBase could all coexist on the same cluster, sharing resources. This was the architectural prerequisite for Spark's rise — without YARN, Spark would have needed its own separate cluster infrastructure rather than reusing existing Hadoop deployments.

The article also covered the HDFS improvements in Hadoop 2.0: NameNode HA (high availability — no more single point of failure), HDFS Federation (multiple NameNodes serving different namespace partitions), and improved performance. These addressed the operational concerns that had made large-scale Hadoop deployments fragile in 1.0.

## Key points

- YARN separates resource management (ResourceManager) from job scheduling (ApplicationMaster per app)
- Enables non-MapReduce workloads on Hadoop clusters: Apache Spark, Tez, Storm, MPI
- NameNode HA: standby NameNode eliminates the single point of failure that plagued Hadoop 1.0
- HDFS Federation: multiple NameNodes serving different namespace volumes — scales metadata operations
- Released as Hadoop 2.2.0 GA in October 2013
- Apache Spark adoption accelerated dramatically because it could run on existing YARN clusters

[Original](http://readwrite.com/2013/05/24/hadoop-20-yarn-bid-data-mapreduce)
