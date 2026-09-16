---
title: Statistics Revisited
date: 2020-11-11
categories:
  - statistics
  - data-science
  - fundamentals
  - inferential-statistics
  - education
description: A beginner-friendly revisit of descriptive and inferential statistics for data scientists — covering the Central Limit Theorem, confidence intervals, z-scores, and t-distributions with accessible explanations. Good refresher on the probabilistic foundations underlying most ML evaluation.
params:
  source: pinboard
  sourceUrl: https://towardsdatascience.com/statistics-revisited-5541f0bb9c4b
---

## Summary

Alvin Mak's Towards Data Science post covers the foundations of statistics that data scientists regularly use but sometimes understand only instrumentally. The organizing question is: "To what confidence can I trust that sample results speak the truth about the population?" — which frames both descriptive and inferential statistics as answers to the same underlying problem of uncertainty quantification.

The descriptive statistics half covers mean, median, mode, quartiles, variance, and standard deviation — the tools for characterizing a dataset you already have. The inferential statistics half is where things get more interesting: the Central Limit Theorem (why sample means tend toward a normal distribution regardless of the underlying distribution), standard error, confidence intervals (ranges, not point estimates), and when to use z-distributions vs t-distributions (the distinction being sample size and whether population variance is known).

The central takeaway: statistics gives you ranges and probabilities, not certainties. A 95% confidence interval doesn't mean 95% chance the true value is in that range — it means 95% of intervals constructed this way will contain the true value. This distinction matters in practice.

## Key points

- Descriptive statistics describe what's in your data; inferential statistics make claims about populations from samples — the latter involves irreducible uncertainty.
- Central Limit Theorem: sample means approach a normal distribution as n increases, regardless of underlying distribution — the foundation for most parametric testing.
- Standard error measures uncertainty in your sample estimate, not variability in the data itself — smaller with larger samples.
- T-distribution vs z-distribution: use t when sample is small or population variance is unknown (heavier tails account for extra uncertainty).
- Confidence intervals are a property of the procedure, not the specific interval — a subtle but important conceptual point that most practitioners get wrong.

[Original](https://towardsdatascience.com/statistics-revisited-5541f0bb9c4b)
