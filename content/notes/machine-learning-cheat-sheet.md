---
title: Machine Learning Cheat Sheet
date: 2013-06-20
categories:
  - machine-learning
  - reference
  - algorithms
  - data-science
  - cheat-sheet
description: Emanuel Ferm's machine learning cheat sheet — a compact reference covering the main supervised and unsupervised learning algorithms with notes on when to apply each. A quick-reference for practitioners who know the algorithms but want a memory aid for their properties.
params:
  source: pinboard
  sourceUrl: http://eferm.com/machine-learning-cheat-sheet/
---

## Summary

Emanuel Ferm's machine learning cheat sheet is a compact reference covering the major algorithm families — supervised learning (classification and regression) and unsupervised learning (clustering and dimensionality reduction) — with brief descriptions of when each is appropriate, key hyperparameters, and tradeoffs.

Cheat sheets like this served a specific need in the 2013 data science community: practitioners who knew the algorithms at a conceptual level but needed quick reminders about which to reach for and what their assumptions were. Choosing between logistic regression, naive Bayes, support vector machines, and decision trees for a classification problem required knowing not just the mechanics but the practical tradeoffs — interpretability, training speed, performance on high-dimensional data, sensitivity to class imbalance.

The format compresses years of algorithm course material into a scannable reference. The scikit-learn documentation's choosing the right estimator flowchart serves a similar purpose today; Ferm's cheat sheet was an early community effort in the same vein.

## Key points

- Supervised classification: logistic regression (linear, probabilistic outputs), SVM (good for high-dimensional), decision trees / random forests (interpretable, handles non-linearity), naive Bayes (fast, works well for text).
- Supervised regression: linear regression, ridge regression / lasso (regularized), gradient boosting (strong baseline for tabular data).
- Unsupervised: k-means clustering (fast, assumes spherical clusters), hierarchical clustering (no k required), PCA (linear dimensionality reduction).
- Each algorithm's assumptions matter more than the algorithm itself — linear regression fails on non-linear relationships; k-means fails on non-convex clusters.
- scikit-learn had just released version 0.13 in early 2013, standardizing the Python machine learning API — this cheat sheet predates the widely known sklearn algorithm selector.

[Original](http://eferm.com/machine-learning-cheat-sheet/)
