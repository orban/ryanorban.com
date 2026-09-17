---
title: "Flash Boys 2.0: Frontrunning, Transaction Reordering, and Consensus Instability in Decentralized Exchanges"
date: 2022-06-24
categories:
  - mev
  - defi
  - blockchain
  - ethereum
  - security
description: Daian et al. document how arbitrage bots exploit transaction ordering in decentralized exchanges through priority gas auctions, introducing the concept of miner extractable value (MEV). The paper shows that MEV isn't just a trading problem — it creates measurable consensus-layer security risks for Ethereum.
params:
  source: papers
  sourceUrl: https://arxiv.org/abs/1904.05234
---

## Summary

Philip Daian, Steven Goldfeder, Tyler Kell, Yunqi Li, Xueyuan Zhao, Iddo Bentov, Lorenz Breidenbach, and Ari Juels systematically document the phenomenon of frontrunning in decentralized exchanges (DEXes), showing it is not an edge case but a pervasive structural feature of how Ethereum processes transactions. Arbitrage bots monitor the public mempool for profitable trades and submit competing transactions with higher gas fees to execute first — a practice the authors call priority gas auctions (PGAs). They measure this in the wild and find substantial, ongoing extraction from ordinary users.

The paper's most important conceptual contribution is formalizing miner extractable value (MEV) — the total value miners can extract by reordering, inserting, or censoring transactions within blocks. MEV isn't just an application-layer problem; the authors show it creates consensus instability incentives. If MEV opportunities are large enough, rational miners have incentives to fork the chain to capture them, undermining proof-of-work finality. This connects frontrunning directly to the security properties of the blockchain itself.

The paper draws an explicit analogy to Michael Lewis's "Flash Boys" about high-frequency trading on traditional exchanges, arguing that DEXes have recreated and amplified the same dynamics in a fully transparent, permissionless environment. The work directly inspired the creation of Flashbots and the broader MEV supply chain infrastructure (MEV-Boost, MEV-Geth) that now routes the majority of Ethereum block production. It remains the foundational academic reference for MEV research.

## Key points

- Documents priority gas auctions (PGAs) in which bots compete to front-run DEX trades by bidding up gas fees
- Introduces miner extractable value (MEV) as a formal concept: the maximum value extractable by reordering transactions within a block
- Shows MEV creates consensus instability: sufficiently large MEV incentivizes miners to fork the chain to capture it
- Empirically measures bot activity across major DEXes like Uniswap and Bancor, showing millions in annual extraction
- Directly inspired Flashbots and the MEV ecosystem that now shapes Ethereum block production

[Original](https://arxiv.org/abs/1904.05234)
