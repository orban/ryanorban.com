---
title: Stochastic Volatility Modeling with PyMC
date: 2014-01-08
categories:
  - bayesian-inference
  - pymc
  - financial-modeling
  - stochastic-processes
  - probabilistic-programming
description: PyMC example notebook demonstrating stochastic volatility modeling — Bayesian inference for time-varying financial volatility using NUTS sampling. A showcase of what probabilistic programming makes tractable.
params:
  source: pinboard
  sourceUrl: http://nbviewer.ipython.org/github/pymc-devs/pymc/blob/master/pymc/examples/stochastic_volatility.ipynb
---

## Summary

This PyMC example notebook demonstrates stochastic volatility modeling — a Bayesian inference approach to modeling time-varying variance in financial time series. Standard financial models (like Black-Scholes) assume constant volatility, but real markets have volatility clustering: calm periods and turbulent periods that persist in clusters. Stochastic volatility models treat volatility itself as a latent random process that evolves over time.

The notebook shows how probabilistic programming with PyMC makes this tractable: define the generative model (returns driven by time-varying log-volatility following a random walk), then run MCMC sampling — specifically NUTS (No-U-Turn Sampler) — to infer the posterior over the volatility path. Without PyMC, this would require implementing custom samplers; with it, it's ~20 lines of model code.

## Key points

- Stochastic volatility captures volatility clustering in financial returns — the empirical observation that large price moves tend to follow large moves
- The model structure: log-returns follow a normal distribution with time-varying standard deviation; the log-volatility itself follows a random walk (autoregressive process)
- PyMC's NUTS sampler handles the high-dimensional posterior efficiently — each time step has a latent volatility variable, making this a high-dimensional inference problem
- Probabilistic programming advantage: the same model code works for both simulation and inference — the likelihood and prior are specified once
- This notebook was a canonical example of Cameron Davidson-Pilon's approach: real-world problems made approachable through Bayesian modeling tools

[Original](http://nbviewer.ipython.org/github/pymc-devs/pymc/blob/master/pymc/examples/stochastic_volatility.ipynb) → GitHub
