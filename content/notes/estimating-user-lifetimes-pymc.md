---
title: Estimating User Lifetimes with PyMC
date: 2013-08-22
categories:
  - bayesian-inference
  - pymc
  - survival-analysis
  - python
  - customer-analytics
description: yhat's tutorial on estimating customer lifetimes with PyMC using Bayesian survival analysis — fitting probabilistic churn models to get full posterior distributions over lifetime value rather than point estimates. An early example of applied Bayesian modeling in Python before PyMC3 existed.
params:
  source: pinboard
  sourceUrl: http://blog.yhathq.com/posts/estimating-user-lifetimes-with-pymc.html
---

## Summary

This post from yhat (a Python model deployment startup) used PyMC to fit survival models to user behavior data and estimate expected customer lifetimes. Rather than point estimates for churn probability, the Bayesian approach models full posterior distributions over churn rates — giving uncertainty quantification that's useful when making decisions like how much to spend on customer acquisition.

The technique combined Bayesian inference with survival analysis: define a generative model for how customers churn over time (parameterized by a Beta distribution over per-period churn rates), observe the actual data, and use MCMC to draw samples from the posterior. The BG/NBD model (Beta Geometric / Negative Binomial Distribution) was the standard for non-contractual settings — customers who can churn at any time without notice.

yhat was building toward a Python model deployment workflow (deploy scikit-learn and PyMC models as REST APIs), and this survival modeling post was a practical use case: train offline, score in production. The post was part of a wave of Bayesian practitioner writing in 2013 that helped establish PyMC as a serious tool alongside R's `BTYD` and `MCMCpack` packages.

## Key points

- PyMC probabilistic programming: define a generative model, condition on data, draw posterior samples via MCMC — no closed-form math required.
- Survival analysis for user lifetime: model time-to-churn with a parametric distribution (exponential, Weibull, gamma) and fit parameters from observed data.
- BG/NBD model: the standard Bayesian approach for non-contractual customer lifetime value — models both purchase frequency and dropout probability jointly.
- Uncertainty quantification: the Bayesian approach returns distributions over lifetime value — useful for decisions where the variance matters, not just the mean.
- yhat deployment angle: the gap between training a model and serving it in production was a key pain point in 2013 that yhat was addressing.
- Predates PyMC3 — the original PyMC syntax was less ergonomic, but the same Bayesian concepts apply in modern versions.

[Original](http://blog.yhathq.com/posts/estimating-user-lifetimes-with-pymc.html) → REST API
