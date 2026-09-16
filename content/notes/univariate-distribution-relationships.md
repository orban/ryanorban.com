---
title: Univariate Distribution Relationship Chart
date: 2014-05-20
categories:
  - statistics
  - probability
  - distributions
  - reference
  - visualization
description: Lawrence Leemis's interactive chart showing the relationships between 76 univariate probability distributions — which distributions are special cases of others, how they connect via limits and parameter settings. An essential reference chart for anyone working seriously with probability distributions.
params:
  source: pinboard
  sourceUrl: http://www.math.wm.edu/~leemis/chart/UDR/UDR.html
---

## Summary

Lawrence Leemis at William & Mary created this interactive chart mapping the relationships between 76 univariate probability distributions. The connections shown are formal: when one distribution is a special case of another (e.g., the exponential distribution is a special case of the gamma distribution with shape = 1), or when a distribution is the limit of another as parameters change (e.g., binomial distribution → Poisson distribution as n → ∞ and p → 0 with np constant).

The chart is a cheat sheet for knowing where distributions fit in the larger family tree. The normal distribution occupies a central position — it's the limit of sums of independent variables (the central limit theorem), a special case of the stable distribution, and connected to chi-squared, t-distribution, and F-distribution via sums of squares. The exponential distribution anchors the family of memoryless distributions, generalizing to Weibull, gamma, and Erlang.

For practitioners, the chart is most useful when you're modeling data and trying to choose a distributional family. If you know your data is non-negative and right-skewed, the gamma/Weibull/lognormal region of the chart is where to look. If you're dealing with counts, the Poisson/negative binomial corner applies. The relationships between distributions tell you which are more general and which are constrained special cases.

## Key points

- Distinguishes three relationship types: special case (parameter restriction), limit (parameter → 0 or ∞), and transformation (function of a random variable).
- Normal distribution is the limit of most symmetric, finite-variance distributions via the central limit theorem — its centrality in the chart reflects this.
- Exponential distribution is memoryless (the Markov property for continuous time) — making it the basis of queueing theory and Poisson processes.
- Beta distribution is the conjugate prior for Bernoulli/binomial in Bayesian inference — its position in the chart clarifies why.
- Interactive: clicking a distribution shows its PDF, CDF, moments, and relationships — more useful than a static poster.

[Original](http://www.math.wm.edu/~leemis/chart/UDR/UDR.html)
