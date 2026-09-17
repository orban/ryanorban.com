---
title: The Remarkable k-means++
date: 2014-01-03
categories:
  - machine-learning
  - k-means
  - algorithms
  - statistics
  - theory
description: Larry Wasserman's Normal Deviate blog post on k-means++ — the 2007 initialization trick from Arthur and Vassilvitskii that gives k-means an O(log k) approximation guarantee and better convergence in practice.
params:
  source: pinboard
  sourceUrl: https://normaldeviate.wordpress.com/2012/09/30/the-remarkable-k-means/
---

## Summary

Larry Wasserman's Normal Deviate blog post introduces k-means++, the initialization algorithm from David Arthur and Sergei Vassilvitskii (2007) that makes k-means clustering dramatically more reliable. Standard k-means picks initial centroids randomly, which can place two centroids in the same dense region and produce poor final clusters. k-means++ initializes greedily: each new centroid is sampled proportionally to its squared distance from the nearest existing centroid, spreading seeds naturally across the data.

The result is an algorithm with an O(log k) approximation guarantee in expectation — provably competitive with optimal clustering, a guarantee that random initialization provides no analog to. In practice, k-means++ converges faster and to better solutions, not just theoretically but empirically across standard benchmarks.

## Key points

- Replaces random initialization with a probabilistic greedy scheme — each new centroid is sampled proportional to D² distance from the nearest already-chosen centroid
- Provides an O(log k) approximation guarantee that standard k-means initialization lacks — the gap matters most for high-k settings
- Faster convergence in practice, not just in theory — seeds start spread across dense regions rather than clustered together
- Implemented as the default initialization in scikit-learn's `KMeans` (`init='k-means++'`) — most practitioners use it without knowing why
- The Arthur & Vassilvitskii paper is a clean example of a trivial modification to an algorithm yielding strong theoretical guarantees

[Original](https://normaldeviate.wordpress.com/2012/09/30/the-remarkable-k-means/)
