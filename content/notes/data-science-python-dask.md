---
title: Data Science with Python and Dask
date: 2022-04-04
categories:
  - python
  - dask
  - data-science
  - distributed-computing
  - big-data
description: Jesse Daniel's Manning 2019 book teaching Dask for parallel and out-of-core data science in Python — using familiar pandas-like DataFrames and numpy-like arrays across cores and machines. The go-to resource for scaling Python data science workflows beyond single-machine memory limits.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/Jesse C. Daniel - Data Science With Python And Dask-Manning Publications (2019).pdf
---

## Summary

Jesse C. Daniel (Manning, 2019) teaches Dask — the parallel computing library for Python — through a practical data science lens. Dask's design philosophy is to mirror familiar pandas and NumPy APIs exactly, so the reader's existing knowledge transfers directly: a `dask.dataframe` works like a pandas `DataFrame`, a `dask.array` works like a NumPy array, but both operate lazily and can distribute across cores or machines. The book builds from single-machine parallelism through cluster deployment on Kubernetes and cloud providers.

The core problem Dask solves: pandas loads data entirely into memory, which fails for datasets larger than available RAM and underutilizes multicore CPUs even when the data fits. Dask solves both: it partitions DataFrames into chunks that fit in memory and processes them in parallel, deferring actual computation until `.compute()` is called. This lazy evaluation enables Dask to optimize computation graphs before execution — skipping unnecessary work, fusing operations, and managing memory spill to disk.

The book covers the Dask DataFrame, Dask Array, Dask Bag (for unstructured data like JSON logs), and Dask Delayed (for arbitrary Python functions). The cluster deployment chapter covers dask-distributed with the scheduler architecture, Dask Gateway for multi-tenant clusters, and deployment on YARN and Kubernetes. By 2022 when this was saved, Dask had become the standard tool for scaling Python ML pipelines before moving to Spark, Ray, or cloud-native alternatives.

## Key points

- Dask DataFrame: pandas-compatible API operating on partitioned data — same methods, lazy execution, parallel groupby/join/apply
- Dask Array: NumPy-compatible API for arrays larger than memory — parallel FFTs, reductions, and elementwise ops across partitions
- Lazy evaluation graph: `dask.delayed` wraps arbitrary Python into a computational graph optimized before execution — enables optimization like dead code elimination
- dask-distributed scheduler: distributed task graph execution across cores/machines, with a Bokeh dashboard for visualizing task progress and memory use
- When to use vs. alternatives: Dask wins for single-team data science pipelines; consider Ray for ML training, Spark for SQL-heavy enterprise workloads with Hive/Delta integration

[Original PDF →](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/Jesse%20C.%20Daniel%20-%20Data%20Science%20With%20Python%20And%20Dask-Manning%20Publications%20(2019).pdf)
