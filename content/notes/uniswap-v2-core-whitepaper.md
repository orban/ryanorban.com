---
title: Uniswap v2 Core
date: 2022-06-18
categories:
  - defi
  - uniswap
  - amm
  - ethereum
  - smart-contracts
  - liquidity-pools
description: "The Uniswap v2 technical whitepaper describes the core design decisions behind the protocol upgrade: arbitrary ERC20 pairs, a hardened time-weighted average price oracle, flash swaps, and a deactivated protocol fee. Together these make Uniswap v2 the infrastructure layer that DeFi summer was built on."
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/whitepaper.pdf
---

## Summary

Uniswap v2 is the March 2020 upgrade to the original Uniswap protocol, which itself introduced the concept of a constant product market maker (x·y=k) for decentralized token exchange on Ethereum. This whitepaper by Hayden Adams, Noah Zinsmeister, and Dan Robinson (of Paradigm) documents the key design decisions and new features, several of which became foundational infrastructure for the broader DeFi ecosystem.

The most significant change is support for arbitrary ERC20/ERC20 pairs — v1 only allowed ERC20/ETH pairs, requiring multi-hop trades and creating unnecessary ETH exposure. V2 also introduces a time-weighted average price (TWAP) oracle that accumulates price data at the beginning of each block, making it manipulation-resistant enough for on-chain use by other protocols. This TWAP oracle became the standard pricing reference for early DeFi protocols including lending markets.

Flash swaps are the third major innovation: traders can borrow any amount of tokens from a Uniswap pool for the duration of a single transaction, paying only if they don't return the assets. This enables flash loans, arbitrage without upfront capital, and on-chain liquidation bots. The architecture also introduces a 1/6 protocol fee that can be switched on by governance — currently off, but designed as a future revenue mechanism. The contracts are deliberately non-upgradeable.

## Key points

- Uniswap v2 enables arbitrary ERC20/ERC20 pairs, eliminating the need to route all trades through ETH and enabling more efficient liquidity pools for stablecoin and non-ETH pairs.
- The TWAP oracle accumulates cumulative price sums per block rather than spot prices, making it resistant to single-block manipulation — the on-chain price reference mechanism for early DeFi.
- Flash swaps allow any amount to be borrowed from a pool within a single transaction, enabling flash loans and capital-efficient arbitrage bots as primitives.
- The constant product formula (x·y=k) is unchanged from v1; all innovation is in the protocol architecture, oracle design, and fee structure.
- Non-upgradeability is a deliberate security choice — the contracts are immutable, pushing governance to a future factory pattern rather than proxy upgrades.

[Original paper](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/whitepaper.pdf)
