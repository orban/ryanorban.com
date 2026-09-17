---
title: Dune Analytics SQL Snippets
date: 2022-05-26
categories:
  - dune-analytics
  - blockchain
  - sql
  - analytics
  - ethereum
description: A GitHub collection of SQL query snippets for Dune Analytics and Google BigQuery targeting on-chain Ethereum data. Practical reference for blockchain data analysts who want reusable queries for common DeFi analytics tasks.
params:
  source: pinboard
  sourceUrl: https://github.com/sambacha/dune-snippets
---

## Summary

[dune-snippets](/notes/dune-snippets/) by sambacha is a GitHub repository collecting SQL query templates for Dune Analytics (the dominant on-chain analytics platform) and Google BigQuery. The target audience is blockchain data analysts who want reusable query building blocks rather than starting from scratch each time.

Dune Analytics democratized Ethereum on-chain analysis: it provides a PostgreSQL-compatible SQL interface over decoded Ethereum transaction and event data, plus decoded DeFi protocol tables (Uniswap trades, Aave liquidations, etc.). Before Dune, getting this data required running an archive node, writing custom indexers, or paying for The Graph subgraph access. After Dune, a SQL analyst could query on-chain data directly — which produced a wave of DeFi analytics dashboards and research.

Common query patterns in collections like this include: identifying liquidity provider returns on Uniswap (complex because of impermanent loss), tracking MEV extraction by known bot addresses, following token flows between wallets and contracts, measuring DEX volume by protocol and token pair, and computing TVL (total value locked) over time. The SQL snippets serve as both reference implementations and starting points for more complex queries.

## Key points

- SQL snippets for Dune Analytics and Google BigQuery — reusable templates for Ethereum on-chain analysis
- Dune Analytics provides decoded Ethereum data in a SQL interface — major unlock for the data analyst community
- Common patterns: LP returns, MEV bot tracking, token flow analysis, DEX volume, TVL computation
- Dune uses SparkSQL/Hive-dialect and later moved to a trino-based engine — snippet syntax may need adaptation
- Pairs with [EigenPhi](/notes/eigenphi/) (MEV visualization) and [Flipside Crypto](/notes/flipside-crypto/) for alternative on-chain data platforms
- sambacha is a prolific Ethereum tooling contributor with multiple open-source repositories

[Original](https://github.com/sambacha/dune-snippets)
