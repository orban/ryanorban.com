---
title: Multi-Armed Bandits
date: 2014-01-27
categories:
  - bandits
  - bayesian
  - machine-learning
  - probability
  - statistics
description: Cameron Davidson-Pilon's blog post on multi-armed bandits from a Bayesian perspective — draws on the same probabilistic programming intuition as his 'Bayesian Methods for Hackers' book. Frames bandits as the natural application of iterative belief updating.
params:
  source: pinboard
  sourceUrl: http://camdp.com/blogs/multi-armed-bandits
---

## Summary

Cameron Davidson-Pilon — author of "Probabilistic Programming and Bayesian Methods for Hackers" — covers multi-armed bandits from a Bayesian angle. The framing matches his broader pedagogical approach: treat uncertainty explicitly through probability distributions and update beliefs as data arrives, rather than making hard decisions at confidence thresholds.

In the Bayesian treatment of bandit problems, each arm's reward probability is modeled with a Beta distribution initialized to a flat prior (Beta(1,1)). After each pull, the posterior updates: a success increments the alpha parameter, a failure increments beta. Thompson Sampling uses these posteriors directly — sample once from each arm's distribution, pick the arm with the highest sample. This naturally balances exploration and exploitation without any tuning parameters.

Cameron's perspective connects bandits to the broader Bayesian workflow: the prior represents initial beliefs about arm quality, the posterior represents updated beliefs after observation, and the decision rule (Thompson Sampling) follows naturally from wanting to act optimally under the current posterior. This is cleaner conceptually than frequentist bandit algorithms like UCB1, which derive their exploration bonus from concentration inequalities rather than probability distributions.

## Key points

- Multi-armed bandits as Bayesian belief updating: each arm has a Beta distribution posterior over reward probability, updated with each observation.
- Thompson Sampling is the natural decision rule: sample from each posterior, choose the arm with the highest sample.
- Contrast with UCB1: UCB1 uses confidence bounds (frequentist), Thompson Sampling uses posterior samples (Bayesian) — both solve the exploration-exploitation tradeoff.
- The Beta distribution is the conjugate prior for Bernoulli reward observations — posteriors update analytically, no MCMC needed.
- Connection to A/B testing: bandits are the adaptive alternative, trading statistical purity for better real-time performance.

[Original](http://camdp.com/blogs/multi-armed-bandits)
