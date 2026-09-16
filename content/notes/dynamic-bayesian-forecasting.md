---
title: "Surfing Silver: Dynamic Bayesian Forecasting for Fun and Profit"
date: 2016-04-14
categories:
  - bayesian
  - forecasting
  - time-series
  - statistics
  - talk
description: Slides from a Data Popup talk on dynamic Bayesian forecasting — applying Bayesian state-space models to time series prediction with uncertainty quantification. One of the cleaner practitioner introductions to Bayesian time series methods from the mid-2010s data science speaker circuit.
params:
  source: pinboard
  sourceUrl: https://speakerdeck.com/clearspandex/surfing-silver-dynamic-bayesian-forecasting-for-fun-and-profit
---

## Summary

These slides from the Data Popup conference cover [dynamic Bayesian forecasting](/notes/dynamic-bayesian-forecasting/) — applying Bayesian state-space models to time series prediction. The dynamic in the title means the model parameters are allowed to evolve over time rather than being fixed, which makes it appropriate for non-stationary series: sales with seasonality shifts, user behavior that changes gradually, demand forecasting where the underlying patterns drift.

The Bayesian framing gives the forecasting approach two advantages over classical time series methods like ARIMA: explicit uncertainty quantification (the forecast is a distribution, not just a point estimate) and the ability to incorporate prior domain knowledge. When you have strong beliefs about seasonality or trend structure, you can encode them as priors rather than hoping the algorithm infers them from sparse data.

State-space models express the time series as the output of a hidden state process — the silver in the title is likely a reference to Nate Silver and the contemporary interest in probabilistic prediction. The approach is related to the Kalman filter (which is the Gaussian linear special case) but extends to non-Gaussian settings via particle filters and variational approximations.

## Key points

- Dynamic Bayesian model: parameters evolve over time — suited for non-stationary series.
- Forecast output is a distribution, providing confidence intervals naturally.
- State-space models separate observation noise from latent process noise.
- Priors allow encoding domain knowledge: seasonality structure, trend direction, change points.
- Related to Kalman filter for linear-Gaussian case; generalizes via particle filter / MCMC.
- Delivered at Data Popup Austin 2016 — part of the practitioner Bayesian methods movement.

[Original](https://speakerdeck.com/clearspandex/surfing-silver-dynamic-bayesian-forecasting-for-fun-and-profit)
