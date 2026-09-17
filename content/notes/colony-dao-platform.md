---
title: Colony — Decentralized Organization Platform
date: 2022-01-06
categories:
  - dao
  - web3
  - governance
  - organizations
  - tools
description: Colony is a DAO platform focused on decentralized organizations — structured around teams, tasks, and reputation rather than pure token voting. An alternative DAO framework that tries to capture work contribution as a governance signal.
params:
  source: pinboard
  sourceUrl: https://colony.io/product
---

## Summary

Colony is a DAO platform and framework with a distinctive design philosophy: instead of pure token voting governance, it structures organizations around teams, domains, tasks, and reputation earned through contribution. The core insight is that governance tokens alone create plutocracy — whale wallets control outcomes regardless of who actually does the work. Colony's reputation system tries to weight governance influence by demonstrated contribution over time.

The technical architecture uses a domain/subdomain structure similar to how companies have departments, each with their own budget and governance. Reputation is earned by completing tasks and rated by other contributors; it decays over time so participation must be ongoing to maintain influence. Funding proposals and decisions flow through these reputation-weighted domains rather than a single flat governance pool.

This places Colony in a different design cluster than Aragon (which provides general-purpose governance infrastructure) or Snapshot (off-chain signaling). Colony is opinionated about *how* DAOs should be structured — toward meritocracy and contribution rather than capital. The tension between reputation systems and token systems is real: reputation is hard to transfer or commodify, which is both a feature (sybil resistance) and a limitation (less liquid, harder to bootstrap).

## Key points

- Reputation-weighted governance: governance influence earned through work, not just token holdings
- Domain/subdomain structure: organizations divided into teams, each with budget and local governance
- Reputation decays over time — ongoing participation required to maintain influence, not one-time token purchase
- Contrasts with Snapshot (off-chain signaling) and Compound Governor (pure on-chain token voting)
- Addresses plutocracy concern: in pure token voting, large holders can override community contributor preferences

[Original](https://colony.io/product)
