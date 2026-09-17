---
title: A Data Science Chat with Kevin Novak from Uber
date: 2014-07-10
categories:
  - data-science
  - uber
  - video
  - career
  - industry
description: A talk by Kevin Novak, data scientist at Uber, covering how Uber approaches data science in practice — from surge pricing models to driver supply forecasting. An early window into how a hypergrowth tech company used data science operationally.
params:
  source: pinboard
  sourceUrl: https://www.youtube.com/watch?v=HIbzibEAcr8
---

## Summary

Kevin Novak was an early data science lead at Uber during its hypergrowth period, making this YouTube talk a primary source for how Uber operationalized data science in 2014. Uber at this time was rapidly expanding cities and building the models that made the core product work: surge pricing (dynamic pricing to balance supply and demand), driver supply forecasting, ETA prediction, and market expansion analytics.

The data hacking framing that Ryan Orban noted from this talk reflects Uber's culture: move fast, use data aggressively to make decisions, and don't wait for perfect methodology when a quick model will do. This was the operational data science philosophy that contrasted with academic or slow-moving enterprise approaches — building models that work in production, not models that are theoretically elegant.

Uber's data science stack in 2014 used a mix of Python, R, SQL, and early Hadoop-based infrastructure for the scale analytics. The interesting tension in talks like this: Uber was simultaneously doing impressive engineering (real-time pricing models at scale) and cowboy data analysis (A/B testing corners cut, questionable methodology).

## Key points

- Surge pricing as a real-time supply-demand matching problem: the model responds to driver availability and ride request rates, requiring sub-minute latency.
- Geospatial data is central to Uber's data science: driver and rider location, routing, coverage area analysis — a domain many data scientists hadn't worked with before.
- The "data hacking" framing: bias for action and approximate models over slow perfect analysis — a tension with statistical rigor that hypergrowth companies navigate continuously.
- Uber in 2014 was a model for operationally-embedded data science — models directly affecting pricing, dispatching, and incentives, not just informing decisions.
- Kevin Novak later became Chief Data Officer at Roofstock — his career trajectory follows the DS-to-CDO path that became common for early practitioners.

[Original](https://www.youtube.com/watch?v=HIbzibEAcr8)
