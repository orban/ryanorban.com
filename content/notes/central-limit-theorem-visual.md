---
title: The Central Limit Theorem — Visual Explanation
date: 2013-06-03
categories:
  - statistics
  - visualization
  - education
  - probability
description: Victor Powell's interactive visualization of the Central Limit Theorem, showing how sample means converge to a normal distribution regardless of the underlying population distribution. A beautiful interactive demonstration that makes the theorem's implications visceral rather than abstract.
params:
  source: pinboard
  sourceUrl: http://blog.vctr.me/posts/central-limit-theorem.html
---

## Summary

Victor Powell's interactive visualization demonstrates the Central Limit Theorem (CLT) by letting users draw samples from various non-normal distributions — uniform, bimodal, exponential — and observe how the distribution of sample means converges to a normal distribution as sample size increases. The result is visceral in a way that no equation or proof can quite match: you see the normal distribution emerge from fundamentally non-normal data.

The CLT states that the mean of n independent samples from *any* distribution with finite variance converges to a Gaussian distribution as n → ∞, regardless of the original distribution's shape. This is why so many things in nature and statistics approximate normal distributions: they're aggregates of many independent factors. It also underlies why the standard error of the mean shrinks as √n — another thing the visualization makes intuitive.

This kind of interactive statistical visualization was a hallmark of the early D3.js era (2012–2015). Before these tools, statistical concepts required either textbook derivations or special-purpose software. Victor Powell and Lewis Lehe made a series of these visualizations that set a high bar for explaining mathematical concepts without dumbing them down.

## Key points

- CLT: sample means from any distribution with finite variance → normal distribution as n → ∞
- Rate of convergence depends on the original distribution's skewness; uniform converges fast, heavy-tailed converges slowly
- Standard error of the mean = population σ / √n — visualization makes the √n relationship tangible
- Why it matters: justifies using normal-distribution-based tests (t-test, ANOVA) on non-normal populations when samples are large enough
- D3.js interactive visualizations as a teaching medium — this was among the best examples of the form
- Companion visualizations by Powell include Markov chains, conditional probability, and confidence intervals

[Original](http://blog.vctr.me/posts/central-limit-theorem.html)
