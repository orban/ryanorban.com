---
title: How a Kalman Filter Works, in Pictures
date: 2015-08-11
categories:
  - kalman-filter
  - signal-processing
  - statistics
  - bayesian
  - robotics
description: The clearest visual explanation of how a Kalman filter works — building from Gaussian distributions to the prediction-update cycle without losing the intuition in the math. A reference that makes the algorithm genuinely understandable rather than just computable.
params:
  source: pinboard
  sourceUrl: http://www.bzarg.com/p/how-a-kalman-filter-works-in-pictures/
---

## Summary

This article by Tim Babb is the definitive intuitive explanation of the Kalman filter — a recursive algorithm for estimating the state of a dynamic system when both your model and your sensors are uncertain. The core insight is that the filter maintains a Gaussian distribution over the system state at each timestep, and its two-step predict-update cycle is just the algebra of combining two Gaussian distributions.

The **predict step** uses a system model (a matrix F) to advance the state estimate forward in time. As time passes without new observations, uncertainty grows. The **update step** takes a new sensor reading (also modeled as a Gaussian, accounting for sensor noise), and the key operation is multiplying the two probability distributions together. Multiplying Gaussians produces another Gaussian centered between the two means, weighted by their respective uncertainties. This is the Kalman gain — a scalar (or matrix) that automatically blends prediction and measurement based on how uncertain each is.

What makes the Kalman filter elegant is that it exploits correlations: if position and velocity are correlated in the state estimate, the filter extracts information from velocity measurements to refine position estimates and vice versa. This is encoded in the covariance matrix, which the filter tracks alongside the state estimate. The filter is provably optimal for linear systems with Gaussian noise — and in practice works well on many nonlinear systems, especially when extended (EKF) or unscented (UKF) variants are applied.

## Key points

- Two-step cycle: **predict** (advance state, grow uncertainty) → **update** (incorporate measurement, shrink uncertainty).
- Kalman gain weights prediction vs. measurement by their respective uncertainties — high sensor noise → trust the model more.
- The filter is Bayesian inference applied recursively: each update is a posterior update given new evidence.
- Provably optimal for linear systems + Gaussian noise; extended (EKF) and unscented (UKF) variants handle nonlinearity.
- Used in GPS/INS fusion, robot localization, financial time series smoothing, and sensor fusion generally.
- The covariance matrix is as important as the state estimate — it encodes what the filter knows about correlations.

[Original](http://www.bzarg.com/p/how-a-kalman-filter-works-in-pictures/)
