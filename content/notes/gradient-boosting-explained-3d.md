---
title: Gradient Boosting Explained
date: 2016-07-27
categories:
  - machine-learning
  - gradient-boosting
  - visualization
  - algorithms
  - education
description: Alex Rogozhnikov's interactive 3D visualization of gradient boosting — shows how decision boundaries evolve as the ensemble builds up trees. One of the cleaner intuition-builders for gradient boosting before XGBoost dominance made it feel like a black box.
params:
  source: pinboard
  sourceUrl: https://arogozhnikov.github.io/2016/06/24/gradient_boosting_explained.html
---

![Gradient Boosting Explained](/images/notes/gradient-boosting-explained-3d.png)

## Summary

This interactive explainer by Alex Rogozhnikov (author of the hep_ml library and arranger of many ML visualizations) uses 3D plots to show what gradient boosting is actually doing. The central pedagogical move: rather than explaining boosting algebraically, Rogozhnikov shows the decision boundary evolving step by step as each new decision tree is added to the ensemble. Watching the boundary sharpen across iterations makes the mechanism visceral in a way that equations alone don't.

The key insight the visualization conveys: gradient boosting works by having each successive tree fit the *residuals* of the previous ensemble — the errors that remain. This is equivalent to gradient descent in function space. The loss surface is traversed by adding small functions (trees) that point in the direction that most reduces loss. The 3D visualization shows this gradient descent happening geometrically, with the prediction surface approaching the true function.

In 2016, XGBoost had just popularized gradient boosting for structured/tabular data after winning several Kaggle competitions. This was the moment when ML practitioners started using gradient boosting widely but often without deep understanding of why it worked. Articles like this one filled a gap: giving practitioners enough geometric intuition to make better decisions about hyperparameters (learning rate, tree depth, number of trees) without requiring them to read the original Friedman papers. By 2020, LightGBM and XGBoost were the dominant frameworks, and tools like SHAP had added post-hoc interpretability on top.

## Key points

- Visualizes gradient boosting as function-space gradient descent — each tree is a step in the direction that reduces residual error.
- 3D plots make the decision boundary's evolution concrete: you see the ensemble get more complex and more accurate with each tree added.
- Connects gradient boosting to gradient descent rigorously: fitting to residuals = following the negative gradient of the MSE loss.
- Published in 2016 when XGBoost was newly dominant on Kaggle — served as an intuition builder for practitioners using it.
- Alex Rogozhnikov also built yandex's hep_ml library for physics ML applications.

[Original](https://arogozhnikov.github.io/2016/06/24/gradient_boosting_explained.html)
 → GitHub
