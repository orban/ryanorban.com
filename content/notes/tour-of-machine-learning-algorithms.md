---
title: A Tour of Machine Learning Algorithms
date: 2014-07-03
categories:
  - machine-learning
  - algorithms
  - overview
  - reference
description: Jason Brownlee's taxonomy of machine learning algorithms organized by learning style and similarity — a map of the algorithm space useful for orienting newcomers. The categorization gives a mental model for when to reach for which algorithm family.
params:
  source: pinboard
  sourceUrl: http://machinelearningmastery.com/a-tour-of-machine-learning-algorithms/
---

## Summary

Jason Brownlee of [Machine Learning Mastery](/notes/machine-learning-mastery/) organized this overview as a map of the machine learning algorithm space, grouped by learning style and then by similarity of approach. In 2014 this kind of taxonomy was genuinely useful: scikit-learn had made dozens of algorithms accessible through the same API, but practitioners still needed a mental model for which family to try on a given problem.

The top-level grouping is by learning paradigm: supervised learning (labeled training examples), unsupervised learning (no labels, find structure), and semi-supervised learning / reinforcement learning (specialized settings). Within supervised learning, the main split is regression (continuous output) versus classification (discrete output). Within unsupervised, the main split is clustering versus dimensionality reduction.

The deeper grouping is by algorithm family: regression algorithms (linear, logistic, LASSO, ridge regression), instance-based algorithms (k-nearest neighbors), decision tree methods, Bayesian methods (naive Bayes), kernel methods (support vector machine), ensemble methods (random forest, gradient boosting), and neural networks. Each family has distinct assumptions about data structure, and knowing which family a new algorithm belongs to gives you a head start on understanding it.

## Key points

- The fundamental split: supervised learning requires labels; unsupervised learning finds structure without them — most real-world problems are supervised.
- Instance-based learning (k-NN) stores training data directly; model-based learning (linear regression, SVM) abstracts it into parameters.
- Ensemble methods (random forest, gradient boosting, bagging) consistently outperform single models by combining multiple weak learners.
- Bias-variance tradeoff runs through every algorithm family: simple models (linear) underfit, complex models (deep trees) overfit.
- In 2014, gradient boosting (especially XGBoost which emerged that same year) was becoming the dominant algorithm for tabular data — a position it still holds.

[Original](http://machinelearningmastery.com/a-tour-of-machine-learning-algorithms/)
