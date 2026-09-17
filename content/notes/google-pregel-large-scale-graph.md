---
title: Large-Scale Graph Computing at Google (Pregel)
date: 2012-07-07
categories:
  - graph-processing
  - distributed-systems
  - big-data
  - google
  - research
description: Google Research's 2009 blog post introducing Pregel — their internal system for large-scale graph computation using a bulk-synchronous-parallel model. The post that launched the graph processing systems category and eventually spawned Apache Giraph, GraphX, and the whole vertex-centric computing tradition.
params:
  source: pinboard
  sourceUrl: http://googleresearch.blogspot.com/2009/06/large-scale-graph-computing-at-google.html
---

![Large-Scale Graph Computing at Google (Pregel)](/images/notes/google-pregel-large-scale-graph.png)

## Summary

This 2009 Google Research blog post introduced Google Pregel to the public — a system Google built internally for large-scale graph computation that established the vertex-centric programming model now used throughout distributed graph processing. MapReduce was Google's workhorse for batch data processing, but graph algorithms like PageRank, shortest paths, and community detection are inherently iterative: each round of computation depends on the results of the previous round. Forcing this into MapReduce meant a full job per iteration — expensive disk I/O and job startup costs that made it impractical for serious graph workloads.

Pregel addressed this with the BSP (bulk synchronous parallel) model. Computation happens in supersteps: every vertex executes its `compute()` function in parallel within a superstep, sends messages to neighbors, and then the framework synchronizes before starting the next superstep. This keeps state in memory between iterations, eliminating the disk I/O penalty. The programming model is deliberately simple — a vertex sees only its own value and the messages in its inbox — which makes it easy to reason about correctness and enables efficient distributed execution.

The Pregel paper (published formally at SIGMOD 2010) had significant impact. It inspired Apache Giraph (Facebook's open-source implementation), GraphX in Apache Spark, and GraphLab at CMU. The model influenced thinking about how to structure distributed computation for graph-structured data, and the insight that vertex-centric thinking maps naturally to the underlying graph topology proved durable. The 2012 bookmark was part of a broader big data research session alongside Apache Giraph, Dremel, YARN, Apache Hive, and Apache HBase.

## Key points

- Google Pregel introduced the vertex-centric (think like a vertex) programming model for large-scale iterative graph computation.
- BSP execution: vertices compute in parallel supersteps, passing messages to neighbors; global synchronization at superstep boundaries eliminates disk I/O between iterations.
- Problem: MapReduce requires a full job per iteration for graph algorithms — Pregel keeps state in memory across supersteps, cutting I/O to zero.
- Open-source successors: Apache Giraph (Facebook), GraphX (Apache Spark), PowerGraph — all derived from the Pregel model.
- Published at SIGMOD 2010; the blog post (2009) was the first public announcement.
- PageRank is the canonical Pregel example: each vertex sums incoming rank contributions, divides by out-degree, sends to neighbors — convergence in ~30 supersteps on billion-node graphs.

[Original](http://googleresearch.blogspot.com/2009/06/large-scale-graph-computing-at-google.html)
