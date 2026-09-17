---
title: Scoring Aave Accounts for Creditworthiness
date: 2022-07-19
categories:
  - defi
  - credit-scoring
  - machine-learning
  - blockchain
description: Cred Protocol's paper (arXiv:2207.07008) proposing a credit scoring system for Aave v2 accounts using a tree-based classifier trained to predict 'position delinquency' — whether a borrow position's health factor will drop below 1 within 90 days. It's a direct attempt to bring FICO-style credit infrastructure to DeFi, enabling undercollateralized lending.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/cred.pdf
---

## Summary

This paper (arXiv:2207.07008, July 2022) from Cred Protocol proposes a credit scoring system for Ethereum accounts that interact with Aave v2, a major DeFi liquidity protocol. The central challenge is that Aave has no concept of discrete loans — instead each account holds a dynamic "position" consisting of borrowed and collateral assets, with creditworthiness captured by a single aggregate statistic called the health factor (HF = weighted collateral value / total debt). When HF drops below 1, the position becomes eligible for liquidation. The paper reframes traditional binary credit classification around this concept: predicting whether a new position will become eligible for liquidation within 90 days.

The authors train a tree-based classifier (the tree-based variant outperforms logistic regression and several baselines) on the Aave v2 Health Factor Dataset, a 15-minute interval time series of positions and health factors. Features include account age, historical health factor aggregations, interaction patterns with the protocol, and asset composition. A notable finding is that a simple single-feature baseline — counting the number of historical blocks where HF < 1 — achieves AUC of 0.932, nearly matching the full model, which makes intuitive sense: past financial behavior is a strong predictor of future behavior, and accounts can use smart contracts to automatically rebalance positions.

The final Cred score is an integer in [300, 1000], mapped from the classifier's delinquency probability via a quantile transform calibrated to approximate the empirical FICO score distribution. The paper frames this as infrastructure for enabling undercollateralized lending in DeFi — currently most protocols require 150-348% collateralization precisely because no reliable credit signal exists.

## Key points

- Aave v2 has no atomic loans, so traditional credit scoring model assumptions don't apply; the paper redefines delinquency as HF < 1 within 90 days of opening a position
- A single-feature baseline (count of historical blocks with HF < 1) achieves AUC 0.932 — showing that on-chain behavioral history is highly informative even without complex modeling
- The tree-based classifier outperforms logistic regression and random/simple baselines across all test folds; evaluation uses out-of-fold AUC on a temporal holdout of ~2,500 rows
- Quantile transform maps predicted delinquency probability to an integer score calibrated to resemble the FICO score distribution (300-850 range stretched to 300-1000)
- Applications beyond lending: risk-adjusted portfolio construction, assessing DAO or multi-sig wallet fidelity, and intrinsically motivating constructive on-chain financial behavior

[Original](file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/cred.pdf)
