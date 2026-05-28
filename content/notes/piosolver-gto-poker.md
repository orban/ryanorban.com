---
title: "PioSOLVER: Game Theory Optimal Poker Solver"
date: 2022-01-19
categories:
  - poker
  - game-theory
  - gto
  - software
  - strategy
  - optimization
description: PioSOLVER is the industry-standard GTO (Game Theory Optimal) solver for poker — computes Nash equilibrium strategies for heads-up and multi-way spots using CFR algorithms. Used by professional players to study theoretically unexploitable play.
params:
  source: pinboard
  sourceUrl: https://www.piosolver.com/pages/pio-starting-page
---

![PioSOLVER: Game Theory Optimal Poker Solver](/images/notes/piosolver-gto-poker.png)

## Summary

PioSOLVER is the dominant software tool for studying Game Theory Optimal (GTO) poker strategy — the application of Nash equilibrium computation to Texas Hold'em hand analysis. It's used by professional poker players and coaches to study theoretically unexploitable strategies for specific game situations.

The core computation: given a game tree (two players, their possible hand ranges, the community cards, the pot size, and a set of allowed bet sizes), PioSOLVER solves for the strategy pair where neither player can improve their expected value by deviating unilaterally — the Nash equilibrium of that specific spot. This is done via counterfactual regret minimization (CFR), an iterative algorithm that progressively reduces strategy exploitability until convergence.

Why this matters for poker: in a zero-sum game, if your opponent plays GTO, you cannot exploit them. By studying GTO strategies with PioSOLVER, players build intuition for balanced ranges, bet sizing theory, and how strategy changes with stack depths and pot geometry. The tradeoff: GTO play is theoretically unexploitable but not necessarily maximally exploitative against opponents who deviate from GTO — exploitative adjustments require reading actual opponents.

## Key points

- Computes Nash equilibrium strategies for poker hand situations using CFR (counterfactual regret minimization).
- Inputs: player hand ranges, board cards, pot size, allowable bet sizes — outputs balanced GTO frequencies for every decision.
- Studies theoretically unexploitable play — the foundation for understanding why certain bet sizes or frequencies are correct.
- GTO ≠ maximally exploitative: optimal against exploitative opponents requires deviating from GTO based on reads.
- Industry standard used by professional players, coaches, and training sites for hand history review and spot study.

[Original](https://www.piosolver.com/pages/pio-starting-page)
