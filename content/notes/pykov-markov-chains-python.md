---
title: Pykov — Finite Markov Chains in Python
date: 2014-10-06
categories:
  - python
  - markov-chains
  - statistics
  - probability
  - library
description: Pykov is a small Python library for working with finite regular Markov chains — define chains from scratch or load from files, compute stationary distributions, simulate walks, and analyze steady-state behavior. Useful for any system that can be modeled as probabilistic state transitions.
params:
  source: pinboard
  sourceUrl: https://github.com/riccardoscalco/Pykov
---

## Summary

Pykov is a small Python library by Riccardo Scalco for working with finite regular Markov chains. The library treats a Markov chain as a weighted directed graph where nodes are states and edge weights are transition probabilities. You can define a chain from scratch by specifying transition probabilities, or read it from a text file in a specified format.

A Markov chain has the Markov property: the next state depends only on the current state, not on history. For a finite regular chain (every state reachable from every other state in finite steps), there exists a unique stationary distribution — a probability vector over states that remains unchanged by applying the transition matrix. This is the long-run fraction of time the chain spends in each state.

Pykov exposes the standard Markov chain operations: computing the stationary distribution, computing the distribution after n steps from a given start state, simulating random walks, and computing hitting times (expected steps to reach a target state). These operations are all matrix algebra under the hood — the transition matrix to the n-th power gives n-step probabilities.

Use cases for Markov chains in data science: text generation (character-level language models), recommendation systems (random walks on item graphs), web analytics (page transition models), and simulation of queuing systems.

## Key points

- Pykov: define finite Markov chains from edge weights, compute stationary distributions, simulate walks.
- Markov property: next state depends only on current state — enables efficient matrix-based computation.
- Stationary distribution: left eigenvector of the transition matrix with eigenvalue 1 — long-run state frequencies.
- n-step distribution: transition matrix raised to power n — useful for simulating after n steps, where am I?
- Hitting time: expected steps to first reach a target state — key for analyzing absorbing states.
- Finite regular chains always have a unique stationary distribution — the foundation of PageRank and Markov-based recommendation.

[Original](https://github.com/riccardoscalco/Pykov) → GitHub
