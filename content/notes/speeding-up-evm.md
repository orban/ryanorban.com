---
title: Speeding Up the EVM (Flashbots Research)
date: 2022-03-02
categories:
  - ethereum
  - evm
  - performance
  - flashbots
  - blockchain
description: Flashbots research on techniques to speed up the Ethereum Virtual Machine — covering parallelism, caching, and other optimizations to increase throughput beyond the EVM's sequential execution model. Relevant to scaling Ethereum L1 without moving to L2.
params:
  source: pinboard
  sourceUrl: https://writings.flashbots.net/research/speeding-up-evm-part-1/
---

## Summary

A research post from Flashbots on optimizing Ethereum Virtual Machine (EVM) execution performance. The EVM is the computation engine of Ethereum — every smart contract runs on it, and its performance directly constrains how many transactions Ethereum can process per second. The EVM is inherently sequential by design (each transaction may depend on the state changes from the previous one), which makes simple parallelism difficult.

Flashbots is primarily known for MEV (maximal extractable value) research, but their position in the ecosystem — building infrastructure that processes large volumes of transactions — gives them direct incentive to optimize EVM execution. The post likely covers: speculative execution (execute transactions in parallel optimistically, roll back on conflicts), caching strategies for storage lookups (storage I/O is one of the most expensive operations in the EVM), JIT compilation for the EVM bytecode (interpreting the stack machine is slow; compiling to native code is faster), and possibly EVMONE or similar native EVM implementations.

The broader context is the Ethereum scaling debate circa 2022: L2 rollups (Optimism, Arbitrum) were the dominant scaling path, but there was parallel interest in making L1 itself faster. EIP-4337 (account abstraction) and future proposals like EIP-4488 affected transaction costs. Meanwhile, projects like Monad and Polygon Miden were building new EVM-compatible chains designed from scratch for parallel execution.

## Key points

- The EVM's sequential execution model limits Ethereum L1 throughput — each transaction executes in order.
- Potential optimizations: speculative execution (parallel with rollback), JIT compilation, storage caching.
- Flashbots' position processing high volumes of transactions gives them direct data on EVM bottlenecks.
- Alternative path: L2 rollups (Optimism, Arbitrum) scale computation off-chain; EVM optimization scales the L1 itself.
- Emerging competitors: Monad is building an EVM-compatible chain with native parallel execution from scratch.

[Original](https://writings.flashbots.net/research/speeding-up-evm-part-1/)
