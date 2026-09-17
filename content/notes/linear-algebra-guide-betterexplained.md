---
title: An Intuitive Guide to Linear Algebra
date: 2022-04-01
categories:
  - mathematics
  - linear-algebra
  - education
  - machine-learning
  - reference
description: BetterExplained's intuitive guide to linear algebra — builds geometric intuition for vectors, matrices, and transformations rather than drilling algebraic procedures. The right starting point before the formal treatment.
params:
  source: pinboard
  sourceUrl: https://betterexplained.com/articles/linear-algebra-guide/
---

## Summary

BetterExplained (Kalid Azad's site) approaches linear algebra by building geometric intuition before algebraic formalism. The core reframe: linear algebra is the mathematics of transformations. A matrix isn't a grid of numbers — it's a description of how space gets stretched, rotated, or reflected. Multiplication isn't row-dot-column — it's applying one transformation after another. This perspective, which takes several linear algebra courses to arrive at naturally, is established from page one.

The key conceptual moves: vectors are arrows in space with direction and magnitude; matrix multiplication is function composition (apply transformation A, then transformation B, result is AB); the determinant is the volume scaling factor of a transformation (determinant 0 = the transformation collapses space to a lower dimension, i.e., it's not invertible); eigenvectors are the directions that survive a transformation unchanged (they just scale by the eigenvalue). These geometrize every operation that textbooks present as mechanical rules.

The practical payoff for ML practitioners: linear algebra underpins almost all of machine learning. Neural network forward passes are matrix multiplications; the softmax function's stability depends on understanding transformations; PCA (Principal Component Analysis) is finding the eigenvectors of the data covariance matrix; SVD decomposes any matrix into rotations and scalings. The BetterExplained treatment gives the intuition needed to reason about these operations rather than just apply them mechanically.

## Key points

- Reframes linear algebra as the mathematics of geometric transformations — matrices describe how space changes.
- Matrix multiplication = function composition: multiplying AB means apply B then A in transformation terms.
- Determinant = volume scaling factor — a determinant of zero means the transformation is non-invertible (collapses dimensions).
- Eigenvectors are the fixed-point directions of a transformation; eigenvalues are their scaling factors.
- Practical ML connections: neural networks = stacked matrix multiplications; PCA = eigenvectors of covariance; SVD = any matrix as rotation-scale-rotation.
- By Kalid Azad at BetterExplained — known for building deep intuition before formal notation.

[Original](https://betterexplained.com/articles/linear-algebra-guide/)
