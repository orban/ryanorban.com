---
title: Speeding Up Your Python Code
date: 2013-03-18
categories:
  - python
  - performance
  - optimization
  - profiling
description: Max Burstein's practical guide to Python performance — profiling-driven optimization covering list comprehensions, generators, local variable access, string concatenation, and C extension use. A good 2013-era reference for the pragmatic Python performance techniques.
params:
  source: pinboard
  sourceUrl: http://maxburstein.com/blog/speeding-up-your-python-code/
---

![Speeding Up Your Python Code](/images/notes/speeding-up-python-code.png)

## Summary

Max Burstein's post covered the practical Python performance techniques that were most commonly useful in 2013: the approaches that yield meaningful speedups for everyday code without requiring architectural changes. The context was a Python ecosystem where NumPy and Cython were available for numerical work, but pure Python code was often the bottleneck in data processing scripts, web applications, and general-purpose tooling.

The core techniques covered: list comprehensions instead of loops (Python bytecode evaluates comprehensions in a tighter loop with less overhead than explicit for loops and append calls), generator expressions for memory efficiency (avoid materializing large lists in memory when only iterating), and local variable access being faster than global or attribute lookup in the CPython interpreter (LOAD_FAST vs. LOAD_GLOBAL bytecode instructions). String concatenation via `+` in a loop is O(n²) due to immutable string copying; joining a list of strings is O(n). All of these follow from understanding CPython's object model.

The profiling advice was the most durable part: use `cProfile` before optimizing anything, identify the actual hotspot, then apply targeted optimizations. This predated py-spy and modern sampling profilers but the principle — don't guess, measure — remains the correct approach. For numerical work, the advice pointed toward NumPy for vectorized operations and Cython or Ctypes for wrapping C extensions when Python itself was genuinely insufficient.

## Key points

- list comprehensions are faster than equivalent for loops in CPython because the bytecode engine processes them differently (no per-iteration LOAD_FAST for append)
- Local variables (LOAD_FAST) are faster than globals or attribute lookups (LOAD_GLOBAL, LOAD_ATTR) — cache frequently used attributes to locals inside tight loops
- String concatenation: `"".join(list)` is O(n), `str1 + str2 + ...` in a loop is O(n²) — use join for loop-built strings
- generator expressions vs. list comprehensions: generators yield lazily, avoiding memory allocation when you're only iterating once
- cProfile for deterministic profiling, then target the actual hotspot — premature optimization without measurement is the classic mistake
- NumPy, Cython, Ctypes, and cffi for C-level performance when Python itself is the bottleneck — accept that Python's strength is development speed, not runtime speed

[Original](http://maxburstein.com/blog/speeding-up-your-python-code/)
