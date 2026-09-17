---
title: Proofs, Arguments, and Zero-Knowledge
date: 2022-05-30
categories:
  - zero-knowledge-proofs
  - cryptography
  - snarks
  - interactive-proofs
  - textbook
description: ""
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/ProofsArgsAndZK.pdf
---

## Summary

*Proofs, Arguments, and Zero-Knowledge* by Justin Thaler (Georgetown University) is the standard graduate-level textbook for interactive proof systems, argument systems, and zero-knowledge proofs. It is freely available and has become the canonical reference for anyone entering the ZK ecosystem from a theoretical computer science background. The book covers the material that practitioners working on SNARKs and STARKs need to understand — not just how to use the tools, but why they work.

The book is organized around proof complexity. It starts with interactive proofs and the sumcheck protocol — the workhorse underlying a surprising number of modern SNARK constructions. The sumcheck protocol lets a prover convince a verifier that the sum of a multivariate polynomial over a boolean hypercube equals a claimed value, using only logarithmic rounds of communication. From there, Thaler builds up to polynomial commitment schemes, IP and MIP* complexity classes, and the construction of efficient argument systems including Groth16, PLONK, and FRI-based systems.

The MoonMath Manual (at `inbox/2022-10-25-moonmath-manual-zero-knowledge.md`) covers similar territory but at a more accessible level, while Thaler's book goes deeper into proof complexity and provides the theoretical foundations for why specific constructions achieve their claimed security and efficiency properties. For the zkEVM context covered in `inbox/2022-02-08-zksync-zkevm-explainer.md`, this textbook is the theoretical underpinning — ZK-SNARK and ZK-STARK constructions used in rollups all derive from the material here.

## Key points

- Covers interactive proofs, sumcheck protocol, argument systems, SNARKs, STARKs, and zero-knowledge proofs from first principles
- Sumcheck protocol is the core primitive — understanding it unlocks most modern SNARK constructions
- Treatment of polynomial commitment schemes (KZG, FRI) explains the efficiency differences between SNARK families
- Groth16, PLONK, and FRI-based proof systems all derived from principles developed in this book
- Freely available; Justin Thaler maintains the latest version — it has become the standard reference for ZK protocol designers
- Pairs well with MoonMath Manual (more accessible) and ZK Zero to Hero curriculum for a complete self-study path

[Source PDF](file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/ProofsArgsAndZK.pdf)
