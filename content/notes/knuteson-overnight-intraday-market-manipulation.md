---
title: "They Still Haven't Told You: Overnight vs. Intraday Market Anomaly"
date: 2022-01-12
categories:
  - finance
  - market-manipulation
  - quantitative-finance
  - trading
  - forensics
description: Bruce Knuteson documents a decades-long anomaly in global stock markets where overnight returns consistently exceed intraday returns in ways consistent only with a large quant firm systematically expanding its book at open and contracting at close. A forensic finance argument that major market manipulation has gone unreported by the institutions supposed to catch it.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/whattheyhaventtoldyou.pdf
---

## Summary

Bruce Knuteson (arXiv:2201.00223, Jan 2022) presents a forensic finance argument that the world's stock markets have exhibited a decades-long pattern of overnight returns and intraday returns inconsistent with any normal market explanation. The pattern: across major global indices and individual stocks, overnight returns (close-to-open) systematically outperform intraday returns (open-to-close) by an implausible margin — the opposite of what risk-bearing logic predicts, since intraday periods carry more trading risk.

Knuteson's proposed explanation is specific and disturbing: one or more large, long-lived quantitative trading firms have been exploiting their market impact asymmetrically. By expanding their portfolio early in the day (when their trades move prices more) and contracting later (when markets are more liquid and their impact smaller), they sustain the pattern while harvesting mark-to-market gains on their large existing book. The daily round-trip loses money but the long-term position gains from the artificial price movements. This is not a novel claim — the pattern was first documented in 2007 — but no alternative explanation has been advanced in the fourteen years since. Knuteson's provocative angle is the title: regulators, economists, and quants all knew about this pattern and didn't tell the public.

The paper is fully reproducible: all data is public, the code is open-source, and every chart can be regenerated. China is the notable exception to the global pattern (its SSE 50 stocks show a reversed pattern), which Knuteson argues is structurally consistent with different regulatory and ownership constraints on large institutional positions. The accusatory tone is deliberate — the paper names specific regulatory bodies (SEC, FINRA, CFTC) and academic communities as complicit through silence.

## Key points

- Global overnight returns consistently beat intraday returns for decades — the opposite of risk-compensation theory predicts
- Only explanation that fits: a large quant firm deliberately expanding positions at open (high market impact) and contracting at close (lower impact), losing on round-trips but gaining on mark-to-market existing book
- China stock markets show the reversed pattern — consistent with different ownership constraints on large institutional players
- Fully reproducible with public data and open-source code — reproducibility is a core rhetorical move
- Regulators (SEC, FINRA, CFTC) and academic finance economists have known since 2007 and haven't disclosed
- Related to market microstructure, price impact, and the broader question of whether financial regulators adequately police large quant firms

[Original PDF](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/whattheyhaventtoldyou.pdf)
