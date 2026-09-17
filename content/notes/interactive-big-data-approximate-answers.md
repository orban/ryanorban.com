---
title: Interactive Big Data Analysis Using Approximate Answers
date: 2013-08-18
categories:
  - big-data
  - approximate-query-processing
  - streaming
  - algorithms
  - data-engineering
description: O'Reilly Strata coverage of approximate query processing for interactive big data analysis — using sketches and sampling to get fast approximate answers over large datasets when exact computation is too slow. An important design pattern for data products that prioritize responsiveness over precision.
params:
  source: pinboard
  sourceUrl: http://strata.oreilly.com/2013/08/interactive-big-data-analysis-using-approximate-answers.html
---

## Summary

This O'Reilly Strata piece covered approximate query processing (AQP) — the class of techniques that trade exactness for speed by returning statistically sound approximate answers over large datasets rather than exact counts. The core insight: for many analytical workloads, an answer that's 99% accurate and returns in 100ms is more valuable than an exact answer that takes 10 minutes, because it enables interactive exploration.

Approximate query processing techniques include sampling (run the query on a representative subset), sketches (data structures like HyperLogLog and Count-Min Sketch that answer specific query types in sublinear space), and online aggregation (return increasingly accurate results as more data is processed, allowing the user to stop early). Systems like BlinkDB (from AMPLab at UC Berkeley) were making these techniques accessible as SQL extensions with explicit accuracy/latency tradeoffs specified in queries.

The context was 2013's interactive analytics problem: Hadoop MapReduce was designed for batch processing, not interactive analysis. Users who wanted to explore data iteratively waited minutes per query, which broke the exploratory analysis flow. Apache Spark was one answer (in-memory computation). AQP was a complementary answer: get results instantly by being approximate.

## Key points

- HyperLogLog: estimates cardinality (COUNT DISTINCT) in a fixed amount of memory with ~1-2% error — one of the most practically useful sketches.
- Count-Min Sketch: estimates frequency counts over a stream in sublinear space — trades false positive rate for memory efficiency.
- BlinkDB: a system from UC Berkeley AMPLab that added approximate query support to Hive/Spark — users specify error bounds or latency targets in SQL queries.
- Online aggregation: results improve continuously as more data is processed — can stop early once confidence interval is narrow enough.
- Trade-off framing: not approximate is wrong but "approximate is a choice with quantified error bounds" — changing how analysts think about query semantics.
- Connected to streaming algorithms more broadly: many AQP sketches are streaming-compatible, making them useful for real-time data as well.

[Original](http://strata.oreilly.com/2013/08/interactive-big-data-analysis-using-approximate-answers.html)
