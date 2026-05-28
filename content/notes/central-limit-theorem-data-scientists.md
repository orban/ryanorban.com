---
title: The Theorem Every Data Scientist Should Know
date: 2016-07-07
categories:
  - statistics
  - mathematics
  - data-science
  - education
  - probability
description: Jean-Nicholas Hould's explainer on the Central Limit Theorem as the foundational theorem every data scientist needs to internalize — why sample means approach normality, and why this underpins most of frequentist hypothesis testing and confidence intervals.
params:
  source: pinboard
  sourceUrl: http://www.jeannicholashould.com/the-theorem-every-data-scientist-should-know.html
---

![The Theorem Every Data Scientist Should Know](/images/notes/central-limit-theorem-data-scientists.png)

## Summary

Jean-Nicholas Hould argues that the Central Limit Theorem (CLT) is the single most important mathematical result for practicing data scientists — the theorem that makes most of classical hypothesis testing, confidence intervals, and A/B testing work in practice.

The CLT states that the sum (or mean) of a sufficiently large number of independent, identically distributed random variables with finite variance will be approximately normally distributed, regardless of the underlying distribution of the individual variables. This is remarkable: the distribution of the original data can be skewed, bounded, discrete, or nearly anything — and yet averages of large enough samples will follow a bell curve. The theorem has two practical consequences that data scientists use constantly: first, it's why we can use normal-distribution-based tests even when the data itself isn't normal (as long as sample sizes are adequate); second, it explains why standard errors shrink predictably with sample size.

The post is pitched at the practitioner level — connecting the theorem to concrete scenarios like testing whether two marketing campaigns have different conversion rates, or whether a new feature changes user engagement. This grounding matters because the CLT is one of those results that's easy to memorize as a fact and hard to actually internalize as a tool. Hould's companion post on the same blog is a critique of R-squared, suggesting a recurring theme: statistical tools that practitioners use routinely but often misunderstand.

## Key points

- Central Limit Theorem: sample means of large n are approximately normal regardless of the underlying distribution — the foundation of frequentist inference.
- Why it matters practically: enables t-tests, z-tests, and confidence intervals on non-normal data when n is large enough.
- Standard error = σ / √n — the CLT implies how much sample means vary, which powers all frequentist A/B testing.
- Large enough n is context-dependent: well-behaved symmetric distributions need ~30 samples; heavy-tailed or skewed distributions may need hundreds.
- Written by Jean-Nicholas Hould, same author as the companion post on why R-squared misleads.

[Original](http://www.jeannicholashould.com/the-theorem-every-data-scientist-should-know.html)
