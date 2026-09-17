---
title: Building Blockchain Data Pipelines with The Graph & Singer
date: 2022-07-16
categories:
  - blockchain
  - ethereum
  - the-graph
  - data-engineering
  - singer
description: A tutorial on building blockchain data pipelines using The Graph's subgraph queries piped through Singer, the open-source ETL standard. Shows how to treat on-chain indexed data like any other data source in a standard analytics stack.
params:
  source: pinboard
  sourceUrl: https://evenson.io/2022/05/24/tap-thegraph/
---

## Summary

This Matt Evenson post demonstrates integrating The Graph protocol with Singer — the open-source ETL specification from Stitch Data — to build structured data pipelines from Ethereum blockchain data. The combination is pragmatic: The Graph provides indexed, queryable GraphQL APIs over on-chain data, while Singer provides a standardized tap/target interface for moving that data into data warehouses and analytics systems.

The Graph solves the indexing problem: raw Ethereum nodes aren't designed for complex queries (no "give me all swaps on Uniswap in the last 30 days"). Subgraphs define event-triggered indexing logic that maintains queryable state. By 2022, The Graph hosted subgraphs for most major DeFi protocols — Uniswap, Aave, Compound, Curve — making it a de facto API layer for on-chain analytics.

Singer is the data plumbing: a specification for taps (data sources) and targets (data destinations) with a simple JSON-based message format. Connecting a Singer tap to The Graph's GraphQL endpoint treats blockchain data like any other data source, enabling incremental syncs, schema discovery, and standard pipeline monitoring. This is the approach data engineers who know traditional analytics tooling (Stitch, Airbyte, dbt) would gravitate toward rather than blockchain-specific ETL tools.

## Key points

- The Graph protocol provides queryable GraphQL APIs over indexed Ethereum event data via subgraphs
- Singer taps expose data sources as streams; targets write to data warehouses (BigQuery, Postgres, Snowflake)
- Combining them brings blockchain data into standard data engineering workflows without blockchain-specific tooling
- Incremental sync via cursor tracking means you don't re-index from genesis on every run
- Alternative to [ethereum-etl](/notes/ethereum-etl/) + BigQuery for teams already using Singer/Stitch/Airbyte infrastructure

[Original](https://evenson.io/2022/05/24/tap-thegraph/)
