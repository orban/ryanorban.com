---
title: Holographic Consensus — DAOstack's Scaling Mechanism
date: 2022-01-06
categories:
  - dao
  - governance
  - daostack
  - mechanism-design
  - blockchain
description: Matan Field's foundational paper on holographic consensus — DAOstack's mechanism for scaling DAO governance by using prediction markets to surface which proposals deserve the full DAO's attention. The core intellectual contribution behind the Genesis DAO and DAOstack protocol.
params:
  source: pinboard
  sourceUrl: https://medium.com/daostack/holographic-consensus-part-1-116a73ba1e1c
---

## Summary

[Holographic consensus](/notes/holographic-consensus/) is a governance mechanism designed by Matan Field (co-founder of DAOstack) to solve the scalability problem in DAO governance. The core problem: as a DAO grows, the number of proposals grows, but the attention of token holders is fixed. Full consensus (everyone votes on everything) doesn't scale; simple token voting with low participation leads to plutocracy.

[Holographic consensus](/notes/holographic-consensus/) inserts a prediction market layer between proposal creation and full governance voting. Anyone can boost a proposal by staking GEN tokens (DAOstack's governance token) on it, betting that it will pass. If the prediction market shows genuine support (enough stakers predicting passage), the proposal gets boosted — it can now pass by relative majority (the proposal with the most votes passes) rather than requiring absolute majority from all token holders. This means the DAO can process many more proposals without requiring full participation on each one.

The mechanism is clever: it aligns the incentives of curators (stakers who boost proposals) with quality — if you boost a proposal that passes, you earn a return; if you boost a bad proposal, you lose stake. This creates a filtering layer where only proposals with genuine support get elevated to full governance attention. The Genesis DAO was the first organization to run on this mechanism in 2018-2019.

The critique: prediction market boosting can be gamed, and the separation between boosted and unboosted voting creates two-tier governance that might not reflect actual community preferences.

## Key points

- Solves the DAO attention-scaling problem: full consensus doesn't scale, [holographic consensus](/notes/holographic-consensus/) uses prediction markets as an attention filter
- GEN token staking boosts proposals — stakers bet proposals will pass; correct predictions earn returns
- Boosted proposals pass by relative majority; unboosted proposals require absolute majority
- DAOstack implemented this in the Genesis DAO (2018-2019) — first real-world test of the mechanism
- Connects to prediction market design theory and mechanism design more broadly

[Original](https://medium.com/daostack/holographic-consensus-part-1-116a73ba1e1c)
