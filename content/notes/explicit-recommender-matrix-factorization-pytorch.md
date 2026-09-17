---
title: Explicit Recommender System — Matrix Factorization in PyTorch
date: 2020-09-03
categories:
  - machine-learning
  - recommender-systems
  - pytorch
  - matrix-factorization
  - collaborative-filtering
description: A tutorial implementing explicit recommender systems via matrix factorization in PyTorch — using Embedding layers for user and item factors, trained with alternating gradient descent. Concrete implementation of collaborative filtering fundamentals.
params:
  source: pinboard
  sourceUrl: https://medium.com/@rinabuoy13/explicit-recommender-system-matrix-factorization-in-pytorch-f3779bb55d74
---

## Summary

This tutorial implements a classic matrix factorization recommender system in PyTorch for explicit feedback data (numerical ratings, not implicit signals like clicks). Explicit recommender systems predict user preferences from direct feedback, making them a cleaner starting point than implicit models.

Collaborative filtering via matrix factorization decomposes the sparse user-item interaction matrix (most users haven't rated most items) into two lower-dimensional factor matrices: user factors and item factors. The assumption is that hidden latent factors (genre preferences, style affinity, etc.) explain why users rated items the way they did. Reconstructing the original matrix from these factors fills in the missing ratings — giving predictions for unrated items.

The PyTorch implementation uses `nn.Embedding` layers to represent user and item factors (learnable lookup tables), plus bias terms per user and item. Training minimizes mean squared error between predicted and actual ratings using stochastic gradient descent, processing batches of user-item pairs over 1,000 epochs. The alternating gradient descent approach updates user parameters with item parameters fixed, then swaps — similar to the original ALS (Alternating Least Squares) algorithm but using autodiff.

## Key points

- `nn.Embedding` in PyTorch is the natural primitive for user/item factor tables — a learnable matrix where each row is a latent factor vector, indexed by user/item ID.
- Bias terms per user and item capture systematic tendencies (users who always rate high, items that are universally popular) separately from preference alignment.
- Explicit feedback (ratings) vs. implicit (clicks, views): explicit is cleaner to model but rarer. Most modern production systems use implicit feedback — BPR (Bayesian Personalized Ranking) is the implicit counterpart to this approach.
- The cold start problem applies: new users and items with no ratings can't be represented in the learned embeddings. Content-based features or hybrid approaches address this.
- PyTorch allows GPU acceleration of embedding lookups — significant speedup for large embedding tables at production scale.

[Original](https://medium.com/@rinabuoy13/explicit-recommender-system-matrix-factorization-in-pytorch-f3779bb55d74)
