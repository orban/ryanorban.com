---
title: Random Forest — MLU-Explain
date: 2022-08-03
categories:
  - machine-learning
  - random-forest
  - visualization
  - education
  - ensemble-methods
description: MLU-Explain's visual, interactive introduction to the Random Forest algorithm — animated trees, bootstrap sampling, and feature importance built into the browser. Part of Amazon's ML University series of interactive learning tools.
params:
  source: pinboard
  sourceUrl: https://mlu-explain.github.io/random-forest/
---

## Summary

MLU-Explain is Amazon's series of interactive, browser-based visual explainers for machine learning concepts, and the Random Forest entry is one of its strongest. The visualization builds the algorithm from first principles: starting from a single decision tree showing how splits work, then illustrating bootstrap aggregation (bagging) to show how multiple trees are trained on random samples of the data, and finally showing how predictions from many trees are combined into a final prediction via majority vote.

Random Forest sits at the foundation of practical ML: it's ensemble learning's most accessible entry point, handles both classification and regression, has relatively few hyperparameters to tune, and naturally provides feature importance scores. Before gradient boosting methods (XGBoost, LightGBM) dominated Kaggle, Random Forest was often the first serious baseline people reached for. Even today it's a good starting point when interpretability matters and you need feature importance without black-box neural network complexity.

The MLU-Explain format — interactive and animated rather than static diagrams — is well-suited to this algorithm because the intuition for why averaging trees reduces variance is hard to convey in text alone. Seeing 50 noisy individual trees converge toward a stable prediction as you watch them vote is the kind of conceptual moment that static diagrams can't replicate.

## Key points

- Random Forest = bagging (bootstrap sampling) + decision trees trained on random feature subsets
- Reduces variance compared to a single tree by averaging predictions from diverse trees
- Naturally provides feature importance via mean decrease in impurity across all trees
- The visualization animates bootstrap sampling, tree construction, and majority voting
- Part of [MLU-Explain](/notes/mlu-explain/) — Amazon's open-source visual ML education series
- Contrast with gradient boosting: RF trains trees in parallel (independent), boosting trains sequentially (correcting errors)

[Original](https://mlu-explain.github.io/random-forest/) → GitHub
