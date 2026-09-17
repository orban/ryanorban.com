---
title: Notes on Ethereum L2 Solutions
date: 2022-06-27
categories:
  - ethereum
  - layer-2
  - rollups
  - blockchain
  - scaling
description: Jin's 2021 notes on Ethereum L2 scaling solutions — covering optimistic rollups, ZK-rollups, state channels, and plasma. A solid survey of the L2 design space written before rollups became the dominant paradigm.
params:
  source: pinboard
  sourceUrl: https://jinsnotes.com/2021-03-22-ethereum-l2
---

## Summary

Jin's technical notes from March 2021 survey the Ethereum layer-2 scaling landscape, written at a pivotal moment: Optimistic rollups were just launching (Optimism in Jan 2021, Arbitrum in May 2021), and ZK-rollups were still largely theoretical for general-purpose computation. The notes capture the design space when it was still being actively contested.

The taxonomy at the time: payment channels and state channels (Lightning Network style, later Raiden) for off-chain bilateral interactions; Plasma for batched off-chain state secured by fraud proofs; optimistic rollups for general EVM execution with a fraud proof window; and ZK-rollups for math-verified state transitions. Each has a different tradeoff profile between data availability, latency, and EVM compatibility.

Optimistic rollups won the near-term race for general-purpose scaling because they could run existing Solidity contracts without modification — Arbitrum Nitro and Optimism both achieved this. ZK-rollups (zkSync, Polygon zkEVM, StarkNet) took longer due to the complexity of building a ZK proof system for the full EVM opcode set. The hierarchy that the notes sketch — rollup data goes to L1 for security, execution happens off-chain — is exactly the architecture that shipped.

## Key points

- Optimistic rollups: assume transactions are valid, allow 7-day fraud proof window for challenges — enables EVM compatibility but creates withdrawal delays
- ZK-rollups: generate validity proofs that prove correct execution cryptographically — instant finality but complex to build EVM-compatible
- Plasma: earlier L2 approach with limited data availability guarantees; largely superseded by rollups
- State channels: bilateral off-chain agreements for high-frequency interactions; limited generality
- The notes pre-date EIP-4844 (proto-danksharding) which later dramatically reduced rollup data costs

[Original](https://jinsnotes.com/2021-03-22-ethereum-l2)
