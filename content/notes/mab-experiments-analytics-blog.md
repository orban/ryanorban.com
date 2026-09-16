---
title: Multi-Armed Bandit Experiments
date: 2014-01-27
categories:
  - machine-learning
  - bandits
  - experimentation
  - a-b-testing
  - online-learning
description: Analytics blog post on multi-armed bandit experiments as a replacement for static A/B testing in website optimization — covers epsilon-greedy, UCB, and Thompson Sampling with practical framing for product teams.
params:
  source: pinboard
  sourceUrl: http://analytics.blogspot.ca/2013/01/multi-armed-bandit-experiments.html
---

## Summary

This analytics blog post covers multi-armed bandit algorithms as a practical alternative to traditional A/B testing for website optimization. The framing is product-first: static A/B tests lock a fixed fraction of users into an inferior variant throughout the experiment, wasting traffic. Bandit algorithms adaptively route more traffic to better-performing variants as evidence accumulates, reducing total regret across the experiment.

The post reviews the main algorithm families: epsilon-greedy (random exploration at a fixed rate), UCB (Upper Confidence Bound, which explores optimistically based on uncertainty), and Thompson Sampling (Bayesian approach that samples from posterior reward distributions). Each has different exploration-exploitation tradeoffs and implementation complexity.

## Key points

- Multi-armed bandit framing recasts A/B testing as an optimization problem with an explicit regret metric — total suboptimal exposure — rather than just a hypothesis test
- Epsilon-greedy: explore randomly ε% of the time, exploit best arm otherwise — simple but wasteful since exploration rate doesn't decrease as confidence grows
- UCB algorithms prioritize arms with high uncertainty (wide confidence intervals) alongside high estimated reward — principled exploration without tuning ε
- Thompson Sampling draws from the posterior distribution of each arm's reward probability and picks the highest draw — naturally reduces exploration as data accumulates
- The practical tradeoff: bandits optimize the experiment itself but complicate statistical analysis (causal inference from bandit data requires specialized methods)

[Original](http://analytics.blogspot.ca/2013/01/multi-armed-bandit-experiments.html)
