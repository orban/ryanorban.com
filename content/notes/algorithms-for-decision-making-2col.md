---
title: Algorithms for Decision Making (2-column edition)
date: 2022-04-22
categories:
  - decision-making
  - reinforcement-learning
  - planning
  - pomdp
  - textbook
description: A two-column or second-edition variant of the MIT Press textbook by Mykel Kochenderfer covering decision-making under uncertainty, from MDPs and POMDPs through reinforcement learning and multi-agent systems. This copy predates the primary 2023-01 vault entry and may represent an earlier draft or reformatted version.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/algorithms for decision making 2.pdf
---

## Summary

This is a variant copy of the MIT Press textbook *Algorithms for Decision Making* by Mykel Kochenderfer, Tim Wheeler, and Kyle Wray — likely a two-column formatted or early-draft version of the same text already in the vault (see 2023-01-09-algorithms-for-decision-making). The book is the canonical graduate-level reference for sequential decision-making under uncertainty, organized around a progression from exact methods to approximations to learning.

The textbook's central framework is the Markov decision process (MDP) and its extension to partial observability via the POMDP (partially observable MDP). For MDPs, the book covers both exact methods (value iteration, policy iteration) and approximate approaches (fitted value functions, policy gradient). The POMDP treatment is particularly thorough: belief state representation, point-based value iteration, SARSOP, and online planning via Monte Carlo tree search.

Reinforcement learning enters as one approach to solving MDPs when a transition model is unavailable — situating RL within the broader planning and optimal control literature rather than treating it as a standalone field. The multi-agent section covers Nash equilibrium, correlated equilibrium, and decentralized POMDPs. The full text is freely available at algorithmsbook.com and is widely used alongside Sutton and Barto.

## Key points

- Unified framework: MDPs → POMDPs → multi-agent settings, covering exact and approximate algorithms for each
- Belief state representation converts POMDPs into continuous-space MDPs solvable by point-based value iteration
- Monte Carlo tree search (MCTS) enables online planning without a full transition model — the basis of AlphaGo
- Policy gradient methods and actor-critic architectures handle continuous action spaces; PPO is the robust modern variant
- This copy (saved 2022-04-22) likely predates or differs in format from the primary entry at 2023-01-09-algorithms-for-decision-making

[Original PDF](file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/algorithms for decision making 2.pdf)
 → AI agent
