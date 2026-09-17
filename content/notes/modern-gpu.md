---
title: Modern GPU
date: 2013-05-20
categories:
  - gpu
  - cuda
  - parallel-computing
  - high-performance-computing
  - algorithms
description: Sean Baxter's moderngpu library — a CUDA toolkit providing high-level primitives (sort, reduce, scan, join) for GPU programming. Published by NVIDIA Research, it demonstrated that expressive, composable GPU programming was achievable without sacrificing raw throughput.
params:
  source: pinboard
  sourceUrl: http://nvlabs.github.io/moderngpu/
---

## Summary

Sean Baxter's moderngpu is a CUDA library published under NVIDIA Research that provides high-performance implementations of fundamental parallel primitives: sort, scan (prefix sum), reduce, merge, join, and segmented operations. The project's thesis: GPU programming should be expressive and composable, not just fast — you shouldn't have to write raw CUDA kernel code to get near-optimal throughput for common operations.

The library was influential in 2013 because it demonstrated that GPU computing for non-graphics workloads (scientific computing, data processing, machine learning) could be approachable. The CUDA programming model (threads, blocks, warps, shared memory) is notoriously difficult to use correctly and efficiently, and libraries like moderngpu abstracted the tricky parts while preserving performance.

The timing matters: 2013 was when deep learning was beginning its GPU-powered ascent. The foundational GPU operations that neural networks rely on — matrix multiplication, convolutions, reductions — are exactly the primitives that libraries like moderngpu optimized. The GPU computing ecosystem (cuBLAS, cuDNN, later CUDA Toolkit) was being built out during this period.

## Key points

- moderngpu provides high-level composable primitives: sort, reduce, scan, merge, join — all GPU-accelerated
- Written in CUDA C++; publishes the implementation techniques alongside working code
- Parallel prefix scan (parallel reduction) is the fundamental GPU primitive that scan, sort, and histogram all reduce to
- Performance: within 2x of hand-written optimal CUDA for most primitives, with far better readability
- Influenced subsequent GPU libraries; the techniques map to GPU computing concepts that remain relevant
- 2013 was early in the deep learning GPU wave — CUDA expertise was a differentiator

[Original](http://nvlabs.github.io/moderngpu/) → GitHub
