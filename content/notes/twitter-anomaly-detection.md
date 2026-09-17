---
title: Introducing Practical and Robust Anomaly Detection in a Time Series
date: 2015-01-06
categories:
  - anomaly-detection
  - time-series
  - statistics
  - open-source
  - twitter
description: Twitter's 2015 release of AnomalyDetection — an open-source R library using STL decomposition and the Generalized ESD test to find anomalies in time series. One of the first production-grade anomaly detection tools to be open-sourced by a major tech company.
params:
  source: pinboard
  sourceUrl: https://blog.twitter.com/2015/introducing-practical-and-robust-anomaly-detection-in-a-time-series
---

## Summary

Twitter released AnomalyDetection, an open-source R library for robust time-series anomaly detection, in early 2015. The technical approach combines STL decomposition (Seasonal-Trend decomposition using Loess) with the Generalized ESD test (Extreme Studentized Deviate) — a statistically principled method that handles seasonality, noise, and multiple anomalies in a single pass.

The core problem the library solves: naive anomaly detection (e.g., flag anything beyond 3 standard deviations) fails badly on real-world time series with seasonal patterns. Traffic to a website is higher during business hours and lower on weekends — deviations from the seasonal pattern are the signal, not deviations from the global mean. STL decomposition separates the seasonal, trend, and residual components; the ESD test then finds statistical outliers in the residual.

The Generalized ESD test is an improvement on Grubbs' test that handles multiple outliers simultaneously without requiring you to specify how many there are in advance. This matters in practice: real anomaly events often span multiple consecutive points, and the test needs to identify them without one masking another.

## Key points

- STL decomposition removes seasonality + trend before anomaly testing — essential for real-world time series.
- Generalized ESD test finds multiple outliers without prespecifying count — avoids masking effect.
- Open-sourced in R — one of the first production-grade anomaly detection tools from a major tech company.
- Handles both point anomalies (single outlier) and contextual anomalies (unusual given seasonal context).
- Used at Twitter for metrics monitoring; influenced a wave of similar tools (Luminol, Prophet).
- Facebook Prophet (2017) is the successor in terms of industry influence — also handles seasonality but focuses on forecasting.

[Original](https://blog.twitter.com/2015/introducing-practical-and-robust-anomaly-detection-in-a-time-series)
