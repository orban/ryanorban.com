---
title: Bayesian Methods for Hackers
date: 2013-06-06
categories:
  - bayesian
  - probabilistic-programming
  - python
  - education
  - statistics
description: Cameron Davidson-Pilon's open-source book teaching Bayesian inference through computational examples in Python, using PyMC3 for probabilistic programming. The approach is computation-first rather than math-first — ideal for programmers who want to apply Bayesian reasoning without heavy statistics background.
params:
  source: pinboard
  sourceUrl: https://github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers
---

## Summary

Cameron Davidson-Pilon's *Probabilistic Programming and Bayesian Methods for Hackers* is an open-source Jupyter notebook-based book that teaches Bayesian inference computationally rather than mathematically. The central premise: most programmers can intuit Bayesian reasoning (update beliefs given evidence) but get stuck on the math. By starting with PyMC3 (a Python probabilistic programming library) and building intuition from code and visualizations, the book sidesteps the derivation-heavy approach of classical Bayesian textbooks.

The book covers the core ideas — prior distributions, likelihoods, Markov Chain Monte Carlo (MCMC) sampling, posterior inference — but frames them as algorithms a programmer can run and inspect rather than integrals a mathematician must solve analytically. This makes it a natural complement to frequentist statistics exposure: many programmers have seen p-values and confidence intervals but have never been able to reason about uncertainty in a principled way.

Bayesian methods became increasingly relevant in data science as problems grew more complex. Where A/B testing with frequentist statistics requires fixed sample sizes and rigid test designs, Bayesian approaches allow updating beliefs continuously as data arrives — a better fit for real product decisions.

## Key points

- Computation-first: uses PyMC3 to express probabilistic models as code, letting MCMC handle the inference
- Covers Poisson processes, change point detection, A/B testing, loss functions, and hierarchical models
- Free and open-source on GitHub, implemented as Jupyter notebooks — runnable, inspectable examples
- Markov Chain Monte Carlo makes Bayesian inference tractable for models where the posterior has no closed form
- The book's value is bridging the gap between statistical theory and working code, not depth on any single topic
- A companion to Think Bayes (Downey) and Statistical Rethinking (McElreath) — less rigorous but more immediately practical

[Original](https://github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers)
