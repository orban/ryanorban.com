---
title: "Awesome-MEV: MEV Research Resource List"
date: 2022-09-06
categories:
  - mev
  - ethereum
  - blockchain
  - defi
  - research
description: A curated list of MEV (Maximal Extractable Value) research papers and talks — the definitive reading list for understanding how miners and validators extract value from transaction ordering on Ethereum. MEV is simultaneously a market efficiency mechanism and a form of tax on users.
params:
  source: pinboard
  sourceUrl: https://github.com/0xemperor/Awesome-MEV
---

## Summary

[Awesome-MEV](/notes/awesome-mev/) is a curated GitHub repository collecting MEV (Maximal Extractable Value, formerly Miner Extractable Value) research papers, blog posts, and talks. MEV refers to the profit that block producers (miners, then validators post-Ethereum Merge) can extract by controlling transaction ordering within a block — frontrunning, backrunning, sandwich attacks, and arbitrage.

The canonical paper anchoring the field is Flash Boys 2.0 by Philip Daian et al. (2019), which coined the term "miner extractable value" and showed that Ethereum mempool ordering created a shadow market of gas price bidding (Priority Gas Auctions, or PGAs). Flashbots emerged as the response: a research organization that built MEV-Boost and the Flashbots Auction to democratize MEV access and reduce harmful externalities like failed transaction spam and network instability.

MEV matters beyond DeFi: it's a fundamental property of any blockchain with a public mempool and programmable execution. Transaction ordering is a form of power, and whoever controls ordering can extract rents from users who don't understand or can't avoid it. Sandwich attacks on DEX trades are the most visible user-facing harm — a bot frontruns your swap to move the price, your trade executes at the worse price, and the bot backruns to capture the profit. MEV-aware design (commit-reveal schemes, private mempools, SUAVE) attempts to neutralize this.

## Key points

- MEV = profit from transaction ordering control within a block; affects all Ethereum-based DeFi users.
- Flash Boys 2.0 (Daian et al., 2019) is the foundational paper; coined miner extractable value.
- Common MEV strategies: frontrunning, sandwich attacks, backrunning, liquidation sniping.
- Flashbots created MEV-Boost to route MEV to validators via auctions rather than gas wars.
- User impact: sandwich attacks extract real value from DEX swaps without user consent.
- MEV-aware design patterns (commit-reveal, private mempools, batch auctions) attempt to neutralize it.

[Original](https://github.com/0xemperor/Awesome-MEV)
