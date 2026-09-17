---
title: "benchm-ml: ML Algorithm Benchmark Comparison"
date: 2015-08-12
categories:
  - machine-learning
  - benchmarking
  - performance
  - xgboost
  - python
  - r
description: A systematic benchmark of machine learning algorithms across platforms and implementations — comparing gradient boosting, random forests, neural networks, and others on speed and accuracy. One of the best empirical references for choosing between ML tools in 2015, when the xgboost vs sklearn debate was live.
params:
  source: pinboard
  sourceUrl: https://github.com/szilard/benchm-ml
---

## Summary

*benchm-ml* by Szilard Pafka is a systematic empirical comparison of machine learning algorithms across tools and platforms. The benchmark runs gradient boosting, random forest, neural networks, logistic regression, and others on standard classification tasks, measuring both prediction accuracy and training time. The goal: answer the practical question of which tool to actually use, not which one is theoretically optimal.

The benchmark was particularly timely in 2015 when XGBoost was emerging as a dominant tool. Szilard's results consistently showed XGBoost outperforming other implementations on speed and accuracy — the benchmark helped validate what Kaggle competitors already knew empirically, contributing to XGBoost becoming the default choice for tabular data competitions and production models alike.

The comparison also covers R vs Python implementations, H2O, Spark MLlib, and GPU-accelerated training. A recurring finding: naive scikit-learn implementations are slower than specialized libraries by an order of magnitude for large datasets, which matters enormously when iterating on models.

## Key points

- Compares gradient boosting (XGBoost, H2O), random forest, deep nets, and others on speed + accuracy.
- XGBoost consistently outperformed in 2015 — the benchmark was empirical validation for what Kaggle practitioners already observed.
- scikit-learn implementations often 10x+ slower than specialized libraries at scale.
- Covers R, Python, H2O, Spark MLlib — useful cross-language comparison.
- By Szilard Pafka; regularly updated as new tools emerged (LightGBM, CatBoost arrived later).
- Methodology: fixed binary classification task, varying sample sizes from 10K to 10M rows.

[Original](https://github.com/szilard/benchm-ml) → GitHub
