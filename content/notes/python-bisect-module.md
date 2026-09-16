---
title: Using Python's bisect Module
date: 2020-11-22
categories:
  - python
  - algorithms
  - data-structures
  - stdlib
  - binary-search
description: A practical walkthrough of Python's bisect standard library module — binary search for maintaining sorted lists and efficient data binning. Covers two key use cases with code examples.
params:
  source: pinboard
  sourceUrl: https://johnlekberg.com/blog/2020-11-21-stdlib-bisect.html
---

## Summary

Python's `bisect` standard library module implements binary search for maintaining and querying sorted lists. This blog post by John Lekberg covers two practical use cases that illustrate when the module is the right tool: statistical data binning and maintaining sorted lists for order statistics.

The first use case is binning continuous data into categories — for example, converting a raw test score into a letter grade. Rather than a chain of `if/elif` conditions (O(n) per lookup), `bisect` navigates sorted bin boundaries in O(log n). The second is maintaining a sorted list when insertions are infrequent but statistics like median need to be computed cheaply: `bisect.insort()` inserts in sorted order in O(n) time (versus O(n log n) for append-then-sort), making median retrieval O(1) from the maintained order.

The module also has left and right variants — `bisect_left` and `bisect_right` — which differ in where they place duplicates. Understanding this distinction matters when values repeat.

## Key points

- `bisect.bisect()` returns the insertion point for a value in a sorted list — core primitive for both search and insert operations.
- `bisect.insort()` inserts a value while maintaining sort order — useful when you need sorted access but insertions come one at a time.
- Data binning with bisect reduces O(mn) sequential condition checks to O(m + n log m) — meaningful at scale.
- Works best when the list is mostly-read, occasionally-written: if you're inserting constantly, a heap or sorted container (like `sortedcontainers.SortedList`) is more appropriate.
- Part of Python's standard library — no dependencies, pure Python, and fast enough for most use cases.

[Original](https://johnlekberg.com/blog/2020-11-21-stdlib-bisect.html)
