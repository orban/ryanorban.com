---
title: Quandl — Intelligent Search for Numerical Data
date: 2013-04-05
categories:
  - data
  - finance
  - economics
  - api
  - open-data
description: Quandl is a search engine for numerical data — financial series, economic indicators, and alternative datasets unified behind a single API. In 2013 it was the go-to free source for quantitative researchers who needed structured time-series data without Bloomberg Terminal access.
params:
  source: pinboard
  sourceUrl: http://www.quandl.com/
---

## Summary

Quandl launched as a search engine for numerical and financial data — a unified interface for finding and downloading time-series datasets that were otherwise scattered across government portals, academic databases, and proprietary sources. In 2013, if you were building a quantitative finance model or an economics analysis and you didn't have access to a Bloomberg Terminal or Reuters feed, your options were terrible: manually downloading CSV files from FRED, hunting through World Bank portals, or scraping data from websites. Quandl aggregated hundreds of free and premium datasets behind a single search interface and API.

The business model was freemium: many datasets (government economic indicators, FRED series, historical stock prices) were free; proprietary or curated alternative datasets (satellite imagery analysis, credit card spending data, corporate governance metrics) were premium. The API was the key product — `quandl.get("WIKI/GOOGL")` returned a pandas DataFrame with GOOGL historical prices, making it trivially easy to incorporate market data into Python or R analysis workflows.

For the emerging algorithmic trading community on platforms like Quantopian, Quandl was the default data source for non-subscribers. It solved the where do I get data? problem that blocked many researchers from ever writing a backtest. Nasdaq later acquired Quandl in 2018, integrating it into their data licensing business.

## Key points

- Unified data API: single `quandl.get()` call across hundreds of datasets — abstracted away the per-source authentication and format differences.
- Core free datasets: FRED (Fed economic data), World Bank, historical stock prices from WIKI (community-maintained), options data.
- Alternative data marketplace: early mover in selling non-traditional datasets to quants — satellite, credit card transactions, web traffic.
- Quantopian integration: Quandl was the default external data source for Quantopian's backtesting environment.
- Acquired by Nasdaq in 2018 — validated the alternative data market that Quandl helped create.

[Original](http://www.quandl.com/)
