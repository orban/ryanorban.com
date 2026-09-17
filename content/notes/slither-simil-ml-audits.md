---
title: "Slither-simil: ML-Assisted Smart Contract Audits"
date: 2022-05-29
categories:
  - smart-contracts
  - security
  - machine-learning
  - ethereum
  - auditing
description: Trail of Bits introduces Slither-simil, a tool that uses ML embeddings to find smart contracts similar to a known-vulnerable one — dramatically accelerating audits by surfacing candidate contracts before manual review. An early example of applying ML to the smart contract security problem.
params:
  source: pinboard
  sourceUrl: https://blog.trailofbits.com/2020/10/23/efficient-audits-with-machine-learning-and-slither-simil/
---

## Summary

Slither-simil is a tool from Trail of Bits built on top of their Slither static analysis framework for Solidity smart contracts. The core idea: represent functions as embeddings using a word2vec-style model trained on a large corpus of Ethereum contracts, then use cosine similarity to find functions that are semantically similar to a known-vulnerable function. An auditor who finds a vulnerability in one contract can immediately search the entire corpus for contracts with similar code structure.

This addresses a real bottleneck in smart contract security. Manual audits are expensive and slow — Trail of Bits and OpenZeppelin auditors typically review a contract over days or weeks. But many vulnerability classes (unchecked return values, reentrancy patterns, integer overflow) appear in structurally similar code across many contracts. If you've found a reentrancy bug in protocol A, there's likely a contract in protocol B with very similar code structure. Slither-simil automates the search for those candidates.

The ML component is a code2vec-style approach where function bytecodes or AST representations are embedded into a vector space. Functions from the same "family" (e.g. ERC-20 transfer implementations) cluster together; functions with unusual patterns (potential vulnerabilities) appear as outliers or cluster with other known-vulnerable functions. This is representation learning applied to program analysis — a precursor to the LLM-based code analysis that emerged later.

## Key points

- Slither-simil finds contracts similar to a target (e.g. known-vulnerable) function using ML embeddings over Solidity ASTs
- Built on Slither, Trail of Bits' static analysis framework for Ethereum smart contracts
- Training corpus: large dataset of deployed Ethereum contracts — embeddings capture common patterns and outliers
- Use case: given a newly discovered vulnerability, rapidly triage which other contracts in a project share the same pattern
- Complements traditional static analysis (rule-based) with learned similarity — catches variants that rules miss
- Related tools: Mythril, Manticore (symbolic execution), Echidna (fuzzer) — the broader Trail of Bits security toolkit
- Precursor to LLM-based code analysis tools like Copilot for Security and Code Shield

[Original](https://blog.trailofbits.com/2020/10/23/efficient-audits-with-machine-learning-and-slither-simil/)
