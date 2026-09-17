---
title: "Clockwork Finance: Automated Analysis of Economic Security in Smart Contracts"
date: 2022-05-29
categories:
  - defi
  - cryptography
  - formal-verification
  - smart-contracts
  - mev
  - blockchain
description: Clockwork Finance Framework (CFF) is a formal verification system for reasoning about economic security in DeFi smart contracts, introducing 'extractable value' (EV) as a rigorous notion. Applied to Uniswap, Sushiswap, and MakerDAO, it automatically discovers $56M/month in MEV-like opportunities.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/2021-1147.pdf
---

## Summary

The Clockwork Finance Framework (CFF), from Kushal Babel, Philip Daian, Mahimna Kelkar, and Ari Juels at Cornell Tech and IC3, is a formal verification framework for mechanized reasoning about the economic security of composed DeFi protocols. The paper introduces **extractable value** (EV) — a formalization of what has come to be called MEV (maximal extractable value) — as the rigorous foundation for analysis. CFF is designed to be contract-complete (can model any smart contract platform), attack-exhaustive by construction (automatically extracts all possible economic attacks), and compositional (can reason over interacting contracts jointly).

The key technical challenge CFF addresses is that DeFi protocols compose in complex ways — a trade on Uniswap creates opportunities in MakerDAO which interact with Sushiswap — and analyzing security in isolation misses attacks that only emerge from composition. CFF models each protocol in a modular, human-readable specification language, then uses a state-of-the-art deductive verifier to exhaustively enumerate economically profitable deviations from normal protocol behavior. This is formal program verification applied to adversarial economic reasoning, not just correctness.

Applied to four protocols representing $17B in total value locked (Uniswap V1, Uniswap V2, Sushiswap, MakerDAO), CFF discovers an expected $56M/month in extractable value without any pre-specified attack strategies. The results demonstrate that even well-audited protocols, when composed, expose extraction opportunities that no single-protocol analysis would find. This directly informs the MEV research agenda and the design of MEV-resistant protocols.

## Key points

- Introduces **extractable value (EV)** as a rigorous formalization of what's extractable by a rational miner/validator from composed DeFi contracts — foundational concept for MEV research
- CFF is attack-exhaustive: it doesn't require specifying attack patterns in advance; the framework mechanically enumerates all profitable deviations
- Composability is the key feature: reasoning over Uniswap + MakerDAO + Sushiswap together reveals extraction opportunities invisible to per-protocol analysis
- Discovers $56M/month average EV across four deployed protocols — concrete evidence of scale of the problem
- Directly informed subsequent MEV mitigation work (Flashbots, MEV-boost, order flow auctions) by establishing a formal baseline

[Original (PDF)](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/2021-1147.pdf)
