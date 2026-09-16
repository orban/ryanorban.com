---
title: German Tank Problem
date: 2014-02-22
categories:
  - statistics
  - bayesian
  - estimation
  - history
  - probability
description: "The German tank problem: WWII Allies estimated German tank production by applying statistical estimation to captured tank serial numbers. A compelling historical case study in the power of statistical inference over conventional intelligence methods."
params:
  source: pinboard
  sourceUrl: http://en.wikipedia.org/wiki/German_tank_problem
---

## Summary

During WWII, Allied statisticians estimated German tank production rates using serial numbers from destroyed or captured tanks — and their estimates turned out to be far more accurate than conventional intelligence methods (spy reports, intercepted communications). The problem is now a classic in statistical estimation: given a sample of serial numbers drawn uniformly at random from {1, 2, ..., N}, estimate N.

The maximum likelihood estimator (MLE) is simply the maximum observed serial number: N_hat = m (where m is the largest observed serial number). This is intuitive but biased downward — you'll never observe a number above N, so m underestimates N. The minimum variance unbiased estimator (MVUE) corrects for this: N_hat = m + m/k - 1, where k is the number of tanks sampled. This turns out to be optimal — no other unbiased estimator has lower variance.

The Bayesian approach treats N as a random variable with a prior distribution (often Pareto or uniform over some range), then updates it given the observations. For a uniform prior on {m, m+1, ..., ∞}, the posterior mean is 2m - k, close to the MVUE. The historical validation is striking: the statistical estimate for mid-1940 German tank production was 169 per month; post-war German records showed 122. Conventional intelligence had estimated 1,400.

## Key points

- The MVUE for the German tank problem: `N_hat = m * (k+1)/k - 1` where m is the max serial number and k is sample size.
- Maximum likelihood estimator (MLE = m) is biased downward; the MVUE corrects the bias by accounting for sample size.
- Bayesian inference approach: place a prior on N, update with observations — posterior mean close to MVUE for reasonable priors.
- Historical validation: statistical estimate (169/month) vs conventional intelligence (1,400/month) vs ground truth (122/month) — statistics wins decisively.
- Applications beyond tanks: estimating software version numbers, population sizes, the number of competitors in a market.

[Original](http://en.wikipedia.org/wiki/German_tank_problem)
