---
title: Algorithms for Modern Hardware
date: 2022-02-18
categories:
  - performance-engineering
  - hardware
  - algorithms
  - systems
  - cpp
description: A free online textbook on algorithms for modern hardware — covers SIMD, cache optimization, branch prediction, and CPU microarchitecture from a performance engineering perspective. One of the most practical resources for writing truly fast code on real hardware.
params:
  source: pinboard
  sourceUrl: https://en.algorithmica.org/hpc/
---

## Summary

Algorithms for Modern Hardware (also called Algorithmica HPC) is a free textbook by Sergey Slotin focused on writing code that runs fast on actual hardware — not in the idealized RAM model that most algorithms textbooks use. The central thesis is that algorithmic complexity alone doesn't determine performance; understanding how CPU caches, SIMD instructions, branch prediction, and memory bandwidth work is equally critical for real-world software.

The book covers the full hardware-aware stack: from memory hierarchy fundamentals (why cache-oblivious algorithms beat cache-aware ones in practice) through SIMD vectorization with x86 intrinsics, to branch prediction pitfalls and instruction-level parallelism. It's closely related in spirit to MIT's Performance Engineering of Software Systems course (6.172) but freely available and updated for modern x86/ARM.

The approach is practical rather than theoretical — each concept comes with benchmarks on real hardware and concrete C++ code. This makes it especially useful for anyone building high-performance computing systems, low-latency infrastructure, or squeezing performance out of ML training loops.

## Key points

- Memory hierarchy first: cache misses often dominate real-world performance more than algorithmic choices.
- SIMD vectorization: x86 AVX/AVX-512 intrinsics can multiply throughput 8–32x for data-parallel code.
- Branch prediction mispredicts carry a ~15-cycle penalty — structuring code to be predictable matters.
- Profiling-driven methodology: the book teaches how to measure before optimizing, using `perf`, `cachegrind`, and microbenchmarks.
- Complements computer architecture courses with a software-side focus on performance optimization.

[Original](https://en.algorithmica.org/hpc/)
