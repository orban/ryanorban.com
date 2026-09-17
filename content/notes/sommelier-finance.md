---
title: Sommelier Finance — Automated DeFi Strategy Platform
date: 2021-12-22
categories:
  - defi
  - ethereum
  - yield
  - automation
  - web3
description: Sommelier Finance is a DeFi protocol that uses off-chain computation (Cosmos-based co-processor) to automate Uniswap v3 liquidity position management — rebalancing concentrated liquidity ranges without requiring constant manual intervention.
params:
  source: pinboard
  sourceUrl: https://sommelier.finance/
---

## Summary

[Sommelier Finance](/notes/sommelier-finance/) addresses one of the most painful aspects of Uniswap v3 liquidity provision: concentrated liquidity positions require active management. In Uniswap v3, liquidity providers choose a price range for their capital — if the market price moves outside that range, their position stops earning fees and sits idle. Optimal range management requires monitoring prices continuously and rebalancing frequently, which is gas-intensive and impractical for most users.

Sommelier uses a Cosmos-based off-chain computation layer (a co-processor or sidechain) to run the strategy logic — computing optimal rebalancing decisions without paying Ethereum gas for every calculation. Only the actual rebalancing transactions execute on Ethereum, dramatically reducing gas costs relative to fully on-chain strategy execution. The architecture separates strategy computation (cheap, off-chain) from execution (expensive, on-chain).

The product model is like an automated vault or cellar: you deposit WETH/USDC or similar pairs, and the protocol manages the Uniswap v3 position on your behalf — adjusting the range as prices move, compound harvesting fees, and optimizing for maximum fee capture. This is the DeFi equivalent of delegating a discretionary investment account.

## Key points

- Solves Uniswap v3 active management problem: concentrated liquidity requires constant rebalancing to earn fees
- Cosmos co-processor architecture: strategy logic runs off-chain cheaply; only execution hits Ethereum mainnet
- Vault model: deposit assets, protocol manages Uniswap v3 position automatically
- Alternative approaches: Arrakis Finance, Gamma Strategies, Ichi Finance — competing active LP management protocols
- Key risk: smart contract risk + strategy model risk + co-processor centralization risk — more moving parts than passive LP

[Original](https://sommelier.finance/)
