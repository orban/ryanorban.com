---
title: "Parakeet: A Faster Python for a Better Tomorrow"
date: 2013-10-10
categories:
  - python
  - performance
  - jit
  - scientific-computing
  - compiler
description: Parakeet was a Python JIT compiler targeting NumPy array operations, promising to make numerical Python code run at near-native speeds without rewriting in C or Cython. An early attempt at the problem that Numba later solved more completely.
params:
  source: pinboard
  sourceUrl: http://preview.getprismatic.com/story/1381382025412?share=true
---

![Parakeet: A Faster Python for a Better Tomorrow](/images/notes/parakeet-faster-python.png)

## Summary

Parakeet was a JIT compiler for Python that targeted NumPy array operations specifically. The pitch was straightforward: Python loops over arrays are slow; C is fast but requires rewriting code; Cython helps but requires type annotations; Parakeet would compile regular Python/NumPy code to fast native code automatically.

The problem Parakeet was trying to solve was real and important in 2013. Scientific Python users relied on NumPy vectorized operations to get C-like performance — but sometimes an algorithm naturally required loops, and those were 100x slower than the vectorized equivalent. Parakeet promised to JIT-compile those loops.

Numba, developed by Continuum Analytics (now Anaconda), ultimately won this space — it used LLVM to JIT-compile NumPy-heavy functions and later added CUDA GPU compilation. Parakeet was an earlier attempt in the same direction. The broader pattern — making Python fast for numerical computing without requiring users to leave Python — also drove PyPy, Cython, and eventually Numba.

## Key points

- Parakeet: JIT compiler for NumPy-heavy Python code; automatic compilation of loops to native speed without rewriting.
- Target audience: scientific Python users who needed loops (couldn't vectorize everything) but didn't want to drop into C/Cython.
- Numba later solved this problem more completely using LLVM with added GPU support via CUDA.
- Part of a broader 2013 conversation about making Python faster for data science without sacrificing the language's expressiveness.
- Reflects the bottleneck that was clear even then: Python the language was beloved; Python the runtime was too slow for production numerical work.

[Original](http://preview.getprismatic.com/story/1381382025412?share=true)
