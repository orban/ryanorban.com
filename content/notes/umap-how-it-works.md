---
title: How UMAP Works
date: 2021-07-03
categories:
  - machine-learning
  - dimensionality-reduction
  - umap
  - visualization
  - mathematics
description: The official UMAP documentation explaining the mathematical intuition behind the algorithm — Riemannian geometry and fuzzy simplicial sets as the conceptual foundation. More rigorous than most t-SNE/UMAP comparisons and explains why UMAP preserves global structure better.
params:
  source: pinboard
  sourceUrl: https://umap-learn.readthedocs.io/en/latest/how_umap_works.html
---

![How UMAP Works](/images/notes/umap-how-it-works.png)

## Summary

UMAP (Uniform Manifold Approximation and Projection) is a dimensionality reduction algorithm from Leland McInnes at Tutte Institute that has largely displaced t-SNE for high-dimensional data visualization in machine learning. The official documentation explains the mathematical foundations: UMAP is built on Riemannian geometry and fuzzy simplicial sets — a more rigorous foundation than t-SNE's probabilistic perplexity approach.

The core intuition: UMAP assumes high-dimensional data lies on a manifold, and it learns a fuzzy topological representation of that manifold from the data. Then it optimizes a low-dimensional representation that has a similar fuzzy topological structure. This is different from t-SNE's approach (which models local neighborhood probabilities) in a key way: UMAP's objective explicitly tries to preserve both local structure (nearby points stay nearby) and global structure (the relative arrangement of clusters in the full space).

Practically: UMAP is faster than t-SNE (especially for large datasets), produces embeddings that better preserve the global geometry of the data, supports supervised and semi-supervised variants, and has hyperparameters that are easier to interpret (`n_neighbors` controls local vs. global tradeoff; `min_dist` controls how tightly points cluster). For embedding visualization — projecting high-dimensional word embeddings or image features into 2D — UMAP is now the standard tool.

## Key points

- UMAP is grounded in Riemannian geometry and fuzzy simplicial sets — mathematically cleaner than t-SNE's probabilistic foundation.
- Better global structure preservation than t-SNE: cluster relationships in the full space are reflected in the 2D projection.
- Faster than t-SNE at scale, especially for large N.
- Key hyperparameters: `n_neighbors` (local vs. global), `min_dist` (cluster tightness), `metric` (distance function).
- Supports supervised UMAP: use class labels to enforce separation in the embedding space.

[Original](https://umap-learn.readthedocs.io/en/latest/how_umap_works.html)
