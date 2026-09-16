---
title: fastcore — Python Extensions by fast.ai
date: 2020-09-03
categories:
  - python
  - library
  - functional-programming
  - fast-ai
  - tools
description: fastcore is fast.ai's Python utility library extending the standard library with mixins, delegation, functional programming patterns, and parallel processing helpers. Used heavily in fast.ai's deep learning courses and libraries.
params:
  source: pinboard
  sourceUrl: https://fastcore.fast.ai/
---

## Summary

fastcore is a Python utility library developed by [fast.ai](/notes/fastai/) (Jeremy Howard and Sylvain Gugger) that extends Python's standard library with patterns borrowed from other languages and fills gaps in Python's built-in tooling. It's the foundational library underlying [fastai](/notes/fastai/)'s deep learning framework and is used throughout [fast.ai](/notes/fastai/)'s course materials.

The library is organized into three main modules: `fastcore.test` (testing utilities), `fastcore.foundation` (core Python enhancements — mixins, delegation, composition), and `fastcore.xtras` (functional programming helpers, parallel processing, enhanced list type). The design philosophy is to make Python more expressive without losing its readability — borrowing Ruby's mixin pattern and Haskell's currying and binding concepts.

Key capabilities: the enhanced `L` list type with NumPy-style operations, `@patch` for adding methods to existing classes (monkey-patching with better syntax), `delegates()` for clean method delegation, `parallel()` for easy parallel processing, and `@typedispatch` for type-based method dispatch. These solve real ergonomic problems that arise repeatedly in data science and ML code.

## Key points

- The `L` list type supports filtering, mapping, and indexing with a cleaner API than list comprehensions — similar to pandas Series operations but for arbitrary Python objects.
- `@patch` is fastcore's answer to Ruby mixins — add methods to existing classes without subclassing, keeping related code co-located.
- `delegates()` solves the Python anti-pattern of `**kwargs` that hides parameter names — it auto-populates the function signature from delegated functions.
- [fast.ai](/notes/fastai/) uses fastcore throughout [fastai](/notes/fastai/) — so reading fastai source code requires familiarity with fastcore's idioms, especially `L`, `@patch`, and `delegates`.
- Designed for intermediate-to-advanced Python programmers; beginners may find the unconventional patterns confusing rather than helpful.

[Original](https://fastcore.fast.ai/)
