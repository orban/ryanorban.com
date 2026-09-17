---
title: Markov Chains Explained Visually
date: 2016-03-22
categories:
  - statistics
  - probability
  - visualization
  - markov-chains
  - interactive
description: Setosa.io's interactive visual explainer for Markov chains — manipulable transition matrices, live state diagrams, and steady-state convergence demonstrated in browser. The best introductory treatment of the concept available on the web.
params:
  source: pinboard
  sourceUrl: http://setosa.io/ev/markov-chains/
---

## Summary

Setosa.io's Explorable Explanations series produced this interactive treatment of Markov chains, which makes the core concept tangible through direct manipulation. A Markov chain is a process where the next state depends only on the current state — not the history. This Markov property is deceptively simple but underlies an enormous range of applications: text generation, Google PageRank, search algorithms, Monte Carlo simulations, and more.

The interactive element is the key: you can edit the transition matrix (where each entry is the probability of moving from state A to state B) and watch the state distribution converge toward a steady state. This makes the concept of stationary distribution intuitive — after enough transitions, the chain forgets where it started and settles into a stable probability distribution over states.

The visualization also reveals why ergodicity matters: a chain must be irreducible (every state reachable from every other state) and aperiodic for a unique steady state to exist. These conditions are easy to see when you can toggle transition probabilities directly.

## Key points

- Markov property: next state depends only on current state, not history.
- Transition matrix: each row sums to 1.0, encoding probabilities of all possible transitions.
- Stationary distribution: the long-run probability over states that the chain converges to.
- Applications: text generation, PageRank, Monte Carlo simulation, Hidden Markov Models.
- Ergodicity requires irreducibility and aperiodicity — visualized directly in the interactive.

[Original](http://setosa.io/ev/markov-chains/)
