---
title: Model for Massively Parallel Computation — MapReduce Theory
date: 2014-10-13
categories:
  - distributed-systems
  - mapreduce
  - big-data
  - algorithms
  - parallel-computing
description: Grigory Yaroslavtsev's theoretical treatment of MapReduce as a model for massively parallel computation — covering the MRC complexity class and what it tells us about which problems can be solved efficiently at scale.
math: true
params:
  source: pinboard
  sourceUrl: http://grigory.us/blog/mapreduce-model/
---

## Summary

MapReduce is commonly discussed as a programming model and infrastructure system, but Grigory Yaroslavtsev's post approaches it as a theoretical model of computation — what is the complexity class of problems that MapReduce can solve efficiently, and how does it relate to classical parallel computation models like PRAM?

The MRC (MapReduce Class) framework, developed by Karloff, Suri, and Vassilvitskii, models MapReduce computation in terms of rounds (iterations of map + reduce), memory per machine, and total memory across the cluster. A key result: many problems that require multiple sequential passes over data can be solved in $O(1)$ or $O(\log n)$ MapReduce rounds with appropriate algorithms — but other problems are provably hard to parallelize this way.

This theoretical lens is useful for understanding when Apache Spark (which generalized MapReduce to support iterative algorithms via in-memory caching) actually helps. Spark's advantage over Hadoop MapReduce is primarily reducing the I/O overhead between rounds — but if an algorithm fundamentally requires many sequential rounds, even Spark can't help much. The theoretical model predicts this.

## Key points

- MapReduce as a complexity model: MRC framework defines rounds, per-machine memory, and total memory as parameters.
- Karloff-Suri-Vassilvitskii result: many graph problems and sorting can be solved in $O(1)$ or $O(\log n)$ MRC rounds.
- Round complexity is the key bottleneck — each round requires a full shuffle phase.
- Apache Spark reduces I/O between rounds but can't reduce the number of rounds required by an algorithm's structure.
- Connection to PRAM: MapReduce is strictly weaker than PRAM in terms of what can be computed efficiently.
- Practical takeaway: algorithm design for distributed systems requires thinking about data locality and round minimization.

[Original](http://grigory.us/blog/mapreduce-model/)
