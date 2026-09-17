---
title: HyperLogLog in Pure SQL
date: 2014-05-31
categories:
  - databases
  - sql
  - algorithms
  - probabilistic-data-structures
  - analytics
description: Periscope Data's post implementing HyperLogLog in pure SQL — a probabilistic cardinality estimator that counts distinct values using a fixed amount of memory regardless of dataset size. Clever engineering that demonstrates how probabilistic algorithms can be embedded in SQL-only environments.
params:
  source: pinboard
  sourceUrl: https://periscope.io/blog/hyperloglog-in-pure-sql.html
---

## Summary

HyperLogLog is a probabilistic data structure for cardinality estimation: it approximates COUNT(DISTINCT ...) over arbitrarily large datasets using a small, fixed amount of memory. The algorithm was introduced by Philippe Flajolet et al. in 2007 and achieves typical error rates under 2% using only a few kilobytes of state — regardless of whether you're counting thousands or billions of distinct values.

The Periscope Data post implements HyperLogLog in pure SQL — no custom extensions or UDFs required. The trick relies on hash functions already available in the database: you hash each value, count leading zeros in the hash (which follows a predictable distribution), and maintain a set of buckets that capture the maximum leading zeros seen in each partition. The harmonic mean of these bucket values estimates the cardinality.

This matters for analytics at scale because exact distinct count queries require storing every unique value seen — which is O(n) memory. HyperLogLog is O(1) in memory, making it practical for real-time analytics pipelines and large-scale data warehouse workloads. Apache Spark, Redis, BigQuery, and PostgreSQL have all built-in HLL support, but implementing it in SQL clarifies the mechanism and makes it portable.

## Key points

- HyperLogLog achieves ~2% error for distinct counts using a fixed memory budget — typically 12KB can handle any cardinality up to 10^18.
- The insight: the maximum number of leading zeros in a hash of n random values grows as log₂(n) — this is the information that drives the estimator.
- Multiple hash buckets (registers) average out variance — more registers → lower error, but more memory.
- Pure-SQL implementations rely on bit manipulation and aggregation functions; useful when custom extensions aren't available.
- Underpins real-time unique visitor counts in web analytics and user funnel analysis in data warehouses.

[Original](https://periscope.io/blog/hyperloglog-in-pure-sql.html)
