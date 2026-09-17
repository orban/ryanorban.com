---
title: Python Best Practice Patterns (Vladimir Keleshev — Notes)
date: 2014-03-01
categories:
  - python
  - best-practices
  - software-design
  - oop
  - clean-code
description: Steven Loria's notes from Vladimir Keleshev's talk on Python best practice patterns — covers protocol classes, named tuples, reducing coupling, and using Python's data model idiomatically. Practical design advice for writing maintainable Python.
params:
  source: pinboard
  sourceUrl: http://stevenloria.com/python-best-practice-patterns-by-vladimir-keleshev-notes/
---

## Summary

Steven Loria (creator of TextBlob, the simplified NLP library for Python) took notes from Vladimir Keleshev's talk on Python best practice patterns. Keleshev was known for arguing that many software design patterns from other languages are either unnecessary in Python or have better Pythonic alternatives — the language's data model and dynamic features enable cleaner solutions than pattern-matching from Java-style OOP.

The patterns covered focus on reducing coupling and using Python's protocol system: instead of defining abstract base classes with explicit inheritance, write functions that accept any object implementing the relevant protocol (duck typing). Named tuples (`collections.namedtuple`) are preferred over plain tuples for structured data because they're self-documenting and support unpacking without index magic. The `__slots__` pattern reduces memory for classes with many instances. Using `@property` for computed attributes keeps the interface clean without getters/setters.

The broader theme connects to Python's design philosophy: prefer protocols over inheritance hierarchies, prefer composition over inheritance, and let Python's runtime do the work that other languages require explicit machinery for. Keleshev was also the creator of `docopt` (the argument parser that derives CLI spec from docstrings), which exemplifies this approach — the interface specification is the documentation.

## Key points

- Duck typing over abstract base classes: write functions that accept any object with the right methods, not objects that inherit from a specific class.
- Named tuples: `collections.namedtuple` for structured, immutable data — cleaner than index-based tuples, lighter than full classes.
- `@property`: computed attributes that look like attributes to callers — avoids getter/setter boilerplate while keeping the class interface clean.
- Reducing coupling: depend on interfaces (protocols), not implementations — makes code testable and swappable.
- Vladimir Keleshev also created `docopt` — a CLI argument parser where the help text is the specification, exemplifying the convention over configuration aesthetic.

[Original](http://stevenloria.com/python-best-practice-patterns-by-vladimir-keleshev-notes/)
