---
title: Benchmarking High Performance I/O with SSD for Cassandra on AWS
date: 2012-07-19
categories:
  - cassandra
  - ssd
  - aws
  - performance
  - netflix
  - distributed-systems
  - benchmarking
description: Netflix's 2012 benchmark of SSD-backed Cassandra on AWS EC2 — showing 3-4x latency improvements over spinning disk for their use case. An early real-world data point on SSD economics in cloud distributed databases.
params:
  source: pinboard
  sourceUrl: http://techblog.netflix.com/2012/07/benchmarking-high-performance-io-with.html
---

## Summary

Netflix's 2012 tech blog post is a practical engineering document: they ran Cassandra on SSD-backed EC2 instances and measured the performance improvement over spinning disk configurations. The headline result was roughly 3-4x latency improvement for their read-heavy workloads, with the SSD advantage being most pronounced at the 99th percentile — exactly where it matters for user-facing services.

The context matters. In 2012, SSDs on cloud instances were new and more expensive than spinning disk. Netflix was already a heavy Cassandra user (it was a core part of their streaming infrastructure), and the engineering blog was influential — a Netflix uses X post carried significant weight in the ops community. This post effectively validated SSD as a serious option for Cassandra deployments, not just a premium curiosity.

Cassandra's access pattern is particularly well-suited to SSD: it writes sequentially to commit logs and compacts SSTables, while reads can be random. The random read case is where SSD shows the largest advantage over HDD — roughly 100x faster random access. The sequential write case is closer, but SSDs still win on throughput and latency consistency. The Netflix benchmark gave operators concrete numbers to plug into their own capacity planning.

## Key points

- Netflix measured 3-4x latency improvement for Cassandra on SSD vs HDD-backed EC2 instances in 2012.
- 99th percentile latency showed the greatest improvement — critical for user-facing services where tail latency matters.
- Cassandra's write path (sequential commit log + SSTable compaction) and read path (potentially random) map naturally to SSD strengths.
- The economic calculation changed significantly between 2012 and today: SSD cost per GB has dropped dramatically, making the tradeoff obvious in most cases now.
- Netflix engineering blog posts were highly influential in the ops community — this post accelerated SSD adoption for NoSQL deployments across the industry.

[Original](http://techblog.netflix.com/2012/07/benchmarking-high-performance-io-with.html)
