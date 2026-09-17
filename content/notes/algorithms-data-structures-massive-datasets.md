---
title: Algorithms and Data Structures for Massive Datasets
date: 2022-04-04
categories:
  - algorithms
  - data-structures
  - big-data
  - probabilistic
  - streaming
description: Manning 2021 textbook covering algorithms and data structures built for massive datasets — Bloom filters, HyperLogLog, Count-Min Sketch, LSH, and streaming algorithms. Practical treatment of how to handle data that won't fit in memory or where exact answers are too expensive.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/(Manning Early Access Program) Dzejla Medjedovic, Emin Tahirovic - Algorithms and Data Structures for Massive Datasets-Manning Publications (2021).pdf
---

## Summary

Dzejla Medjedovic and Emin Tahirovic (Manning, 2021) systematically cover the algorithmic toolkit for working with datasets too large for traditional in-memory approaches — both probabilistic data structures for approximate answers and streaming algorithms for single-pass computation. The book bridges the gap between academic treatments (which prove guarantees but skip implementation) and engineering resources (which implement but don't explain the math). It's aimed at practitioners who need to understand why these tools give the guarantees they do, not just how to import a library.

The probabilistic data structures section covers Bloom filters (set membership with tunable false-positive rate, zero false-negatives), Count-Min Sketch (frequency estimation for streams), HyperLogLog (cardinality estimation using minimal memory), and the Flajolet-Martin sketch. What unifies them is the idea that by relaxing the requirement for exact answers, you can achieve orders-of-magnitude improvements in memory footprint. A Bloom filter uses ~10 bits per element for a 1% false-positive rate; exact set membership with a hash set uses 64+ bits per element.

The streaming algorithms coverage includes reservoir sampling (uniform random sample from a stream of unknown length), frequency estimation (heavy hitters, frequent elements), and [locality-sensitive hashing](/notes/locality-sensitive-hashing/) (LSH) for approximate nearest neighbor search. LSH is particularly important for the modern era because it underlies much of the infrastructure for vector search, deduplication, and near-duplicate detection at scale. The book connects these classical streaming results to their practical applications in modern data engineering.

## Key points

- Bloom filters: configurable false-positive rate via multiple hash functions, O(k) time per query, no false negatives — fundamental for cache pre-filtering and database index operations
- HyperLogLog: estimates cardinality of multi-billion datasets using kilobytes of memory, ±2% error — used in Redis `PFCOUNT`, Spark `approxCountDistinct`
- Count-Min Sketch: stream frequency estimation with additive error guarantees — finds heavy hitters in network traffic or click streams without materializing all items
- LSH: locality-sensitive hashing for approximate nearest neighbor search — projects high-dimensional vectors to hash buckets that preserve proximity, foundation for vector databases
- Reservoir sampling: O(n) algorithm for uniform random sample of size k from a stream of unknown length n — essential for unbiased sampling in production pipelines

[Original PDF →](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/(Manning%20Early%20Access%20Program)%20Dzejla%20Medjedovic%2C%20Emin%20Tahirovic%20-%20Algorithms%20and%20Data%20Structures%20for%20Massive%20Datasets-Manning%20Publications%20(2021).pdf)
