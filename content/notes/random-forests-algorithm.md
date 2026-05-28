---
title: Random Forests Algorithm
date: 2013-09-25
categories:
  - random-forest
  - machine-learning
  - ensemble-methods
  - algorithms
  - tutorial
description: An introduction to the Random Forests algorithm — explaining how ensembling many decorrelated decision trees reduces variance and produces a robust classifier. A standard explainer from the Data Science Central era.
params:
  source: pinboard
  sourceUrl: http://preview.getprismatic.com/story/1380088662431?share=true
---

## Summary

Random Forest is an ensemble method that builds many decision trees and aggregates their predictions, typically by majority vote for classification or averaging for regression. The key insight: individual decision trees have high variance (they overfit), but averaging many trees trained on different random subsets of data and features reduces that variance dramatically while keeping bias low.

Two sources of randomness give Random Forest its name: **bootstrap sampling** (each tree is trained on a random sample with replacement from the training set) and **feature subsampling** (at each split, only a random subset of features is considered). The feature subsampling is what makes the trees decorrelated — without it, all trees would use the same dominant features and be nearly identical, providing no benefit from ensembling.

Random Forest was introduced by Leo Breiman in 2001 and became one of the dominant algorithms in the 2010s — competitive on structured/tabular data with almost no hyperparameter tuning required, robust to outliers and missing values, and providing built-in feature importance estimates. scikit-learn's implementation made it accessible to any Python user with `RandomForestClassifier`.

## Key points

- Random Forest: ensemble of decision trees with bootstrap sampling + random feature subsets → decorrelated trees → averaged prediction reduces variance.
- Leo Breiman's 2001 algorithm; remains state-of-the-art for tabular data alongside gradient boosting methods.
- Built-in feature importance: mean decrease in impurity across all trees gives a ranking of feature relevance.
- Robust defaults: works well with minimal hyperparameter tuning; number of trees is the main parameter (more is generally better up to a point).
- The key distinction from Gradient Boosting: trees are built independently in parallel (RF) vs. sequentially correcting errors (GB).

[Original](http://preview.getprismatic.com/story/1380088662431?share=true)
