---
title: "SimTigerBeetle: TigerBeetle in WebAssembly"
date: 2025-11-01
categories:
  - databases
  - wasm
  - tigerbeetle
  - simulation
  - fintech
description: SimTigerBeetle runs TigerBeetle — the high-performance financial accounting database — compiled to WebAssembly in the browser. An interactive simulator for understanding TigerBeetle's consistency model and transaction semantics without local setup.
params:
  source: pinboard
  sourceUrl: https://sim.tigerbeetle.com/?scenario=0
---

![SimTigerBeetle: TigerBeetle in WebAssembly](/images/notes/simtigerbeetle-wasm-browser.png)

## Summary

SimTigerBeetle runs TigerBeetle compiled to WebAssembly, executing the actual database engine in the browser. TigerBeetle is a high-performance, ACID-compliant financial accounting database built around a strict double-entry bookkeeping model — designed for applications where ledger consistency is non-negotiable.

The simulator provides interactive scenarios for understanding TigerBeetle's transaction semantics, consistency guarantees, and account balance model. By running the actual WASM binary, it's not a mock or a simplified educational model — it's the real database with browser-level interactivity. This lets you experiment with transactions, transfers, pending credits/debits, and error conditions without installing anything.

TigerBeetle's design philosophy is interesting: it rejects general-purpose database flexibility in exchange for maximum performance and correctness on a single data model (financial accounts and transfers). The simulator makes this tradeoff tangible — you can see exactly what the database can and can't express. For engineers evaluating TigerBeetle for fintech or financial infrastructure use cases, the interactive simulator is the fastest way to understand the model.

## Key points

- TigerBeetle compiled to WebAssembly and running in the browser — the real engine, not a mock.
- Interactive scenarios for TigerBeetle's transaction semantics and consistency model.
- TigerBeetle is an ACID financial accounting database optimized for double-entry bookkeeping.
- No install required — try transactions, transfers, error conditions directly in the browser.
- Good evaluation tool for teams considering TigerBeetle for financial infrastructure.

[Original](https://sim.tigerbeetle.com/)
