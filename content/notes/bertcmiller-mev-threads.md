---
title: "@bertcmiller MEV Threads"
date: 2022-05-17
categories:
  - mev
  - ethereum
  - defi
  - research
  - twitter
description: "@bertcmiller's chronological index of his MEV Twitter threads — the most cited informal resource for understanding MEV strategies, Flashbots, and searcher mechanics. Essential reading for anyone entering the MEV space."
params:
  source: pinboard
  sourceUrl: https://mobile.twitter.com/bertcmiller/status/1402665992422047747
---

![@bertcmiller MEV Threads](/images/notes/bertcmiller-mev-threads.png)

## Summary

bertcmiller (Bert Miller) is a pseudonymous MEV researcher whose Twitter threads became the go-to informal education resource for the Ethereum searcher community in 2021-2022. This tweet is his self-curated index of all MEV threads in chronological order — covering frontrunning, sandwich attacks, generalized frontrunners, Flashbots, and the mechanics of how searcher bots actually work.

The threads filled a gap: academic papers like Flash Boys 2.0 established the theory, and Flashbots docs covered the infrastructure, but nobody had written accessible, practitioner-level explanations of *how* MEV strategies are actually implemented. bertcmiller did that — with code snippets, real on-chain examples, and clear explanations of the mempool dynamics that make each strategy possible. His thread on generalized frontrunning (bots that copy any profitable transaction, not just known patterns) is particularly cited.

The Twitter format meant these threads spread widely in the DeFi community and onboarded many searchers who would otherwise have had to piece together knowledge from Discord and GitHub. Alongside [Awesome-MEV](/notes/awesome-mev/) and the Flashbots documentation, bertcmiller's threads are one of three core entry points into MEV education in this era.

## Key points

- Self-indexed collection of MEV Twitter threads by bertcmiller in chronological order
- Covers: frontrunning, sandwich attacks, generalized frontrunners, arbitrage, Flashbots mechanics
- Practitioner-level detail: mempool monitoring, bundle construction, profitability estimation
- Generalized frontrunning: bots that simulate any incoming transaction and front-run it if profitable — no knowledge of the target protocol needed
- Pairs with [Flashbots docs](/notes/flashbots-docs/) for infrastructure detail and [Awesome-MEV](/notes/awesome-mev/) for research papers
- The MEV community in 2022 was still heavily Twitter-native; threads like these were the primary knowledge diffusion mechanism

[Original](https://mobile.twitter.com/bertcmiller/status/1402665992422047747)
