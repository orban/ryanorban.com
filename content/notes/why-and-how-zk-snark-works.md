---
title: Why and How zk-SNARK Works
date: 2022-07-02
categories:
  - cryptography
  - zero-knowledge-proofs
  - zk-snark
  - blockchain
  - mathematics
  - arxiv
description: Maksym Petkus provides a pedagogical ground-up explanation of zk-SNARKs, answering not just how they work but why each component exists. Structured to build from first principles with no cryptography prerequisites, making it the standard accessible reference for developers wanting to understand the math behind zkEVM and privacy-preserving protocols.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/1906.07221.pdf
---

## Summary

Petkus wrote this 65-page paper as a pedagogical companion to the zk-SNARK literature, which he characterizes as a black box for many. The paper's structure is unusual: rather than presenting the construction and asking readers to trust its properties, it answers *why* each component exists before introducing it. This makes the exposition longer but far more comprehensible for developers and engineers who need to work with zero-knowledge proofs without a background in algebraic geometry or advanced cryptography.

The construction builds from foundational ideas in polynomial commitments and homomorphic encryption through to the full Groth16 and related SNARK constructions. Key concepts covered include arithmetic circuits, rank-1 constraint systems (R1CS), quadratic arithmetic programs (QAP), and how the prover-verifier interaction can be made non-interactive using the Fiat-Shamir heuristic and a common reference string. Each step is motivated by the limitations of the previous construction, so the reader develops intuition for why the complexity is necessary.

Practically, this paper is the standard prerequisite reading for anyone working with Ethereum zkEVM systems, Zcash-style privacy coins, or zk-rollups. Understanding SNARK internals matters because circuit design choices directly affect proof generation time and on-chain verification cost.

## Key Points

- Builds zk-SNARK from first principles: polynomial commitments → arithmetic circuits → R1CS → QAP → full SNARK construction
- Pedagogical emphasis on *why* each step exists, not just how — specifically designed for readers without cryptography prerequisites
- Covers the path from interactive proofs to non-interactive via Fiat-Shamir heuristic and common reference string
- Essential background for working with zkEVM, zk-rollups, Zcash, and other zero-knowledge proof systems
- 65 pages; connects algebraic intuition to practical circuit design tradeoffs in production systems

[Original](https://arxiv.org/abs/1906.07221)
