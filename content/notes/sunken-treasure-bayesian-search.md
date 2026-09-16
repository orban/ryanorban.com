---
title: How Data Nerds Found a 131-Year-Old Sunken Treasure
date: 2015-05-13
categories:
  - bayesian-statistics
  - search-theory
  - data-journalism
  - fivethirtyeight
  - history
description: FiveThirtyEight on locating the SS Republic shipwreck using Bayesian search theory — the same framework used to find Air France 447 and guide military submarine searches. A clear demonstration that search is a statistics problem as much as a logistics one.
params:
  source: pinboard
  sourceUrl: http://fivethirtyeight.com/features/how-data-nerds-found-a-131-year-old-sunken-treasure/
---

## Summary

This FiveThirtyEight piece tells the story of locating the SS Republic — a Civil War-era steamship that sank in 1865 with gold and silver coins — using Bayesian search theory. The same mathematical framework was used to find Air France Flight 447 (after two years of searching) and has guided military submarine searches since the Cold War. The core insight is that search is a statistics problem: you don't search randomly, you search the highest-probability location first and update your beliefs with each failure.

Bayesian search theory works by maintaining a probability distribution over where the target could be. The prior comes from everything you know before searching: historical records of where the ship was last sighted, oceanographic drift models, eyewitness accounts, bathymetric charts. The likelihood function models the probability of detecting the target given it's in a particular cell — accounting for sonar coverage, depth, and visibility conditions. Multiplying prior by likelihood and normalizing gives the posterior; you always search the highest-posterior-probability cell.

The crucial insight is that failed searches are informative. When you search a cell and find nothing, Bayes' theorem redistributes that probability mass to the remaining unsearched cells. Over time, the distribution concentrates on where the target must be. This is sequential Bayesian updating applied to a physical search problem — and it works dramatically better than systematic grid search when prior information is available.

## Key points

- Bayesian search theory: maintain a probability distribution over target location; search highest-probability cell; update on failure.
- Prior = historical records + drift models. Likelihood = detection probability given location.
- Failed searches are *informative* — they shift probability mass, not just coverage.
- Same framework as Air France Flight 447 recovery and Cold War submarine searches.
- Civil War-era gold coins: historical records gave strong geographic priors.
- Demonstrates the general principle: any search problem with prior information benefits from probabilistic rather than exhaustive methods.

[Original](http://fivethirtyeight.com/features/how-data-nerds-found-a-131-year-old-sunken-treasure/)
