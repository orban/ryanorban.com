---
title: Top Mistakes Developers Make When Using Python for Big Data Analytics
date: 2015-01-23
categories:
  - python
  - big-data
  - performance
  - data-engineering
  - best-practices
description: A practical rundown of the top Python performance mistakes for big data workloads — covering generator vs. list comprehension choices, pandas anti-patterns, and when to reach for NumPy. Still relevant since Python's core performance traps haven't changed.
params:
  source: pinboard
  sourceUrl: https://www.airpair.com/python/posts/top-mistakes-python-big-data-analytics
---

## Summary

This AirPair post targets developers who know Python well enough to write working code but haven't internalized the performance characteristics that matter at large data scales. The core theme: Python's dynamism and expressive syntax encourage patterns that are fine for small data but disastrous for large datasets.

The main categories of mistakes: Using Python lists where NumPy arrays should be — pure Python loops over lists are 100x slower than vectorized NumPy operations for numerical work. Using `append()` in loops to build collections instead of list comprehensions or generator expressions — each `append` call is O(1) amortized but the repeated function call overhead adds up. Using pandas `.apply()` when a vectorized pandas operation exists — apply runs a Python function per row, bypassing pandas' underlying C/Cython implementation.

Memory management is another theme: loading entire datasets into memory when streaming or chunked processing would suffice. Pandas `read_csv()` with `chunksize` parameter, generators instead of lists, and lazy evaluation patterns all address this. The post predates the Dask and Polars era — modern alternatives that push the boundary of what's tractable in Python have changed the landscape since, but the underlying principles remain valid.

## Key points

- NumPy vectorization vs. Python loops: 100x+ speed difference for numerical operations.
- Pandas `.apply()` is a performance trap — vectorized pandas operations use C/Cython under the hood.
- Memory: load data lazily or in chunks instead of all at once for datasets that don't fit in RAM.
- List comprehensions and generators >> repeated `append()` calls in loops.
- Profiling first: use `cProfile` or `line_profiler` before optimizing — don't guess.
- Pre-dates Dask, Polars, and Arrow — those tools solve many of these problems at the library level now.

[Original](https://www.airpair.com/python/posts/top-mistakes-python-big-data-analytics)
