---
title: "Unidata: Open Web3 Data Aggregation Protocol"
date: 2022-07-16
categories:
  - web3
  - blockchain
  - data
  - open-source
  - cross-chain
description: Unidata is an open protocol for aggregating and standardizing user activity data across Web3 — social posts, NFT collections, token holdings, DeFi positions — into a unified queryable graph. Designed as a data portability layer for decentralized applications.
params:
  source: pinboard
  sourceUrl: https://unidata.app/
---

## Summary

[Unidata](/notes/unidata/) is an open-source protocol and API for aggregating user-centric Web3 data across chains and applications into a standardized format. Instead of each dApp querying multiple disparate sources (Ethereum node for tokens, OpenSea API for NFTs, Lens Protocol for social, Mirror for writing), Unidata provides a unified interface where you query a user's address and get back a structured representation of their entire on-chain footprint.

The data model covers: Notes (social posts on Lens, Mirror, Farcaster), Assets (NFT holdings, token balances), Links (follows, connections in social graphs), and Profiles (identity data across platforms). The protocol is blockchain-agnostic, aggregating from Ethereum, Polygon, BSC, and any chain where the underlying data providers have coverage.

The motivation is data portability and interoperability: in Web3, your social graph on Lens shouldn't be siloed from your NFT collection on OpenSea or your DeFi history on Uniswap. Unidata attempts to unify these into a graph structure that applications can query consistently. This is the same problem RSS3 and Mask Network also worked on — a Web3 data aggregation layer that makes building social and identity-aware dApps easier.

## Key points

- Aggregates NFT holdings, token balances, social posts, and connections across chains into a unified data model
- Four core types: Notes (content), Assets (holdings), Links (social connections), Profiles (identity)
- Open-source, developer-facing API — not a consumer product but infrastructure for dApp builders
- Competes with RSS3 and Mask Network's data layer in the unified Web3 social data space
- Relevant for building decentralized social apps that need to read cross-platform user histories

[Original](https://unidata.app/)
