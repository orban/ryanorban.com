---
title: redframes — Python Data Manipulation Library
date: 2022-10-25
categories:
  - python
  - data-science
  - dataframes
  - pandas
  - open-source
description: redframes is a general-purpose Python data manipulation library that wraps pandas with a more consistent, readable API — aimed at making common data wrangling tasks less verbose without abandoning the pandas ecosystem.
params:
  source: pinboard
  sourceUrl: https://github.com/maxhumber/redframes
---

## Summary

redframes is a Python data manipulation library by Max Humber that wraps pandas with a cleaner, more consistent API. The goal is to make common data wrangling tasks less verbose and more readable, without abandoning the pandas ecosystem entirely. The library lets you do standard DataFrame operations in a functional, method-chaining style that's easier to read than raw pandas syntax.

The criticism redframes responds to is real: pandas has a notoriously inconsistent API — some operations modify in place, some return new objects; some use `.apply()`, some use vectorized operations; the distinction between `.loc`, `.iloc`, and bracket indexing confuses beginners. Libraries like redframes, siuba, plydata, and dfply have all tried to create a more coherent R-style or dplyr-style interface for Python data work.

The tradeoff is that any wrapper over pandas adds a layer of abstraction that can obscure what's happening underneath, and often limits access to pandas' full feature set. Polars took a different approach — a new DataFrame library written in Rust with no pandas dependency — and has largely superseded the better pandas API category by offering a genuinely different paradigm (lazy evaluation, no mutable state, better performance) rather than just a cleaner surface.

## Key points

- Python DataFrame library wrapping pandas with a cleaner, more consistent method-chaining API.
- Addresses pandas' API inconsistency: in-place vs. return, `.loc`/`.iloc` confusion.
- Part of a category: siuba, plydata, dfply all tried similar wrappers with dplyr-style interfaces.
- Superseded in many use cases by Polars, which offers a genuinely new paradigm rather than a pandas wrapper.
- Appropriate for data practitioners who prefer the pandas ecosystem but want less verbose syntax.

[Original](https://github.com/maxhumber/redframes) → GitHub
