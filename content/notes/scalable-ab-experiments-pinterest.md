---
title: Scalable A/B Experiments at Pinterest
date: 2014-08-21
categories:
  - a-b-testing
  - experimentation
  - statistics
  - pinterest
  - data-engineering
description: Pinterest's engineering blog on how they built scalable A/B testing infrastructure — covering experiment assignment, metric computation, and statistical significance at Pinterest's scale. A practitioner's account of the gap between textbook A/B testing and production experimentation.
params:
  source: pinboard
  sourceUrl: http://engineering.pinterest.com/post/95378137929/scalable-a-b-experiments-at-pinterest
---

## Summary

Pinterest's engineering team describes their A/B testing infrastructure in 2014, when Pinterest had hundreds of millions of pins and needed experimentation at scale. The engineering challenges at Pinterest's scale go well beyond what a textbook A/B test covers: user assignment that's consistent across sessions and devices, metric computation across petabytes of event logs, and statistical frameworks that handle the multiple comparison problem across many simultaneous experiments.

The core infrastructure problem: users must be consistently assigned to the same experiment bucket across sessions, devices, and surface areas. This requires a deterministic hash function on user ID (not random per-session), a central experiment configuration store, and client/server libraries that read the configuration and apply the hash consistently. At Pinterest's scale, the assignment system needs to be available and fast — it's in the critical path of every page load.

Metric computation is the other hard part. A/B test results require computing metrics (CTR, engagement, retention) for two groups across time. At scale, this means running aggregation jobs over event log data — the statistical computations are simple but the data pipeline engineering is substantial. Pinterest likely ran these on Hadoop or early Spark jobs, with the results feeding into dashboards that tracked experiment health.

## Key points

- User assignment: deterministic hash on user ID — consistent across sessions/devices, unlike per-request randomization.
- Experiment config store: centralized, fast-read system that defines which users are in which bucket.
- Metric computation: aggregation over event logs (clicks, pins, engagement) per experiment arm — the ETL pipeline challenge.
- Multiple experiments simultaneously: need to detect and control for interaction effects between concurrent experiments.
- Novelty effect: new features show artificial engagement spikes at launch — run experiments long enough to wash this out.
- Pinterest's scale made standard textbook approaches insufficient — motivated the development of specialized experimentation platforms.

[Original](http://engineering.pinterest.com/post/95378137929/scalable-a-b-experiments-at-pinterest)
