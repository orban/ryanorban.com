---
title: "Apollo: Cross-Chain ETL for EVM Chaindata"
date: 2022-07-16
categories:
  - blockchain
  - ethereum
  - etl
  - data-engineering
  - evm
description: Apollo is a cross-chain ETL tool from Chainbound for extracting raw EVM chaindata — transactions, logs, traces — across multiple networks simultaneously. Designed for analysts who need low-level on-chain data without running their own full archive nodes.
params:
  source: pinboard
  sourceUrl: https://github.com/chainbound/apollo
---

## Summary

Apollo is an open-source ETL tool by Chainbound designed for extracting raw data from EVM-compatible blockchains. Unlike [ethereum-etl](/notes/ethereum-etl/) which focuses primarily on Ethereum and the Google BigQuery pipeline, Apollo targets multi-chain extraction with a focus on lower-level chaindata access: raw transactions, event logs, internal call traces, and state diffs across Ethereum, Polygon, Arbitrum, Optimism, and other EVM networks simultaneously.

The tool is aimed at the segment of blockchain data engineers who need to work across chains without standing up separate ETL pipelines for each one. The EVM-compatibility of these chains means the data structures are similar enough to extract with a unified codebase, but the node APIs and performance characteristics differ enough to require careful abstraction. Apollo handles that layer, providing a consistent interface for multi-chain data collection.

The Chainbound team was part of a 2022 wave of blockchain infrastructure companies building tools for the professional on-chain data market — sitting between raw node providers (Alchemy, QuickNode, Infura) and analytics platforms (Dune Analytics, Nansen, [Flipside Crypto](/notes/flipside-crypto/)). Apollo sits in the middle, providing ETL primitives rather than a complete analytics environment.

## Key points

- Multi-chain: extracts from Ethereum, Polygon, Arbitrum, Optimism, and other EVM networks via a unified interface
- Covers transactions, event logs, internal traces, and state diffs — lower-level than most analytics tools expose
- Complements [ethereum-etl](/notes/ethereum-etl/) for cross-chain workflows where Google BigQuery export isn't the primary target
- Part of Chainbound's broader focus on Ethereum infrastructure tools (also built fiber, a fast block propagation network)
- Written in Rust, reflecting the performance focus typical of Chainbound tooling

[Original](https://github.com/chainbound/apollo) → GitHub
