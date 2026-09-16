---
title: 10 Types of Regressions. Which One to Use?
date: 2015-05-13
categories:
  - machine-learning
  - statistics
  - regression
  - reference
  - data-science
description: A reference guide to 10 regression types and when to use each — covering linear, logistic, ridge, lasso, polynomial, and more. The kind of practical decision map that was useful before sklearn docs became as thorough as they are now.
params:
  source: pinboard
  sourceUrl: http://www.datavizualization.com/blog/10-types-of-regressions-which-one-to-use
---

## Summary

This reference maps the landscape of regression methods and their appropriate use cases — a practical decision guide. The 10 types cover the range from basic to regularized to nonlinear: linear regression, logistic regression, polynomial regression, stepwise regression, ridge regression, lasso regression, ElasticNet regression, Bayesian linear regression, quantile regression, and principal component regression.

The decision logic follows a few key axes: Is the outcome continuous or binary? That determines linear vs. logistic as the starting point. Is multicollinearity a problem? Ridge regression (L2 penalty) shrinks coefficients without zeroing them; Lasso regression (L1 penalty) produces sparse solutions by zeroing out irrelevant features. Need both effects? ElasticNet combines L1 and L2. Is the relationship nonlinear? Polynomial regression extends linear models into curved relationships at the cost of overfitting risk with high degrees.

The post reflects the data science bootcamp pedagogical moment of 2015: practitioners needed practical guidance on which tool to reach for without the full statistical theory. Scikit-learn had made all these methods available through the same `fit/predict` interface, lowering the cost of trying multiple approaches — but you still needed to know which ones to try on a given problem.

## Key points

- Continuous outcome → linear regression variants; binary/categorical → logistic regression.
- Regularization choice: ridge regression (L2) shrinks coefficients; lasso regression (L1) zeros out irrelevant ones.
- ElasticNet combines L1 + L2 — useful when ridge and lasso give conflicting guidance.
- Polynomial regression for nonlinear relationships — degree selection is a bias-variance tradeoff.
- Quantile regression when you care about conditional quantiles, not just the conditional mean.
- All available via scikit-learn's consistent API — low cost to try multiple.

[Original](http://www.datavizualization.com/blog/10-types-of-regressions-which-one-to-use)
