---
title: "Blaze: A Python Compiler for Big Data"
date: 2012-12-18
categories:
  - python
  - big-data
  - data-science
  - numpy
  - continuum-analytics
description: Continuum Analytics' announcement of Blaze — a Python compiler and array expression system designed to scale NumPy-style computations beyond in-memory datasets. An early attempt to bring Python's scientific computing ecosystem to big data before Spark/Dask became dominant.
params:
  source: pinboard
  sourceUrl: http://continuum.io/blog/blaze
---

![Blaze: A Python Compiler for Big Data](/images/notes/blaze-python-big-data.png)

## Summary

Continuum Analytics (later renamed Anaconda) announced Blaze in December 2012 as a project to extend the NumPy programming model to out-of-core and distributed data. The core idea: Python's scientific computing ecosystem (NumPy, SciPy, Pandas) was excellent but inherently in-memory — array operations required data to fit in RAM. Blaze aimed to compile NumPy-style expressions to execute on distributed storage systems (HDF5, databases, Hadoop) without requiring users to rewrite their analysis code.

Continuum Analytics was founded by Travis Oliphant (the creator of NumPy) and [[Peter Wang]. They had strong credibility in the Python scientific computing community and positioned Blaze as a natural extension of the NumPy data model to handle the scale problems that were limiting scientific Python for large datasets.

The competitive context in December 2012: Apache Spark had been released at UC Berkeley in 2012 but was not yet the dominant big data processing framework it became. Hadoop MapReduce was the incumbent but was awkward for iterative algorithms. Blaze's bet was that scientists would rather extend Python than learn a new paradigm. The bet was partially right: Dask (also from Continuum) later became more successful at this, and Blaze itself was largely superseded. But the design direction — Python-native big data with familiar API semantics — proved correct.

## Key points

- Blaze: expression compiler for out-of-core array computation; translates NumPy-like operations to backend storage systems
- Travis Oliphant: NumPy creator; co-founder of Continuum Analytics; gave the project significant credibility
- Design philosophy: preserve the NumPy interface while adding backend flexibility — users write pandas/numpy, Blaze compiles to the appropriate executor
- Dask later succeeded where Blaze struggled, using lazy evaluation and task graphs rather than compilation
- Historical context: December 2012 was before Spark's dominance; Python big data was an open problem

[Original](http://continuum.io/blog/blaze)
