---
title: Big-O Notation Explained by a Self-Taught Programmer
date: 2013-07-26
categories:
  - algorithms
  - computer-science
  - complexity
  - fundamentals
description: A self-taught programmer's accessible guide to Big-O notation — explaining time and space complexity from first principles without assuming a CS degree. A good on-ramp for practitioners who need to reason about algorithm performance.
params:
  source: pinboard
  sourceUrl: http://justin.abrah.ms/computer-science/big-o-notation-explained.html
---

![Big-O Notation Explained by a Self-Taught Programmer](/images/notes/big-o-notation-explained.png)

## Summary

Big-O notation is the standard language for describing how an algorithm scales as the size of its input grows. This post explains it from a self-taught practitioner's angle: the focus is on building intuition for time complexity and space complexity without getting lost in formal mathematical proofs.

The core idea is that Big-O notation describes the *worst-case* upper bound on an algorithm's growth rate. An O(n) algorithm's runtime grows linearly with input size. An O(n²) algorithm's runtime grows quadratically — doubling the input means roughly four times the work. What makes Big-O useful in practice is that it strips away constants and lower-order terms, letting you compare algorithms at meaningful scale rather than benchmarking on toy inputs.

The self-taught framing matters here: CS textbooks often introduce Big-O through formal proof and mathematical limits, which is pedagogically backwards for engineers who learn by doing. Starting from concrete examples — scanning a list is O(n), binary search is O(log n), nested loops are usually O(n²) — and building up the intuition before formalizing it is a better approach for most working programmers.

## Key points

- O(1) (constant time): operations that take the same time regardless of input size — hash table lookups, array access by index.
- O(log n): each step halves the problem — binary search is the canonical example; the input can be enormous and the search is still fast.
- O(n): linear scan — reading every element once. Unavoidable for unsorted search.
- O(n log n): the lower bound for comparison-based sorting — merge sort and quicksort hit this; you can't do better for a general sort.
- O(n²): nested loops over the same input — bubble sort, naive duplicate detection. Falls apart quickly at scale.

[Original](http://justin.abrah.ms/computer-science/big-o-notation-explained.html)
