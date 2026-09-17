---
title: Flashbots Documentation
date: 2022-05-17
categories:
  - mev
  - ethereum
  - flashbots
  - blockchain
  - defi
description: The official Flashbots documentation covering MEV-Geth, the Flashbots auction, searcher bundle submission, and the broader philosophy behind transparent MEV extraction. The canonical reference for anyone building MEV searchers or integrating with Flashbots infrastructure.
params:
  source: pinboard
  sourceUrl: https://docs.flashbots.net/
---

![Flashbots Documentation](/images/notes/flashbots-docs.png)

## Summary

Flashbots is the organization that built the dominant MEV infrastructure for Ethereum — starting with MEV-Geth (a modified Ethereum client) and evolving into the Flashbots Auction, MEV-Boost, and ultimately SUAVE. The documentation covers the full stack: how searcher bots submit transaction bundles, how builders assemble those bundles into blocks, and how validators select the most profitable block via MEV-Boost.

The core insight behind Flashbots was that MEV was happening anyway — bots were competing via Priority Gas Auctions (PGA), causing failed transactions, gas spikes, and chain congestion as a negative externality on all users. Rather than trying to eliminate MEV, Flashbots gave it a structured channel: bundles submitted privately to builders, no failed transactions in the mempool, reduced gas price wars. The trade-off is centralization risk — a large fraction of Ethereum blocks now flow through Flashbots infrastructure.

The documentation is the entry point for MEV searchers: how to construct an `eth_sendBundle` RPC call, how bundles are atomically included (all or nothing), how to target a specific block number, and how to use simulations to test bundle profitability before submission. The architecture evolved significantly between the Proof of Work era (MEV-Geth) and Proof of Stake era (MEV-Boost with proposer-builder separation).

## Key points

- Flashbots Auction: searchers submit bundles to builders, builders construct blocks, validators select highest-bid block via MEV-Boost
- Proposer-builder separation (PBS): validators propose but don't build blocks — reduces validator-side MEV extraction
- `eth_sendBundle`: the core RPC call; bundles are atomic (all included or none), can target a specific block number
- Private mempool: bundles never appear in the public mempool, eliminating the frontrunning that happens with public transactions
- The SUAVE project (Single Unifying Auction for Value Expression) is Flashbots' next chapter — a decentralized block building network
- Related: [Awesome-MEV](/notes/awesome-mev/), [Dogetoshi MEV](/notes/dogetoshi-mev/), [EigenPhi](/notes/eigenphi/) for monitoring MEV activity

[Original](https://docs.flashbots.net/)
