---
title: Set Operations in the Unix Shell
date: 2013-06-18
categories:
  - unix
  - shell
  - data-engineering
  - tools
description: Peteris Krumin's catonmat guide to implementing set operations (union, intersection, difference, complement) using Unix command-line tools. A concise demonstration that shell pipelines can express set algebra without any code.
params:
  source: pinboard
  sourceUrl: http://www.catonmat.net/blog/set-operations-in-unix-shell/
---

## Summary

Peteris Krumin's catonmat blog covers how to perform set operations — union, intersection, difference, and Cartesian product — using standard Unix command-line tools. The tools involved are primarily `sort`, `uniq`, `comm`, and `join`, which together form a complete vocabulary for set algebra on text files. No Python, no database, no custom code required.

The post is a practical complement to the Ad Hoc Data Analysis From the Unix Command Line tradition. The key insight: sorted files of unique lines are sets, and `comm` (which compares two sorted files) directly implements intersection and difference. Union is just `cat` followed by `sort -u`. These primitives compose cleanly through Unix pipes.

This approach matters beyond trivia. When you're working with lists of IDs, log lines, or any membership data, shell set operations are often faster than loading data into pandas or running a database query — especially for files too large to hold in memory but too small to justify a cluster.

## Key points

- `sort -u file1 file2` → union (sorted unique lines from both files)
- `comm -12 <(sort f1) <(sort f2)` → intersection (lines in both)
- `comm -23 <(sort f1) <(sort f2)` → difference (lines only in f1)
- `comm -13 <(sort f1) <(sort f2)` → difference (lines only in f2)
- `join` handles Cartesian product and equi-joins on sorted files by key
- Process substitution (`<()`) is the shell mechanism that makes multi-file operations composable

[Original](http://www.catonmat.net/blog/set-operations-in-unix-shell/)
