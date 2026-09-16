---
title: Scikit-Learn Cheat Sheet (2021)
date: 2021-04-03
categories:
  - machine-learning
  - python
  - scikit-learn
  - data-science
  - reference
description: A cheat sheet for scikit-learn's main API patterns — estimator interface, preprocessing, model selection, and pipelines. Useful for quickly recalling the consistent fit/predict/transform pattern across all sklearn objects.
params:
  source: pinboard
  sourceUrl: https://towardsdatascience.com/scikit-learn-cheat-sheet-2021-python-for-data-science-c634fd5dcbd0
---

## Summary

Scikit-learn is Python's dominant classical machine learning library — covering classification, regression, clustering, dimensionality reduction, preprocessing, and model selection under a single consistent API. This cheat sheet covers the main patterns needed to use it effectively.

The core design principle of scikit-learn is the estimator interface: every object (model, preprocessor, transformer) exposes `fit()`, `predict()`, and/or `transform()` methods. This consistency means that once you know the interface, any algorithm works the same way. `Pipeline` composes estimators into chains — fit the whole pipeline, and preprocessing + model training happens in the right order automatically, with no data leakage from validation folds.

Key API patterns covered: data splitting (`train_test_split`, `cross_val_score`), preprocessing (`StandardScaler`, `MinMaxScaler`, `LabelEncoder`, `OneHotEncoder`), model selection (`GridSearchCV`, `RandomizedSearchCV`), evaluation metrics (`accuracy_score`, `roc_auc_score`, `mean_squared_error`), and common algorithms (RandomForest, SVM, LogisticRegression, KMeans).

## Key points

- Scikit-learn's estimator interface: every object has `fit()`, `predict()`, `transform()` — consistent across all algorithms.
- Pipeline chains preprocessing and model steps — prevents data leakage in cross-validation by design.
- `GridSearchCV` / `RandomizedSearchCV` for hyperparameter tuning with built-in cross-validation.
- Classical ML only — neural networks belong to PyTorch or TensorFlow; scikit-learn covers everything else.
- Still the go-to library for tabular data; complements XGBoost and LightGBM which follow the same interface.

[Original](https://towardsdatascience.com/scikit-learn-cheat-sheet-2021-python-for-data-science-c634fd5dcbd0)
