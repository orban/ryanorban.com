---
title: Jito MEV Dashboard
date: 2022-08-12
categories:
  - mev
  - solana
  - blockchain
  - defi
  - jito
description: Jito's public MEV dashboard tracking Maximal Extractable Value on Solana — validator tips, arbitrage volumes, and extraction rates. One of the first transparent MEV tracking tools for Solana, predating Jito's later block engine infrastructure.
params:
  source: pinboard
  sourceUrl: https://jito.retool.com/embedded/public/7e37389a-c991-4fb3-a3cd-b387859c7da1
---

![Jito MEV Dashboard](/images/notes/jito-mev-dashboard.png)

## Summary

Jito is a Solana-focused infrastructure project building tools around MEV (Maximal Extractable Value) — the profit validators and block producers can extract by reordering, inserting, or excluding transactions. The Retool-based public dashboard tracks MEV activity on Solana, showing metrics like validator tips, arbitrage volumes, and MEV extraction rates over time.

MEV was a major topic in 2022 blockchain circles. On Ethereum, MEV research had produced Flashbots and an ecosystem of searchers, builders, and validators competing for extractable value. Solana's architecture is different — its high-throughput, short block times, and Proof of History ordering create distinct MEV opportunities — and Jito emerged to study and monetize this.

The public dashboard represents a transparency move: rather than MEV being purely opaque, Jito made extraction data visible. This matters for DeFi users (often the victim of MEV extraction via sandwich attacks and arbitrage) and for understanding the health of the Solana ecosystem. Jito later built a block engine and bundle infrastructure that became a significant part of Solana's transaction ordering stack.

## Key points

- Tracks MEV on Solana — validator tips, arbitrage volumes, extraction rates over time.
- Built by Jito, which later became a major Solana MEV infrastructure provider.
- Retool-based public dashboard — transparency move in the typically opaque MEV space.
- MEV on Solana differs from Ethereum: high throughput and Proof of History create unique extraction patterns.
- 2022 context: Flashbots had mapped Ethereum MEV; Solana was the next frontier.
- Jito evolved from tracking MEV to building the block engine and bundle infrastructure.

[Original](https://jito.retool.com/embedded/public/7e37389a-c991-4fb3-a3cd-b387859c7da1)
