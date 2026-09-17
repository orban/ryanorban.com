---
title: EVM EIPs and Hard Forks Reference
date: 2022-06-12
categories:
  - ethereum
  - evm
  - smart-contracts
  - security
  - eips
description: Trail of Bits' learning resource mapping Ethereum EIPs to the hard forks that introduced them — essential context for auditors and developers who need to know which EVM opcodes and behaviors are available at different protocol versions. Part of the building-secure-contracts curriculum.
params:
  source: pinboard
  sourceUrl: https://github.com/crytic/building-secure-contracts/blob/master/learn_evm/eips_forks.md
---

## Summary

This document, part of Trail of Bits' building-secure-contracts curriculum hosted on GitHub, maps Ethereum Improvement Proposals (EIPs) to the hard forks that activated them. It's a reference for EVM developers and auditors who need to know: "at which protocol version was opcode X introduced, and what changed in fork Y?"

The EVM is not static. Each Ethereum hard fork (Homestead, Byzantium, Constantinople, Istanbul, Berlin, London, Shanghai) introduced new opcodes, changed gas costs, and modified behaviors that smart contracts can depend on. For auditors, this matters because a contract deployed before EIP-1559 (London fork) behaves differently with respect to gas than one written after — and a contract that checks `block.basefee` requires London or later. For security analysis, knowing which fork introduced EIP-1884 (gas cost repricing) or EIP-2929 (cold/warm storage access costs) is necessary to understand whether an exploit path was available at a given point in time.

The building-secure-contracts curriculum from Trail of Bits is a broader attempt to systematize smart contract security knowledge — covering the EVM internals, common vulnerability patterns, testing with Echidna and Manticore, and writing secure Solidity. The EIPs/forks reference is the foundational layer: before understanding what can go wrong, you need to understand what the VM actually does.

## Key points

- Maps each major EIP to its activating hard fork — a reference table for auditors and EVM engineers
- Key security-relevant forks: London (EIP-1559, base fee), Berlin (EIP-2929 storage gas repricing), Istanbul (EIP-1884 opcode repricing)
- EIP-2929 changed cold/warm storage access costs, breaking some gas-sensitive reentrancy guards
- Part of Trail of Bits' building-secure-contracts curriculum — covers EVM internals, vulnerability patterns, Echidna/Manticore
- Ethereum's upgrade mechanism requires tracking protocol version alongside contract code for correct security analysis
- Companion reference: the Yellow Paper for formal EVM semantics; evm.codes for interactive opcode reference

[Original](https://github.com/crytic/building-secure-contracts/blob/master/learn_evm/eips_forks.md)
