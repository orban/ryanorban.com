---
title: Crypto Wash Trading
date: 2021-12-21
categories:
  - cryptocurrency
  - finance
  - market-manipulation
  - forensics
  - fraud-detection
description: A finance paper by Cong, Li, Tang, and Yang that introduces systematic statistical tests for detecting wash trading on unregulated cryptocurrency exchanges, finding over 70% of reported volume is fake. The methodology — Benford's Law, size rounding patterns, tail distributions — is reusable forensic infrastructure for any manipulated market.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/crypto-wash-trading.pdf
---

## Summary

Lin William Cong, Xi Li, Ke Tang, and Yang Yang introduce systematic tests for detecting wash trading on cryptocurrency exchanges, exploiting the fact that real markets produce statistical patterns (Benford's Law distributions, characteristic size rounding, specific tail distributions) that fake trading cannot easily replicate. They apply these tests to 29 exchanges, finding rampant manipulation on unregulated platforms while regulated exchanges show the patterns consistently observed in legitimate financial markets.

The quantification is stark: wash trading on unregulated exchanges averaged over 70% of reported volume — meaning the $2+ trillion annual volumes widely cited in 2021 crypto coverage were largely fabricated. The paper documents how these inflated volumes improve exchange rankings, temporarily distort prices, and correlate with exchange age, user base size, and market conditions. This is forensic finance in the tradition of detecting manipulation via statistical fingerprints rather than direct observation.

The methodology draws on Benford's Law (abnormal first-significant-digit distributions), size rounding analysis, and transaction tail distributions. These behavioral patterns emerge from human and institutional trading behavior and are not easily faked at scale. The approach is general — analogous methods could detect manipulation in any market where natural trading patterns have predictable statistical signatures.

## Key points

- 70%+ of reported volume on unregulated crypto exchanges found to be wash trading — fabricated to improve rankings
- Benford's Law, size rounding, and tail distribution tests are the core detection signals — natural trading leaves consistent statistical fingerprints
- Fake volume temporarily distorts prices and meaningfully improves exchange ranking in industry listings
- Regulated exchanges show statistically normal trading patterns; unregulated ones are categorically different
- Methodology is broadly applicable forensic finance infrastructure — detects manipulation via statistical deviation, not surveillance

[Original PDF](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/crypto-wash-trading.pdf)
