---
title: MapReduce Patterns, Algorithms, and Use Cases
date: 2013-04-27
categories:
  - mapreduce
  - hadoop
  - big-data
  - distributed-systems
  - algorithms
  - patterns
description: Ilya Katsov's comprehensive taxonomy of MapReduce design patterns — from basic counting and filtering through complex join strategies and graph algorithms. The field guide for wringing correct and efficient computation out of the MapReduce model.
params:
  source: pinboard
  sourceUrl: http://highlyscalable.wordpress.com/2012/02/01/mapreduce-patterns/
---

## Summary

This Highly Scalable Blog post by Ilya Katsov is a systematic taxonomy of MapReduce design patterns — the canonical reference for how to translate common computational problems into the map → shuffle → reduce model. Much of distributed systems programming in the Hadoop era (2010-2015) amounted to recognizing which pattern applied to your problem, so a well-organized catalogue like this was genuinely high-value.

The patterns are organized into categories: **Summarization** (counting, min/max, statistics, index building — these are the "easy" MapReduce jobs), **Filtering** (sampling, top-N records, distinct values — mapper does the filtering, reducer collects), **Data Organization** (structured-to-hierarchical conversion, partitioning, binning — restructuring data format without aggregation), and most importantly, **Join patterns** (reduce-side join, map-side join, semi-join). The join patterns matter because SQL joins that are trivial in a relational database become complex orchestrations in MapReduce — you have to explicitly manage how the datasets arrive at the same reducer.

The most instructive section covers iterative computation in MapReduce — algorithms like PageRank, k-means clustering, and matrix factorization that require multiple passes over the data. MapReduce's write-to-HDFS-between-iterations cost is exactly why Apache Spark later won: a k-means that requires 100 iterations means 100 full HDFS read-write cycles in Hadoop, versus 100 in-memory iterations in Spark. Understanding these patterns makes it obvious why in-memory computation was such a breakthrough.

## Key points

- **Summarization patterns**: counting (word count is the canonical hello-world), statistical aggregation, inverted index building
- **Join patterns**: reduce-side join (shuffle both datasets to reducer by key), map-side join (broadcast smaller dataset), semi-join (filter large dataset using smaller one)
- **Iterative patterns**: PageRank, k-means, matrix decomposition — each iteration requires a full MapReduce cycle, making HDFS I/O the bottleneck
- Top-N pattern: mappers emit candidates, single reducer takes global top-N — common in recommendation and ranking pipelines
- **Graph algorithms** (BFS, shortest path) map naturally to iterative MapReduce but are expensive due to per-iteration overhead
- These patterns are largely superseded by Apache Spark RDD operations and SparkSQL, but the conceptual taxonomy remains useful for reasoning about distributed computation

[Original](http://highlyscalable.wordpress.com/2012/02/01/mapreduce-patterns/)
