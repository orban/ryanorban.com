---
title: sktime — Unified Machine Learning with Time Series
date: 2020-09-21
categories:
  - machine-learning
  - time-series
  - python
  - scikit-learn
  - forecasting
description: sktime is a Python library providing a unified scikit-learn-compatible interface for time series machine learning — forecasting, classification, regression, clustering, and anomaly detection. Solves the ecosystem fragmentation problem for temporal data.
params:
  source: pinboard
  sourceUrl: https://github.com/alan-turing-institute/sktime
---

## Summary

[sktime](/notes/sktime/) is an open-source Python library from the Alan Turing Institute that provides a unified, scikit-learn-compatible API for time series machine learning. The ecosystem problem it solves: time series tasks (forecasting, classification, clustering, anomaly detection) have historically required different libraries with incompatible interfaces — statsmodels for classical forecasting, tslearn for classification, custom code for everything else. sktime unifies these under a single framework.

The supported task types cover: **time series forecasting** (predicting future values), **time series classification** (labeling entire sequences — e.g., activity recognition from sensor data), **time series regression** (predicting continuous outcomes from sequences), **clustering** (grouping similar temporal patterns), **anomaly and changepoint detection**, and **transformations** (feature engineering for temporal data). Critically, the API design enables pipeline composition — you can chain transformations, ensemble forecasters, and cross-validate time series models using familiar scikit-learn patterns.

[sktime](/notes/sktime/)'s interoperability extends to existing libraries: it wraps statsmodels, pmdarima, tbats, and others, making their algorithms accessible through a consistent interface without replacing them. This is the reduction approach: applying algorithms designed for one task (e.g., tabular regression) to another (time series regression) through principled transformations.

## Key points

- Unified API design matters: switching between forecasting and classification in sktime doesn't require learning a new interface — lowering the barrier to experimenting with task types.
- Pipeline composition for time series is the key feature gap vs. raw statsmodels: train-test splits, cross-validation, and hyperparameter tuning all need temporal awareness (no future leakage).
- [sktime](/notes/sktime/) wraps existing algorithms rather than reimplementing them — practical choice that leverages existing validated implementations.
- Growing competition from Darts, NeuralForecast, and Prophet (Facebook) in the forecasting space; sktime's strength is the multi-task unified API rather than a single best-in-class algorithm.
- Developed at the Alan Turing Institute — UK's national AI research institute, which signals a research-oriented design.

[Original](https://github.com/alan-turing-institute/sktime) → GitHub
