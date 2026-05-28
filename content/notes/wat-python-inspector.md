---
title: "wat: Deep Inspection of Python Objects"
date: 2024-07-26
categories:
  - python
  - debugging
  - developer-tools
  - introspection
  - open-source
description: wat is a Python deep inspection tool for exploring objects at runtime — type, value, methods, parent classes, source code, and signatures, all with one expression. Fills the gap between dir() and a full debugger.
params:
  source: pinboard
  sourceUrl: https://github.com/igrek51/wat
---

![wat: Deep Inspection of Python Objects](/images/notes/wat-python-inspector.png)

## Summary

wat is a Python runtime inspection tool designed for interactive exploration of unfamiliar objects. The name fits the use case: you encounter something you don't recognize, and `wat / object` tells you everything about it — its type with module origin, formatted value, methods, parent class hierarchy, function signatures, documentation, and even source code.

The syntax is intentionally minimal. `wat / obj` uses operator overloading to trigger inspection. Modifiers chain to customize output: `wat.short / obj` hides attributes for a concise summary, `wat.code / obj` shows the source, `wat.dunder / obj` reveals dunder attributes normally hidden by `dir()`. You can chain multiple modifiers. The Insta-Load feature lets you use it in any Python session without installation by pasting a single line.

wat sits in a useful gap between Python's built-in `dir()` (which gives names but no context) and a full debugger (which requires setup). For exploratory work in notebooks, REPLs, or when working with unfamiliar libraries, being able to inspect any object with a single expression is genuinely useful. It's one of those tools that becomes a muscle-memory habit once you use it.

## Key points

- `wat / object` syntax inspects any Python object: type, value, methods, classes, signatures, docs, source.
- Modifier system: `.short`, `.code`, `.long`, `.dunder`, `.locals`, `.globals` — chainable.
- No dependencies; Insta-Load enables use without installation (paste one line).
- Integrates with Python debugger via `breakpoint()`.
- Fills the gap between `dir()` (shallow) and a full debugger (heavy setup).
- Useful in Jupyter notebooks, REPLs, and exploratory Python development.

[Original](https://github.com/igrek51/wat) → GitHub
