---
title: "Didact AI: The Anatomy of an ML-Powered Stock Picking Engine"
date: 2022-09-27
categories:
  - machine-learning
  - finance
  - quantitative-finance
  - stock-picking
  - ml-systems
description: A technical teardown of Didact AI's ML-powered stock picking engine — covering feature engineering, model architecture, training pipeline, and how uncertainty quantification informs position sizing. Rare public documentation of a production ML trading system.
params:
  source: pinboard
  sourceUrl: https://principiamundi.com/posts/didact-anatomy/
---

## Summary

This post on Principia Mundi is a detailed technical breakdown of Didact AI's machine learning system for stock selection. Rare in finance: most production ML trading systems are closely guarded, so a public architecture writeup provides unusual insight into what it actually takes to build one.

The system combines fundamental analysis (balance sheet data, earnings, revenue growth), technical analysis (price and volume patterns), and alternative data sources. Features are engineered at multiple time horizons — the same company might have very different signals at 1-day vs. 1-month vs. 1-year windows. The model stack uses gradient boosting and neural networks for different feature types, with an ensemble combining their predictions.

A key architectural decision: uncertainty quantification. Rather than just outputting a predicted return, the system outputs a probability distribution over outcomes. This directly informs position sizing — higher model uncertainty → smaller position. This is standard Bayesian portfolio construction, but seeing it applied to an ML stock picker is instructive. The system also includes feature importance tracking to detect when market regimes change and historical feature-return relationships break down.

## Key points

- Combines fundamental analysis, technical analysis, and alternative data as features.
- Multi-horizon feature engineering — same features computed across multiple time windows.
- Ensemble of gradient boosting and neural networks for different feature types.
- Uncertainty quantification drives position sizing — confidence → exposure.
- Feature importance monitoring for regime detection: know when your model stops working.
- Rare public documentation of a production ML-driven trading system architecture.

[Original](https://principiamundi.com/posts/didact-anatomy/)
