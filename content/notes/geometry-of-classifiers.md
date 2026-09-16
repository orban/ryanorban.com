---
title: The Geometry of Classifiers
date: 2014-12-23
categories:
  - machine-learning
  - classifiers
  - geometry
  - decision-theory
description: Nina Zumel's geometric treatment of machine learning classifiers — how decision boundaries, margins, and probability regions look in feature space. Builds visual intuition for why different classifier families make the tradeoffs they do.
params:
  source: pinboard
  sourceUrl: http://www.win-vector.com/blog/2014/12/the-geometry-of-classifiers/
---

## Summary

Nina Zumel of Win-Vector LLC approaches classification from a geometric perspective: rather than describing classifiers by their mathematical formulas, she frames them by the shapes they carve into feature space. This geometric lens is particularly useful for building intuition about when a classifier will or won't work on a given dataset.

Every binary classifier defines a decision boundary — a surface in feature space that separates the two classes. The shape of this boundary is the key geometric property. Logistic regression draws a hyperplane (linear boundary). SVM with a linear kernel also draws a hyperplane but maximizes the margin to the nearest training points. SVM with an RBF kernel can draw non-linear boundaries that wrap around clusters. Decision trees draw axis-aligned rectangular partitions. k-NN draws Voronoi boundaries that conform to local density.

The practical payoff of geometric thinking: if you plot your data and the classes form linearly separable clusters, a linear classifier is sufficient and adding complexity risks overfitting. If the classes are arranged in concentric rings or XOR patterns, you need non-linear boundaries. Kernel methods solve this by implicitly projecting data into higher dimensions where a linear boundary in the high-dimensional space corresponds to a curved boundary in the original space.

## Key points

- Every classifier defines a decision boundary — the surface dividing classes in feature space.
- Logistic regression and linear SVM: linear (hyperplane) boundaries — fast, low variance, works when classes are separable.
- SVM with RBF kernel: non-linear boundaries via the kernel trick — maps to high-dimensional space implicitly.
- Decision trees: axis-aligned box boundaries — interpretable but can't capture diagonal structure without many splits.
- k-NN: Voronoi diagram boundaries — adapts to local geometry but expensive at inference time.
- Geometric intuition is the fastest path to diagnosing whether a model is a good fit for a dataset's structure.
- Written by Nina Zumel, co-author of *Practical Data Science with R*.

[Original](http://www.win-vector.com/blog/2014/12/the-geometry-of-classifiers/)
