---
title: Interpreting Random Forests
date: 2014-12-23
categories:
  - machine-learning
  - random-forests
  - interpretability
  - feature-importance
description: A deep dive into techniques for interpreting random forest models — going beyond accuracy to understand what the model has learned. Particularly useful because random forests were the dominant ensemble method before gradient boosting took over, and interpretability was the main complaint against them.
params:
  source: pinboard
  sourceUrl: http://blog.datadive.net/interpreting-random-forests/
---

## Summary

Random forests are accurate but famously opaque — you get a prediction but not a clear explanation of why. The datadive.net blog post addresses this by walking through the techniques available at the time (2014) for extracting insight from trained random forest models. This was a live research concern: random forests were the workhorse ensemble method of early-2010s machine learning, and the interpretability gap versus simpler models like logistic regression was a genuine obstacle to deployment in regulated industries.

The main interpretability lever is feature importance, which random forests expose natively. Each tree in the ensemble tracks how much each feature reduces impurity (gini or entropy) at splits that use it. Averaging across all trees gives a global importance ranking. The post likely covers this along with partial dependence plots, which show the marginal effect of a single feature after averaging out all others.

A key subtlety: feature importance in random forests can be misleading when features are correlated. If two features carry similar signal, the importance gets split between them arbitrarily — neither appears strongly important even though the combined signal is high. This is one reason why permutation importance (shuffling a feature and measuring accuracy drop) became preferred over the default Gini-based importance.

## Key points

- Random forest feature importance = average reduction in impurity (Gini/entropy) per feature across all trees.
- Correlated features dilute each other's importance scores — a known failure mode of tree-based importance.
- Permutation importance is more reliable: shuffle a feature's values and measure the accuracy drop.
- Partial dependence plots show the marginal effect of one feature while averaging out the rest.
- Interpretability was the central criticism of random forests vs. simpler models in production settings.
- Predates SHAP values (2017), which became the standard approach to tree model interpretability.

[Original](http://blog.datadive.net/interpreting-random-forests/)
