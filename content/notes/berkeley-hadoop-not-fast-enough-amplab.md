---
title: "Welcome to Berkeley: Where Hadoop Isn't Nearly Fast Enough"
date: 2013-04-18
categories:
  - hadoop
  - apache-spark
  - amplab
  - berkeley
  - big-data
  - distributed-systems
description: GigaOM's April 2013 profile of UC Berkeley's AMPLab making the case that Hadoop is too slow for interactive and iterative workloads — the academic origin story of Apache Spark, Shark (early Spark SQL), and Mesos. A snapshot of the moment Spark was about to go mainstream.
params:
  source: pinboard
  sourceUrl: http://gigaom.com/2013/04/17/welcome-to-berkeley-where-hadoop-isnt-nearly-fast-enough/
---

![Welcome to Berkeley: Where Hadoop Isn't Nearly Fast Enough](/images/notes/berkeley-hadoop-not-fast-enough-amplab.png)

## Summary

This GigaOM piece from April 2013 profiled UC Berkeley AMPLab at the moment its projects were gaining industry traction. The central argument: Hadoop MapReduce's batch-only, disk-heavy model was a bottleneck for the emerging class of workloads that required interactivity (ad-hoc queries answered in seconds, not minutes) and iteration (machine learning algorithms that require dozens or hundreds of passes over data). The lab's answer to this was Apache Spark, then only version 0.7.

AMPLab (Algorithms, Machines, and People Lab) was building what became the BDAS stack (Berkeley Data Analytics Stack): Apache Spark for in-memory compute, Shark (early Spark SQL) for interactive queries, MLlib for distributed machine learning, and Apache Mesos for cluster resource management. These projects were designed to work together as a coherent alternative to the Hadoop stack — not just faster batch, but interactive and iterative from the ground up.

The key technical bet: DRAM had gotten cheap enough that keeping datasets in memory between compute stages was economically viable. A k-means clustering job that required 100 MapReduce iterations (100 full HDFS read/write cycles) could run 100 iterations in memory with Spark, reducing wall-clock time from hours to minutes. The Resilient Distributed Dataset (RDD) abstraction was the mechanism: immutable, lazily-evaluated distributed collections that tracked lineage for fault recovery without checkpointing to disk.

## Key points

- AMPLab's key insight: commodity DRAM made in-memory distributed computation economically viable — obsoleting the disk-heavy MapReduce model
- Apache Spark was already in production at Facebook, Twitter, and Conviva by April 2013 (before the famous AMPLab Daytona GraySort benchmark in November 2013)
- Apache Mesos came from the same lab — Spark and Mesos were designed as a pair before YARN became dominant
- Shark (Spark-based SQL) was the forerunner of Spark SQL — showed that interactive query on HDFS data could be fast
- Michael Franklin, Ion Stoica, Scott Shenker were the faculty leads — Matei Zaharia was the Spark PhD student
- This was the turning point: academic projects like Spark moved from interesting research to production-critical within 18 months of this article

[Original](http://gigaom.com/2013/04/17/welcome-to-berkeley-where-hadoop-isnt-nearly-fast-enough/)
