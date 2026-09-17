---
title: Quandl Python API
date: 2013-04-05
categories:
  - python
  - data
  - finance
  - api
  - quandl
description: Quandl's Python API documentation — the quandl Python library that let researchers pull financial and economic time-series data directly into pandas DataFrames with a single function call. The key practical interface for data scientists using Quandl.
params:
  source: pinboard
  sourceUrl: http://www.quandl.com/help/python
---

## Summary

The Quandl Python library provided a clean interface for pulling financial and economic data directly into Python analysis workflows. The core function — `quandl.get("WIKI/AAPL")` — returned a pandas DataFrame with historical prices, volumes, and corporate action adjustments for any dataset in Quandl's catalog. This single-line data access was significant in 2013: getting clean, adjusted historical price data previously required either a Bloomberg Terminal, scraping Yahoo Finance, or manual CSV downloads.

The library abstracted authentication (API key passed once), pagination (large date ranges fetched automatically), and format conversion (always returns a DataFrame indexed by date) — the three most tedious parts of working with financial data APIs. It also supported filtering by date range, frequency transformation (daily → monthly), and column selection, making it behave like a structured query against a time-series database.

For quantitative finance researchers and students using tools like Zipline, NumPy, and SciPy, Quandl's Python client was the standard way to get historical data into a backtest or model. Quantopian integrated Quandl data directly into their research environment for similar reasons. The simplicity was the point: `import quandl; data = quandl.get("FRED/GDP")` and you have US GDP data in a DataFrame — no manual steps required.

## Key points

- `quandl.get()` returns a pandas DataFrame indexed by date — directly usable in any Python data analysis workflow.
- Covers FRED, World Bank, historical stock prices (WIKI dataset), commodity futures, FX rates, and hundreds of other free datasets.
- API key authentication: rate-limited to 50 calls/day without a key, unlimited with free registration.
- Date range and frequency parameters: `start_date`, `end_date`, `collapse="monthly"` — built-in resampling.
- Used extensively with Zipline for backtesting trading strategies on Quantopian.

[Original](http://www.quandl.com/help/python)
