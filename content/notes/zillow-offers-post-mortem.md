---
title: Zillow Did Not Have Metallic Balls
date: 2021-11-28
categories:
  - business
  - real-estate
  - algorithms
  - market-making
  - startups
description: Steve Buccini's post-mortem on Zillow Offers dissects why Zillow's iBuying program failed — they were making a market in illiquid assets with a flawed pricing model and no mechanism to cut losses. A case study in the difference between algorithmic pricing and actual market-making discipline.
params:
  source: pinboard
  sourceUrl: https://www.stevenbuccini.com/zillow-offers
---

## Summary

Zillow Offers was Zillow's attempt to become an iBuyer — a company that makes instant cash offers on homes, does light renovations, and relists for a profit. In November 2021, Zillow shut down the program after disclosing $304 million in inventory write-downs and announcing it would sell 7,000+ homes at a loss.

Steve Buccini's analysis focuses on the market-making lens: Zillow was running a dealer business, not an algorithm business. Market makers profit by maintaining tight bid-ask spreads and managing inventory risk — when your position moves against you, you cut it quickly. Zillow's mistake was treating iBuying as a machine learning problem (predict the right price) rather than a trading problem (manage your book). They doubled down on bad positions and let inventory accumulate rather than cutting losses.

The pricing model used Zestimate (Zillow's AVM, automated valuation model) as a foundation, but housing markets have features that break most ML predictions: illiquidity, local idiosyncrasy, renovation cost uncertainty, and time-on-market risk. The model could predict average prices reasonably well but couldn't price tail risks — the houses that sit, the markets that soften, the renovations that go over budget. Those tail events blew up the program.

## Key points

- iBuying is fundamentally a market-making business, not a tech/ML business — the discipline is managing inventory and risk, not optimizing predictions.
- Zestimate could predict median home values reasonably well but failed at pricing the tail risks that determine profitability in thin-margin dealer businesses.
- Accumulating inventory in a softening market rather than cutting losses was the critical operational failure — the metallic balls the title references.
- Opendoor continues iBuying with stricter underwriting and faster turnover — the model isn't inherently broken, Zillow's execution was.
- More broadly: high prediction accuracy ≠ profitable trading. Market-making requires discipline around position sizing and loss-cutting, not just model accuracy.

[Original](https://www.stevenbuccini.com/zillow-offers)
