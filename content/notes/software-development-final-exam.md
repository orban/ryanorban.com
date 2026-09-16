---
title: "Software Development Final Exam Answers: Part 1"
date: 2012-10-17
categories:
  - algorithms
  - computer-science
  - education
  - programming
  - data-structures
description: "Colin Percival grades a software development final exam and finds most developers can recall what data structures do but not why they're useful in specific contexts — the gap between memorization and understanding. Average score: 15.2/25."
params:
  source: pinboard
  sourceUrl: http://www.daemonology.net/blog/2012-10-17-software-development-final-answers-part-1.html
---

![Software Development Final Exam Answers: Part 1](/images/notes/software-development-final-exam.png)

## Summary

Colin Percival (of Tarsnap and scrypt fame) ran a software development exam and published graded answers and commentary. Five questions covered big-O notation, quicksort performance, binary search trees vs B-trees, heap operations, and graph bipartiteness. Average score across respondents was 15.2/25, with roughly equal distribution across performance bands.

The most revealing result was on heap construction. Most developers knew that extracting the minimum from a heap is O(log n), but few recognized that building a heap from scratch can be done in O(n) time through a bottom-up approach — you work from leaves to root, sifting down at each level, and the sum across levels converges to linear time. That this was the lowest-scored question (average 2.2/5) suggests developers often learn heap operations as isolated facts rather than understanding the algorithm well enough to derive the time complexity themselves.

The big-O question exposed another gap: whether O(2^n) equals O(3^n). It doesn't — their ratio approaches zero as n grows, so they're distinct asymptotic classes. But many developers treat big-O as a categorization system (polynomial vs. exponential) rather than a precise bound relationship. The B-tree vs. binary search tree question also showed that understanding *when* a data structure excels (B-trees for disk-based storage, where minimizing disk seeks matters more than comparison count) requires context knowledge, not just definition recall.

## Key points

- Heap construction is O(n), not O(n log n) — the bottom-up build converges to linear time, but this is underknown even among experienced developers.
- O(2^n) ≠ O(3^n): big-O is a precise relationship, not just an exponential bucket.
- B-trees outperform binary search trees for disk-based storage because they minimize I/O operations by packing more keys per node — the disk seek cost dominates comparison cost.
- Quicksort averages O(n log n) but degrades to O(n²) in worst case; most developers got this right (4.8/5 average).
- The graph bipartiteness test (2-coloring via BFS/DFS) revealed gaps in algorithmic reasoning beyond memorized procedures.

[Original](http://www.daemonology.net/blog/2012-10-17-software-development-final-answers-part-1.html)
