---
title: Python Mocking Minimal Working Examples
date: 2023-09-21
categories:
  - python
  - testing
  - mocking
  - unit-tests
  - reference
description: A minimal working example (MWE) repository demonstrating Python mocking patterns with unittest.mock — covering patch, MagicMock, side_effect, and common gotchas. A practical reference for developers who know they should mock but keep forgetting the syntax.
params:
  source: pinboard
  sourceUrl: https://github.com/data-day-science/python_mocking_mwe
---

![Python Mocking Minimal Working Examples](/images/notes/python-mocking-mwe.png)

## Summary

This repository from Data Day Science provides minimal working examples (MWEs) for Python mocking patterns using unittest.mock — the standard library module for replacing objects during testing. The common complaint about Python mocking is that it works correctly once you understand the mental model, but the path to that understanding is full of subtle bugs: patching the wrong namespace, forgetting `return_value` vs. `side_effect`, mocking at the wrong level of abstraction.

unittest.mock provides `patch` (a decorator/context manager for replacing objects), `MagicMock` (a flexible mock that records all calls and allows attribute chaining), `Mock`, and `AsyncMock`. The most common gotcha: you must patch the object where it's used (the importing module's namespace), not where it's defined. `from module import func` followed by `@patch('module.func')` patches the original, not the local name.

A collection of small, focused examples covering each pattern is far more useful than documentation for a library where the details matter — which is why this kind of MWE repository gets bookmarked by working engineers.

## Key points

- unittest.mock reference: `patch`, `MagicMock`, `Mock`, `AsyncMock` with concrete examples.
- Patch where the object is used (importing namespace), not where it's defined — the #1 gotcha.
- `return_value` sets what a mock returns; `side_effect` lets you raise exceptions or use a function.
- MWE format: each file demonstrates one pattern in isolation, copy-pasteable.
- From Data Day Science — data engineering / ML testing context.
- Pairs with pytest fixtures and factory_boy for a complete Python testing toolkit.

[Original](https://github.com/data-day-science/python_mocking_mwe) → GitHub
