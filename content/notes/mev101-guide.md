---
title: "MEV101: The 0 to 1 Guide for Maximal Extractable Value"
date: 2022-07-27
categories:
  - cryptocurrency
  - ethereum
  - mev
  - defi
  - blockchain
  - trading
description: A ground-up guide to Maximal Extractable Value (MEV) in Ethereum and DeFi, covering sandwiching, arbitrage, liquidations, generalized frontrunning, flash loans, and Flashbots. A practitioner's introduction to the adversarial game theory and dark-forest economics underlying transaction ordering in public blockchains.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/MEV101.pdf
---

## Summary

This informal guide (by @0xmebius, 2021) provides a comprehensive introduction to Maximal Extractable Value (MEV) in Ethereum and DeFi, structured as a curated curriculum that builds from blockchain fundamentals to advanced MEV strategies. MEV refers to the profit available to block producers (miners/validators) or sophisticated searchers by reordering, inserting, or censoring transactions within a block — exploiting the transparent mempool of public blockchains.

The guide covers the full DeFi infrastructure stack: smart contracts, ERC-20 tokens, stablecoins, automated market makers (particularly Uniswap V2/V3 and Curve), lending protocols (AAVE, Compound), and oracle designs. Against this foundation, it covers the main MEV strategies: sandwich attacks (frontrunning and backrunning a victim's large trade), DEX arbitrage across price discrepancies, liquidation of undercollateralized positions, generalized frontrunning (copying and front-inserting any profitable transaction), and JIT (just-in-time) liquidity provision. Flashbots is introduced as the infrastructure that moved the MEV competition from on-chain gas wars (Priority Gas Auctions) to off-chain sealed-bid auctions, reducing network congestion.

The guide frames MEV as a game-theoretic arms race where extractable value is structurally guaranteed by DeFi's design, and the competition for it drives sophisticated searchers to invest heavily in infrastructure, speed, and on-chain simulation. Understanding MEV is essential for DeFi protocol design, as many protocols have been retroactively harmed by MEV vectors their designers didn't anticipate.

## Key Points

- MEV is profit extracted by reordering or inserting transactions in a block, structurally guaranteed by DeFi's transparent mempool design
- Key strategies: sandwich attacks on AMM trades, cross-DEX arbitrage, liquidation of undercollateralized loans, generalized frontrunning
- Flashbots transformed MEV from on-chain gas wars to sealed-bid off-chain auctions, reducing network congestion while concentrating MEV to sophisticated searchers
- Flash loans enable capital-free MEV extraction — borrow, exploit, repay in one atomic transaction
- MEV is a mechanism design failure mode: transparent public transaction ordering creates persistent adversarial extraction pressure on every DeFi protocol

[Original paper](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/MEV101.pdf)
