---
title: Visualizing High-Dimensional Data in the Browser with SVD, t-SNE and Three.js
date: 2014-12-01
categories:
  - data-visualization
  - dimensionality-reduction
  - t-sne
  - svd
  - javascript
description: Datacratic's exploration of rendering high-dimensional data in the browser using SVD and t-SNE for dimensionality reduction and Three.js for 3D visualization. An early example of interactive ML visualization before dedicated tools like TensorBoard existed.
params:
  source: pinboard
  sourceUrl: http://datacratic.com/site/blog/visualizing-high-dimensional-data-browser-svd-t-sne-and-threejs
---

## Summary

High-dimensional data is invisible to human perception — a dataset with 100 features lives in a 100-dimensional space that can't be directly rendered. Datacratic's post addresses this by combining two complementary approaches: dimensionality reduction to compress the data into 2D or 3D, and Three.js for interactive WebGL rendering in the browser.

The two reduction techniques used are SVD (singular value decomposition) and t-SNE (t-distributed stochastic neighbor embedding). SVD is linear — it finds the orthogonal directions of maximum variance in the data (equivalent to PCA when centered). t-SNE is non-linear — it preserves local neighborhood structure, so clusters in the high-dimensional space appear as visible clusters in 2D. t-SNE had become the dominant visualization technique for high-dimensional ML outputs by 2014, particularly after Colah's visualizations of neural network representations.

Three.js is the JavaScript library that abstracts WebGL, making 3D graphics in the browser practical without writing shader code. Rendering dimensionality-reduced embeddings in 3D (rather than 2D) preserves more variance and lets the user rotate to find structure — an important advantage for exploratory data analysis.

## Key points

- t-SNE: non-linear dimensionality reduction that preserves local neighborhood structure — best for finding clusters visually.
- SVD/PCA: linear reduction that maximizes variance explained — fast, interpretable, good first pass.
- Three.js: WebGL-based 3D graphics in the browser — makes interactive 3D scatter plots feasible without plugins.
- 2D vs 3D: 3D preserves more structure and allows rotation to reveal cluster separation not visible from one angle.
- Datacratic (Montreal-based ML company) was doing production machine learning infrastructure before MLOps was a term.
- Precedes TensorBoard Projector (2016) which made this kind of embedding visualization standard.

[Original](http://datacratic.com/site/blog/visualizing-high-dimensional-data-browser-svd-t-sne-and-threejs)
