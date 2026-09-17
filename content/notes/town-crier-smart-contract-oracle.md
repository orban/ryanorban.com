---
title: Town Crier — Authenticated Data Feed for Smart Contracts
date: 2022-10-20
categories:
  - blockchain
  - smart-contracts
  - oracle
  - ethereum
  - cryptography
  - trust
description: Town Crier is an authenticated data feed system for smart contracts that uses Intel SGX trusted execution environments to fetch external data with cryptographic attestation. An early, rigorous oracle design predating Chainlink's dominance.
params:
  source: pinboard
  sourceUrl: https://www.town-crier.org/
---

## Summary

Town Crier is an oracle system that provides authenticated external data to smart contracts on Ethereum and similar blockchains. The fundamental problem oracles solve: smart contracts can only read on-chain data, but many contracts need real-world information (prices, weather, sports scores, election results). An oracle bridges this gap, but introduces a trust problem — how do you verify the data hasn't been tampered with between the external source and the contract?

Town Crier's approach is Intel SGX (Software Guard Extensions) — a trusted execution environment (TEE) that provides hardware-level attestation. The program running inside an SGX enclave can produce a cryptographic proof that it ran specific code without modification. Town Crier uses this to guarantee that the data fetched from a web source is unmodified: the SGX enclave fetches data over HTTPS, and the attestation proves the data came through intact without the operator being able to tamper with it.

The system was designed by Fan Zhang, Ittay Eyal, Robert Escriva, Ari Juels, and Gunnar Morling at Cornell and Cornell Tech. Ari Juels is a major figure in cryptography and blockchain security; the paper was academically rigorous compared to most oracle designs at the time. Chainlink became the dominant oracle network in practice by using a more pragmatic economic security model (staking + reputation), but Town Crier established the theoretical foundation for how trustworthy oracles could work with TEEs.

## Key points

- Smart contract oracle using Intel SGX TEE to provide tamper-proof external data feeds.
- SGX attestation: cryptographic proof that specific code ran unmodified — guarantees data integrity.
- Solves the oracle trust problem with hardware-level guarantees rather than economic incentives.
- Developed at Cornell Tech by Ari Juels and collaborators.
- Preceded Chainlink; established TEE-based oracle as a viable design pattern.
- Intel SGX approach trades on hardware trust vs. Chainlink's decentralization + economic security.

[Original](https://www.town-crier.org/)
