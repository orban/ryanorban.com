---
title: "Functools: The Power of Higher-Order Functions in Python"
date: 2021-07-09
categories:
  - python
  - programming
  - functional-programming
  - functools
  - education
description: Martin Heinz's guide to Python's functools module — partial application, memoization via lru_cache, reducing sequences, and higher-order function patterns. The companion to itertools for functional-style Python.
params:
  source: pinboard
  sourceUrl: https://martinheinz.dev/blog/52
---

![Functools: The Power of Higher-Order Functions in Python](/images/notes/python-functools.png)

## Summary

Martin Heinz covers Python's functools standard library module — the toolkit for higher-order functions, memoization, and partial application. Functools provides utilities that treat functions as first-class values: wrapping, caching, and transforming them.

Key functions in the module: `partial()` — creates a new function by pre-filling arguments of an existing function, useful for creating specialized versions of general-purpose functions. `lru_cache()` / `cache()` — memoization decorator that caches function results by input arguments, making dynamic programming-style recursion dramatically faster without manual caching code. `reduce()` — applies a binary function cumulatively over a sequence to produce a single value (the functional `fold`). `wraps()` — preserves function metadata when writing decorators, so the wrapped function's `__name__` and `__doc__` survive. `total_ordering` — given `__eq__` and one comparison method, fills in the rest automatically.

The most practically used of these is `lru_cache` — it's a one-line addition that converts naive recursive code into efficient memoized code without restructuring anything. `partial` sees use in callback-heavy code where you need to bind some arguments ahead of time. Together with itertools, functools gives Python a surprisingly complete functional programming toolkit without adding a dependency.

## Key points

- `lru_cache` / `cache`: one-line memoization — attach to any pure function to cache its results.
- `partial()`: partial application — pre-fill arguments to create specialized versions of functions.
- `reduce()`: the functional fold — reduce a sequence to a single value with a binary operation.
- `wraps()`: preserve function metadata in decorators — don't write a decorator without it.
- Companion to itertools: together they form Python's built-in functional programming toolkit.

[Original](https://martinheinz.dev/blog/52)
