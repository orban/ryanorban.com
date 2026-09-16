---
title: Ethereum EVM Illustrated
date: 2022-02-16
categories:
  - ethereum
  - evm
  - blockchain
  - smart-contracts
  - architecture
description: A visual primer on the Ethereum Virtual Machine internals — accounts, transactions, message calls, gas, the stack/memory/storage architecture, and Go-Ethereum source code. The best single-document mental model for how the EVM actually works at the bytecode level.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/ethereum_evm_illustrated.pdf
---

## Summary

[Ethereum EVM Illustrated](/notes/ethereum-evm-illustrated/) by Takenobu T. (Rev. 0.01.1, 2018) is a visual walkthrough of the Ethereum Virtual Machine internals — how Ethereum works as a transaction-based state machine, what an account is, how transactions and messages flow, and how the EVM stack executes bytecode. It's structured as annotated diagrams rather than prose, making it unusually effective for building a spatial mental model.

The central framing: Ethereum is a state machine where each block applies a sequence of transactions to transform the world state from $s_t$ to $s_{t+1}$. The world state is a mapping from 160-bit addresses to account states. There are two practical account types: externally owned accounts (EOAs) controlled by private keys, and contract accounts containing EVM code and storage. Transactions either create contracts (passing `init` code) or call existing ones (passing `input data`). Messages are the data-and-value payloads passed between accounts, either triggered by a transaction or by EVM code via the `CALL` instruction.

The EVM architecture is a simple stack machine with 256-bit word size and three storage spaces: a 1024-element stack (volatile), byte-addressable linear memory (volatile), and persistent key-value account storage (256-bit to 256-bit, accessed via `SSTORE`/`SLOAD`). All execution costs gas, denominated in wei; running out of gas throws an exception and reverts state. The document covers the Go-Ethereum (`geth`) implementation directly, showing `StateDB`, `stateObject`, `Stack`, `Memory`, and `Interpreter` structs and key functions like `ApplyTransaction`.

## Key points

- Ethereum as a transaction-based state machine: each block transitions world state via ordered transactions.
- Two account types: EOA (private-key controlled, no code) and contract account (code + storage).
- EVM architecture: 256-bit stack (max 1024 elements), byte-addressable volatile memory, persistent key-value storage.
- Gas enforces execution costs; out-of-gas is an exception that reverts state changes atomically.
- Message calls via `CALL` instruction are depth-limited to 1024; arguments/return values pass through memory.
- EVM is big-endian; `PUSH` instructions are right-aligned. Shift operations use `MUL`/`DIV` (no dedicated shift opcode until later hard forks).
- Go-Ethereum (`geth`) source: `core/vm/interpreter.go` runs the main execution loop; `core/state/statedb.go` manages world state.
- Compilation chain: Solidity / Viper / LLL → compiler → EVM bytecode — the EVM is the runtime target for all smart contract languages.

[Original](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/ethereum_evm_illustrated.pdf)
