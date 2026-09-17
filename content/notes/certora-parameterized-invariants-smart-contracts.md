---
title: Finding Bugs Automatically in Smart Contracts with Parameterized Invariants
date: 2022-07-15
categories:
  - formal-verification
  - smart-contracts
  - blockchain
  - security
  - specification
description: A 2020 WIP paper from Certora describing a framework of reusable parameterized invariants for automatically finding bugs in smart contracts, with the Certora Prover discovering two real bugs in MakerDAO's Multi-Collateral Dai. The core insight is that the hardest problem in formal verification is specification, and smart contracts are unusually amenable to shared invariants — enabling a community network effect.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/sbc2020.pdf
---

## Summary

This WIP paper from Certora (Bernardi, Dor, Fedotov, Grossman, and colleagues from Tel Aviv University, MIT, and UMass) argues that formal verification of smart contracts is more tractable than commonly believed — not because verification is easy, but because specification can be shared. The key observation: the same correctness invariants apply across many different smart contract implementations and platforms, creating a potential network effect where verification costs drop as the community's repertoire of reusable specs grows.

The paper proposes formalizing smart contract correctness using parameterized Hoare triples — a variant of Hoare logic where the invariant properties are parameterized over abstract functions (like `totalSupply()` or `balanceOf()`), making them robust to differences between implementations. Five canonical invariants are proposed: Bounded Supply (no infinite minting), Aggregated Ledger Integrity (aggregate values stay consistent), Authorized Operations (privileged actions require authorization), Proportional Token Distribution (exchange fairness), and Robustness (small inputs produce small output changes). These are formalized using Cartesian Hoare Logic for the two-trace Robustness property.

The paper grounds these abstractions in two real bugs found in MakerDAO's Multi-Collateral Dai (MCD) test version using the Certora Prover. In the first, a flaw in the Flopper auction contract allows the total token supply to reach 2²⁵⁶ — a clear Bounded Supply violation. In the second, the Flapper auction's `kick` function fails to transfer the initial bid amount to the auction contract, violating Aggregated Ledger Integrity. Both bugs were confirmed by the Maker team. The Certora Prover also verified invariants for Compound Finance and Celo with termination times between 15 minutes and 5 hours.

## Key points

- The hardest problem in formal verification isn't the verification itself — it's writing the specification. Most deployed smart contracts have no formal spec at all, making automated verification impossible.
- Parameterized invariants act as a shared vocabulary: one invariant like Bounded Supply can be instantiated across hundreds of different ERC20 token contracts, each with different implementations of `totalSupply()`.
- The Certora Prover found that 8 out of 24 ERC20 tokens violated Bounded Supply — 6 because they relied on out-of-band constraints on minting that couldn't be expressed on-chain.
- The Aggregated Ledger Integrity bug in MakerDAO MCD also showed up as an Authorized Operations violation — illustrating how higher-level invariants can expose bugs that function-level checks would miss.
- Applied to Compound Finance, MakerDAO, and Celo: the prover terminated with decisive answers (no inconclusives) in all cases, suggesting the domain is tractable for SMT solver-based reasoning.
- Contrast with Move Prover and Clockwork Finance Framework approaches: Certora's approach targets Solidity on Ethereum and is property-specific rather than exhaustive, which makes it fast in practice.

[Original (sbc2020.pdf)](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/sbc2020.pdf)
