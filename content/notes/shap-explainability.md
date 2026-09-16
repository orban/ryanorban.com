---
title: "SHAP: SHapley Additive exPlanations"
date: 2021-02-24
categories:
  - machine-learning
  - explainability
  - python
  - interpretability
  - open-source
description: SHAP (SHapley Additive exPlanations) is the standard Python library for explaining individual predictions from any ML model using game-theoretic Shapley values. It works across tree models, deep neural networks, and linear models, and produces both local and global interpretability.
params:
  source: pinboard
  sourceUrl: https://github.com/slundberg/shap
---

## Summary

SHAP (SHapley Additive exPlanations) by Scott Lundberg applies game theory to machine learning interpretability. The core idea: for any prediction, distribute the contribution of each feature according to the Shapley value — the average marginal contribution of that feature across all possible orderings of features. Unlike earlier approaches like LIME (which is model-agnostic but samples locally), SHAP provides provably consistent, locally accurate, and globally comparable attribution.

The library includes optimized implementations for different model types: TreeSHAP for tree ensembles like XGBoost, LightGBM, and scikit-learn's random forests (exact computation, polynomial time); DeepSHAP for neural networks (approximate, using backpropagation); LinearSHAP for linear models; and KernelSHAP as a model-agnostic fallback. The speed of TreeSHAP in particular made SHAP practical for production — computing exact Shapley values for tree models takes milliseconds per prediction.

The visualization suite (summary plots, waterfall plots, dependence plots, force plots) made SHAP the default choice for explainable AI in applied ML. Summary plots show feature importance globally (like traditional feature importance, but directional); force plots show how each feature pushed a specific prediction higher or lower. It's now common practice to run SHAP on any model being deployed to production, especially in regulated domains like finance and healthcare.

## Key points

- Shapley values provide theoretically grounded, consistent attribution — unlike permutation importance or gain-based importance which can be misleading.
- TreeSHAP is exact and fast for tree ensembles (XGBoost, LightGBM, Random Forest) — the main reason SHAP became the standard.
- Works with any model via KernelSHAP, though this is much slower than model-specific implementations.
- Enables both local interpretability (why did this prediction come out this way?) and global understanding (which features matter overall?).
- Companion to ELI5 and Yellowbrick in the explainability ecosystem; SHAP is more theoretically rigorous.

[Original](https://github.com/slundberg/shap) → GitHub
