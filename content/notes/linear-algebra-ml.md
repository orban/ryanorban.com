---
title: Linear Algebra — Math for Machine Learning
date: 2022-07-16
categories:
  - machine-learning
  - linear-algebra
  - mathematics
  - education
  - youtube
description: A YouTube course on linear algebra specifically framed for machine learning — covering vectors, matrices, eigenvalues, and the operations that underlie neural networks. Useful complement to theoretical ML reading when the math intuition is missing.
params:
  source: pinboard
  sourceUrl: https://www.youtube.com/watch?v=uZeDTwWcnuY
---

## Summary

This YouTube course on linear algebra is aimed at machine learning practitioners who need the mathematical foundation to understand what's actually happening inside models. Linear algebra is the core language of deep learning: weights are matrix multiplications, activations are vector transformations, and backpropagation traces gradients through those operations.

The topics covered map directly to ML practice: vector spaces and why inputs are points in high-dimensional space; matrix multiplication as the fundamental operation in neural network forward passes; eigenvalues and eigenvectors as the language of principal component analysis (PCA) and singular value decomposition (SVD); and dot products as the operation behind attention scores in transformer models.

This kind of resource is useful in 2022 for the ML-curious developer who has been building systems on top of PyTorch or TensorFlow without fully internalizing the math. The transformer architecture had become ubiquitous by mid-2022 — self-attention, softmax over scaled dot products, projection matrices — and those concepts require comfort with linear algebra to understand at more than a surface level.

## Key points

- Core prerequisite for understanding transformer architectures and attention mechanisms at a mathematical level
- Matrix multiplication is the fundamental building block of all feedforward neural network layers
- SVD and PCA underlie dimensionality reduction, principal component analysis, and some embedding techniques
- Eigendecomposition explains why certain weight initializations work better than others
- Pairs with 3Blue1Brown's Essence of Linear Algebra series for visual intuition

[Original](https://www.youtube.com/watch?v=uZeDTwWcnuY)
