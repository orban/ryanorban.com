---
title: Multi-Armed Bandits and the Stitch Fix Experimentation Platform
date: 2020-09-14
categories:
  - machine-learning
  - experimentation
  - bandits
  - statistics
  - personalization
description: Stitch Fix's blog on multi-armed bandits as an alternative to A/B testing — Thompson Sampling routes traffic toward better-performing arms dynamically, reducing wasted exposure. Strong motivation for when bandits beat traditional experimentation.
params:
  source: pinboard
  sourceUrl: https://multithreaded.stitchfix.com/blog/2020/08/05/bandits/
---

## Summary

Stitch Fix's engineering team argues for multi-armed bandits as a superior alternative to classical A/B testing in many experimentation contexts. The core problem with A/B tests: they allocate fixed traffic to all variants throughout the experiment, which means inferior variants receive sustained exposure even after early signals suggest they're worse. Bandits solve this by dynamically reallocating traffic toward better-performing variants as evidence accumulates.

Stitch Fix uses Thompson Sampling as their preferred bandit algorithm. Thompson Sampling works by maintaining a probability distribution over the reward probability of each arm, then selecting the arm by sampling from each distribution and picking the highest sample. This naturally balances exploration and exploitation: arms with high uncertainty get sampled more often (exploration) while arms with high estimated reward get more traffic (exploitation). Thompson Sampling guarantees eventual convergence to the optimal arm and self-corrects instantly as new data arrives — unlike epsilon-greedy approaches, which have fixed exploration rates.

The tradeoff: bandits make statistical analysis harder. A/B tests with fixed traffic splits support clean confidence interval calculations. Bandit experiments have non-stationary traffic allocation, which complicates classical frequentist analysis. But for Stitch Fix's use case — personalization experiments with many variants and limited traffic — the efficiency gains outweigh the statistical complexity.

## Key points

- Multi-armed bandits reduce regret — total suboptimal exposures over the experiment — compared to A/B tests that maintain fixed splits regardless of performance signals.
- Thompson Sampling dominates epsilon-greedy for adaptive allocation: it naturally reduces exploration as evidence accumulates, rather than maintaining a fixed exploration rate.
- Bandits excel over A/B tests when traffic is limited, there are many variants, or the experiment should auto-optimize rather than just inform a decision.
- The statistical analysis tradeoff is real: bandit experiments need specialized analysis approaches (e.g., off-policy evaluation, inverse propensity scoring).
- Stitch Fix applies bandits in a personalization context where the same exploration/exploitation tradeoff governs recommendation systems themselves.

[Original](https://multithreaded.stitchfix.com/blog/2020/08/05/bandits/)
