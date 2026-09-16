---
title: Gradient Boosted Decision Trees
date: 2020-10-06
categories:
  - machine-learning
  - gradient-boosting
  - decision-trees
  - algorithms
  - ensemble-methods
description: An illustrated explainer of gradient boosted decision trees — how sequential weak learners correct prior errors by fitting residuals, and how this connects to gradient descent. Covers regression, binary classification, and multi-class variants.
params:
  source: pinboard
  sourceUrl: https://www.simonwardjones.co.uk/posts/gradient_boosted_decision_trees/
---

## Summary

Simon Ward-Jones' post explains gradient boosted decision trees (GBDTs) through the lens of sequential error correction. The core algorithm is: train a weak learner (a decision tree) on residuals from the previous stage, then update predictions additively: `F_m = F_{m-1} + (learning_rate × f_m)`. This process repeats for M rounds, with each tree targeting the remaining prediction error.

The connection to gradient descent is fundamental. Rather than updating model parameters by stepping in the direction of the negative gradient of a loss function, GBDTs update the predictions themselves. For common loss functions (mean squared error), the negative gradient of the loss with respect to predictions equals the residuals — which is why fit to residuals and fit to negative gradients are equivalent for regression. For binary classification, trees fit residuals in the transformed (sigmoid/log-odds) space; for multi-class classification, a separate additive model is maintained per class using softmax.

The learning rate (often called shrinkage) scales each tree's contribution — small learning rates reduce variance and overfitting but require more trees. The tradeoff between learning rate and number of estimators is a standard hyperparameter tuning axis for XGBoost, LightGBM, and scikit-learn's GradientBoostingClassifier.

## Key points

- **Sequential, not parallel**: unlike Random Forest which averages independent trees, GBDTs chain trees that each correct the prior's mistakes — order matters.
- Fitting to residuals = fitting to the negative gradient of MSE loss — this generalization is what allows GBDTs to optimize arbitrary differentiable loss functions.
- Learning rate controls the contribution of each tree: smaller rate → more trees needed → lower variance but slower training.
- GBDTs are the dominant tabular data model in practice — XGBoost and LightGBM win most structured-data Kaggle competitions.
- Interpretability is tractable: feature importance from GBDTs (gain, cover, frequency) is well-understood, and tools like SHAP extend this to per-prediction explanations.

[Original](https://www.simonwardjones.co.uk/posts/gradient_boosted_decision_trees/)
