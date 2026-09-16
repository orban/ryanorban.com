---
title: "ThetaGang: Options Premium Collection Bot"
date: 2021-01-30
categories:
  - finance
  - options
  - automation
  - python
  - ibkr
description: ThetaGang is an open-source Python bot for Interactive Brokers that automates theta-positive options strategies — selling covered calls and cash-secured puts to collect premium. Designed for passive income from options rather than directional trading.
params:
  source: pinboard
  sourceUrl: https://github.com/brndnmtthws/thetagang
---

## Summary

ThetaGang is an open-source Python trading bot for Interactive Brokers (IBKR) that automates theta-positive options strategies. The strategy is mechanical: sell covered calls on positions you own and cash-secured puts on stocks you'd be willing to buy, collecting options premium as recurring income. The name refers to theta decay — the rate at which options lose time value as expiration approaches. Sellers of options benefit from this decay.

The implementation connects to IBKR's TWS API to query positions, check account balance, select strikes based on delta targets, and submit orders automatically. Configuration is done via a YAML file specifying which tickers to trade, target delta for strike selection, and position sizing rules. The bot runs on a schedule, checking whether positions need to be rolled (moved to the next expiration) or new positions opened.

This is an example of a niche but concrete algorithmic trading application: not high-frequency trading or machine learning-based alpha, but systematic execution of a well-understood options strategy that most retail investors run manually. The main risks are assignment (being forced to buy or sell shares) and model risk (the strategy assumes you're comfortable owning the underlying). It's useful as a reference implementation for anyone building their own IBKR automation.

## Key points

- Automates covered call and cash-secured put selling via the IBKR TWS API — collect options premium without manual order entry.
- Delta-targeted strike selection: configure how far out-of-the-money to sell based on your risk tolerance.
- YAML configuration for tickers, position sizing, roll timing, and account constraints.
- All execution happens through Interactive Brokers' standard API — no exchange connectivity to manage.
- Useful reference for Python algorithmic trading automation patterns beyond just strategy logic.

[Original](https://github.com/brndnmtthws/thetagang) → GitHub
