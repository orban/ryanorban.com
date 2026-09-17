---
title: "Gauntlet: DeFi Economic Security Platform"
date: 2022-02-22
categories:
  - defi
  - risk-management
  - simulation
  - ethereum
  - economic-security
description: Gauntlet is a DeFi economic security platform that uses agent-based simulation to stress-test protocol parameters — finding safe collateral ratios, liquidation thresholds, and interest rate curves for lending protocols. The risk management layer that keeps Aave and Compound from getting drained.
params:
  source: pinboard
  sourceUrl: https://gauntlet.network/
---

## Summary

Gauntlet (founded by Tarun Chitra) is a quantitative risk management platform for DeFi protocols. The core product: agent-based simulation that models millions of market scenarios to find safe parameter settings for lending protocols. For a protocol like Aave or Compound, parameters like collateral factors (how much you can borrow against an asset), liquidation bonuses, and interest rate curves directly determine whether the protocol stays solvent during market stress events.

The simulation approach works by modeling realistic market behavior: price crashes, whale positions, liquidity conditions, gas costs during congestion. Gauntlet runs these scenarios to find parameter combinations where protocol solvency holds — and recommends those to governance. This is genuinely hard: the right liquidation threshold for ETH depends on ETH's volatility, the size of positions, liquidity on DEXs, and gas costs — all of which interact nonlinearly.

Gauntlet works with Aave, Compound, MakerDAO, Uniswap, and other major protocols. Their reports influenced billions in collateral parameters. The company represents a broader trend: as DeFi TVL grew to hundreds of billions, the economic security of protocol parameters became too important to set by intuition. Game theory, financial modeling, and simulation became the tools for governance decisions — a real demand for quantitative rigor in decentralized finance.

## Key points

- Agent-based simulation: model realistic market actors and stress scenarios to find safe protocol parameters.
- Works with Aave, Compound, MakerDAO — recommendations influence governance on multi-billion TVL protocols.
- Parameters at stake: collateral factors, liquidation thresholds, interest rate models, reserve factors.
- Founded by Tarun Chitra, a well-known figure in DeFi research and simulation.
- Related to economic security research: mechanism design, game theory, and financial risk modeling applied to smart contracts.

[Original](https://gauntlet.network/) → AI agent
