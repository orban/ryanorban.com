---
title: "less_slow.cpp: Learning High-Performance C++"
date: 2025-03-12
categories:
  - cpp
  - performance
  - simd
  - cuda
  - systems-programming
  - education
description: less_slow.cpp is a benchmarking and teaching repository by Ash Vardanian covering high-performance C++ from SIMD vectorization to CUDA and io_uring — designed to build intuition for performance-oriented design through measurements, not theory. A practical companion to reading architecture manuals.
params:
  source: pinboard
  sourceUrl: https://github.com/ashvardanian/less_slow.cpp
---

![less_slow.cpp: Learning High-Performance C++](/images/notes/less-slow-cpp.png)

## Summary

less_slow.cpp is an educational benchmarking repository by Ash Vardanian (of USearch and SimSIMD fame) covering performance-oriented C++ programming from basic numerics up to GPU kernels. The core idea is that you can't reason about performance without measuring it — the repo provides runnable benchmarks that reveal counterintuitive performance characteristics and build the right intuitions for writing fast code.

The coverage is unusually wide: SIMD vectorization, cache-friendly data structures, OpenMP and Intel oneTBB parallelism, io_uring kernel bypass networking, CUDA C++, PTX assembly, tensor cores, and modern C++20 features like coroutines and ranges. This isn't a learn C++ tutorial — it assumes you know the language and wants to teach you where the performance comes from and where it gets destroyed.

The benchmarks span multiple hardware platforms (x86-64, ARM, multiple GPU architectures), which makes the counterintuitive results actually portable — it's not an artifact of one architecture. The project belongs alongside The Art of Writing Efficient Programs (Fedor Pikus), Performance Analysis and Tuning on Modern CPUs (Denis Bakhvalov), and Computer Systems: A Programmer's Perspective as a hands-on reference for systems performance work.

## Key points

- Wide coverage: SIMD, memory/cache, OpenMP, io_uring, CUDA, PTX, C++20 (coroutines, ranges, consteval).
- Benchmarks not just theory: numbers on real hardware reveal counterintuitive costs.
- From Ash Vardanian, the author of USearch and SimSIMD — credible source on performance.
- Multi-platform: x86-64, ARM, multiple GPU architectures.
- Installs as a learning complement to low-level architecture documentation.
- Not for beginners — assumes C++ knowledge, teaches performance intuition.

[Original](https://github.com/ashvardanian/less_slow.cpp) → GitHub
