---
title: Programming Bitcoin — Jimmy Song
date: 2021-12-22
categories:
  - bitcoin
  - blockchain
  - programming
  - cryptography
  - education
description: Jimmy Song's 'Programming Bitcoin' book repository — a hands-on O'Reilly book that teaches Bitcoin internals by implementing the cryptography and protocol layer from scratch in Python. The deepest technical introduction to how Bitcoin actually works.
params:
  source: pinboard
  sourceUrl: https://github.com/jimmysong/programmingbitcoin
---

## Summary

Programming Bitcoin by Jimmy Song is an O'Reilly book that teaches Bitcoin at the implementation level — not the what is Bitcoin explainer level, but the cryptographic and protocol internals. The approach is pedagogically rigorous: you implement elliptic curve cryptography, ECDSA signatures, hash functions (SHA-256, RIPEMD-160), Script (Bitcoin's scripting language), transaction parsing, block validation, and eventually the SPV (Simple Payment Verification) protocol from scratch in Python.

The GitHub repository contains the code and exercises that accompany the book. This makes it possible to read the text alongside running code — you write the implementation, test it against real Bitcoin data, and understand exactly why each piece exists. This is the most technically demanding standard Bitcoin education resource, and the most rewarding for people who want to actually understand the protocol rather than use it.

The prerequisite is comfort with Python and basic math — finite field arithmetic and elliptic curves are introduced from first principles, but you need to follow mathematical reasoning. People who've completed Programming Bitcoin come away with a mental model of Bitcoin that makes most protocol discussions immediately comprehensible. It's also the entry point into understanding why Bitcoin Script has the limitations it does (by contrast with Ethereum's Solidity).

## Key points

- Implement ECDSA, SHA-256, RIPEMD-160, Bitcoin Script, transaction parsing from scratch in Python
- O'Reilly book + GitHub exercises; real Bitcoin data used for validation throughout
- By Jimmy Song: prominent Bitcoin educator and developer, author and podcaster
- Prerequisites: Python + ability to follow mathematical reasoning (finite field arithmetic introduced from scratch)
- Most rigorous technical Bitcoin introduction available; contrasts with Ethereum developer focus in most 2021 crypto education

[Original](https://github.com/jimmysong/programmingbitcoin)
