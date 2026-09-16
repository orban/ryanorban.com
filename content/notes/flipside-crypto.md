---
title: Flipside Crypto — Blockchain Analytics Platform
date: 2022-07-16
categories:
  - blockchain
  - analytics
  - defi
  - data
  - sql
description: Flipside Crypto is a blockchain analytics platform providing SQL-queryable on-chain data across Ethereum, Solana, Terra, and other chains. Notable for its bounty model where analysts earn FLOW tokens for producing quality dashboards — crowdsourcing blockchain data analysis.
params:
  source: pinboard
  sourceUrl: https://app.flipsidecrypto.com/velocity?nav=Discover
---

## Summary

[Flipside Crypto](/notes/flipside-crypto/) is a blockchain data analytics platform that provides SQL-queryable access to normalized on-chain data across multiple chains: Ethereum, Solana, Terra, Algorand, Osmosis, and others. The platform abstracts away the complexity of working with raw node data, providing clean tables for transactions, DeFi events (swaps, liquidations, borrows), NFT sales, and token transfers.

The business model was unusual: Flipside operated an analyst bounty system where blockchain projects could fund data analytics questions, and community analysts earned FLOW tokens for producing high-quality dashboards. This created a marketplace for on-chain intelligence where protocols (who want their ecosystem analyzed) subsidize analysts (who want to be paid for data work). The resulting dashboards were often of professional quality and publicly visible.

This competed with Dune Analytics (which favored power users and custom SQL), Nansen (which focused on labeled wallet analysis), and The Graph (which focused on indexed event data via subgraphs). Flipside's advantage was cross-chain coverage and the bounty incentive structure that produced more dashboards than a pure subscription model would.

## Key points

- SQL interface to normalized on-chain data across 10+ chains — no raw node access required
- Bounty program: projects pay for data analysis, analysts earn FLOW tokens — aligns incentives across the ecosystem
- Covers DeFi events (Uniswap swaps, Aave borrows/liquidations), NFT sales, governance activity, token flows
- Competes with Dune Analytics on SQL analytics; covers more chains but with less raw access
- Important for MEV researchers and DeFi analysts who need historical transaction data without running their own indexer

[Original](https://app.flipsidecrypto.com/velocity?nav=Discover)
