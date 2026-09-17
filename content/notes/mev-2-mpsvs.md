---
title: "MEV 2.0: The Rise of MPSVs"
date: 2022-07-14
categories:
  - mev
  - ethereum
  - defi
  - blockchain
  - research
description: A Reciprocal Ventures piece arguing that MEV is evolving from searcher-bot competition to MPSV (Maximal Protocol Surplus Value) — protocols themselves capturing ordering value rather than external actors extracting it. Reframes MEV as a design choice rather than an inevitable externality.
params:
  source: pinboard
  sourceUrl: https://www.recvc.com/mev-2-0-the-rise-of-mpsvs/
---

## Summary

This Reciprocal Ventures piece argues that MEV (Maximal Extractable Value) is undergoing a second phase: from external actors extracting value from protocol users (the Flashbots-era framing) toward protocols themselves internalizing that value as MPSV (Maximal Protocol Surplus Value). The shift is conceptual but has real design consequences for DeFi protocol architecture.

In MEV 1.0, searcher bots arbitraged price differences and ran sandwich attacks — value extracted by third parties, often at the expense of regular users. The Flashbots response was to give this market structure (private mempools, MEV-Boost, PBS — proposer-builder separation) but not to eliminate it. In MEV 2.0, protocols like Curve, Uniswap v3, and early CoW Protocol designs started building mechanisms that capture ordering value for the protocol treasury or LPs rather than leaving it to bots. This is MPSV: the surplus from transaction ordering flows *into* the protocol's value accrual rather than *out* of user experience.

The thesis is relevant for protocol design: if MEV is inevitable, the question becomes who captures it and how. A protocol that designs its AMM mechanics to internalize arbitrage profits (e.g. Uniswap v4 hooks, dynamic fees) is effectively converting extractable value into protocol revenue. This changes the incentive analysis for token holders and LPs significantly.

## Key points

- MEV 1.0: external searcher bots extract value from transaction ordering, users are harmed
- MEV 2.0 (MPSV): protocols design mechanisms to capture ordering value themselves via dynamic fees, auction mechanisms, or AMM redesign
- Proposer-builder separation (PBS) created infrastructure for value capture but doesn't determine who benefits
- Related work: Flash Boys 2.0, SUAVE (Single Unifying Auction for Value Expression), CoW Protocol
- Key question for protocol design: is your mechanism a value-extracting surface or a value-capturing asset?

[Original](https://www.recvc.com/mev-2-0-the-rise-of-mpsvs/)
