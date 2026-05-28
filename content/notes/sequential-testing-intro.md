---
title: The Importance of Sequential Testing
date: 2014-01-02
categories:
  - statistics
  - experimentation
  - sequential-testing
  - bayesian
  - a-b-testing
description: Austin Rochford's introduction to sequential testing — the SPRT and Bayesian alternatives to fixed-horizon A/B tests that let you stop early when results are clear without inflating false positive rates.
params:
  source: pinboard
  sourceUrl: http://www.austinrochford.com/posts/2014-01-01-intro-to-sequential-testing.html
---

## Summary

Austin Rochford introduces sequential testing as an alternative to fixed-horizon A/B testing. The core problem: when you peek at A/B test results before the planned sample size and stop early if something looks significant, you inflate your false positive rate. The intuitive fix — just wait until the end — is rarely followed in practice because there's always business pressure to act on early results.

Sequential testing methods like Wald's SPRT (Sequential Probability Ratio Test) are designed to support early stopping with valid error control. The Bayesian approach goes further: instead of binary reject/fail-to-reject decisions, you track posterior probability that a treatment is better than control, and stop when you're confident enough by whatever criterion you set.

## Key points

- Peeking at A/B test p-values before the planned sample size inflates the false positive rate — this is the peeking problem that sequential testing addresses
- Wald's SPRT is the classical sequential test: define error bounds α and β, and compute a likelihood ratio after each observation — stop when it crosses a threshold
- Bayesian sequential testing tracks the posterior directly: P(treatment > control | data), which is always interpretable and doesn't require a fixed stopping rule
- Sequential methods allow optional stopping without validity loss — valuable when early results are extremely strong (either clearly good or clearly harmful)
- Connects to the multi-armed bandit literature: bandits solve a related problem (adaptive allocation, not just valid testing) and the two traditions increasingly inform each other

[Original](http://www.austinrochford.com/posts/2014-01-01-intro-to-sequential-testing.html)
