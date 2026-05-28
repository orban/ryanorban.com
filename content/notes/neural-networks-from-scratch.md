---
title: Neural Networks from Scratch in Python
date: 2024-01-17
categories:
  - machine-learning
  - deep-learning
  - python
  - education
  - books
description: Neural Networks from Scratch (NNFS) is a book by Harrison Kinsley and Daniel Kukiela that builds neural networks in pure Python with no frameworks — the go-to resource for understanding what's actually happening inside backpropagation and gradient descent.
params:
  source: pinboard
  sourceUrl: https://nnfs.io/
---

![Neural Networks from Scratch in Python](/images/notes/neural-networks-from-scratch.png)

## Summary

[Neural Networks from Scratch](/notes/neural-networks-from-scratch/) (NNFS) is a book by Harrison Kinsley (sentdex) and Daniel Kukiela that teaches deep learning by building everything from scratch in pure Python — no PyTorch, no TensorFlow, no NumPy beyond basic array operations. The goal is to build a real working neural network while understanding every piece: forward pass, backpropagation, gradient descent, activation functions, loss functions, and optimization.

The from scratch framing matters because frameworks abstract away the operations that are most important to understand. When you use `model.fit()`, you don't see the chain rule being applied layer by layer or how gradients flow backward through activation functions. NNFS makes these mechanics explicit — which is the fastest route to understanding why your framework-based model isn't training, why vanishing gradients happen, or what batch normalization is actually doing.

The book works through increasingly complex networks: dense layers, activation functions (ReLU, softmax), loss functions (categorical cross-entropy, mean squared error), backpropagation through each layer type, dropout, and basic regularization. The code is available online chapter by chapter. For anyone who has used ML frameworks but wants to understand what's happening underneath, NNFS is the most direct path.

## Key points

- Builds neural networks in pure Python, no ML frameworks — every operation implemented explicitly.
- Covers forward pass, backpropagation, gradient descent, activation functions, loss functions, dropout.
- Best for: developers who use frameworks but want to understand what they're doing.
- Authors: Harrison Kinsley (sentdex YouTube) and Daniel Kukiela.
- Code available online; book sold on nnfs.io.
- Complements resources like 3Blue1Brown's neural network series for visual intuition.

[Original](https://nnfs.io/)
