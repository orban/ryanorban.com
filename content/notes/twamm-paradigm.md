---
title: "TWAMM: Time-Weighted Average Market Maker"
date: 2022-06-07
categories:
  - defi
  - amm
  - ethereum
  - research
  - paradigm
description: Paradigm's paper introducing the Time-Weighted Average Market Maker (TWAMM) — a DEX primitive designed to execute large orders over time by continuously trading against an embedded AMM. Elegant solution to the large-order MEV problem that haunts standard AMMs.
params:
  source: pinboard
  sourceUrl: https://www.paradigm.xyz/2021/07/twamm
---

## Summary

TWAMM (Time-Weighted Average Market Maker) is a DeFi primitive proposed by Paradigm researchers Dave White, Dan Robinson, and Uniswap founder Hayden Adams. The problem it solves: executing large token swaps on a standard AMM like Uniswap is expensive. A whale selling 1000 ETH in a single transaction moves the price against themselves and invites sandwich attacks — bots that front-run the trade, extract value, and leave the large trader with worse execution.

TWAMM embeds a long-term order mechanism directly in the AMM contract. Instead of executing immediately, a large trade is broken into infinitely many infinitesimal swaps spread over a user-specified time window (e.g. "sell 1000 ETH over the next 24 hours"). The contract maintains an embedded virtual AMM that continuously processes these microscopic trades between any two users who have submitted opposing long-term orders. When a regular swap triggers the pool, it first catches up the virtual AMM by computing the analytical solution to the continuous-time trading equations.

This is elegant because it solves the large-order problem without requiring off-chain infrastructure or order books. The TWAP execution naturally tracks the time-weighted average price — which is exactly what large traders (institutions, treasury managers) want when executing size. The sandwich attack surface is minimized because individual transactions from the large order are infinitesimally small. The key insight is treating the AMM as a continuous-time system with a closed-form solution rather than a discrete-step ledger.

## Key points

- TWAMM executes large orders as a continuous stream of infinitesimal swaps against an embedded AMM — not as individual transactions
- Closed-form math: the continuous-time swapping has an analytical solution that gets applied in one contract call (no loop)
- Dramatically reduces sandwich attack exposure for large trades vs. executing a single large transaction
- Use case: institutional-size swaps, DAO treasury management, DCA (dollar-cost averaging) strategies
- Built on top of any AMM with virtual reserves — extends Uniswap-style constant product curves
- Paradigm has historically published ideas before building them — TWAMM influenced Uniswap v4 hooks and derivative protocols

[Original](https://www.paradigm.xyz/2021/07/twamm)
