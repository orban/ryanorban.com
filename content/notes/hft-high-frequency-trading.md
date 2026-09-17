---
title: HFT — High-Frequency Trading
date: 2013-04-15
categories:
  - finance
  - trading
  - hft
  - markets
  - algorithms
description: Scarce Capital's explainer on high-frequency trading — how co-location, order types, and microsecond latency advantages let HFT firms extract value from modern equity markets. A critical but fair-minded overview of a frequently misunderstood practice.
params:
  source: pinboard
  sourceUrl: http://scarcecapital.com/hft/
---

## Summary

High-frequency trading (HFT) became a flashpoint in financial markets around 2012–2013, with regulators, politicians, and the press debating whether it helped or hurt markets. Scarce Capital's overview offered a technical explainer aimed at understanding what HFT firms actually do — cutting through the moral panic to describe the mechanics.

The core mechanics: HFT firms co-locate their servers in exchange data centers to minimize network latency to microseconds. They use custom FPGA hardware for order processing (faster than software), proprietary order types offered by exchanges (like flash orders that give a first-look advantage), and sophisticated market microstructure models to detect and trade on short-term price patterns. The business model is built on tiny margins captured at enormous volume — thousands of trades per second, each extracting a fraction of a cent.

The legitimate function argument: HFT firms act as market makers, providing liquidity and tightening bid-ask spreads. Academic research in this period generally found that HFT reduced transaction costs for retail investors on average. The criticism: they do so selectively — withdrawing liquidity during market stress (the 2010 Flash Crash being exhibit A), and engaging in practices like quote stuffing and layering that exploit slower participants without adding real economic value. The debate was ultimately about market structure design: should exchanges be designed to reward speed, or should speed advantages be explicitly limited?

## Key points

- Co-location: renting rack space inside exchange data centers to minimize signal travel time — the physical limit matters at microsecond timescales.
- FPGA-based order processing: custom silicon that processes orders in nanoseconds vs. milliseconds for software, a hard latency floor for competitors.
- Market maker defense: HFT firms claim they provide liquidity and tighten spreads — true on average, contested during stress events like the Flash Crash.
- Quote stuffing and layering: manipulative practices where firms flood the order book with orders they intend to cancel, misleading other participants about supply/demand.
- Regulatory response: SEC and CFTC were investigating HFT practices in 2013; Michael Lewis's *Flash Boys* (2014) later brought the debate to mainstream attention.

[Original](http://scarcecapital.com/hft/)
