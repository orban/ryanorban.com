---
title: Outlier Detection via Markov Chain Monte Carlo
date: 2014-04-27
categories:
  - machine-learning
  - bayesian
  - mcmc
  - outlier-detection
  - pymc
description: Bugra Akyildiz's walkthrough of outlier detection using Markov Chain Monte Carlo via PyMC — fitting a Bayesian mixture model to separate inliers from outliers using posterior inference. A more principled alternative to distance-based outlier methods.
params:
  source: pinboard
  sourceUrl: http://bugra.github.io/work/notes/2014-04-26/outlier-detection-markov-chain-monte-carlo-via-pymc/
---

## Summary

Most outlier detection methods are heuristic: flag points that are far from the mean, or use distance-based rules like isolation forest or LOF. Bayesian inference offers a more principled alternative: model the data-generating process explicitly, including a component for outliers, and let MCMC posterior inference tell you which points are most likely anomalous.

Bugra Akyildiz's post implements this in PyMC, the Python probabilistic programming library. The approach models the dataset as a mixture: most observations come from a "normal" distribution, while a fraction come from a more diffuse outlier distribution. MCMC then samples from the posterior over which component each point belongs to — giving you a probability of being an outlier for each observation rather than a hard label.

This Markov Chain Monte Carlo approach has real advantages: it quantifies uncertainty (you get a distribution over outlier probabilities, not just a flag), it incorporates prior knowledge naturally, and it handles small datasets gracefully where heuristic methods are unreliable. The main cost is computation — MCMC is much slower than distance-based methods, which matters when data is large.

## Key points

- MCMC-based outlier detection fits a Bayesian mixture model with an explicit outlier component.
- PyMC handles the sampling — MCMC posterior gives probability of being an outlier per point.
- More principled than heuristic methods: handles uncertainty, works well with small samples.
- Computationally expensive vs. isolation forest or LOF — better for analysis than production scoring.
- Related to Bayesian inference and probabilistic programming — same ideas as PyMC3 examples.

[Original](http://bugra.github.io/work/notes/2014-04-26/outlier-detection-markov-chain-monte-carlo-via-pymc/) → GitHub
