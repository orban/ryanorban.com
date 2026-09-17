---
title: Advanced Data Structures in Python
date: 2013-12-18
categories:
  - python
  - data-structures
  - algorithms
  - reference
  - computer-science
description: Pypix overview of advanced data structures in Python beyond the built-in list/dict/set — covering heaps, tries, segment trees, and other structures that Python's standard library either implements partially or not at all.
params:
  source: pinboard
  sourceUrl: http://pypix.com/python/advanced-data-structures/
---

## Summary

This Pypix article covers data structures in Python that go beyond the standard list, dict, and set — the structures that come up in competitive programming, performance-critical applications, and systems work. Python's standard library covers some of these (the `heapq` module for heaps, `collections.deque` for double-ended queues), but others require custom implementations or third-party libraries.

The article covers structures like tries (prefix trees for efficient string lookup and autocomplete), heaps (for priority queues and k-largest/smallest problems), segment trees and Fenwick trees (for range queries with updates), disjoint set union (union-find for connected component problems), and skip lists. These structures appear regularly in algorithms interviews and in real systems: tries in search autocomplete, heaps in scheduling, union-find in network connectivity.

In 2013, before LeetCode had fully taken over technical interviews and before competitive programming resources were as abundant, posts like this served as practical curriculum for engineers wanting to level up their algorithms foundations using a language they already knew.

## Key points

- Trie (prefix tree): O(k) lookup by prefix where k = key length. Used for autocomplete, spell-check, IP routing.
- Heap / `heapq`: min-heap in Python stdlib. Use `heapq.nlargest`/`nsmallest` for k-largest problems.
- Segment tree: range queries (sum, min, max) in O(log n) with O(log n) updates. Standard competitive programming structure.
- Union-Find (disjoint set): near-O(1) amortized union/find with path compression and rank. Used for connected components.
- Skip list: probabilistic alternative to balanced BSTs, easier to implement correctly.
- Python's built-in structures cover many cases well (`collections.OrderedDict`, `collections.Counter`, `collections.deque`).

[Original](http://pypix.com/python/advanced-data-structures/)
