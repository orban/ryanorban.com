---
title: Why Apache Spark is a Crossover Hit for Data Scientists
date: 2014-03-04
categories:
  - apache-spark
  - data-science
  - hadoop
  - big-data
  - distributed-systems
description: Cloudera's post on why Apache Spark resonated with data scientists in ways Hadoop MapReduce never did — the interactive REPL, Python support, and in-memory computation made it feel like a supercharged pandas rather than a distributed systems project.
params:
  source: pinboard
  sourceUrl: http://blog.cloudera.com/blog/2014/03/why-apache-spark-is-a-crossover-hit-for-data-scientists/
---

## Summary

Cloudera's blog (likely authored by Sandy Ryza or Josh Wills) made the case in early 2014 for why Apache Spark was gaining traction with data scientists — not just distributed systems engineers — in a way that Hadoop MapReduce never had. The argument: Spark meets data scientists where they work.

The key differentiators: **Interactive shell** (Spark's `pyspark` and `spark-shell` provide a REPL for exploring data interactively — MapReduce requires submitting a compiled job for every iteration). **Python support**: `pyspark` let data scientists use the language they already knew rather than writing Java. **In-memory computation**: iterative algorithms (like k-means, logistic regression with SGD, PageRank) benefit enormously from keeping data in memory between iterations rather than writing to HDFS after every MapReduce step. **MLlib**: a growing library of distributed ML algorithms that used Spark's RDD model.

The crossover hit framing acknowledges that Spark was initially a distributed systems project but was achieving adoption from a completely different audience. Data scientists weren't adopting it because of its architectural elegance — they were adopting it because `pyspark` felt like a distributed Pandas that could handle datasets their laptops couldn't. This audience crossover is what accelerated Spark's ecosystem growth beyond what pure systems-focused tools achieved.

## Key points

- Apache Spark's REPL (`pyspark`, `spark-shell`): interactive exploration of distributed datasets — the missing feature that made Hadoop inaccessible to data scientists.
- In-memory computation: iterative ML algorithms that required many passes over data (gradient descent, EM) were 10-100x faster than Hadoop MapReduce's disk-based rounds.
- Python first-class support: data scientists could use familiar libraries and transition smoothly to distributed scale.
- MLlib: Spark's distributed ML library — logistic regression, k-means, collaborative filtering, decision trees, all on RDDs.
- The crossover pattern: technical infrastructure adopted by a new audience (data scientists) who had different priorities than the original users (systems engineers) — drove rapid ecosystem expansion.

[Original](http://blog.cloudera.com/blog/2014/03/why-apache-spark-is-a-crossover-hit-for-data-scientists/)
