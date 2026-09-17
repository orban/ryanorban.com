---
title: "Luabase: Web3 Data Stack"
date: 2022-08-25
categories:
  - web3
  - blockchain
  - data
  - etl
  - sql
description: Luabase is a blockchain data platform that ETLs on-chain data into queryable SQL tables — 'we ETL blockchains so you don't have to.' An early attempt to give analysts standard SQL access to blockchain activity without dealing with raw node data.
params:
  source: pinboard
  sourceUrl: https://www.luabase.com/
---

## Summary

[Luabase](/notes/luabase/) is a blockchain data platform that handles the ETL (extract, transform, load) pipeline for on-chain data, exposing blockchain activity as queryable SQL tables. Analyzing Ethereum or Solana blockchain data normally requires running a full node, processing raw transaction data, and writing custom parsers for contract events — or paying for a commercial data provider with limited query interfaces. [Luabase](/notes/luabase/) abstracts this into standard SQL.

The positioning as "the web3 data stack" places it alongside other blockchain analytics tools like Dune Analytics, [Flipside Crypto](/notes/flipside-crypto/), and Nansen, all of which emerged to serve the analytical demand created by DeFi and NFT activity. The SQL interface is the key insight: data analysts comfortable with traditional databases could query blockchain data without learning web3-specific tooling. This lowered the barrier to on-chain analytics substantially.

This was bookmarked in August 2022 during a period when web3 analytics tooling was expanding rapidly — driven by demand to understand DeFi protocol behavior, track MEV, analyze NFT markets, and audit DAO treasury activity. The underlying technical problem — blockchain data is denormalized, high-volume, and stored in formats unlike traditional databases — made purpose-built tools like [Luabase](/notes/luabase/) genuinely valuable.

## Key points

- ETLs blockchain data into queryable SQL tables — standard analytical interface for on-chain data.
- Competes with Dune Analytics, [Flipside Crypto](/notes/flipside-crypto/), Nansen in web3 analytics.
- Key insight: SQL interface makes blockchain data accessible to analysts without web3 expertise.
- Addresses the problem that raw blockchain data is denormalized and not natively queryable.
- Use cases: DeFi protocol analysis, NFT market tracking, DAO treasury auditing, MEV analysis.
- Part of the web3 data stack wave that paralleled the modern data stack movement in traditional analytics.

[Original](https://www.luabase.com/)
