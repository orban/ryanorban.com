---
title: A Practical Guide to Multi-Objective Reinforcement Learning and Planning
date: 2022-04-13
categories:
  - reinforcement-learning
  - multi-objective-optimization
  - planning
  - research
  - survey
description: A Springer survey on multi-objective reinforcement learning and planning — covers scalarization, Pareto-based methods, and utility-based approaches for agents that must balance competing rewards. Useful reference for RL research where single-reward framing is inadequate.
params:
  source: pinboard
  sourceUrl: https://link.springer.com/article/10.1007/s10458-022-09552-y
---

## Summary

This survey, published in Springer's *Autonomous Agents and Multi-Agent Systems* journal in 2022, covers the problem of multi-objective reinforcement learning (MORL) — the case where an agent must optimize multiple, potentially conflicting reward signals simultaneously. Standard reinforcement learning assumes a single scalar reward, but most real-world problems involve tradeoffs: a robot balancing speed against safety, a recommendation system balancing engagement against user wellbeing, a trading agent balancing return against drawdown.

The three main approaches the paper covers are: (1) scalarization — combining multiple objectives into a single scalar reward via a weighted sum, which is simple but requires knowing the weights upfront and can't discover the full tradeoff landscape; (2) Pareto-based methods — maintaining a set of Pareto-optimal policies that represent the frontier of achievable tradeoffs, useful when preferences aren't known in advance; and (3) utility-based methods — learning a utility function over the objective space from human preferences or constraints. Each has different sample complexity, scalability, and knowledge requirements.

The survey is "practical" in that it emphasizes algorithmic guidance over theoretical proofs — which approaches work in which settings, what the computational and sample costs are, and what the implementation pitfalls are. MORL connects to Pareto optimization, multi-objective evolutionary algorithms, constrained MDPs, and the broader safe RL literature. The timing (2022) captures the state of the field before it intersected heavily with RLHF from human feedback — though the utility-based section is directly relevant to how preference learning works in LLM alignment.

## Key points

- Three MORL paradigms: scalarization (weighted sum), Pareto-based (full tradeoff frontier), utility-based (learned preference function).
- Scalarization is efficient but requires prior knowledge of preference weights — misses Pareto-dominated regions.
- Pareto front methods scale poorly with the number of objectives (curse of dimensionality in objective space).
- Directly relevant to safe RL, constrained optimization, and RLHF preference learning.
- Multi-objective planning covered alongside RL — extends to classical tree search and MDP solvers.
- Published in *Autonomous Agents and Multi-Agent Systems* (AAMAS journal) — the main venue for agent-oriented RL research.

[Original](https://link.springer.com/article/10.1007/s10458-022-09552-y) → AI agent
