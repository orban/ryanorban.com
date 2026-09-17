---
title: "Proof of Useful Work: Blockchain Web Services"
date: 2022-06-16
categories:
  - blockchain
  - consensus
  - proof-of-work
  - machine-learning
  - energy
description: A 2022 technical whitepaper proposing Proof of Useful Work (PoUW) as an alternative to Bitcoin's proof-of-work, directing miners' computation toward paying clients' ML training jobs and scientific simulations instead of purposeless hash puzzles. A direct response to the energy waste criticism of PoW mining.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/PoUW_Tech_White_Paper-v4.1-220406.pdf
---

## Summary

Proof of Work (PoW) consensus, as implemented in Bitcoin, requires miners to burn vast computational resources solving cryptographic hash puzzles that serve no purpose beyond being hard to compute. The energy expenditure is a feature — it's what makes the ledger costly to attack — but it produces nothing else of value. Proof of Useful Work (PoUW), proposed by Lihu, Harvilla, Gerzanics, Jain, Zheng in this 2022 whitepaper, replaces the hash puzzle with genuinely useful computation: machine learning training jobs, scientific simulations, and other compute tasks that paying clients submit to the network.

The core mechanism works through verifiable computation receipts. Clients submit compute jobs to the network; miners perform the work and produce cryptographically verifiable proofs that the computation was performed correctly. These receipts serve as the basis for blockchain consensus — the chain advances based on accumulated verifiable work, not accumulated hashes. Miners earn fees from clients for the useful computation, replacing the block reward logic of traditional PoW. The system achieves the same Sybil resistance and double-spend protection that hash puzzles provide, while redirecting the energy expenditure toward economically valuable output.

The whitepaper addresses the key attack vector: can a miner fake useful work without performing it? The solution draws on techniques from verifiable computation and zero-knowledge proofs — specifically, periodic checkpointing with cryptographic commitments to intermediate states that are expensive to precompute but cheap to verify. The proposal connects to a cluster of related ideas — Proof of Learning (PoLe, arXiv:2007.15145), proof-of-stake as the non-compute alternative — all responding to the growing recognition that Bitcoin's energy footprint is politically and economically unsustainable.

## Key points

- PoUW directs mining compute toward client-submitted ML training and simulation jobs rather than hash puzzles
- Verifiable computation receipts replace hash difficulty as the basis for consensus — the chain advances on accumulated useful work
- Miners earn client fees, changing the economic model from block rewards funded by inflation to service fees funded by demand
- The anti-cheating mechanism uses cryptographic checkpointing: intermediate states committed before results are submitted
- Closely related to Proof of Learning (PoLe) and represents a family of proposals trying to make proof-of-work economically productive

[Source](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/PoUW_Tech_White_Paper-v4.1-220406.pdf)
