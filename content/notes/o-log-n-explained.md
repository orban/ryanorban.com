---
title: What Does O(log n) Mean Exactly?
date: 2013-05-26
categories:
  - algorithms
  - complexity
  - education
  - computer-science
description: A Stack Overflow answer explaining O(log n) complexity with a highly upvoted intuitive explanation using binary search. The 'halving' intuition — each step eliminates half the remaining problem space — is the cleanest way to build the mental model.
params:
  source: pinboard
  sourceUrl: http://stackoverflow.com/questions/2307283/what-does-olog-n-mean-exactly/2307314#2307314
---

![What Does O(log n) Mean Exactly?](/images/notes/o-log-n-explained.png)

## Summary

This Stack Overflow answer gives one of the clearest intuitive explanations of O(log n) time complexity. The core insight: logarithmic time means that doubling the input size only adds a single extra operation. If searching 16 items takes 4 steps, searching 32 items takes 5 steps, and searching a billion items takes only about 30 steps. The operation count grows with the *logarithm* of the input, not the input itself.

The canonical example is binary search: at each step, you compare against the midpoint and discard half the remaining elements. After k steps, you've narrowed 2^k → 1 items. Inverting: k = log₂(n) steps to reach a single item. Any algorithm that repeatedly halves its working set — whether on a sorted array, a binary search tree, or a balanced BST like AVL tree or Red-Black tree — has O(log n) behavior.

This is the foundation for understanding why hash tables with O(1) average lookup beat BSTs with O(log n) for most workloads, but why O(log n) is still dramatically better than O(n) for large datasets. At n = 1 billion, O(log n) ≈ 30 operations vs. O(n) = 1 billion operations.

## Key points

- O(log n): doubling input adds one step — the operation count is the exponent in n = 2^k
- Intuition: each step halves the problem; after k halvings you reach 1 element
- Binary search on a sorted array is the textbook O(log n) example
- Binary search tree operations (search, insert, delete) are O(log n) on a balanced tree
- Merge sort and quicksort are O(n log n): n elements × log n comparisons per merge pass
- Practical meaning: O(log n) algorithms scale to arbitrarily large inputs — a billion-row log search takes ~30 comparisons with a B-tree index

[Original](http://stackoverflow.com/questions/2307283/what-does-olog-n-mean-exactly/2307314#2307314)
