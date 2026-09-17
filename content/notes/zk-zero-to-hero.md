---
title: "ZK: Zero to Hero"
date: 2022-06-19
categories:
  - zero-knowledge
  - cryptography
  - ethereum
  - education
  - zk-proofs
description: A curated learning path for understanding zero-knowledge proofs from scratch — covering the math foundations, SNARK/STARK constructions, and practical applications in blockchain. One of the more organized community-built ZK curricula from 2022.
params:
  source: pinboard
  sourceUrl: https://steelperlot.notion.site/steelperlot/ZK-Zero-to-Hero-1157a665a4a249d9805aebd5efea6460
---

## Summary

[ZK: Zero to Hero](/notes/zk-zero-to-hero/) is a community-built learning path hosted on Notion by Steelperlot, designed to take someone from no background in cryptography to a working understanding of zero-knowledge proofs and their applications in blockchain systems. In 2022, ZK knowledge was concentrated in a small group of cryptographers and researchers — the broader developer community found the math barrier steep and the existing resources scattered. Curricula like this one tried to fix that.

The learning path covers the conceptual foundations first: what does it mean to *prove* something without revealing the underlying witness? The classic example is graph 3-coloring — you can prove you have a valid coloring without revealing which color goes where. From there, it builds toward practical constructions: SNARKs (Succinct Non-Interactive Arguments of Knowledge) and STARKs (Scalable Transparent Arguments of Knowledge), the two dominant proof systems in the Ethereum ecosystem. SNARKs (like Groth16, PLONK) require a trusted setup but are compact; STARKs don't require trust but produce larger proofs.

The applied section covers ZK-rollups — how zkSync, StarkNet, and Polygon zkEVM use ZK proofs to batch transactions and post a single proof to Ethereum mainnet rather than all transaction data. This is the dominant use case driving ZK development: proving correct execution of an off-chain computation on-chain, enabling Ethereum to scale without sacrificing security.

## Key points

- Structured learning path: cryptography foundations → SNARKs/STARKs constructions → ZK-rollup applications
- SNARKs (Groth16, PLONK): compact proofs, require trusted setup ceremony — dominant in DeFi privacy tools
- STARKs (FRI protocol): no trusted setup, quantum-resistant, larger proofs — used by StarkNet and StarkEx
- ZK-rollups are the primary commercial application: batch prove execution, post proof to Ethereum for cheap on-chain verification
- Prerequisite math: finite fields, elliptic curve cryptography, polynomial commitments — the guide introduces these
- Pairs with [Espresso Systems](/notes/espresso-systems/) (shared sequencing + ZK privacy) and [Ethereum L2 notes](/notes/ethereum-l2-notes/) for applied context

[Original](https://steelperlot.notion.site/steelperlot/ZK-Zero-to-Hero-1157a665a4a249d9805aebd5efea6460)
