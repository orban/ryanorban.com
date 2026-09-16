---
title: "Scalene: High-Performance Python Profiler"
date: 2022-02-26
categories:
  - python
  - profiling
  - performance
  - developer-tools
  - open-source
description: Scalene is a high-performance Python profiler that measures CPU time, GPU time, and memory simultaneously with very low overhead — and attributes memory allocation and copy costs line-by-line. The best profiler for Python if you care about both speed and memory.
params:
  source: pinboard
  sourceUrl: https://github.com/plasma-umass/scalene
---

## Summary

Scalene is an open-source Python profiler from the PLASMA lab at UMass Amherst that simultaneously profiles CPU time, GPU time, and memory allocation at the line level with very low overhead. It does things standard profilers like `cProfile` can't: it distinguishes time spent in Python code from time spent in native C/C++ extensions, tracks memory allocation by line (not just total), detects memory copy operations (often the hidden cost in NumPy and PyTorch code), and reports potential GPU memory usage.

The architecture is clever: instead of instrumenting every function call (which is what `cProfile` does, creating overhead proportional to function call frequency), Scalene uses statistical sampling at the OS level via signals. A timer fires at regular intervals and records where the program is — similar to how `perf` or `Instruments` work for C programs. This makes Scalene fast enough to run on production-like workloads rather than just small benchmarks.

For machine learning and data science work specifically, the memory profiling is the killer feature. NumPy and PyTorch operations can silently create large intermediate arrays; the memory copy tracking helps identify when data is being unnecessarily copied between CPU and GPU memory, which is often the actual performance bottleneck in training loops.

The output is a color-coded HTML report or terminal output, showing each line of code with its CPU%, GPU%, memory allocation, and peak memory. The AI-powered optimization suggestions (added in later versions) use an LLM to suggest code changes based on profiling data.

## Key points

- Simultaneously profiles CPU, GPU, and memory — most profilers only do one.
- Line-level attribution for both time and memory allocation — not just function-level.
- Detects memory copy overhead (a frequent hidden cost in NumPy/PyTorch workflows).
- Statistical sampling via OS signals = low overhead, suitable for profiling realistic workloads.
- Distinguishes Python time from native extension time — pinpoints whether bottlenecks are in Python or C extensions.
- From PLASMA lab at UMass — same group that built Cython and other Python performance tooling.

[Original](https://github.com/plasma-umass/scalene) → GitHub
