---
title: How To Choose The Right Test Options When Evaluating Machine Learning Algorithms
date: 2014-03-03
categories:
  - machine-learning
  - model-evaluation
  - cross-validation
  - statistics
  - best-practices
description: Jason Brownlee's guide to choosing between hold-out validation, k-fold cross-validation, and bootstrap estimation when evaluating ML algorithms. Covers when each approach is appropriate given dataset size and computational budget.
params:
  source: pinboard
  sourceUrl: http://machinelearningmastery.com/how-to-choose-the-right-test-options-when-evaluating-machine-learning-algorithms/
---

## Summary

Jason Brownlee at [Machine Learning Mastery](/notes/machine-learning-mastery/) cuts through the confusion around model evaluation methods by framing the choice as dependent on dataset size and what you're trying to estimate. The three main options — train/test split, k-fold cross-validation, and bootstrap estimation — make different tradeoffs between computational cost, bias, and variance of the performance estimate.

Train/test split: split data into a fixed training set (typically 70-80%) and a test set (20-30%), train once, evaluate once. Fast and simple, but high variance — the performance estimate depends heavily on which examples ended up in the test set. Only appropriate when you have a very large dataset where the test set is large enough to give a stable estimate. **K-fold cross-validation**: split data into k folds, train k models (each using a different fold as the test set), average the k performance scores. Lower variance than a single split, more expensive. 10-fold is the standard default. **Bootstrap estimation**: resample with replacement to create many training sets, evaluate on the out-of-bag examples. Better than k-fold for small datasets because it uses more of the data for training.

The practical guidance: default to 10-fold CV unless your dataset is very large (hold-out) or very small (bootstrap). For hyperparameter tuning, use nested CV (inner loop for tuning, outer loop for evaluation) to avoid data leakage from using the test set to select hyperparameters.

## Key points

- Train/test split: fast, high variance — only appropriate for large datasets where the test set itself is large enough for stable estimates.
- K-fold cross-validation: lower variance, k× more expensive — 10-fold is the community default for most problems.
- Bootstrap estimation: better for small datasets — samples with replacement, uses out-of-bag examples as the test set.
- Nested cross-validation: outer loop for unbiased performance estimation, inner loop for hyperparameter selection — prevents data leakage from parameter tuning.
- Stratified k-fold: preserve class distribution in each fold for imbalanced classification problems.

[Original](http://machinelearningmastery.com/how-to-choose-the-right-test-options-when-evaluating-machine-learning-algorithms/)
