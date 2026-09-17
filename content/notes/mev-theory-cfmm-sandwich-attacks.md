---
title: "Towards a Theory of Maximal Extractable Value I: Constant Function Market Makers"
date: 2022-07-01
categories:
  - mev
  - defi
  - cryptocurrency
  - game-theory
  - amm
  - blockchain
description: Kulkarni, Diamandis, and Chitra's first paper in a theory series on Maximal Extractable Value in constant function market makers, showing sandwich attack price impact scales as O(log n) in trade count. It establishes the game-theoretic framework for MEV analysis that the field needed.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/MEV_CFMM.pdf
---

## Summary

Maximal Extractable Value (MEV) is the excess value that miners or validators extract from users by reordering, inserting, or censoring transactions. Kshitij Kulkarni (Berkeley), Theo Diamandis (MIT), and Tarun Chitra (Gauntlet) develop a formal game-theoretic framework for MEV in constant function market makers (CFMMs) like Uniswap, the dominant class of automated market makers in DeFi.

The paper focuses on two MEV types: **reordering MEV** (sandwich attacks) and **routing MEV** (exploiting multi-hop liquidity paths). For sandwich attacks, the key result is that the maximum price impact of reordering relative to average price impact is O(log n) in the number of user trades — meaning impact scales slowly with trade volume, which has implications for both attackers estimating profitability and protocol designers estimating costs. The routing analysis reveals a counter-intuitive finding: MEV existence sometimes *improves* routing quality, not just degrades it, depending on liquidity topology.

They construct an analogue of the price of anarchy from algorithmic game theory to quantify routing MEV. When sandwich attack impact is localized (affects only nearby trades in the ordering), the price of anarchy is constant — bounded, not unbounded. This is a structural property of CFMM design that limits worst-case MEV extraction.

## Key points

- MEV is formalized as a game where miners choose transaction orderings to maximize extractable value; this paper is the first rigorous treatment for CFMMs.
- Sandwich attack price impact scales as O(log n) in the number of trades — giving both searchers and protocol designers a quantitative bound to reason about.
- Routing MEV analysis uses Pigou network and Braess paradox analogues to show MEV can paradoxically improve routing efficiency in some network topologies.
- Price of anarchy for routing MEV is constant when sandwich impact is localized — a positive structural result for CFMM designers.
- This is part 1 of a series; it focuses on CFMMs only. Follow-on work presumably addresses order book DEXes and more complex MEV types.

[Original paper](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/MEV_CFMM.pdf)
