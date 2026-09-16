---
title: "Sec3 Pro Auto Auditor: Automated Solana Security"
date: 2022-05-29
categories:
  - smart-contracts
  - security
  - solana
  - auditing
  - automated
description: Sec3 (formerly Soteria) launches their automated smart contract auditor for Solana programs — static analysis for Anchor/native Rust programs targeting common vulnerability classes. One of the first automated security tools built specifically for the Solana/Rust ecosystem.
params:
  source: pinboard
  sourceUrl: https://medium.com/coinmonks/official-sec3-pro-auto-auditor-general-public-release-90485156a33
---

## Summary

Sec3 (formerly Soteria) released their automated smart contract auditor targeting Solana programs — specifically Anchor framework programs and native Rust-based programs. Unlike Ethereum security tools (which target Solidity and EVM bytecode), this tool needed to be built from scratch for Solana's very different execution model: Solana programs are stateless eBPF bytecode, accounts are passed explicitly as parameters, and the common vulnerability classes are distinct from Ethereum (account confusion, missing signer checks, unsigned integer wrapping, etc.).

The auto auditor applies static analysis and symbolic execution to Rust source code and Anchor IDL definitions to detect vulnerability patterns. Common targets include: missing signer checks (authority validation), account data confusion (passing the wrong account type), arithmetic overflow in Rust integer operations, and reentrancy via Cross-Program Invocations (CPIs). These vulnerabilities have caused several high-profile Solana exploits.

The release in mid-2022 came amid a wave of Solana DeFi exploits and growing demand for security tooling. The Ethereum ecosystem had years of hardening — Slither, Mythril, Echidna, Certora — while the Solana ecosystem was largely doing manual audits. Sec3's tooling helped close that gap and established patterns for what automated Rust smart contract analysis should look like.

## Key points

- Automated static analysis for Solana programs: Anchor framework and native Rust targets
- Detects: missing signer checks, account data confusion, arithmetic overflow, CPI reentrancy
- Solana vulnerability profile is different from Ethereum — stateless programs, explicit account passing, no EVM memory model
- Released 2022 during a period of high-profile Solana DeFi exploits — filling a tooling gap vs. the mature Ethereum audit ecosystem
- Complements manual audits by Neodyme, OtterSec, and Halborn (main Solana audit firms of the era)
- Rust's ownership model prevents some bug classes but introduces new ones (integer wrapping, unsafe blocks) that the auditor targets

[Original](https://medium.com/coinmonks/official-sec3-pro-auto-auditor-general-public-release-90485156a33)
