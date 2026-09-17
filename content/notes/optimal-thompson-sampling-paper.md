---
title: "Optimal Thompson Sampling: Asymptotic Analysis"
date: 2014-01-27
categories:
  - bandits
  - thompson-sampling
  - statistics
  - research-paper
  - bayesian
description: Emilie Kaufmann's arXiv paper on the asymptotic optimality of Thompson Sampling for multi-armed bandits — the theoretical grounding that explains why Thompson Sampling works as well as it does empirically. Proves it achieves near-optimal regret bounds.
params:
  source: pinboard
  sourceUrl: http://perso.telecom-paristech.fr/~kaufmann/Arxiv_OptimalThompson_v2.pdf
---

## Summary

This paper by Emilie Kaufmann, Olivier Cappé, and Aurélien Garivier provides the theoretical backing for Thompson Sampling as a nearly optimal multi-armed bandit algorithm. The empirical observation that Thompson Sampling performs well had been around since W.R. Thompson's 1933 paper, but rigorous regret analysis had lagged behind algorithms like UCB1 that were easier to analyze with frequentist concentration inequalities.

The key result: Thompson Sampling achieves asymptotic expected regret matching the Lai-Robbins lower bound — the information-theoretic optimal rate. For Bernoulli-distributed rewards, Thompson Sampling with a Beta distribution prior achieves `O(log n)` regret, and the constant in front of that log matches what the theory says is the best possible. UCB1 achieves the same asymptotic rate but with a larger constant — Thompson Sampling is not just competitive, it's asymptotically as good as any algorithm can be.

The analysis relies on connecting Thompson Sampling to the concept of an optimistic algorithm: at each round, sampling from the posterior is equivalent to optimistically assuming the true parameter is as favorable as your sample. This links the Bayesian intuition (updating beliefs) to the frequentist analysis framework (regret bounds relative to oracle). The paper made Thompson Sampling academically respectable in the bandit literature at the same time practitioners were independently discovering its empirical effectiveness.

## Key points

- Thompson Sampling achieves the Lai-Robbins lower bound asymptotically — no algorithm can have fundamentally smaller per-round regret.
- Beta distribution posteriors for Bernoulli rewards update analytically: alpha += success, beta += failure. No sampling approximation needed.
- The connection between posterior sampling and optimism: sampling from the posterior is like assuming your best-case scenario for each arm.
- UCB1 is also asymptotically optimal but with a larger constant — Thompson Sampling is strictly better in this sense.
- Historically: Thompson wrote the original paper in 1933; the field ignored it for decades in favor of UCB-style analysis; this 2012-era work rehabilitated it.

[Original](http://perso.telecom-paristech.fr/~kaufmann/Arxiv_OptimalThompson_v2.pdf)
