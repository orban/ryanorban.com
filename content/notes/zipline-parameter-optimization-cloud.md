---
title: Parameter Optimization with Zipline, PiCloud, StarCluster, and IPython Parallel
date: 2013-04-12
categories:
  - quantitative-finance
  - algorithmic-trading
  - python
  - distributed-computing
  - backtesting
description: Quantopian's blog post on running parameter optimization for trading strategies using Zipline backtester on PiCloud, StarCluster, and IPython Parallel — a 2013 example of cloud-distributed backtesting before it was a product. Shows the DIY infrastructure that Quantopian later packaged into their platform.
params:
  source: pinboard
  sourceUrl: http://blog.quantopian.com/zipline_in_the_cloud/
---

## Summary

Quantopian published this post in 2013 showing how to run parameter sweeps for algorithmic trading strategies by distributing Zipline backtests across cloud compute. Zipline was Quantopian's open-source Python backtesting library — an event-driven simulator that replayed historical market data and evaluated strategy logic. The problem: finding good parameters (moving average windows, threshold values, position sizes) requires running the backtest many times with different inputs, which is embarrassingly parallel but serially slow.

The solution combined three tools: PiCloud (a Python cloud execution service that could run arbitrary Python functions on EC2 instances), StarCluster (a toolkit for spinning up EC2 HPC clusters with SGE job scheduling), and IPython Parallel (distributed execution of Python code across a pool of engines). Any of these could scatter backtests across many cores; the post probably showed multiple approaches. The result: a parameter optimization that might take hours on a single machine finished in minutes across a cluster.

This was a meaningful technical milestone for retail quantitative finance. Parameter optimization (grid search or random search) is standard practice in professional quant shops but was computationally inaccessible to individual researchers in 2012. The democratization of cloud compute via EC2 — combined with Python tooling that abstracted away cluster management — made sweep-based strategy research accessible outside of institutions with dedicated hardware.

## Key points

- Zipline: Quantopian's open-source event-driven backtesting library — the engine underneath Quantopian's platform.
- PiCloud: Python cloud execution platform that let you call `cloud.call(func, *args)` and run arbitrary Python on EC2 without managing servers.
- StarCluster: AWS toolkit for launching HPC clusters with SGE (Sun Grid Engine) job scheduling — popular in academic computing.
- IPython Parallel: distributed Python execution via a cluster of IPython engines — allowed `dview.map_sync(backtest_func, param_grid)` style parallelism.
- Parameter optimization for trading strategies: grid search or random search across hyperparameter space — embarrassingly parallel, well-suited to cloud scatter-gather.
- Precursor to Quantopian's later integrated research environment and optimizer tools.

[Original](http://blog.quantopian.com/zipline_in_the_cloud/)
