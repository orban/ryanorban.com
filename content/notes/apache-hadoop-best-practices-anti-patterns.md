---
title: "Apache Hadoop: Best Practices and Anti-Patterns"
date: 2013-04-25
categories:
  - hadoop
  - mapreduce
  - performance
  - best-practices
  - yahoo
description: Yahoo's engineering blog guide on Hadoop best practices and anti-patterns from the team that ran the world's largest Hadoop clusters in 2010 — practical tuning advice from first-hand production experience at scale.
params:
  source: pinboard
  sourceUrl: http://developer.yahoo.com/blogs/hadoop/posts/2010/08/apache_hadoop_best_practices_a/
---

![Apache Hadoop: Best Practices and Anti-Patterns](/images/notes/apache-hadoop-best-practices-anti-patterns.png)

## Summary

This Yahoo Hadoop engineering blog post came from the team that was running some of the world's largest Hadoop clusters in 2010 — Yahoo was using Hadoop for web indexing and ad targeting at multi-petabyte scale. The advice reflects what they learned operating at a scale that nobody else had reached yet, making it unusually authoritative compared to documentation written from a theoretical perspective.

The post organized advice around common anti-patterns: **Too many small files** (the HDFS NameNode stores file metadata in memory — millions of tiny files exhausts NameNode heap before exhausting actual storage), **Unbalanced reducers** (skewed key distributions cause one reducer to receive 90% of the data while others sit idle — the job's runtime is the slowest reducer), **Inefficient serialization** (using text format for intermediate data instead of binary formats like Avro or Sequence Files wastes I/O), and **Excessive network shuffle** (moving too much data between mappers and reducers when aggregation could happen locally with a Combiner).

The best practices section emphasized Combiners (mini-reducers that aggregate output locally on the mapper node before the network shuffle), proper partitioning (ensuring the custom Partitioner distributes keys evenly across reducers), and sizing input splits appropriately (too many small splits → excessive task startup overhead; too few large splits → poor parallelism).

## Key points

- Small files problem: HDFS NameNode holds all file metadata in RAM — millions of small files exhaust NameNode memory before disk fills up; use SequenceFiles or HBase for many-small-records use cases
- Data skew: uneven key distribution means one reducer processes most data — profile key distributions before running large jobs
- Combiner pattern: add a Combiner (same class as Reducer for commutative/associative aggregations) to reduce network shuffle volume dramatically
- Compression: compress intermediate data with LZO or Snappy (splittable + fast) — reduces shuffle I/O without requiring decompression for splits
- **Speculative execution**: Hadoop can re-launch slow (straggler) tasks — useful for heterogeneous hardware but creates correctness issues for non-idempotent operations
- Many of these anti-patterns are less relevant with Apache Spark (no shuffle to HDFS between stages) but the underlying data distribution principles remain applicable

[Original](http://developer.yahoo.com/blogs/hadoop/posts/2010/08/apache_hadoop_best_practices_a/)
