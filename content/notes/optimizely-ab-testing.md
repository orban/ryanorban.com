---
title: How Optimizely (Almost) Got Me Fired
date: 2014-09-29
categories:
  - ab-testing
  - statistics
  - data-science
  - experimentation
  - pitfalls
description: "SumAll's account of how Optimizely's 'optional stopping' in A/B tests produced false positives that led to bad product decisions — a landmark post in the backlash against naive A/B testing tools. The core issue: peeking at results and stopping when p<0.05 inflates false positive rates dramatically."
params:
  source: pinboard
  sourceUrl: http://blog.sumall.com/journal/optimizely-got-me-fired.html
---

## Summary

This SumAll blog post became one of the most-cited criticisms of naive A/B testing tools when it was published. The author ran experiments through Optimizely, declared winners based on the platform's significance indicators, shipped changes — and later discovered the winning variants were not actually better. The culprit: **optional stopping**, also called the peeking problem.

Standard frequentist hypothesis testing assumes you fix the sample size before running the test, collect all the data, then test once. When practitioners instead check significance continuously and stop the moment p < 0.05 is reached, they exploit the natural randomness of the sampling process — early flukes can look statistically significant even when there's no true effect. Under continuous peeking, the false positive rate can be as high as 25-30% for a test nominally run at 5% significance.

Optimizely's early interface displayed live significance statistics and encouraged stopping when significance was reached — a design that actively incentivized the peeking pattern. The fix requires either preregistering sample sizes (standard frequentist approach), using sequential testing methods designed for continuous monitoring (SPRT, always-valid confidence intervals), or using Bayesian A/B testing which handles optional stopping more naturally.

## Key points

- **Peeking problem**: checking significance continuously and stopping at p < 0.05 inflates false positive rate to 25-30%+.
- The fix: preregister sample size, or use sequential testing (SPRT) or Bayesian testing methods.
- Optimizely's early UI design actively encouraged peeking — interface design creates statistical behavior.
- Practitioners were making real product decisions based on noise, not signal.
- Led to industry-wide reconsideration of A/B testing practices; Optimizely later added better statistical controls.
- Connects to p-hacking, HARKing, and the replication crisis — the same optional stopping problem at scale.

[Original](http://blog.sumall.com/journal/optimizely-got-me-fired.html)
