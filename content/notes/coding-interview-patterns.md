---
title: Patterns to Ace Coding Interviews
date: 2022-03-26
categories:
  - algorithms
  - interview
  - data-structures
  - programming
  - reference
description: A pattern-based framework for coding interview preparation — reduces hundreds of LeetCode problems to ~20 recognizable patterns. Knowing which pattern applies is usually harder than solving once the pattern is identified.
params:
  source: pinboard
  sourceUrl: https://hackernoon.com/5-to-23-patterns-to-ace-any-coding-interview
---

## Summary

This HackerNoon article makes the case that coding interview preparation is more tractable than it appears once you recognize that most problems map to one of ~20 fundamental patterns. Rather than solving hundreds of LeetCode problems randomly, studying the patterns first creates a recognition framework: when you see a problem, you identify which pattern applies, then apply that pattern's template. The original 5 patterns evolved to 23 as the framework expanded, but the core insight holds.

The key patterns identified: sliding window (contiguous subarray/substring problems), two pointers (sorted array or linked list traversal), fast and slow pointers (cycle detection in linked lists), merge intervals (overlapping interval problems), cyclic sort (problems involving array indices 1 to n), in-place linked list reversal, BFS tree traversal, DFS tree traversal, two heaps (median maintenance), subsets (backtracking and combinations), modified binary search, top K elements (heap-based), k-way merge, and topological sort for DAG-based ordering problems.

The practical observation is that pattern recognition is the hard SKILL, not the algorithm implementation. Given "find the longest substring without repeating characters," an experienced candidate immediately thinks sliding window with a hashmap; an inexperienced one stares at the problem. The patterns compress the problem space — most LeetCode mediums map to one or two patterns — and the patterns themselves compress to underlying data structure choices (heap for top-K, BFS for shortest path, two pointers for sorted arrays).

## Key points

- ~20 patterns cover the majority of coding interview questions — pattern recognition > problem memorization.
- Sliding window: contiguous subarray optimizations — avoids O(n²) brute force; expand/contract window based on constraint.
- Two pointers: sorted arrays, palindrome checks, pair-sum problems — O(n) over O(n²) brute force.
- Topological sort: prerequisite/dependency ordering — BFS-based Kahn's algorithm or DFS-based post-order traversal.
- Top K elements: maintain a heap of size K instead of sorting (O(n log K) vs. O(n log n)).
- Best used alongside Grokking the Coding Interview (Educative) and NeetCode roadmap — patterns are the framework, practice problems build fluency.

[Original](https://hackernoon.com/5-to-23-patterns-to-ace-any-coding-interview)
