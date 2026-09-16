---
title: Law of Large Numbers and Central Limit Theorem
date: 2014-06-29
categories:
  - statistics
  - probability
  - central-limit-theorem
  - law-of-large-numbers
description: Bugra Akyildiz's notes on the law of large numbers and the central limit theorem with Python demonstrations — two of the most important foundational theorems in statistics that together explain why averages are well-behaved and why the normal distribution appears everywhere.
params:
  source: pinboard
  sourceUrl: http://bugra.github.io/work/notes/2014-06-26/law-of-large-numbers-central-limit-theorem/
---

## Summary

The law of large numbers and central limit theorem are two of the most foundational results in probability theory, and this post by Bugra Akyildiz covers both with Python simulations that make the convergence behavior concrete. The two theorems are related but distinct: the law of large numbers tells you that sample averages converge to the true mean as n → ∞; the central limit theorem tells you the shape of the distribution of those averages.

The law of large numbers comes in two forms: the weak version says the sample mean converges in probability; the strong version says it converges almost surely. Practically, both mean the same thing: flip a coin enough times and the empirical frequency of heads will get arbitrarily close to 0.5. This is why Monte Carlo simulations work — you can estimate intractable expectations by averaging samples.

The central limit theorem (CLT) is more surprising: regardless of the underlying distribution's shape, the distribution of sample means approaches a normal distribution as sample size grows. This is why the normal distribution appears so often in statistics — many real-world measurements are sums or averages of independent contributions, and the CLT applies. It also justifies z-tests and t-tests for hypothesis testing, as long as sample sizes are large enough.

## Key points

- Law of large numbers: sample averages converge to the population mean — the mechanism that makes Monte Carlo simulation and survey sampling reliable.
- Central limit theorem: distribution of sample means approaches normal distribution regardless of the underlying data distribution — explains why normal is so ubiquitous.
- The CLT requires independence and finite variance — correlated data or heavy-tailed distributions can violate both conditions.
- Both theorems underpin A/B testing, confidence intervals, and hypothesis testing via z-tests and t-tests.
- Python simulations (averaging dice rolls, coin flips) make the convergence rate visible — important for intuition about how fast CLT kicks in.

[Original](http://bugra.github.io/work/notes/2014-06-26/law-of-large-numbers-central-limit-theorem/) → GitHub
