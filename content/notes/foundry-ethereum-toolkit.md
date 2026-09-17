---
title: "Foundry: Ethereum Development Toolkit in Rust"
date: 2022-01-18
categories:
  - ethereum
  - smart-contracts
  - rust
  - defi
  - developer-tools
  - solidity
  - testing
description: Foundry is a blazing-fast Ethereum development toolkit written in Rust — Forge for testing, Cast for chain interaction, Anvil for local node, Chisel for REPL. Tests written in Solidity itself, with fuzzing and invariant testing built in. 2-5x faster than Hardhat.
params:
  source: pinboard
  sourceUrl: https://github.com/gakonst/foundry
---

![Foundry: Ethereum Development Toolkit in Rust](/images/notes/foundry-ethereum-toolkit.png)

## Summary

Foundry is an Ethereum smart contract development toolkit written in Rust, built for speed and developer experience. The original repository (`gakonst/foundry`) was by Georgios Konstantopoulos of Paradigm; the project is now maintained at `foundry-rs/foundry`. It replaced Hardhat and Truffle as the default choice for serious Solidity development.

The key insight in Foundry's design is that tests should be written in Solidity, not JavaScript. This eliminates the context switch between the language you're building in and the language you're testing in, and lets test code use all of Solidity's native types and idioms directly. Forge is the test runner; it supports standard unit tests, fuzz testing (random input generation to find edge cases), and invariant testing (asserting properties that must always hold across arbitrary sequences of transactions).

The Rust implementation produces dramatic speed improvements: compilation is 2.1x–5.2x faster than Hardhat, and certain test suites run 147x faster. Anvil provides a local EVM node that can fork mainnet at any block, enabling realistic integration tests against live protocol state. Cast handles command-line chain interaction (call contracts, send transactions, query storage). Chisel is a Solidity REPL for interactive development.

## Key points

- Tests written in Solidity — no JavaScript test context switch; native type system throughout.
- Forge: unit tests + fuzzing (random inputs) + invariant testing (property assertions across arbitrary tx sequences).
- Anvil: local EVM node with mainnet forking — test against live DeFi protocol state.
- Cast: CLI for contract interaction and chain queries; Chisel: interactive Solidity REPL.
- 2-147x faster than Hardhat depending on workload — Rust compilation pipeline vs. JavaScript runtime.
- Standard choice for professional DeFi protocol development as of 2022.

[Original](https://github.com/gakonst/foundry) → GitHub
