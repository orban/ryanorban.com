---
title: Foundry Template for Solidity Smart Contracts
date: 2022-10-31
categories:
  - solidity
  - ethereum
  - smart-contracts
  - foundry
  - open-source
  - developer-tools
description: A production-ready Foundry project template for Solidity smart contract development — opinionated defaults for testing, linting, and CI. Foundry replaced Hardhat as the preferred Solidity toolchain for many developers around 2022.
params:
  source: pinboard
  sourceUrl: https://github.com/paulrberg/foundry-template
---

## Summary

This is Paul Rberg's Foundry-based template for developing Solidity smart contracts — a preconfigured project setup with sensible defaults for testing, linting, CI, and deployment. Foundry (by Paradigm) emerged as the primary alternative to Hardhat for Ethereum smart contract development: written in Rust, significantly faster for compilation and test execution, and using Solidity for tests rather than requiring JavaScript.

The template provides: Forge configuration for testing, Solhint for linting, Prettier for formatting, GitHub Actions for CI, and a project structure that follows community conventions. For developers starting a new smart contract project in late 2022, this saved the friction of configuring everything from scratch and codified the patterns that had emerged as best practices in the DeFi and NFT development communities.

Foundry's rise was tied to developer frustration with Hardhat's JavaScript testing layer — writing Solidity tests in Solidity is more natural and faster to iterate on than writing them in JavaScript. The performance advantage was also significant: a test suite that took minutes in Hardhat could run in seconds in Foundry. Paul Rberg is known for the PRBMath Solidity fixed-point arithmetic library; his templates tend to be well-structured.

## Key points

- Foundry-based Solidity project template — preconfigured testing, linting, CI defaults.
- Foundry by Paradigm: Rust-based toolchain, Solidity-native testing, significantly faster than Hardhat.
- The key Foundry advantage: write Forge tests in Solidity rather than JavaScript.
- By Paul Rberg, known for PRBMath and well-regarded Solidity library work.
- Codifies late-2022 best practices for Ethereum smart contract project structure.
- Part of the broader shift from Hardhat to Foundry in the Ethereum developer community.

[Original](https://github.com/paulrberg/foundry-template) → GitHub
