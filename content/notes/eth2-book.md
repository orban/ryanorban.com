---
title: The Eth2 Book
date: 2022-03-12
categories:
  - ethereum
  - blockchain
  - proof-of-stake
  - education
  - books
description: An online book covering Ethereum 2.0 — the move from proof-of-work to proof-of-stake via the Beacon Chain. Written in early 2022 as The Merge was approaching, providing technical depth on Casper FFG, attestations, and validator mechanics.
params:
  source: pinboard
  sourceUrl: https://eth2.incessant.ink/book/00__introduction/00__forward.html
---

## Summary

An online book documenting Ethereum 2.0 — the upgrade path from proof-of-work Ethereum to the proof-of-stake system called the Beacon Chain. Published at `eth2.incessant.ink`, the book was written as The Merge was approaching in 2022, offering technical depth for readers who wanted to understand what Eth2 actually was, mechanically, rather than just its marketing.

The forward covers the motivation: proof-of-work consumes massive energy to achieve security through computational cost, while proof-of-stake secures the network by having validators put up ETH as collateral that can be slashed (destroyed) for malicious behavior. The energy argument was significant — Ethereum's proof-of-work was estimated to consume as much electricity as some small countries before The Merge completed in September 2022.

The book likely covers Casper FFG (the finality gadget), LMD-GHOST (the fork choice rule), attestations (validators voting on the head of the chain), committees, and the validator lifecycle. These mechanics are more complex than Bitcoin's proof-of-work: rather than a single miner finding a block, Eth2 uses committees of validators who must attest to blocks, with economic penalties for equivocation and inactivity.

The 2022 timing matters as context: when this was saved, The Merge hadn't happened yet and there was genuine uncertainty about execution. Reading it now, with The Merge having completed successfully, the book is a technical record of how Ethereum engineering approached one of the most complex live system upgrades in blockchain history.

## Key points

- Technical documentation of Ethereum 2.0 / Beacon Chain mechanics, written pre-The Merge.
- Proof-of-stake security model: validators stake ETH as collateral, slashing replaces proof-of-work's energy cost.
- Covers Casper FFG finality, LMD-GHOST fork choice, attestations, and validator lifecycle.
- The Merge (September 2022) successfully completed — this book documents the design as it was being built.
- Energy comparison: proof-of-work Ethereum used ~100 TWh/year; proof-of-stake reduced this by ~99.95%.

[Original](https://eth2.incessant.ink/book/00__introduction/00__forward.html)
