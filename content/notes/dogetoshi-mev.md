---
title: "Dogetoshi/MEV: Curated MEV Resources"
date: 2022-07-17
categories:
  - mev
  - ethereum
  - defi
  - blockchain
  - research
description: Dogetoshi's MEV repository is a curated collection of resources on maximal extractable value — papers, talks, tools, and code for understanding how searchers, builders, and validators profit from transaction ordering on Ethereum.
params:
  source: pinboard
  sourceUrl: https://github.com/Dogetoshi/MEV
---

![Dogetoshi/MEV: Curated MEV Resources](/images/notes/dogetoshi-mev.png)

## Summary

Dogetoshi is a pseudonymous DeFi researcher and MEV (Maximal Extractable Value) practitioner known for detailed technical analysis of Ethereum transaction ordering dynamics. The MEV GitHub repository is a curated collection of resources for understanding the MEV ecosystem: foundational papers, technical explainers, tools used by searchers, and code examples. Think of it as a well-maintained reading list for someone trying to go from understanding MEV conceptually to participating as a searcher or understanding the competitive dynamics.

MEV refers to profit that can be extracted by controlling transaction ordering within a block — or more precisely, the set of transactions you include and in what order. Miners (pre-Merge) and validators (post-Merge) have this power; so do searchers who submit bundles to Flashbots' MEV-Boost system. Common strategies include frontrunning DEX trades, sandwich attacks on AMM swaps, arbitrage between DEXes, and liquidation of undercollateralized positions.

The repository complements [Awesome-MEV](/notes/awesome-mev/) (the broader community list) with Dogetoshi's own curation perspective. Dogetoshi's particular focus was on Solana MEV dynamics alongside Ethereum — Solana's architecture (no mempool, different ordering guarantees) creates distinct MEV opportunities. The work is representative of the 2022 period when MEV had moved from academic curiosity to serious professional trade.

## Key points

- Curated MEV resources: papers, tools, code — by Dogetoshi, a pseudonymous DeFi MEV researcher
- MEV strategies covered: frontrunning, sandwich attacks, arbitrage, liquidations
- Flashbots ecosystem context: searchers submit bundles, builders assemble blocks, validators propose
- Solana MEV coverage in addition to Ethereum — Solana's no-mempool architecture creates unique dynamics
- Pairs with [Awesome-MEV](/notes/awesome-mev/) and [Jito MEV dashboard](/notes/jito-mev-dashboard/) for a complete picture of the ecosystem
- 2022 context: MEV had become a professional trade; searcher bots competed for billions in annual extraction

[Original](https://github.com/Dogetoshi/MEV)
