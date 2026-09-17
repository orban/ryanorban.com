---
title: "Flipping a Coin: Bayesian Updating of Probability Distributions"
date: 2013-09-23
categories:
  - bayesian
  - probability
  - statistics
  - tutorial
  - updating
description: A walkthrough of Bayesian probability updating using coin flipping — showing how a prior distribution over coin bias is updated with each flip observation. The cleanest possible introduction to Bayesian reasoning as a process.
params:
  source: pinboard
  sourceUrl: http://java.dzone.com/articles/flipping-coin-bayesian
---

![Flipping a Coin: Bayesian Updating of Probability Distributions](/images/notes/bayesian-updating-coin-flip.png)

## Summary

The coin flip example is the canonical introduction to Bayesian updating because it's mathematically tractable and intuitively clear. You start with a prior distribution over the coin's bias (say, uniform — any bias from 0 to 1 is equally likely). You flip the coin and observe heads or tails. You update the distribution using Bayes' theorem to get a posterior distribution that's more concentrated around the true bias. Repeat with more flips — the posterior sharpens.

The Beta distribution is the natural prior for coin bias because it's conjugate to the Binomial likelihood — meaning the posterior is also a Beta distribution, just with updated parameters. This conjugacy makes the math clean: if you start with Beta(α, β), flip H heads and T tails, you end with Beta(α + H, β + T). No numerical integration required.

This article was likely a first-principles walkthrough of this exact calculation — showing the prior, the likelihood, and the posterior update in code or math. For someone at Zipfian Academy learning statistics in late 2013, this was foundational: understanding that Bayesian inference is just systematic belief updating using data is the conceptual foundation everything else builds on.

## Key points

- Bayesian updating: observe data → update prior belief via Bayes' theorem → get posterior → repeat. Belief becomes more concentrated around truth with more data.
- Beta distribution as conjugate prior for coin bias: prior Beta(α, β) + (H heads, T tails) → posterior Beta(α+H, β+T). Analytically tractable.
- The coin flip is the simplest possible case of Bayesian inference, where every concept can be computed and visualized directly.
- Conjugate priors are the key to tractable Bayesian analysis: they keep the posterior in the same distribution family as the prior.
- Saved during Zipfian Academy period — building statistical foundations alongside the applied ML curriculum.

[Original](http://java.dzone.com/articles/flipping-coin-bayesian)
