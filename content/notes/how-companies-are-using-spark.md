---
title: How Companies Are Using Spark
date: 2013-11-12
categories:
  - apache-spark
  - big-data
  - data-engineering
  - distributed-systems
description: Strata/O'Reilly coverage of how companies were adopting Apache Spark in 2013, early in the engine's rise to ubiquity. A snapshot of early enterprise Spark use cases before it displaced Hadoop MapReduce as the default.
params:
  source: pinboard
  sourceUrl: http://preview.getprismatic.com/story/1384103679571?share=true
---

## Summary

By late 2013, Apache Spark had been released publicly but was still considered experimental in most production environments. This Strata piece (via Prismatic) documented real-world adoption patterns as companies began moving workloads off Hadoop MapReduce onto Spark's in-memory computation model. The core appeal was speed — Spark could be 10–100x faster than MapReduce for iterative algorithms like those used in machine learning.

Early adopters were using Spark for ETL pipelines that would have been painful in MapReduce, MLlib for distributed machine learning, and Spark Streaming for near-real-time processing. The UC Berkeley AMPLab origins gave Spark academic credibility, and the involvement of Databricks as a commercial backer gave enterprises a support path.

The article reflects a moment when data engineers and data scientists were first seriously evaluating whether Spark could replace their Hadoop stacks, or whether it was a complement for specific use cases. That ambiguity resolved quickly — by 2015 Spark had become the dominant big data processing framework.

## Key points

- Apache Spark's in-memory execution made it dramatically faster than Hadoop MapReduce for iterative workloads like machine learning.
- MLlib brought distributed ML (logistic regression, k-means, collaborative filtering) to the same unified framework as batch and streaming.
- Early enterprise adoption was cautious — many companies ran Spark on top of existing HDFS rather than replacing Hadoop wholesale.
- Databricks, founded by the original UC Berkeley AMPLab Spark team, provided commercial support and drove enterprise adoption.
- The 2013 window was Spark before it became the industry default — a rare look at adoption of a technology that would win decisively.

[Original](http://preview.getprismatic.com/story/1384103679571?share=true)
