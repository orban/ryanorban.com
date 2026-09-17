---
title: 30 Python Language Features and Tricks You May Not Know About
date: 2014-03-09
categories:
  - python
  - programming
  - tips
  - reference
description: Sahand Saba's tour of 30 Python language features that intermediate programmers often overlook — covers unpacking, generators, context managers, decorators, and more. A practical companion to reading the Python docs.
params:
  source: pinboard
  sourceUrl: http://sahandsaba.com/thirty-python-language-features-and-tricks-you-may-not-know.html
---

## Summary

Sahand Saba's post targets the gap between knowing basic Python syntax and using the language idiomatically. Most programmers who pick up Python from other languages learn the obvious features (list comprehensions, indentation-based blocks, dynamic typing) but miss the less-advertised ones that make Python code elegant rather than just functional.

The tricks span multiple areas: data structure manipulation (extended unpacking with `*`, dict/set comprehensions, `defaultdict`), iteration patterns (generators, `itertools`, `enumerate`, `zip`), function features (closures, `*args`/`**kwargs`, decorators), context managers (`with` statements, `contextlib`), and some metaprogramming (`__slots__`, `property`, `__getattr__`). Together they represent the idiom set that distinguishes Python code written by someone thinking in Python versus Python code written by someone thinking in Java or C++.

In the 2014 data science context, these features mattered practically: generators let you process large files without loading them into memory, `defaultdict` simplifies counting and grouping, `itertools.chain` and `itertools.islice` make data pipeline construction cleaner. NumPy and Pandas had their own idioms on top, but understanding core Python well made the library-specific patterns easier to grasp.

## Key points

- Extended unpacking: `a, *b, c = [1, 2, 3, 4, 5]` — assigns head and tail without slicing.
- Generators: `yield`-based lazy evaluation — crucial for large-data processing without holding everything in memory.
- Decorators: functions that wrap other functions — the pattern behind Flask routes, `@property`, `@staticmethod`, and test mocking.
- `defaultdict` and `Counter` from `collections`: avoid manual key-existence checks in accumulation patterns.
- Context managers (`with` statement): guarantee resource cleanup even when exceptions occur — file handles, locks, database connections.

[Original](http://sahandsaba.com/thirty-python-language-features-and-tricks-you-may-not-know.html)
