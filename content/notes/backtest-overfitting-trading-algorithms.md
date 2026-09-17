---
title: "All That Glitters Is Not Gold: Comparing Backtest and Out-of-Sample Performance on a Large Cohort of Trading Algorithms"
date: 2022-03-30
categories:
  - quantitative-finance
  - overfitting
  - backtesting
  - machine-learning
  - trading
description: ""
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/wiecki2016.pdf
---

blurb: "Wiecki, Campbell, Lent, and Stauth at Quantopian study a large cohort of live trading algorithms and confirm empirically that backtest performance is a poor predictor of out-of-sample returns, with overfit strategies systematically underperforming live. A rigorous quantitative study of the overfitting problem in algorithmic trading."

## Summary

Thomas Wiecki, Andrew Campbell, Justin Lent, and Jessica Stauth at Quantopian conduct an empirical study of backtest overfitting in systematic trading strategies. The core problem is well-known in theory: backtesting on historical data and optimizing hyperparameters to that data creates strategies that exploit noise rather than signal. When deployed live, such strategies tend to revert to random or negative returns. This paper tests that hypothesis at scale with a cohort of real algorithms submitted to Quantopian's platform.

The results confirm the theoretical concern: backtest Sharpe ratio and in-sample performance are weak predictors of out-of-sample performance. Algorithms that looked exceptional in backtests frequently underperformed in live trading, with the degree of underperformance correlated with how much the in-sample period was used for optimization. The paper draws on ideas from multiple hypothesis testing and deflated Sharpe ratio work to characterize the severity of the problem.

The practical implications run deep for algorithmic trading and more broadly for any machine learning application where model selection is done on historical data with many hyperparameters. The same dynamics appear in neural architecture search and any setting where repeated evaluation on a fixed held-out set inflates apparent performance. Wiecki's broader work on Bayesian methods for finance (through PyMC3) provides a complementary angle: explicitly modeling uncertainty rather than point-optimizing on backtest metrics.

## Key points

- Large-cohort empirical confirmation that backtest performance is a poor predictor of live out-of-sample returns
- Sharpe ratio inflation from repeated optimization on historical data — multiple testing problem applied to strategy development
- Strategies aggressively fit to in-sample data show systematic regression to the mean or worse when deployed live
- Connects to deflated Sharpe ratio and multiple hypothesis testing frameworks for adjusting performance claims
- Published in Journal of Investing, 2016, by Quantopian data science team (Wiecki, Campbell, Lent, Stauth)

[Original paper](file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/wiecki2016.pdf)
