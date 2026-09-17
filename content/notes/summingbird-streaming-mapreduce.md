---
title: Streaming MapReduce with Summingbird
date: 2013-09-04
categories:
  - twitter
  - streaming
  - mapreduce
  - scala
  - big-data
  - lambda-architecture
description: Twitter's Summingbird library unifies batch (Hadoop/Scalding) and streaming (Storm) MapReduce into a single Scala API — write once, run on either backend. An early practical implementation of the Lambda Architecture's dual-speed compute model.
params:
  source: pinboard
  sourceUrl: https://blog.twitter.com/2013/streaming-mapreduce-with-summingbird
---

![Streaming MapReduce with Summingbird](/images/notes/summingbird-streaming-mapreduce.png)

## Summary

Summingbird is a Scala library Twitter open-sourced in 2013 that lets you write a single MapReduce computation and run it on both batch (Hadoop/Scalding) and streaming (Storm) backends. The core idea: computations that aggregate data (count, sum, top-K, approximate counts via HyperLogLog) can be expressed abstractly using algebraic structures (monoids, semigroups), and those abstractions can be automatically parallelized and run either offline over historical data or online over live streams.

This was Twitter's practical implementation of the Lambda Architecture — Nathan Marz's design pattern for systems that need both low-latency approximate answers from a speed layer and accurate historical answers from a batch layer. The problem with Lambda was that you wrote the same logic twice (once for Storm, once for Scalding). Summingbird collapsed this by making the computation backend-agnostic: write the aggregation once, deploy to both layers.

The algebraic approach is elegant: if your reducer is a commutative monoid (a combining function that's associative and has an identity element), then Summingbird can split, parallelize, and merge partial results safely across any number of nodes and any execution order. This covers most practical aggregations: sums, counts, max/min, set unions, Bloom filters, HyperLogLog cardinality estimates.

## Key points

- Summingbird abstracts over backend: same code compiles to Scalding batch jobs or Storm streaming topology.
- Monoid-based aggregation: if your combine function is associative with an identity, Summingbird handles parallelization and partial results automatically.
- Lambda Architecture in practice: batch layer (Hadoop) for accuracy + speed layer (Storm) for recency, unified at the code level.
- Twitter Scale use cases: timeline aggregations, trending topics, ad metrics — all needed both historical analysis and real-time updates.
- Scalding: Twitter's Scala DSL on top of Cascading/Hadoop — Summingbird builds on it for the batch path.
- Historical note: Apache Spark Streaming largely superseded the Lambda pattern by 2016, but Summingbird was an early and influential attempt to solve the batch/stream unification problem.

[Original](https://blog.twitter.com/2013/streaming-mapreduce-with-summingbird)
