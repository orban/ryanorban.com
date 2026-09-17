---
title: Visualizing K-Means Clustering
date: 2014-01-23
categories:
  - machine-learning
  - k-means
  - visualization
  - interactive
description: Naftali Harris's interactive visualization of k-means clustering — place points on a canvas and watch the algorithm converge step by step. Exposes why initialization matters and where k-means fails.
params:
  source: pinboard
  sourceUrl: http://www.naftaliharris.com/blog/visualizing-k-means-clustering/
---

## Summary

Naftali Harris's interactive k-means clustering visualizer lets you place data points on a canvas, choose an initialization method, and watch the algorithm converge step-by-step. The demo exposes the core mechanics: centroids move toward cluster means, assignments update, and you see exactly how initialization affects which local minimum the algorithm lands in.

The visualization works especially well for building intuition about k-means' sensitivity to initialization. Random initialization sometimes produces poor cluster boundaries that k-means++ was designed to fix. Watching the algorithm iterate makes it clear why: if two centroids start near the same dense region, one cluster absorbs territory that should belong to the other.

## Key points

- Interactive canvas — place Gaussian blobs, line segments, or rings to test clustering behavior on different geometries
- Step-through animation shows centroid movement and assignment updates at each iteration
- Demonstrates k-means++ vs random initialization — the quality difference is visually stark on adversarial inputs
- Shows failure modes clearly: high-variance clusters, unevenly-sized clusters, and non-convex shapes all break k-means
- Pairs well with k-means++ theory — the visualization shows WHY smarter initialization matters before the math does

[Original](http://www.naftaliharris.com/blog/visualizing-k-means-clustering/)
