---
title: "From Python to Rust: YouTube Playlist"
date: 2023-11-06
categories:
  - rust
  - python
  - learning
  - video
  - programming-languages
description: A YouTube playlist teaching Rust to developers who already know Python — bridges concepts across the two languages rather than teaching Rust from scratch. Useful for Python engineers who want to understand Rust's ownership and performance model.
params:
  source: pinboard
  sourceUrl: https://m.youtube.com/playlist?list=PLEIv4NBmh-GsWGE9mY3sF9c5lgh5Z_jLr
---

![From Python to Rust: YouTube Playlist](/images/notes/from-python-to-rust.png)

## Summary

This YouTube playlist bridges Python to Rust — teaching Rust by mapping its concepts onto what a Python developer already knows, rather than starting from first principles. The approach is practical: if you understand Python's reference semantics, GC, and dynamic typing, you can frame Rust's ownership system, lifetimes, and static types as deliberate design choices addressing Python's tradeoffs.

The Python → Rust path is increasingly common for engineers working on performance-critical code in ML infrastructure, systems tooling, or network services. PyO3 makes it practical to write Rust extensions callable from Python, so many teams use Rust for hot paths while keeping Python for the overall application logic. Understanding Rust helps even if you never write a full Rust application.

The conceptual bridges: Python lists → Rust `Vec<T>` (with type annotations), Python dicts → `HashMap`, Python's GC → Rust's ownership + borrow checker, Python exceptions → Rust `Result<T, E>`, Python `None` → `Option<T>`. Framing ownership and lifetimes as the cost of no GC (and the benefit of predictable performance) makes the mental model click faster.

## Key points

- Frames Rust concepts relative to Python analogues — faster conceptual onboarding.
- Key bridges: ownership/borrow checker vs. GC, `Result`/`Option` vs. exceptions/None.
- Rust is increasingly relevant for Python engineers writing performance extensions via PyO3.
- Rust's compile-time guarantees (no null, no data races) are the payoff for the learning curve.
- Complementary resource: the official Rust Book (rustbook) for depth; this playlist for orientation.
- Rust adoption in the Python ecosystem: Ruff, Polars, Pydantic v2 all use Rust.

[Original](https://m.youtube.com/playlist?list=PLEIv4NBmh-GsWGE9mY3sF9c5lgh5Z_jLr)
