---
title: Understanding Multi-Armed Bandit Algorithms
date: 2014-01-25
categories:
  - machine-learning
  - bandits
  - experimentation
  - algorithms
  - tutorial
description: DataBozo's conceptual explanation of multi-armed bandit algorithms — epsilon-greedy, UCB, and Thompson Sampling compared from first principles. Aimed at practitioners who want to understand the tradeoffs before implementing.
params:
  source: pinboard
  sourceUrl: http://www.databozo.com/2013/11/04/Understanding_multi-armed_bandit_algorithms.html
---

## Summary

DataBozo's tutorial explains multi-armed bandit algorithms from first principles, comparing the main approaches on their exploration-exploitation tradeoff. The framing is practical: you're running an online service and want to maximize total reward (clicks, conversions, engagement) over time, not just find the best option eventually. Every suboptimal exposure costs you something, so the question is how to minimize regret while still learning.

The three main families covered: epsilon-greedy (simplest, least efficient), UCB algorithms (principled, based on optimism under uncertainty), and Thompson Sampling (Bayesian, requires a conjugate prior but naturally decays exploration over time). All three have polynomial regret bounds; they differ in constants and in how that bound scales with the number of arms and time horizon.

## Key points

- The exploration-exploitation tradeoff: pure exploitation (always pick current best) gets stuck in local optima; pure exploration wastes all rewards on suboptimal arms — the algorithms navigate between these
- Epsilon-greedy with ε=0.1 means 10% of traffic is wasted on random exploration forever, even when you're already confident — a significant weakness at scale
- UCB1 adds a confidence bonus inversely proportional to how many times an arm has been pulled — arms that haven't been explored recently get an exploration bonus
- Thompson Sampling with Beta-Bernoulli conjugate prior: maintain Beta(α, β) for each arm's success rate, sample once per arm, pick highest sample — elegant and empirically strong
- Regret analysis: all three are sublinear in time (regret grows as O(log T)), but Thompson Sampling typically achieves smaller constants in practice

[Original](http://www.databozo.com/2013/11/04/Understanding_multi-armed_bandit_algorithms.html)
