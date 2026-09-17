---
title: "Bayesian Regression with PyMC: A Brief Tutorial"
date: 2014-05-31
categories:
  - bayesian
  - statistics
  - python
  - pymc
  - regression
  - zipfian-academy
description: A Zipfian Academy student's tutorial on Bayesian linear regression using PyMC — notable both as an accessible introduction to probabilistic modeling and as a window into the Zipfian cohort's learning culture of public writing. PyMC was the dominant Python tool for Bayesian modeling at the time.
params:
  source: pinboard
  sourceUrl: http://sabermetricinsights.blogspot.com/2014/05/bayesian-linear-regression-with-pymc.html
---

## Summary

This tutorial from a Zipfian Academy student covers Bayesian linear regression using PyMC — the Python library for probabilistic programming. The post is part of the broader Zipfian Academy tradition of students writing publicly about what they're learning, which doubles as teaching material and as a record of where practitioners were in 2014.

Bayesian linear regression differs from ordinary least squares regression in its treatment of parameters: rather than finding point estimates (the single "best" slope and intercept), it computes a posterior distribution over all plausible parameter values. You specify a prior distribution encoding your beliefs before seeing data, observe the data (the likelihood), and update to a posterior distribution via Bayes' theorem.

PyMC (later PyMC3, now PyMC v4) implements this using Markov Chain Monte Carlo sampling — specifically No-U-Turn Sampler (NUTS), a variant of Hamiltonian Monte Carlo that automatically tunes step sizes. The result is a full posterior over the regression parameters, enabling credible intervals rather than confidence intervals and explicit propagation of uncertainty through predictions.

## Key points

- Bayesian inference requires specifying prior distributions — uninformative priors (flat, weakly regularizing) are typical for regression when domain knowledge is absent.
- MCMC sampling explores the posterior distribution by simulating a Markov chain — convergence checks (Gelman-Rubin statistic, trace plots) are essential before trusting results.
- PyMC syntax mirrors the generative model: define priors → define likelihood → call `pm.sample()` → inspect posterior.
- The output is samples from the posterior, not point estimates — uncertainty is first-class and propagates naturally through derived quantities.
- Bayesian regression shines for small datasets where frequentist confidence intervals would be unstable, and for incorporating prior knowledge from domain experts.

[Original](http://sabermetricinsights.blogspot.com/2014/05/bayesian-linear-regression-with-pymc.html)
