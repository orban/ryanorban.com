---
title: Jawbone UP API (Unofficial)
date: 2013-06-21
categories:
  - wearables
  - api
  - quantified-self
  - jawbone
  - health-data
description: Eric Blue's unofficial API documentation for the Jawbone UP activity tracker — reverse-engineered from the mobile app's HTTP calls to expose sleep, step, and activity data programmatically. A 2013 snapshot of the unofficial API culture around early consumer wearables.
params:
  source: pinboard
  sourceUrl: http://eric-blue.com/projects/up-api/
---

## Summary

Eric Blue reverse-engineered the HTTP traffic between the Jawbone UP iOS app and Jawbone's backend servers to produce an unofficial API for the UP activity tracker. The UP had no official developer API in 2013 — Jawbone hadn't opened their platform — so practitioners who wanted to access their own sleep, step, and activity data programmatically had to intercept the app's calls and replicate them.

This was a common pattern in the early wearables era. Devices like the Jawbone UP, Fitbit (which had a similarly limited early API), and early Nike FuelBand attracted quantified-self enthusiasts who wanted their data in raw form to analyze outside the vendor's app. The unofficial API approach meant documenting authentication flows, endpoint paths, and response formats from network captures.

The Jawbone UP ultimately failed as a product: the original UP had manufacturing defects, Jawbone shipped multiple iterations, and the company went bankrupt in 2017 without successfully transitioning to a profitable health device business. The story of unofficial API culture around wearables ended with health data platforms like Apple HealthKit (2014) and Google Fit (2014) providing official aggregation layers that reduced the need for device-specific reverse engineering.

## Key points

- Reverse-engineered REST API: intercepted HTTPS traffic from the Jawbone UP mobile app to document authentication and endpoint structure.
- Personal data ownership: the motivation was getting your own data in a usable format — steps, sleep stages, meal logs — without being locked into Jawbone's visualization.
- Quantified self movement: 2013 was near the peak of the track everything era, with communities around personal data analysis growing around devices like the UP.
- Unofficial APIs vs platform openness: Jawbone eventually released a partial official API in 2014, but by then Apple HealthKit and Google Fit were providing device-agnostic data layers.
- Jawbone's bankruptcy (2017): the UP platform and all associated data went offline — a cautionary case for health data locked in proprietary systems.

[Original](http://eric-blue.com/projects/up-api/)
