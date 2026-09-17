---
title: Vowpal Wabbit Tutorial for the Uninitiated
date: 2014-01-07
categories:
  - machine-learning
  - vowpal-wabbit
  - online-learning
  - large-scale-ml
  - tutorial
description: Zinkov's beginner tutorial for Vowpal Wabbit — the fast online learning library from Microsoft Research. Shows the input format, basic invocation, and when VW's out-of-core learning beats batch methods.
params:
  source: pinboard
  sourceUrl: http://zinkov.com/posts/2013-08-13-vowpal-tutorial/
---

## Summary

Rob Zinkov's tutorial introduces Vowpal Wabbit (VW) — the fast online learning library originally from John Langford at Yahoo Research (later Microsoft Research). VW is built around a specific constraint: learn from data that doesn't fit in memory, streaming one example at a time. It uses the hashing trick to represent features, stochastic gradient descent with adaptive learning rates, and a binary input format that's faster to parse than CSV or JSON.

VW was used at scale in production systems — Yahoo's click prediction, Kaggle competition winners — because it could process millions of examples per second on a single CPU core. For the use cases it was designed for, no library was close in speed.

## Key points

- VW reads a streaming text format: `label | feature1:value feature2:value ...` — one example per line, suitable for piping from disk or network
- The hashing trick maps feature names to a fixed-size bit array without storing a vocabulary — handles new features at inference time with no code changes
- Online learning means weights update after each example, not after a full pass — single-pass learning is often enough for very large datasets
- Native support for multi-class classification, regression, cost-sensitive learning, and contextual bandits via `--cb` flag
- The tradeoff: VW is fast and memory-efficient but harder to debug than batch ML (no clean train/eval split, convergence is less transparent)

[Original](http://zinkov.com/posts/2013-08-13-vowpal-tutorial/)
