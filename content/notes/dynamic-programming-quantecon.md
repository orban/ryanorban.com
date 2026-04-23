---
title: "Dynamic Programming: QuantEcon textbook"
date: 2025-12-01
categories:
  - economics
  - mathematics
  - education
  - python
  - optimization
description: QuantEcon's open-source Dynamic Programming textbook teaches the mathematical foundations of sequential decision-making with Python and Julia implementations. Covers Bellman equations, value function iteration, and stochastic control — the tools behind modern RL and macro models alike.
params:
  source: pinboard
  sourceUrl: https://dp.quantecon.org/
---

![Dynamic Programming: QuantEcon textbook](/images/notes/dynamic-programming-quantecon.png)

## Summary

QuantEcon's Dynamic Programming book is an open-source textbook covering the mathematical theory and computational implementation of dynamic programming — the framework for sequential decision-making under uncertainty. The book is rigorous but computational: every concept comes with Python (and often Julia) code, making it possible to move directly from theory to implementation.

Dynamic programming sits at an interesting intersection: it's the core mathematical framework for macroeconomic models (optimal consumption, portfolio choice, firm investment) and also the foundation for modern reinforcement learning (Bellman equations, value function iteration, policy gradients). A solid understanding here pays dividends in both directions — economic modeling and RL research draw on the same toolkit.

The key concepts the book covers: the Bellman equation as a fixed-point operator, value function iteration for solving infinite-horizon problems, policy function iteration as a faster alternative, and extensions into stochastic settings and Markov decision processes. QuantEcon is associated with Thomas Sargent and John Stachurski, both serious economists who have invested heavily in making the math computationally accessible.

## Key points

- Open-source textbook — free online, covers Bellman equations, value function iteration, policy iteration, MDPs.
- Dual audience: economists doing macro modeling and practitioners learning reinforcement learning foundations.
- Python and Julia implementations — not just theory, but runnable code for each concept.
- QuantEcon project by Thomas Sargent and John Stachurski — Nobel-level economic theory made computational.
- The Bellman equation framework underlies both classical economics and modern RL — understanding it connects both fields.
- Companion resources: Seeing Theory for probability intuition, [Python Data Science Handbook](/notes/python-data-science-handbook/) for tooling.

[Original](https://dp.quantecon.org/)
