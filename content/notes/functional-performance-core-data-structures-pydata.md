---
title: Functional Performance with Core Data Structures — PyData SV 2014
date: 2014-05-05
categories:
  - python
  - performance
  - functional-programming
  - pydata
  - data-structures
description: Matthew Rocklin's PyData SV 2014 talk on functional performance with core data structures — showing how functional programming patterns and Python's built-in data structures enable high-performance computation without reaching for C extensions.
params:
  source: pinboard
  sourceUrl: http://nbviewer.ipython.org/github/mrocklin/slides/blob/pydata-sv-2014/pydata-sv-2014.ipynb?create=1
---

## Summary

Matthew Rocklin's PyData SV 2014 talk explored how functional programming patterns combined with Python's built-in data structures (dicts, sets, tuples, frozensets) enable surprisingly high-performance computation. The central argument: before reaching for NumPy arrays or Pandas DataFrames, understanding what core Python data structures already do well can yield fast, readable code.

Rocklin was at the time a Python performance researcher who later created Dask (a library for parallel and distributed computation that extends NumPy/Pandas patterns to larger-than-memory data). His work consistently focused on the boundary between algorithmic clarity and computational efficiency — understanding the memory layout and time complexity of operations before optimizing.

The functional programming angle is about data transformation pipelines: treating computation as a series of transformations (map, filter, reduce) that compose cleanly and enable lazy evaluation. Python generators make this natural, and itertools provides a functional toolkit over arbitrary iterables. This approach often outperforms imperative loops because it reduces intermediate allocations.

## Key points

- Python's built-in data structures (dicts, sets, frozensets) have O(1) lookup — use them before reaching for specialized structures.
- Functional programming patterns (map/filter/reduce) with generators minimize intermediate allocations.
- Matthew Rocklin: later created Dask — the same performance-oriented thinking applied to distributed computing.
- itertools and functools provide the functional toolkit without third-party dependencies.
- Performance first principle: understand algorithmic complexity and data layout before profiling.

[Original](http://nbviewer.ipython.org/github/mrocklin/slides/blob/pydata-sv-2014/pydata-sv-2014.ipynb?create=1) → GitHub
