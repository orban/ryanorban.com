---
title: "Overlay V1 Core: Stability and Robustness for Data-Stream Derivative Markets"
date: 2022-07-15
categories:
  - defi
  - crypto
  - markets
  - protocol
  - risk
description: "Technical paper extending the Overlay Protocol — a decentralized system for creating derivative markets on any data stream — with a three-part risk framework: funding payments, bid-ask pricing, and circuit breakers. The key challenge is managing the risk that any market can have unbounded open interest against the protocol's treasury."
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/overlay v1 core.pdf
---

## Summary

Michael Feldman, Adam Kay, Anantdeep Parihar, Rachel Rybarczyk, and Jonah Lin extend Kay's original Overlay Protocol design toward a production-stable V1. The Overlay Protocol is a DeFi system that creates synthetic derivative markets on any random-process data stream — you could trade on crypto prices, weather data, sports outcomes, or any oracle-connected feed without requiring a counterparty, since the protocol itself takes the other side.

The core risk management problem: if a market has unlimited open interest (total notional positions) against a finite treasury, a strongly one-sided market can drain the treasury. V1 Core introduces three interlocking risk controls: (1) **funding payments** — traders holding positions pay or receive continuous fees based on imbalance between longs and shorts, penalizing the overcrowded side; (2) **bid-ask pricing** — the protocol charges a spread that widens as open interest concentration grows, making positions more expensive to open when risk is elevated; (3) **circuit breakers** — hard limits on exposure per market that trigger when thresholds are exceeded.

The statistical underpinning is explicit: risk parameters must be calibrated based on fits to historical data for each underlying feed. This makes Overlay unusual among DeFi protocols in requiring domain expertise to safely parameterize — the protocol design is principled but implementation requires ongoing quantitative risk management. The paper (March 2022) was produced during Overlay's development phase and reflects the protocol's ambition to enable permissionless derivatives on arbitrary data.

## Key points

- Overlay Protocol: permissionless synthetic derivative markets on any data stream — no counterparty, protocol as market maker
- Core problem: unlimited open interest against finite treasury is an existential solvency risk
- Three-part risk framework: funding payments (penalty on crowded side) + bid-ask spread (wider when concentrated) + circuit breakers
- Risk parameters require quantitative calibration from historical data — unusual rigor for DeFi
- Enables markets on non-tradeable quantities (sports outcomes, weather, elections) that centralized exchanges won't list
- Part of the 2021-2022 wave of novel DeFi derivatives protocols attempting to expand market access beyond traditional assets

[Original (March 2022)](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/overlay%20v1%20core.pdf)
