---
title: Markov Chains Explained Visually
date: 2014-07-29
categories:
  - probability
  - visualization
  - markov-chains
  - statistics
  - interactive
description: Victor Powell's interactive visual explanation of Markov chains using animated state diagrams — one of the best-known examples of explorable explanations in mathematics. Essential reading for anyone building intuition for probabilistic state systems before tackling HMMs, PageRank, or reinforcement learning.
params:
  source: pinboard
  sourceUrl: http://setosa.io/blog/2014/07/26/markov-chains/index.html
---

## Summary

Markov chains are a class of stochastic process where the next state depends only on the current state — not on the history of how you got there. This is the Markov property, sometimes called memorylessness. Victor Powell's interactive visualization on setosa.io makes this concrete: you watch tokens transition between states in real time, with editable transition matrix values that update the animation immediately.

The visual approach is particularly effective here because a Markov chain is fundamentally a directed graph where edges carry transition probabilities. Seeing those probabilities as animated flows — rather than as rows in a matrix — builds immediate intuition for concepts like steady-state distribution and ergodicity. A chain is ergodic if you can eventually reach any state from any other state; the animation makes it visually obvious when a chain is or isn't.

The piece is part of the setosa.io "Explained Visually" series alongside other interactive explorations of principal component analysis and conditional probability. It represents a particular approach to mathematical pedagogy: don't define, simulate. The interactive format predates but anticipates the modern explorable explanations movement.

## Key points

- The Markov property means transitions depend only on current state — the chain has no memory, which makes the math tractable and the simulation straightforward.
- Transition matrix rows must sum to 1 (each row is a probability distribution over next states); the interactive editor enforces this.
- Long-run behavior converges to a steady-state distribution — a fixed point of the transition matrix, solvable as a left eigenvector.
- Markov chains underlie PageRank, hidden Markov models in NLP, Monte Carlo Markov Chain sampling in Bayesian inference, and reinforcement learning formulations.
- The visual format (by Victor Powell) became a reference example for explorable explanations as a genre.

[Original](http://setosa.io/blog/2014/07/26/markov-chains/index.html)
