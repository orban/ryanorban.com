---
title: ELI5 — sklearn Explainability Module
date: 2020-10-04
categories:
  - machine-learning
  - explainability
  - python
  - scikit-learn
  - interpretability
description: ELI5's sklearn module provides model explanation tools for scikit-learn estimators — feature importance, prediction decomposition, and permutation-based importance across linear models, tree ensembles, and SVMs. The explainability companion for sklearn workflows.
params:
  source: pinboard
  sourceUrl: https://eli5.readthedocs.io/en/latest/autodocs/sklearn.html
---

## Summary

ELI5 is a Python library for explaining machine learning model predictions, and its `eli5.sklearn` module integrates directly with scikit-learn estimators. The library covers two complementary explanation types: **weights** (what does the model globally think is important?) and **predictions** (why did this specific input get this output?).

For weights, `explain_weights_sklearn()` surfaces feature importances via coefficients (linear models), tree-based feature importance scores (Random Forest, Gradient Boosting), or permutation importance — which works model-agnostically by measuring how much performance drops when a feature is randomly shuffled. For predictions, `explain_prediction_sklearn()` decomposes individual predictions by tracking score contributions through decision paths (tree models) or computing weighted contributions from each feature (linear models).

The library supports the full scikit-learn classifier/regressor landscape: LogisticRegression, LinearSVC, Ridge, Lasso, SGDClassifier, RandomForest, GradientBoosting, ExtraTrees, SVM variants. There's also support for CountVectorizer integration to get readable feature names for text models, and a FeatureHasher unhashing utility for when features are hashed during preprocessing.

## Key points

- Permutation importance is the most reliable importance method when features are correlated — coefficient magnitudes and tree split gains can be misleading in that case.
- `explain_prediction_sklearn()` for tree models follows the actual decision path — this is exact, not approximate, unlike LIME or SHAP approximations.
- For text models, integrating with CountVectorizer lets you see which words/ngrams drive predictions — useful for debugging NLP classifiers.
- The `show_weights()` and `show_prediction()` helpers render HTML tables in Jupyter notebooks — designed for interactive analysis.
- Predecessor to the more comprehensive SHAP library; SHAP has largely superseded ELI5 for tree models but ELI5 remains simpler for basic linear model explanations.

[Original](https://eli5.readthedocs.io/en/latest/autodocs/sklearn.html)
