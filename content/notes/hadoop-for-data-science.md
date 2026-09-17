---
title: Hadoop for Data Science
date: 2014-01-09
categories:
  - hadoop
  - data-science
  - big-data
  - distributed-computing
  - pig
description: Mortar Data's introduction to Hadoop for data scientists — when to use it, what the MapReduce programming model actually means, and how Pig Latin abstracts away the low-level boilerplate.
params:
  source: pinboard
  sourceUrl: http://blog.mortardata.com/post/61501767090/hadoop-for-data-science
---

## Summary

Mortar Data — a Hadoop-as-a-service startup — published this introduction for data scientists who needed to understand when and how to use Hadoop. The post explains the MapReduce programming model in practical terms: break computation into a map phase (apply a function independently to each record) and a reduce phase (aggregate results by key). For data that fits on a single machine, MapReduce is slow and overkill; for terabytes distributed across a cluster, it's the right abstraction.

The tutorial also introduces Pig Latin — the dataflow scripting language that sits above MapReduce and makes common transformations like joins, filters, and aggregations expressible without writing raw Java map/reduce code. In 2014, Pig was a common stepping stone before Spark made distributed data manipulation significantly more ergonomic.

## Key points

- MapReduce model: map applies a function to each record in parallel across nodes; reduce aggregates by key after shuffling — fault-tolerant via HDFS replication
- Pig Latin abstracts the boilerplate away, exposing a SQL-like dataflow language that compiles to MapReduce jobs
- The choice of Hadoop vs single-machine tools depends on data volume — for anything that fits in memory, pandas or R is faster and easier
- Mortar allowed running Pig scripts on Amazon EMR without managing cluster infrastructure — a 2014 version of managed Spark services
- Apache Spark replaced most Hadoop/MapReduce workflows by 2016, but understanding the MapReduce model remains useful context for distributed systems

[Original](http://blog.mortardata.com/post/61501767090/hadoop-for-data-science)
