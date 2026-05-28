---
title: A Few Things to Remember While Coding in Python
date: 2012-05-20
categories:
  - python
  - programming
  - best-practices
  - reference
description: A practical reference post on Python idioms and gotchas — covering mutable default arguments, list comprehensions, generators, decorators, and other patterns that distinguish experienced Python code from novice code.
params:
  source: pinboard
  sourceUrl: http://satyajit.ranjeev.in/2012/05/17/python-a-few-things-to-remember.html
---

## Summary

Satyajit Ranjeev's 2012 blog post collected practical Python idioms and common gotchas — the kind of knowledge that separates code written by someone who read a Python tutorial from code written by someone who has spent time in the ecosystem. The post was widely shared in developer circles at a time when Python was gaining serious traction for web development (driven by Django and Flask) and scientific computing.

The core patterns the post covers are the durable ones: mutable default arguments (the classic `def f(x, lst=[])` bug where the list persists across calls), the difference between generators and lists (prefer generators for large sequences to avoid materializing everything in memory), list comprehensions as more Pythonic than `map()/filter()`, context managers via `with` statements for resource cleanup, and how decorators work as a clean way to wrap function behavior.

These patterns matter because Python's flexibility lets you write code in many styles, but some styles cause subtle bugs (mutable defaults), some perform poorly at scale (list materializing where generators suffice), and some are just unidiomatic enough to confuse readers. The post served as a quick calibration tool — if you hadn't encountered the mutable default argument bug before, you'd run into it eventually.

## Key points

- Mutable default arguments in Python are initialized once at function definition, not on each call — a persistent source of bugs.
- Prefer generators over lists for large sequences: `(x for x in ...)` vs `[x for x in ...]` avoids memory overhead.
- List comprehensions are idiomatic Python; `map()` and `filter()` are often less readable and not meaningfully faster.
- Decorators (`@functools.wraps`, `@property`, etc.) are just syntactic sugar for higher-order functions.
- Context managers (`with` statement) ensure cleanup even on exceptions — use for files, locks, DB connections.

[Original](http://satyajit.ranjeev.in/2012/05/17/python-a-few-things-to-remember.html)
