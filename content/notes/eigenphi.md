---
title: "EigenPhi: MEV Analytics"
date: 2022-05-17
categories:
  - mev
  - ethereum
  - defi
  - analytics
  - blockchain
description: EigenPhi is an on-chain MEV analytics platform that scans Ethereum blocks for arbitrage, sandwich attacks, and liquidations, showing the bots, victims, and profit flows. One of the first accessible dashboards for visualizing MEV extraction in real time.
params:
  source: pinboard
  sourceUrl: https://eigenphi.io/
---

![EigenPhi: MEV Analytics](/images/notes/eigenphi.png)

## Summary

[EigenPhi](/notes/eigenphi/) is an analytics platform focused on MEV (Maximal Extractable Value) on Ethereum. It scans every block for extractable value events — arbitrage (price discrepancies between DEXes captured by searcher bots), sandwich attacks (frontrunning + backrunning user swaps), and liquidations (bots racing to claim undercollateralized DeFi positions). For each event, [EigenPhi](/notes/eigenphi/) shows the bot address, the victim (if any), and the profit captured.

This kind of visibility was largely absent in early DeFi. Users who got sandwiched often had no idea — their swap executed at a slightly worse price with no obvious on-chain signal. [EigenPhi](/notes/eigenphi/) makes the extraction legible: you can see which bots are most active, how much MEV was extracted in a given block or day, and which protocols are most targeted. Uniswap v2/v3 pools and Curve pools are historically the heaviest sandwich targets because of their high liquidity and frequent retail swaps.

The platform also enables research into MEV patterns over time — whether Flashbots reduced certain types of extraction, how the transition to Proof of Stake affected extraction dynamics, and which bot strategies dominate in different market conditions. This empirical data is valuable both for DeFi protocol designers thinking about MEV-resistant mechanisms and for researchers studying the microeconomics of block production.

## Key points

- Tracks three MEV types: arbitrage, sandwich attacks, liquidations — with bot addresses, victims, and profits
- Makes extraction legible to retail users who experienced worse swap prices without knowing why
- Useful for comparing MEV activity before/after Flashbots adoption and pre/post Merge
- Sandwich attack anatomy: frontrun (buy before victim) + victim swap (moves price) + backrun (sell after) — [EigenPhi](/notes/eigenphi/) shows all three transactions
- Pairs with Flashbots docs for understanding the supply side; [EigenPhi](/notes/eigenphi/) is the demand/extraction side view
- Related: [Jito MEV dashboard](/notes/jito-mev-dashboard/) for Solana MEV; Dune Analytics for custom MEV queries

[Original](https://eigenphi.io/)
