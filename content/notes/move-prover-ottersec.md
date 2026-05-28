---
title: "The Move Prover: A Practical Guide"
date: 2022-09-16
categories:
  - blockchain
  - formal-verification
  - move-language
  - smart-contracts
  - security
description: OtterSec's practical guide to the Move Prover — a formal verification tool for the Move smart contract language used on Sui and Aptos. Covers writing specifications that the prover can check, bridging the gap between formal methods theory and blockchain developer practice.
params:
  source: pinboard
  sourceUrl: https://osec.io/blog/tutorials/2022-09-16-move-prover/
---

![The Move Prover: A Practical Guide](/images/notes/move-prover-ottersec.png)

## Summary

OtterSec's tutorial on the Move Prover — a formal verification tool built into the Move smart contract language ecosystem. Move is the programming language used by Aptos and Sui, developed from Facebook's Diem blockchain project. The prover allows developers to write mathematical specifications about their contract's behavior and automatically verify that the code satisfies those specifications.

The Move Prover uses SMT solvers (specifically Z3) under the hood to check whether the annotated conditions can be violated. Developers write pre-conditions (what must be true before a function runs), post-conditions (what must be true after), and invariants (what must always hold). The prover then checks whether any input could produce a state that violates these conditions.

Formal verification in smart contracts is highly motivated: a bug in a contract can result in irreversible fund loss. Tools like Certora Prover (for Solidity) and the Move Prover represent the frontier of practical formal verification for blockchain code. The challenge is annotation burden — writing correct specs is itself hard, and specs that are too weak don't catch real bugs.

## Key points

- Move Prover does formal verification of Move smart contracts via SMT solvers (Z3).
- Developers annotate functions with pre-conditions, post-conditions, and invariants.
- Prover checks whether any execution path violates the specifications.
- Move language used on Aptos and Sui (derived from Facebook's Diem project).
- Reduces smart contract bugs with mathematical guarantees rather than just testing.
- Tutorial by OtterSec, a blockchain security firm specializing in smart contract audits.

[Original](https://osec.io/blog/tutorials/2022-09-16-move-prover/)
