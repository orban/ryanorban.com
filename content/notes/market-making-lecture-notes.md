---
title: Market Making (Lecture Notes 04a)
date: 2022-09-19
categories:
  - finance
  - market-making
  - market-microstructure
  - trading
description: Lecture notes (module 4a) on market making — the practice of continuously quoting bid and ask prices to provide liquidity in financial markets, managing inventory risk and adverse selection in exchange for earning the spread. A core topic in market microstructure theory with direct practical application in algorithmic trading and quantitative finance.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/04a_MarketMaking.pdf
---

## Summary

These lecture notes cover market making — the practice of continuously posting both bid and ask prices in a financial instrument to earn the bid-ask spread while managing the associated risks. A market maker is the counterparty of last resort: they commit to buying when sellers arrive and selling when buyers arrive, providing liquidity that makes markets function. In return they earn the spread, but they accept two interacting risks: inventory risk (accumulating unwanted positions) and adverse selection risk (trading against informed counterparties who know the true value).

The foundational Avellaneda-Stoikov model formalizes market making as a stochastic control problem. A risk-averse market maker quotes asymmetric spreads as a function of current inventory: when long, they shade their quotes to attract sellers and deter buyers, mean-reverting their inventory toward zero. The optimal quotes depend on the market maker's risk aversion, the volatility of the underlying, and the time remaining in the trading session. This model is widely taught as the starting point for quantitative market making.

Adverse selection is the deeper problem. In models like Glosten-Milgrom, informed traders know the true value and will always trade against the market maker at the posted price — meaning every trade with an informed counterparty loses money. The market maker can only survive by earning enough spread from uninformed (noise traders) to offset losses to the informed. This creates a fundamental tension in market design: tighter spreads attract more order flow but expose the maker to more adverse selection. Real market microstructure — Level 2 order book dynamics, HFT strategies, co-location — can be read as attempts to navigate this tension.

## Key points

- Avellaneda-Stoikov model: optimal market making via stochastic control — quotes are a function of inventory, volatility, risk aversion, and time horizon
- Adverse selection: informed traders extract value from the market maker; only uninformed (noise trader) flow is profitable — forces makers to manage who they trade with
- Glosten-Milgrom model: bid-ask spread as equilibrium outcome when fraction of informed traders is positive — tighter spreads only viable if informed fraction is low
- Inventory risk management: asymmetric quoting (skewing) to mean-revert inventory; more aggressive skew with higher risk aversion
- Connects to high-frequency trading, algorithmic market making, and electronic markets where these models are implemented in microsecond-scale trading systems

[Source PDF](file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/04a_MarketMaking.pdf)
