---
title: Eli Bendersky's Website
date: 2022-07-15
categories:
  - programming
  - systems
  - go
  - python
  - education
description: Eli Bendersky's personal blog is a deep-dive technical reference for systems programming, compilers, and Go/Python internals. His posts on how things work at the implementation level — parsers, ELF binaries, coroutines, LLVM — are consistently among the best on the internet.
params:
  source: pinboard
  sourceUrl: https://eli.thegreenplace.net/
---

## Summary

[Eli Bendersky](/notes/eli-bendersky/) is a software engineer (formerly at Google) who writes long-form technical posts on systems programming, compilers, and language internals. The blog sits in a rare category: expert-level content that's also well-explained, covering topics that are either underdocumented or typically only discussed in textbooks.

The recurring themes: Go internals (goroutine scheduling, memory model, runtime details), Python internals (CPython bytecode, the GIL, coroutines), compiler construction (parsing, AST design, LLVM), and systems programming (ELF file format, dynamic linking, WASM). The posts typically go several levels deeper than official documentation — not here's how to use the API but "here's how the API is implemented, and why."

His work on LLVM and Clang is particularly cited in compiler circles. Posts covering tutorial: writing a compiler with LLVM, IR generation, and the structure of LLVM passes give readers a working-code entry point into a codebase that's notoriously difficult to navigate. Similarly, the Python internals series is frequently linked when people want to understand the CPython implementation.

## Key points

- Deep Go internals posts: goroutine scheduler implementation, memory model, escape analysis, channels implementation
- Python series: CPython bytecode, the GIL, generator/coroutine machinery, object model
- LLVM and Clang tutorials: IR generation, pass structure, practical compiler construction with a real backend
- ELF and dynamic linking series: how binaries work on Linux at the linker and loader level
- Complements colah's blog (ML) and [Jay Alammar](/notes/jay-alammar/) (ML) for a complete set of high-quality technical explanation blogs

[Original](https://eli.thegreenplace.net/)
