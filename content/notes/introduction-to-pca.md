---
title: Introduction to Principal Component Analysis (PCA)
date: 2014-11-03
categories:
  - machine-learning
  - dimensionality-reduction
  - pca
  - statistics
  - linear-algebra
description: Laura Diane Hamilton's accessible introduction to Principal Component Analysis — covering the geometric and algebraic intuition without requiring a linear algebra background. One of the cleaner beginner explanations of a technique that's notoriously hard to explain well.
params:
  source: pinboard
  sourceUrl: http://www.lauradhamilton.com/introduction-to-principal-component-analysis-pca
---

## Summary

Principal Component Analysis (PCA) is one of the most widely used techniques in data science and machine learning, and one of the most commonly poorly explained. Laura Diane Hamilton's introduction approaches it from the intuitive end: PCA finds the directions in your data that capture the most variance, and you can project your data onto fewer of those directions while retaining most of the information.

The geometric picture: imagine a cloud of points in 2D that stretches diagonally. The first principal component is the axis along which the data varies most — a diagonal line through the cloud. The second principal component is perpendicular to the first. PCA rotates the coordinate system so the new axes align with these directions of maximum variance, then you can drop the last few axes (lowest variance) to reduce dimensionality.

The algebraic machinery: PCA is computed via eigendecomposition of the covariance matrix (or equivalently SVD of the centered data matrix). The eigenvectors are the principal components; the eigenvalues tell you how much variance each component explains. Choosing how many components to keep is typically done by looking at the explained variance cumulative plot and picking a threshold (e.g., 95%).

## Key points

- PCA finds orthogonal directions of maximum variance — projecting onto the top-k gives the best k-dimensional representation.
- Eigendecomposition of the covariance matrix: eigenvectors = principal components, eigenvalues = variance explained.
- Equivalently computed via SVD of the centered data matrix — numerically more stable than eigendecomposition.
- Explained variance ratio: how much of total variance each component captures — used to choose number of components.
- Mean-centering (subtracting the mean) is required; scaling (dividing by std dev) is optional but often needed.
- Use cases: visualization (reduce to 2D for plotting), noise reduction, feature compression, preprocessing for other models.
- Related: [Kernel PCA](/notes/kernel-pca/) for non-linear dimensionality reduction, t-SNE and UMAP for neighborhood-preserving visualization.

[Original](http://www.lauradhamilton.com/introduction-to-principal-component-analysis-pca)
