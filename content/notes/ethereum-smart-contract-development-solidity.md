---
title: Ethereum Smart Contract Development in Solidity
date: 2022-06-17
categories:
  - ethereum
  - solidity
  - smart-contracts
  - blockchain
  - web3
description: Zheng, Gao, Huang, and Guan (Springer 2021) provide a comprehensive textbook on developing Ethereum smart contracts in Solidity, covering the EVM, contract patterns, security vulnerabilities, and real-world DApp development. A practical reference for anyone building on Ethereum.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/Gavin Zheng, Longxiang Gao, Liqun Huang, Jian Guan - Ethereum Smart Contract Development in Solidity-Springer Singapore_Springer (2021).pdf
---

## Summary

Gavin Zheng, Longxiang Gao, Liqun Huang, and Jian Guan (Springer Singapore 2021) provide a comprehensive textbook on developing smart contracts on Ethereum using the Solidity programming language. The book is organized around three tiers: understanding the underlying Ethereum Virtual Machine (EVM) and blockchain mechanics, writing and testing Solidity contracts, and building full decentralized applications (DApps) that integrate front-end web interfaces with on-chain logic.

The EVM section covers how Ethereum processes transactions, how gas pricing works as a resource accounting mechanism, and the lifecycle of a contract from source code through bytecode compilation to on-chain deployment. Solidity is presented as a statically typed, contract-oriented language with constructs borrowed from JavaScript and Python but with semantic differences critical for blockchain contexts: all state changes are permanent, execution is public and auditable, and reentrancy and integer overflow are genuine security risks rather than theoretical concerns.

A substantial portion covers smart contract security — the unique vulnerability classes that arise from the EVM's execution model. Reentrancy attacks (as demonstrated in the DAO hack), integer overflow and underflow, front-running, and timestamp dependence all receive dedicated treatment with code examples. The book also covers the OpenZeppelin contract library as the standard safe baseline implementation of token standards (ERC-20, ERC-721), access control, and upgradeable contract patterns. DApp development chapters cover interaction via Web3.js and ethers.js, connecting MetaMask, and deploying on testnets before mainnet.

## Key points

- Ethereum Virtual Machine (EVM): deterministic bytecode-executing environment; all state transitions are permanent and globally auditable.
- Solidity language: statically typed, contract-oriented; differs from web languages in that every computation costs gas and state changes are irreversible.
- Core security vulnerabilities: reentrancy attack, integer overflow/underflow, front-running, timestamp dependence — each with EVM-specific root causes.
- OpenZeppelin contracts: the standard audited implementation of ERC-20 (fungible tokens), ERC-721 (NFTs), access control, and upgradeable proxies.
- DApp architecture: Solidity contracts on-chain + Web3.js or ethers.js front-end + MetaMask wallet integration.
- Testing via Truffle / Hardhat frameworks; testnet deployment before mainnet.

[Original PDF](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/Gavin%20Zheng%2C%20Longxiang%20Gao%2C%20Liqun%20Huang%2C%20Jian%20Guan%20-%20Ethereum%20Smart%20Contract%20Development%20in%20Solidity-Springer%20Singapore_Springer%20%282021%29.pdf)
