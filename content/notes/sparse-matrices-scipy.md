---
title: Sparse Matrices in SciPy
date: 2021-01-01
categories:
  - python
  - scipy
  - linear-algebra
  - data-structures
  - machine-learning
description: A visual explainer of sparse matrix formats in SciPy (COO, CSR, CSC, LIL, DOK) with animated illustrations showing how data is stored. Essential reading before working with high-dimensional feature matrices in ML or graph algorithms.
params:
  source: pinboard
  sourceUrl: https://matteding.github.io/2019/04/25/sparse-matrices/
---

## Summary

Matt Eding's post on sparse matrix formats in SciPy is one of the clearest visual explanations of a topic that's often poorly covered in ML tutorials. Sparse matrices — where most values are zero — appear constantly in ML: bag of words document-term matrices, user-item matrices for collaborative filtering, adjacency matrices for graphs, and feature matrices for wide, sparse datasets. Using a dense NumPy array for these wastes enormous amounts of memory and computation.

SciPy provides several sparse formats, each optimized for different operations:
- **COO** (Coordinate format): stores row, col, value triplets — easy to construct but slow to multiply
- **CSR** (Compressed Sparse Row): efficient for row slicing and matrix-vector products — the default for ML
- **CSC** (Compressed Sparse Column): efficient for column slicing and `A.T @ b` operations
- **LIL** (List of Lists): efficient for incremental construction, then convert to CSR before computing
- **DOK** (Dictionary of Keys): efficient for random element access during construction

The post's animated illustrations show how each format lays data out in memory, making the performance tradeoffs intuitive rather than abstract. Understanding when to convert between formats (construct in LIL, multiply in CSR) is the practical SKILL this post builds.

## Key points

- Sparse matrix formats store only non-zero values, with massive memory and compute savings when most values are zero.
- CSR (Compressed Sparse Row) is the standard format for machine learning — efficient row slices and matrix-vector multiply.
- **Build in LIL or COO, compute in CSR**: LIL supports efficient incremental construction; CSR supports efficient arithmetic.
- scikit-learn natively accepts SciPy sparse matrices — no need to convert to dense for most operations.
- Essential for NLP feature matrices (TF-IDF, bag of words), recommendation systems (collaborative filtering), and graph neural networks.

[Original](https://matteding.github.io/2019/04/25/sparse-matrices/) → GitHub
