---
title: "ethereum-etl: Python ETL for Ethereum Blockchain Data"
date: 2022-07-16
categories:
  - ethereum
  - blockchain
  - etl
  - data-engineering
  - python
description: ethereum-etl is the standard Python library for extracting Ethereum blockchain data into structured formats — blocks, transactions, ERC-20 transfers, receipts, logs, internal transactions — with Google BigQuery export support. The reference implementation for blockchain data pipelines.
params:
  source: pinboard
  sourceUrl: https://github.com/blockchain-etl/ethereum-etl
---

## Summary

[ethereum-etl](/notes/ethereum-etl/) is an open-source Python library by blockchain-etl for extracting, transforming, and loading data from Ethereum into structured formats. It handles the full suite of on-chain objects: blocks, transactions, ERC-20 and ERC-721 token transfers, receipts, event logs, contract bytecodes, and internal transactions (traces). The primary output target is Google BigQuery, which hosts public Ethereum datasets used by thousands of analysts.

The core problem it solves: Ethereum nodes (Geth, Erigon) expose JSON-RPC APIs designed for individual query lookups, not bulk data extraction. Getting a month of transfer events requires thousands of `eth_getLogs` calls with careful rate limiting, pagination, and schema normalization. ethereum-etl wraps all of this into streaming ETL jobs that produce clean CSV or JSONL output, with the BigQuery export being a natural downstream.

By 2022, the Google BigQuery public Ethereum dataset (powered by ethereum-etl) had become the standard environment for blockchain analytics research. You could query the full transaction history with standard SQL. The project also inspired polygon-etl, tron-etl, and similar tools for other chains, and sits upstream of analytics tools like Dune Analytics and [Flipside Crypto](/notes/flipside-crypto/) which build query interfaces on top of similar ETL pipelines.

## Key points

- Extracts blocks, transactions, ERC-20/ERC-721 transfers, event logs, traces — all via Ethereum JSON-RPC
- Streams output to CSV, JSONL, or Google BigQuery  directly
- Powers the public Google BigQuery Ethereum dataset used by academic and commercial analysts
- Works with any Ethereum-compatible node: Geth, Erigon, Infura, Alchemy
- Sibling projects cover Polygon, Tron, and other EVM chains; the blockchain-etl GitHub org is the canonical home

[Original](https://github.com/blockchain-etl/ethereum-etl)
