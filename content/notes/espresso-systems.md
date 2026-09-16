---
title: "Espresso Systems: Shared Sequencing and Privacy for L2 Rollups"
date: 2022-07-09
categories:
  - ethereum
  - layer-2
  - zero-knowledge
  - privacy
  - blockchain
description: Espresso Systems is building shared sequencing and privacy infrastructure for Ethereum L2 rollups — a sequencer marketplace that multiple rollups can use to get MEV protection, fast finality, and cross-rollup atomicity. Positioned at the intersection of rollup scaling and the decentralized sequencer problem.
params:
  source: pinboard
  sourceUrl: https://www.espressosys.com/about
---

## Summary

[Espresso Systems](/notes/espresso-systems/) is an Ethereum infrastructure company working on the sequencing layer for rollups — the part of a rollup that orders transactions before they're batched and settled on Ethereum mainnet. Most rollups in 2022 (including Arbitrum and Optimism) used a single centralized sequencer operated by the rollup team. This creates risks: the sequencer can censor transactions, extract MEV, and represents a single point of failure.

Espresso's approach is a shared, decentralized sequencer marketplace. Instead of each rollup running its own sequencer, multiple rollups can use Espresso's sequencer network, which uses a BFT consensus protocol (HotShot, their custom variant) to provide ordering with fast finality. The key benefits: MEV protection through fair ordering, cross-rollup atomicity (atomic transactions across rollups sharing the same sequencer), and decentralization that removes the rollup team as the ordering authority.

The privacy piece comes from Configurable Asset Privacy for Ethereum (CAPE) — a system Espresso built using ZK-proofs to enable selective disclosure of on-chain data. Users can prove properties about their assets without revealing balances or transaction histories, using Plonk-based zero-knowledge proofs. This combines with sequencing to create a privacy-preserving execution environment for rollup transactions.

## Key points

- Shared sequencer: multiple rollups share a decentralized ordering network instead of each running their own centralized sequencer
- HotShot consensus: Espresso's BFT protocol providing fast finality with cryptographic guarantees
- Cross-rollup atomicity: transactions spanning multiple rollups can be made atomic if they share the same sequencer
- CAPE (Configurable Asset Privacy for Ethereum): ZK-proof-based asset privacy for selective disclosure
- Addresses a real problem in 2022: rollup decentralization was primarily theoretical; sequencers remained centralized long after rollup tech matured

[Original](https://www.espressosys.com/about)
