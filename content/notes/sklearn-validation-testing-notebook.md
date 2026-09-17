---
title: "Scikit-Learn: Model Validation and Testing (PyCon 2013 Notebook)"
date: 2014-03-11
categories:
  - machine-learning
  - scikit-learn
  - python
  - cross-validation
  - model-selection
description: Jake VanderPlas's PyCon 2013 notebook on model validation and testing in scikit-learn — covers train/test splits, cross-validation, and model selection in executable notebook form. A practical tutorial that shaped how Python practitioners learned to evaluate models.
params:
  source: pinboard
  sourceUrl: http://nbviewer.ipython.org/github/jakevdp/sklearn_pycon2013/blob/master/notebooks/09_validation_and_testing.ipynb
---

## Summary

This is notebook 9 from Jake VanderPlas's scikit-learn tutorial series for PyCon 2013 — one of the most widely-followed Python machine learning tutorials of its era. The notebooks were designed to be run interactively, making abstract concepts like cross-validation visible through immediate code execution. IPython Notebook (later Jupyter) was the delivery vehicle, and this tutorial helped establish the notebook as the standard format for data science education.

Validation and testing is the part of machine learning practice that separates practitioners who know algorithms from practitioners who can actually ship reliable models. The core lesson: never evaluate a model on the data it was trained on. Train/test split gives you one unbiased evaluation; k-fold cross-validation gives you k evaluations by rotating which portion of the data is held out, reducing variance in the error estimate.

Scikit-learn makes this accessible with a clean API: `train_test_split()`, `cross_val_score()`, `GridSearchCV` for hyperparameter tuning. The scikit-learn API design — estimators with `.fit()`, `.predict()`, `.score()` — was deliberate to make pipelines composable and testing interchangeable across algorithms.

## Key points

- Train/test split: basic protection against overfitting — hold out a random subset before training, evaluate on it after.
- K-fold cross-validation: more reliable than a single split — rotate which k-th of data is the test set, average the k scores.
- Hyperparameter tuning via GridSearchCV: searches over parameter combinations with cross-validation, avoiding data leakage from using test set for tuning.
- The bias-variance tradeoff is visible in learning curves: models with high bias underfit training data, high variance models overfit it.
- scikit-learn's consistent estimator API makes swapping algorithms trivial — the same validation code works across logistic regression, random forest, SVM, etc.

[Original](http://nbviewer.ipython.org/github/jakevdp/sklearn_pycon2013/blob/master/notebooks/09_validation_and_testing.ipynb) → GitHub
