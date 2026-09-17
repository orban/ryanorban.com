---
title: 100x Faster EVM Traces with Python
date: 2022-07-27
categories:
  - ethereum
  - evm
  - defi
  - python
  - developer-tools
description: banteg's writeup on getting 100x faster EVM transaction traces using Python with an Erigon node backend — replacing slow Geth-based trace_* RPC calls with Erigon's streaming API. Essential reading for DeFi analytics and MEV research.
params:
  source: pinboard
  sourceUrl: https://banteg.mirror.xyz/3dbuIlaHh30IPITWzfT1MFfSg6fxSssMqJ7TcjaWecM
---

## Summary

banteg — a core contributor to Yearn Finance and one of the most technically prolific DeFi developers — published this piece on getting dramatically faster EVM transaction traces using Python. The bottleneck he addresses is that standard Geth-based `trace_*` JSON-RPC calls are slow: each trace request is a sequential blocking call, and tracing thousands of transactions (for MEV analysis, protocol debugging, or DeFi analytics) becomes prohibitively time-consuming.

The solution uses Erigon (the performance-focused Ethereum execution client, previously Turbo-Geth) which provides a streaming trace API that's fundamentally faster than Geth's approach. Combined with banteg's evm-trace Python library and async request handling, the result is approximately 100x throughput improvement. This matters enormously for anyone doing large-scale DeFi analytics: tracing a month of Uniswap transactions, analyzing MEV extraction patterns, or debugging protocol behavior across many blocks.

The broader pattern is representative of 2022 DeFi tooling: serious practitioners building their own fast infrastructure because the standard tools weren't fast enough for production research. banteg's work on evm-trace and related tooling became part of the standard toolkit for MEV searchers and protocol developers. Erigon specifically gained adoption precisely because its architecture (append-only database, streaming API) was better suited to large-scale trace analysis.

## Key points

- Problem: standard Geth `trace_*` JSON-RPC calls are slow for bulk EVM tracing
- Solution: Erigon streaming API + banteg's evm-trace Python library + async requests
- ~100x throughput improvement for large-scale transaction trace analysis
- Critical for: MEV research, protocol debugging, DeFi analytics at scale
- By banteg — Yearn Finance core dev, prolific DeFi tooling author
- Erigon gains adoption partly because its storage architecture enables fast bulk trace queries

[Original](https://banteg.mirror.xyz/3dbuIlaHh30IPITWzfT1MFfSg6fxSssMqJ7TcjaWecM)
