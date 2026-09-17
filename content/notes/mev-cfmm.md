---
title: Maximal Extractable Value and Constant Function Market Makers
date: 2022-07-20
categories:
  - defi
  - mev
  - blockchain
  - market-microstructure
description: Research paper analyzing maximal extractable value (MEV) in the context of constant function market makers (CFMMs) like Uniswap. It formalizes how miners/validators can capture value by reordering, inserting, or censoring transactions, with implications for CFMM mechanism design.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/MEV_CFMM.pdf
---

## Summary

This paper examines maximal extractable value (MEV) — the additional value that block producers on Ethereum and similar proof-of-work or proof-of-stake chains can extract by controlling transaction ordering within a block — specifically in the context of constant function market makers (CFMMs) like Uniswap, Curve Finance, and Balancer. CFMMs define a pricing function over a liquidity pool that automatically executes trades when a user's specified price satisfies the constraint; the paper formalizes how this deterministic pricing mechanism creates systematic opportunities for front-running, sandwich attacks, and arbitrage by actors who can observe the mempool and manipulate transaction sequencing.

The analysis provides a mathematical treatment of CFMM properties — specifically the invariant function (e.g., xy = k for Uniswap v2) — and characterizes the set of profitable MEV strategies available to a miner or searcher. Key results include conditions under which a rational block producer should include or exclude specific user transactions and how much they can extract. The paper distinguishes between benign arbitrage (price correction across venues) and "harmful" MEV that purely redistributes value from users to extractors without improving market efficiency, a distinction relevant to mechanism design for future DeFi protocols.

The paper contributes to an emerging body of work on blockchain market microstructure, connecting to concepts from traditional finance like priority gas auctions (a form of bid submission analogous to co-location in high-frequency trading) and the role of dark pools. It has design implications for CFMMs: features like price impact limits, commit-reveal schemes, and batch auctions can mitigate MEV exposure for ordinary users.

## Key points

- Constant function market makers (CFMMs) use an invariant (e.g., xy = k) to price trades; this deterministic pricing creates predictable profit opportunities when combined with mempool visibility
- Maximal extractable value (MEV) is a superset of miner extractable value: any party who controls transaction ordering — including validators and searchers using Flashbots — can extract value
- Sandwich attacks are the canonical CFMM MEV: front-run a large user trade to move the price, let the user's trade execute at a worse price, then back-run to restore position at profit
- The paper formalizes conditions under which it's rational for a block producer to deviate from a simple first-come-first-served ordering policy — essentially whenever MEV exceeds the cost of block reorganization
- MEV-resistant CFMM designs include time-weighted average price (TWAP) oracles, batch auction settlement, and commit-reveal mechanisms that hide trade intent until execution

[Original](file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/MEV_CFMM.pdf)
