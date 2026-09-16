---
title: "Agoric: JavaScript Smart Contracts with Object-Capability Security"
date: 2022-04-19
categories:
  - blockchain
  - smart-contracts
  - javascript
  - security
  - web3
description: Agoric is a smart contract platform built on JavaScript with a hardened security model — uses object-capability security to make contracts composable and safe by construction. An unusual approach in a space dominated by Solidity and Rust.
params:
  source: pinboard
  sourceUrl: https://github.com/Agoric/
---

## Summary

Agoric is a blockchain platform for building smart contracts in JavaScript, with a security model built on object-capability security (ocaps). The idea is that JavaScript, when hardened (via SES — Secure ECMAScript), is a safe language for expressing the kinds of mutual obligations that smart contracts represent. Agoric's key insight: JavaScript's object model maps naturally onto capability-based security, and developers who already know JS can write contracts without learning Solidity or Rust.

The security model is the most interesting part. In standard smart contract platforms, a contract's security depends entirely on the correctness of its code — any bug can drain funds. Object-capability security flips this: instead of each contract having raw access to global state, objects can only do what they've been explicitly given the capability to do. A contract that receives a token object can use it; it can't spontaneously acquire capabilities it wasn't given. This makes contracts composable by construction — you can audit security locally rather than globally.

Agoric's architecture layers an economic system (ERTP — Electronic Rights Transfer Protocol) on top of this security model. The core primitive is a purse — a capability-secured container for digital assets. Payments (assets in transit), mints (asset issuers), and brands (asset types) form a typed, unforgeable economic graph. The Inter Protocol (IST stablecoin) and AMM are built on this foundation. The technical approach is intellectually coherent and influenced by Mark Miller's decades of work on capability security.

## Key points

- Smart contracts in JavaScript using Hardened JavaScript (SES) — no new language required for JS developers.
- Object-capability security: contracts can only use capabilities explicitly passed to them — local auditability, composable safety.
- ERTP (Electronic Rights Transfer Protocol): typed, unforgeable asset system; purses, payments, mints, brands.
- Built on Cosmos IBC infrastructure — interoperable with the Cosmos ecosystem.
- Mark Miller influence: Agoric is the production application of decades of research on capability-based security.
- Contrast with Solidity: Agoric's security model is fundamentally different — capability-based vs. code-correctness-based.

[Original](https://github.com/Agoric/) → GitHub
