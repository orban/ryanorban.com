---
title: "Optimism in the Face of Uncertainty: the UCB1 Algorithm"
date: 2014-01-27
categories:
  - bandits
  - machine-learning
  - algorithms
  - statistics
  - optimization
description: Jeremy Kun's accessible treatment of the UCB1 algorithm — the principle of 'optimism in the face of uncertainty' formalized as a bandit algorithm with proven regret bounds. Shows why adding a confidence bonus to estimated rewards elegantly solves the exploration-exploitation tradeoff.
params:
  source: pinboard
  sourceUrl: http://jeremykun.com/2013/10/28/optimism-in-the-face-of-uncertainty-the-ucb1-algorithm/
---

## Summary

The multi-armed bandit problem asks: you have k slot machines with unknown payout rates — how do you maximize reward over n pulls? Epsilon-greedy approaches solve this crudely by exploring randomly at a fixed rate. UCB1 (Upper Confidence Bound 1) does something more principled: it treats each arm optimistically, assuming its true reward could be as high as the upper end of a statistical confidence interval.

The UCB1 selection rule is: choose the arm that maximizes `mean_reward_i + sqrt(2 * ln(t) / n_i)`, where `t` is total pulls so far and `n_i` is how many times arm i has been pulled. The confidence bonus `sqrt(2 * ln(t) / n_i)` decreases as an arm is explored (n_i grows) and increases as total time grows (ln(t) grows). This naturally drives exploration toward under-sampled arms without needing a separate exploration parameter to tune.

Jeremy Kun's Math ∩ Programming treatment proves that UCB1 achieves an expected regret of `O(sqrt(k * n * ln(n)))` — sublinear in total pulls, meaning the per-round regret goes to zero. This is a strong guarantee: you pay for exploration upfront but converge to the optimal arm. Compare to Thompson Sampling, which achieves similar or better empirical performance via Bayesian inference over arm reward distributions.

## Key points

- UCB1: select arm maximizing `estimated_mean + confidence_bonus` — balances exploitation (high mean) with exploration (high uncertainty).
- The confidence bonus is `sqrt(2 * ln(t) / n_i)` — derived from Hoeffding's inequality to bound probability that true mean exceeds the estimate.
- "Optimism in the face of uncertainty" is the design principle: assume the best about untested options.
- Proven regret bound: `O(sqrt(k * n * ln(n)))` total regret — asymptotically optimal among algorithms that don't know the reward distributions.
- UCB1 is parameter-free (no epsilon to tune); epsilon-greedy requires tuning exploration rate but is simpler to implement.
- The exploration-exploitation tradeoff is resolved without randomness — UCB1 is deterministic given observed history.

[Original](http://jeremykun.com/2013/10/28/optimism-in-the-face-of-uncertainty-the-ucb1-algorithm/)
