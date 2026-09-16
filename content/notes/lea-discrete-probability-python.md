---
title: Lea — Discrete Probability Distributions in Python
date: 2014-11-10
categories:
  - python
  - probability
  - statistics
  - library
description: Lea is a Python library for working with discrete probability distributions symbolically — defining distributions, computing joint and conditional probabilities, and simulating outcomes. An unusual tool that treats probability as a first-class programming construct.
params:
  source: pinboard
  sourceUrl: https://code.google.com/p/lea/
---

## Summary

Lea is a Python library that models discrete probability distributions as first-class objects. Rather than sampling from distributions (as NumPy or SciPy does), Lea works symbolically: you define distributions, combine them with arithmetic and logical operators, and get exact probability values back. Think of it as a calculator for discrete probability.

The core data structure is a distribution over finite outcomes — e.g., `Lea.fromVals('H', 'T')` for a fair coin. You can combine distributions: sum two dice and Lea gives you the exact distribution of the sum. Condition on events: `P(X > 3 | Y == 2)`. Run Bayesian updates without writing Bayes' rule by hand. This makes Lea useful for educational purposes (working through probability problems computationally) and for exact inference on small discrete systems where sampling introduces unnecessary noise.

The library predates modern probabilistic programming tools like PyMC, Stan, and NumPyro, which handle continuous distributions with MCMC or variational inference. Lea occupies a different niche: small, exact, discrete — useful for teaching probability and for problems where the state space is genuinely small.

## Key points

- Lea: Python library for exact computation with discrete probability distributions — not sampling, but symbolic arithmetic.
- Define distributions, combine them with operators, get exact probability answers.
- Supports conditional probability, joint distributions, and Bayes' theorem application.
- Useful for: teaching probability, modeling dice/card games, small discrete Bayesian networks.
- Predates modern probabilistic programming tools (PyMC, Stan) — fills the small-exact-discrete niche those don't target.
- Hosted on Google Code in 2014 — later migrated to GitHub as Google Code shut down in 2016.

[Original](https://code.google.com/p/lea/)
