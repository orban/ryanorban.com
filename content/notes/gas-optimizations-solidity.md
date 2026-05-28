---
title: Gas Optimizations for the Rest of Us
date: 2022-03-23
categories:
  - ethereum
  - solidity
  - smart-contracts
  - gas-optimization
  - web3
description: Miguel Piedrafita's practical guide to Solidity gas optimization — covers storage layout, calldata vs memory, packing structs, unchecked arithmetic, and other EVM-specific tricks that reduce transaction costs. Written for regular developers, not EVM experts.
params:
  source: pinboard
  sourceUrl: https://m1guelpf.blog/d0gBiaUn48Odg8G2rhs3xLIjaL8MfrWReFkjg8TmDoM
---

![Gas Optimizations for the Rest of Us](/images/notes/gas-optimizations-solidity.png)

## Summary

Miguel Piedrafita (m1guelpf) wrote this as a practical Solidity gas optimization guide for developers who aren't EVM internals experts. Gas costs are a critical concern in Ethereum smart contract development: every computation costs gas, which users pay in ETH. Inefficient contracts are expensive to interact with, which reduces adoption. The guide covers the high-leverage optimizations that don't require deep EVM knowledge.

The biggest wins come from storage — the most expensive operation in the EVM. Reading a cold storage slot costs 2100 gas; writing costs 20,000 gas. The practical implications: cache storage reads in memory variables when you're reading the same slot multiple times, pack multiple small values into a single 32-byte storage slot (since the EVM operates on 32-byte words), and avoid unnecessary state writes. Struct packing is especially impactful — a struct with `uint128` + `bool` + `uint128` packs into one slot; putting them in order `uint128` + `uint256` + `bool` wastes two slots.

calldata vs memory is another significant optimization: function arguments declared as `calldata` avoid copying the data to memory, which saves gas. `unchecked` arithmetic blocks (available since Solidity 0.8) skip overflow/underflow checks when you've already proven the math is safe. Emitting events instead of storing data on-chain is dramatically cheaper when you only need the data for off-chain indexing. The guide also covers using `custom errors` instead of string reverts (strings are expensive to store and emit).

## Key points

- EVM storage is the most expensive operation: minimize reads/writes, cache in memory, use `immutable` for deployment-time constants.
- Struct packing: order variables by size to pack them into fewer 32-byte storage slots — the EVM's word size.
- `calldata` function parameters avoid memory copy; prefer it over `memory` for read-only array arguments.
- `unchecked` blocks for arithmetic where overflow is provably impossible — saves the overflow check gas.
- Custom `error` types (Solidity 0.8+) are cheaper than string `revert` messages.
- Events cost ~375 gas + 8 gas/byte; storage writes cost 20,000 gas — use events for off-chain-only data.

[Original](https://m1guelpf.blog/d0gBiaUn48Odg8G2rhs3xLIjaL8MfrWReFkjg8TmDoM)
