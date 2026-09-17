---
title: "LazyPredict: Fit All scikit-learn Models in One Line"
date: 2021-01-27
categories:
  - machine-learning
  - python
  - scikit-learn
  - automation
  - data-science
description: LazyPredict fits and evaluates all scikit-learn classifiers or regressors on a dataset with a single call, returning a sorted comparison table. A fast baseline scanner for figuring out which model family is worth investing in before tuning.
params:
  source: pinboard
  sourceUrl: https://towardsdatascience.com/lazy-predict-fit-and-evaluate-all-the-models-from-scikit-learn-with-a-single-line-of-code-7fe510c7281
---

## Summary

LazyPredict is a Python library that runs every scikit-learn classifier or regressor on a dataset and returns a comparison table of performance metrics — sorted by accuracy or RMSE. The interface is intentionally minimal: instantiate `LazyClassifier` or `LazyRegressor`, call `.fit()`, get a Pandas DataFrame of results. It's a baseline scanner, not a tuning tool.

The practical use case is early-stage model selection: before spending time on hyperparameter tuning for any specific model family, run LazyPredict to see which algorithms perform best out-of-the-box on your data. A linear model outperforming tree ensembles by default is informative; it suggests the relationship is roughly linear and complex models may be overfitting. This sanity check is faster than manually writing cross-validation loops for each algorithm.

The article by Eryk Lewinson on Towards Data Science introduces the library with practical examples and discusses when the approach is useful versus misleading. The main limitation is that default hyperparameters favor some model families over others, so a poor default-parameter performance isn't necessarily a rejection of that model. But as an initial filter before more careful evaluation, LazyPredict saves real time in exploratory work.

## Key points

- Runs all scikit-learn classifiers or regressors on a dataset and returns a sorted comparison table — no loops, no manual instantiation.
- Good for early model selection before hyperparameter tuning: a quick map of which model families are worth investigating further.
- Works with any dataset that fits in memory; built on scikit-learn's standard `fit`/`predict` interface.
- Limitation: default hyperparameters vary across model families, so comparisons are rough rather than definitive.
- Pairs naturally with SHAP or ELI5 once a candidate model is identified, to understand why it performs well.

[Original](https://towardsdatascience.com/lazy-predict-fit-and-evaluate-all-the-models-from-scikit-learn-with-a-single-line-of-code-7fe510c7281)
