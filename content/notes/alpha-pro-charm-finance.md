---
title: "Alpha Pro: Permissionless Options-Selling on DeFi"
date: 2022-01-18
categories:
  - defi
  - options
  - ethereum
  - strategy
  - yield
  - crypto
description: Alpha Pro is a permissionless DeFi platform from Charm Finance for automated options-selling strategies on Ethereum — earn yield by systematically selling options (strangles, etc.) with on-chain execution and no centralized management. The on-chain equivalent of systematic options-selling desks.
params:
  source: pinboard
  sourceUrl: https://medium.com/charmfinance/introducing-alpha-pro-5a11012c48c1
---

![Alpha Pro: Permissionless Options-Selling on DeFi](/images/notes/alpha-pro-charm-finance.png)

## Summary

Alpha Pro is a product by Charm Finance that brings automated options-selling strategies to DeFi on Ethereum. Launched January 2022, it allows users to deposit assets and participate in systematic options-selling strategies (selling strangles, straddles, covered calls) that are executed entirely on-chain without centralized management.

The premise draws from traditional finance: systematic options-selling strategies (like those used by dedicated hedge funds or structured products) generate yield by collecting premium from options buyers who are hedging or speculating. The seller earns premium in exchange for taking on the risk of large price moves. In DeFi, this is implemented through automated on-chain vaults that sell options through protocols like Opyn or Lyra, collect premiums, and distribute yield to depositors.

Charm Finance had previously launched Alpha Vaults for Uniswap v3 concentrated liquidity management — rebalancing LP positions automatically as prices move. Alpha Pro represents an expansion into the options market-making vertical. The permissionless framing means anyone can deposit without KYC or whitelisting, and strategy logic is specified in smart contracts visible on-chain.

## Key points

- Systematic options-selling vault: earns yield by selling strangles/straddles on Ethereum-based options protocols.
- Fully on-chain execution — strategy logic in smart contracts, no centralized management.
- Permissionless: no KYC, no whitelist — deposit and earn options-selling premium.
- From Charm Finance, builders of Alpha Vaults (Uniswap v3 LP management).
- Risk: large directional price moves cause significant losses for options sellers — the yield comes with real downside.

[Original](https://medium.com/charmfinance/introducing-alpha-pro-5a11012c48c1)
