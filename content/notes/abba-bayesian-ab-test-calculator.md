---
title: A/B Test Calculator — ABBA (Thumbtack)
date: 2014-02-20
categories:
  - a-b-testing
  - bayesian
  - statistics
  - experimentation
  - tools
description: Thumbtack's ABBA (A/B Analysis) tool — a Bayesian A/B test calculator that reports the probability one variant beats another, rather than traditional p-values. Practically more useful than frequentist tests for the decisions product teams actually make.
params:
  source: pinboard
  sourceUrl: http://www.thumbtack.com/labs/abba/
---

## Summary

Thumbtack's ABBA (A/B Analysis) tool was part of a small wave of Bayesian experimentation tools in 2013-2014 that pushed back against the standard frequentist approach to A/B testing. The core problem with the classic frequentist test: a p-value answers "if there were no effect, what is the probability of observing data at least this extreme?" — which is not the question a product manager wants answered. They want "given the data I have, what's the probability that variant B is better than variant A?"

ABBA answers the latter question directly using Bayesian inference. Given conversion counts for control and variant, it computes the posterior distribution over the conversion rate for each variant (using a Beta distribution with a flat prior), then uses Monte Carlo sampling to estimate P(variant B > variant A). The output is an interpretable probability — "there's an 87% chance the new button color outperforms the original" — rather than a p-value with all its associated misinterpretation risks.

The tool is notable for being built by a consumer marketplace (Thumbtack) and released as an open tool for the community — part of the 2014 tech company trend of sharing internal tooling. The Bayesian approach here complements the multi-armed bandit alternatives being developed simultaneously (like Thompson Sampling): bandits adapt during an experiment, while Bayesian tests give a cleaner framework for interpreting fixed-allocation experiments.

## Key points

- ABBA computes P(B beats A) directly via Bayesian inference — the answer product teams actually want, not a p-value they have to interpret indirectly.
- Uses Beta distribution as the prior/posterior over conversion rates — conjugate prior for binomial data, analytically tractable.
- Monte Carlo estimation: sample from both posteriors many times, count how often B sample > A sample — P(B > A) estimate is the fraction.
- Contrast with frequentist statistics A/B testing: chi-square test or z-test gives p-value (probability of data given no effect), not probability of effect given data.
- Built by Thumbtack and open-sourced — a pattern of tech companies productizing their internal statistical tooling.

[Original](http://www.thumbtack.com/labs/abba/)
