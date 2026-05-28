---
title: "Exploring Zero Knowledge: zkSync and the zkEVM"
date: 2022-02-08
categories:
  - ethereum
  - zero-knowledge
  - layer-2
  - zksync
  - scaling
description: An explainer on zkSync and the zkEVM — how zero-knowledge proofs enable EVM-compatible rollups that give instant finality without trusting the operator. Written in early 2022 as zkEVM was the most technically ambitious open problem in Ethereum scaling.
params:
  source: pinboard
  sourceUrl: https://pseudotheos.mirror.xyz/JF8_qjziArLgVPhC0ADl_Adz9PRRSEURb7vGLR9_9AE
---

![Exploring Zero Knowledge: zkSync and the zkEVM](/images/notes/zksync-zkevm-explainer.png)

## Summary

This pseudotheos article (published on Mirror) provides a technical introduction to zkSync and the zkEVM concept — the application of zero-knowledge proofs to create an Ethereum-compatible ZK rollup. Written in early 2022, this was a particularly active research area: Optimistic rollups (Arbitrum, Optimism) were live and capturing TVL, but ZK rollups were considered technically superior because they provide cryptographic validity proofs rather than depending on fraud challenges.

The core challenge explained: standard ZK-SNARK / ZK-STARK systems prove specific circuits efficiently, but the EVM is a general-purpose state machine with 140+ opcodes. Building a circuit that can prove arbitrary EVM execution is dramatically harder than proving fixed computations (like a token transfer). The zkEVM project (and zkSync Era, Scroll, Polygon zkEVM) is the multi-year effort to solve this.

The article situates zkSync (by Matter Labs) within the broader Layer 2 ecosystem and explains why the zkEVM approach matters for DeFi: existing Solidity contracts could deploy without modification, unlike earlier ZK rollup approaches that required custom languages or limited computation. By 2023 multiple zkEVM implementations launched mainnet, validating the approach laid out in this 2022 analysis.

## Key points

- ZK rollup vs Optimistic rollup: ZK provides cryptographic validity proofs; Optimistic relies on fraud windows.
- zkEVM challenge: proving arbitrary EVM execution requires a circuit for every opcode — enormous engineering effort.
- zkSync Era (Matter Labs), Scroll, and Polygon zkEVM are the main zkEVM implementations.
- Instant finality: ZK rollup withdrawals don't need the 7-day challenge period Optimistic rollups require.
- zero-knowledge proofs enable trustless verification — you don't need to trust the rollup operator.

[Original](https://pseudotheos.mirror.xyz/JF8_qjziArLgVPhC0ADl_Adz9PRRSEURb7vGLR9_9AE)
