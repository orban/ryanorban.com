---
title: "Probable Points and Credible Intervals: Bayesian Decision Theory"
date: 2015-01-09
categories:
  - bayesian-statistics
  - decision-theory
  - statistics
  - probability
  - tutorial
description: Part 2 of Rasmus Baath's gentle intro to Bayesian decision theory — covering how credible intervals and probable points are used to make decisions under uncertainty. One of the cleaner elementary treatments of the Bayesian decision framework.
params:
  source: pinboard
  sourceUrl: http://www.sumsar.net/blog/2015/01/probable-points-and-credible-intervals-part-two/
---

## Summary

This post by Rasmus Baath (Part 2 of his "Probable Points and Credible Intervals" series) introduces [Bayesian decision theory](/notes/bayesian-decision-theory/) — the framework for making decisions when you have a posterior distribution over states of the world rather than a single point estimate. It's the natural continuation from Bayesian inference: once you have a posterior, how do you actually use it to make a decision?

The core idea: different loss functions lead to different optimal decision rules. If you want to minimize squared error loss, the optimal estimate is the **posterior mean**. If you want to minimize absolute error loss, it's the **posterior median**. If you care about the single most probable value, it's the **posterior mode** (MAP estimate). The choice of loss function encodes your preferences about what kinds of errors are costly, and the posterior gives you everything you need to minimize expected loss under any loss function.

Credible intervals are the Bayesian analog of confidence intervals — they represent the range of values for the parameter that the posterior assigns high probability to. A 95% credible interval genuinely means "there's a 95% probability the parameter is in this range" (under the posterior), unlike the frequentist confidence interval whose correct interpretation is more convoluted. For decision-making, they quantify where the parameter plausibly lies.

## Key points

- Different loss functions → different optimal point estimates: squared error → posterior mean; absolute error → posterior median.
- Credible intervals = ranges with direct probability interpretation under the posterior.
- Bayesian decision theory = minimize expected loss under the posterior distribution.
- By Rasmus Baath, whose blog is a good practical Bayesian statistics resource.
- Contrast with frequentist hypothesis testing: Bayesian framework directly answers what should I do? under uncertainty.
- Connects to value of information calculations and sequential decision-making.

[Original](http://www.sumsar.net/blog/2015/01/probable-points-and-credible-intervals-part-two/)
