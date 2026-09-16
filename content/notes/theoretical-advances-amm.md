---
title: Theoretical Advances in AMM Understanding
date: 2022-01-30
categories:
  - defi
  - amm
  - market-making
  - mechanism-design
  - crypto
  - economics
description: A technical deep-dive on theoretical advances in understanding automated market makers (AMMs) — covering impermanent loss, concentrated liquidity, and how AMM design choices create different economic tradeoffs for liquidity providers. Essential reading for DeFi protocol design.
params:
  source: pinboard
  sourceUrl: https://fbifemboy.substack.com/p/theoretical-advances-in-amm-understanding
---

## Summary

Automated market makers (AMMs) are the core mechanism of DeFi liquidity — protocols like Uniswap, Curve, and Balancer use mathematical invariants (constant product, stableswap, etc.) rather than order books to price assets and settle trades. This substack post surveys the theoretical advances in understanding how AMMs actually work and what economic tradeoffs different designs create.

The central concept is impermanent loss (IL) — the divergence loss liquidity providers (LPs) experience when the relative price of their deposited tokens changes. If you provide liquidity to an ETH/USDC pool and ETH doubles, you'd have been better off just holding ETH rather than providing liquidity. The impermanent label is misleading — it's only impermanent if prices return to the original ratio, which is not guaranteed. Uniswap v3's concentrated liquidity model increases LP capital efficiency by letting providers specify price ranges, but amplifies IL for positions near current price.

The deeper theoretical work covers how MEV (maximal extractable value) interacts with AMM design: arbitrage bots capture value from LPs through price update latency, and this loss vs. rebalancing (LVR) is increasingly understood as the true cost of AMM LP positions beyond stated fees. Good AMM design attempts to minimize LVR through mechanisms like just-in-time (JIT) liquidity, TWAP-based pricing, and dynamic fees.

## Key points

- Impermanent loss is the core LP economic risk: price divergence between deposited tokens causes portfolio underperformance vs. holding.
- Uniswap v3 concentrated liquidity improves capital efficiency but amplifies IL for active price ranges.
- LVR (loss vs. rebalancing): the true cost of LP positions — arbitrage extraction by MEV bots beyond fee revenue.
- AMM design space: constant product (Uniswap), stableswap (Curve), weighted (Balancer) — each optimizes for different asset types and volatility regimes.
- Active research area: dynamic fees, just-in-time liquidity, TWAP oracles as mechanisms to reduce LVR.

[Original](https://fbifemboy.substack.com/p/theoretical-advances-in-amm-understanding)
