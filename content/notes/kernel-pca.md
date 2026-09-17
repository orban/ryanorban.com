---
title: Kernel PCA
date: 2014-09-28
categories:
  - machine-learning
  - dimensionality-reduction
  - kernel-methods
  - pca
  - python
description: Sebastian Raschka's tutorial on Kernel PCA — extending standard PCA to capture non-linear structure using the kernel trick with RBF kernels. Includes Python implementation, making it one of the clearest practical explanations of the technique available in 2014.
math: true
params:
  source: pinboard
  sourceUrl: http://sebastianraschka.com/Articles/2014_kernel_pca.html
---

## Summary

[Kernel PCA](/notes/kernel-pca/) extends PCA to capture non-linear structure in data by applying the kernel trick — projecting data implicitly into a high-dimensional feature space, computing PCA there, then working entirely in terms of inner products (which the kernel function computes directly). The result: dimensionality reduction that can unroll manifolds and separate classes that are linearly inseparable in the original space.

Sebastian Raschka's 2014 tutorial is a careful walkthrough with Python implementation, covering the math without losing the intuition. The key steps: (1) compute the kernel matrix K where K_ij = k(x_i, x_j) using an RBF kernel (Gaussian); (2) center the kernel matrix in feature space; (3) take the eigendecomposition of the centered kernel matrix; (4) the eigenvectors are the principal components in the high-dimensional space.

The most important practical point: [Kernel PCA](/notes/kernel-pca/) can unroll a Swiss roll dataset (points arranged on a curved 2D manifold embedded in 3D) that standard PCA cannot flatten. This makes it useful when data lies on a curved manifold — a common assumption in image and audio data, though in practice t-SNE and UMAP have largely displaced [Kernel PCA](/notes/kernel-pca/) for visualization because they better preserve neighborhood structure.

## Key points

- [Kernel PCA](/notes/kernel-pca/): applies kernel trick to PCA — enables non-linear dimensionality reduction without explicit feature mapping.
- RBF kernel (Gaussian): $k(x, y) = \exp(-\gamma \|x - y\|^2)$ — the most common kernel choice.
- Kernel trick: compute inner products in high-dimensional space implicitly via the kernel function — no explicit mapping needed.
- Kernel matrix centering is required — parallel to mean-centering in standard PCA.
- Can unroll manifolds (Swiss roll, concentric circles) that linear PCA cannot separate.
- In 2014 this was state-of-the-art for non-linear reduction; t-SNE and UMAP later became dominant for visualization.
- Sebastian Raschka (now at Lightning AI) is one of the best writers of practical ML tutorials with Python.

[Original](http://sebastianraschka.com/Articles/2014_kernel_pca.html)
