---
title: "DeFi Derivatives: A Comprehensive Landscape Guide"
date: 2022-08-30
categories:
  - defi
  - derivatives
  - blockchain
  - ethereum
  - finance
description: A comprehensive GitHub resource mapping the DeFi derivatives landscape — covering options, perpetuals, interest rate swaps, and structured products built on Ethereum. An invaluable reference for understanding how traditional financial derivatives translate to on-chain primitives.
params:
  source: pinboard
  sourceUrl: https://github.com/0xperp/defi-derivatives
---

![DeFi Derivatives: A Comprehensive Landscape Guide](/images/notes/defi-derivatives-guide.png)

## Summary

`0xperp`'s GitHub repository is a curated reference covering the full landscape of DeFi derivative products: perpetual futures, options, interest rate swaps, structured products, and the infrastructure layer beneath them (AMM-based vs. order book-based architectures, oracle dependencies, liquidation mechanisms). It's structured as a reading list and taxonomy — pointing to the major protocols in each category along with papers and explainers.

The core insight the guide organizes around: DeFi derivatives are more complex than spot trading because they require time-aware settlement, reliable price oracles, and margin management — all of which are harder to do correctly on-chain than off. Perpetual contracts (pioneered by dYdX, then replicated by GMX, Synthetix Perps, Drift Protocol, and others) became the dominant form because they sidestep expiry — there's no need to roll positions, which simplifies user experience and liquidity fragmentation.

The options space in DeFi is less developed because options require dynamic hedging (constant delta-hedging requires frequent rebalancing, expensive in gas), implied volatility surfaces, and more sophisticated AMM designs. Projects like Lyra Finance, Dopex, and Hegic each took different approaches to the liquidity and pricing problems. The guide maps these tradeoffs without declaring winners — useful because the landscape was still actively evolving.

## Key points

- Taxonomy of DeFi derivatives: perpetual futures, options, interest rate swaps, structured products.
- Perpetual contracts are dominant in DeFi because they eliminate roll/expiry complexity.
- Options in DeFi face challenges: dynamic hedging is gas-expensive, pricing requires implied volatility surfaces.
- Covers protocol architectures: AMM-based (e.g., GMX) vs. order book-based (e.g., dYdX).
- Oracle dependency is a critical infrastructure risk in derivatives — price manipulation = liquidation attacks.
- Useful taxonomy for understanding DeFi's evolution toward more complex financial primitives.

[Original](https://github.com/0xperp/defi-derivatives)
