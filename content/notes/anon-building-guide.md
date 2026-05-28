---
title: Quick and Dirty Anon Building Guide
date: 2022-02-09
categories:
  - privacy
  - anonymity
  - crypto
  - opsec
  - web3
description: A practical guide to building crypto projects anonymously — covering wallet setup, separate identity compartmentalization, and social media opsec. Reflects the 2021-2022 pattern where many crypto builders went anon to reduce personal legal and regulatory exposure.
params:
  source: pinboard
  sourceUrl: https://hackmd.io/@yBpKEsxORheI8AJoIiZj1Q/BkHtjA1k9
---

![Quick and Dirty Anon Building Guide](/images/notes/anon-building-guide.png)

## Summary

This HackMD guide covers operational security (opsec) for building crypto projects anonymously — a practice that became common in the 2021–2022 DeFi and NFT era. The motivation: regulatory ambiguity around DeFi protocols, DAOs, and token launches meant that publicly identified founders faced personal legal exposure that anonymous builders could avoid. The anon builder became a recognized archetype in the Web3 ecosystem.

The practical guidance follows the core anonymity principle: compartmentalization. Separate wallets for different identities (never mix your personal ETH with your project's treasury), separate devices or VMs for anon work, anon email (ProtonMail) and social accounts (Twitter, Discord), and careful metadata hygiene when publishing code or content. The guide emphasizes that consistency matters — a single slip (signing a transaction from a personal wallet, using your real name once) can permanently link your identities.

This connects to broader privacy thinking: operational security is about reducing the surface area across which an adversary can correlate your identities. The crypto context adds financial stakes — wallet addresses are permanently public on-chain, so anonymity failures are often irreversible. Related concepts: pseudonymity vs true anonymity, zero-knowledge identity, and the right to financial privacy arguments that motivate this work.

## Key points

- Wallet compartmentalization: never mix anon and personal wallets — on-chain transactions are permanently public.
- Separate devices or VMs: prevent browser fingerprinting and cross-account correlation.
- Anon social presence: dedicated Twitter/Discord accounts, no personal details, consistent persona.
- Metadata hygiene: git commits, document metadata, and IP addresses can all leak real identity.
- The tradeoff: anonymity protects from legal risk but reduces credibility and community trust.

[Original](https://hackmd.io/@yBpKEsxORheI8AJoIiZj1Q/BkHtjA1k9)
