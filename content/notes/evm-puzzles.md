---
title: "EVM Puzzles: Solutions Walkthrough"
date: 2022-06-27
categories:
  - ethereum
  - evm
  - smart-contracts
  - security
  - education
description: Solutions walkthrough for EVM Puzzles — a set of interactive challenges that teach the Ethereum Virtual Machine by requiring you to craft calldata or value that makes specific bytecode sequences succeed. Effective hands-on EVM education for smart contract developers.
params:
  source: pinboard
  sourceUrl: https://skogen27.medium.com/evm-puzzles-solutions-80696361b5b6
---

## Summary

[EVM Puzzles](/notes/evm-puzzles/) is a learning project by fvictorio where each puzzle presents raw EVM bytecode and challenges you to construct the calldata, value, or other inputs that make the contract succeed (reach the STOP opcode without reverting). This walkthrough by Skogen explains the solution to each puzzle.

The EVM (Ethereum Virtual Machine) executes opcodes on a stack-based architecture. Understanding opcodes directly — `CALLDATALOAD`, `CALLDATASIZE`, `JUMPI`, `SSTORE`, `CALLER`, `CALLVALUE` — matters for Solidity developers who want to understand what the compiler emits, for security researchers auditing contract bytecode, and for anyone building tooling at the assembly level.

Each puzzle teaches a specific EVM mechanic: puzzle 1 might require sending the right amount of ETH to pass a `CALLVALUE` comparison; another might require crafting calldata whose size equals a specific constant; another might demonstrate how JUMP and JUMPI work for conditional control flow. Working through them builds the kind of low-level EVM fluency that's hard to get from Solidity documentation alone.

By 2022, EVM bytecode literacy was increasingly important for the smart contract security field. Automated tools like Slither and Mythril helped, but manual bytecode analysis remained essential for finding subtle bugs and understanding novel attack vectors. The puzzles are a gentler entry point than jumping straight into Ethernaut or real audit work.

## Key points

- [EVM Puzzles](/notes/evm-puzzles/) are interactive bytecode challenges requiring you to craft inputs that satisfy specific opcode sequences
- Each puzzle isolates one EVM mechanic: value checks, calldata inspection, jump conditions, storage patterns
- EVM is a stack machine: operations push/pop values, with `PUSH1`, `DUP`, `SWAP`, `ADD`, etc. as the basic vocabulary
- Complements higher-level resources: use after Mastering Ethereum bytecode chapter, before real smart contract security audit practice
- Companion to Ethernaut (OpenZeppelin's gamified challenge series) for building security-oriented EVM intuition

[Original](https://skogen27.medium.com/evm-puzzles-solutions-80696361b5b6)
