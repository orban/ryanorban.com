---
title: A Book About Bandit Algorithms
date: 2014-01-27
categories:
  - bandits
  - machine-learning
  - optimization
  - web
  - experimentation
description: John Myles White's free book on bandit algorithms for website optimization — covers epsilon-greedy, softmax, UCB, and Thompson Sampling with practical web application examples. An accessible bridge from theory to product experimentation.
params:
  source: pinboard
  sourceUrl: http://bandits.mynaweb.com/
---

## Summary

John Myles White — statistician and co-author of Machine Learning for Hackers — wrote this book to make multi-armed bandit algorithms accessible to web developers and product teams. The driving argument: classical A/B testing wastes traffic by holding fixed the fraction of users exposed to inferior variants throughout the entire experiment. Bandit algorithms solve this by continuously reallocating traffic toward better-performing options as evidence accumulates.

The book (also published as "Bandit Algorithms for Website Optimization" through O'Reilly) covers the major algorithms in order of sophistication: epsilon-greedy (explore randomly at rate ε, exploit otherwise), softmax (assign traffic proportional to Boltzmann-weighted expected rewards), UCB1 (exploit the arm with highest upper confidence bound), and Thompson Sampling (sample from Bayesian posterior over reward probabilities and pick the highest draw). Each algorithm gets a worked example relevant to website optimization — button colors, headlines, recommendation slots.

The site was associated with mynaweb.com, a company applying bandit algorithms to recommendation systems. The book was one of the first to bridge the gap between the reinforcement learning literature on exploration-exploitation tradeoff and the practical need for faster, more adaptive experimentation in product teams.

## Key points

- Epsilon-greedy: simplest bandit — explore with probability ε, exploit best-known arm otherwise. Easy to implement, hard to tune well.
- Softmax: probabilistic exploration proportional to temperature-scaled expected reward — smoother than epsilon-greedy but also needs a temperature parameter.
- UCB1: deterministic, parameter-free — picks the arm with highest mean + confidence bonus. Proven regret bound.
- Thompson Sampling: Bayesian — maintains a Beta distribution over reward probability for each arm, samples once per decision, picks highest sample. Often best empirically.
- All four outperform classical A/B testing in terms of cumulative reward during the experiment, at the cost of slightly lower statistical power for post-hoc analysis.

[Original](http://bandits.mynaweb.com/)
