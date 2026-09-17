---
title: "DeZero Book: Build a Deep Learning Framework from Scratch"
date: 2022-02-13
categories:
  - deep-learning
  - python
  - education
  - autodiff
  - framework
description: DeZero is a book that builds a deep learning framework from scratch in pure Python — teaching automatic differentiation, computational graphs, and the internals of PyTorch/Chainer by implementing them. The most hands-on way to understand how deep learning frameworks actually work.
params:
  source: pinboard
  sourceUrl: https://koki0702.github.io/dezero-book/en/index.html
---

## Summary

The DeZero book (English translation of Deep Learning from Scratch 3 by Koki Imai, O'Reilly Japan) teaches how deep learning frameworks work by building one from the ground up in pure Python. The framework built — also called DeZero — closely mirrors the design of Chainer and early PyTorch: define-by-run (dynamic computational graphs), automatic differentiation via backpropagation, and a NumPy-backed tensor abstraction.

The learning arc starts from the most basic concepts: what is a computational graph, how does backpropagation flow through it, why do we need to retain the graph for second-order derivatives. It then builds up to more complex features: variable-length inputs/outputs, in-place operations, GPU support via CuPy, and standard layers (linear, convolution, RNN). By the end you've written something that can train a real neural network.

This approach pays dividends beyond framework understanding — you build strong intuition for gradient computation, why vanishing gradients happen, how weight initialization affects training dynamics, and how framework design choices (static vs dynamic graphs) affect usability. It complements the Dive into Deep Learning (d2l.ai) textbook which focuses on usage rather than internals. The framework-from-scratch genre also includes micrograd (Karpathy's minimal autograd) and the tinygrad project.

## Key points

- Define-by-run / dynamic graph: operations define the graph as they execute, enabling natural Python control flow.
- Automatic differentiation: the chain rule implemented as backward passes through a graph of Variable nodes.
- Built in pure Python + NumPy — readable implementation at the cost of performance.
- Progression: scalar autodiff → tensor ops → convolutions → RNNs → full training loop.
- Pairs with micrograd (simpler) and tinygrad (more complete) as framework-from-scratch resources.

[Original](https://koki0702.github.io/dezero-book/en/index.html) → GitHub
