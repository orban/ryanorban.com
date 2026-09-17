---
title: "The Next Big Thing You Missed: Keen IO's Plot to Beat Google at Big Data"
date: 2014-01-29
categories:
  - analytics
  - startups
  - big-data
  - api
  - saas
description: Wired's 2014 profile of Keen IO — a startup offering analytics-as-an-API to let developers add event tracking without building their own data infrastructure. A bet that the analytics pipeline problem was common enough to be sold as a service.
params:
  source: pinboard
  sourceUrl: http://www.wired.com/business/2014/01/keen/
---

## Summary

Wired covered Keen IO when it was still a young San Francisco startup with an audacious pitch: developer-friendly analytics as an API. The idea was that every company building a web or mobile product needed to track events, store them, and query them — and building that infrastructure from scratch was expensive and undifferentiated. Keen IO offered the whole stack (event ingestion, storage, query, and visualization) through a JSON API that any developer could call in a few lines of code.

The beat Google at big data framing in the Wired headline reflects the competitive landscape: Google Analytics was the default analytics tool but was limited to web traffic metrics, not arbitrary custom events. Companies wanting to track product-specific events (purchases, feature usage, game actions) had to either build custom data pipelines into Hadoop or use less-capable alternatives. Keen IO positioned itself in this gap: arbitrarily flexible event tracking with SQL-like query capabilities, without the infrastructure burden.

The 2014 big data ecosystem was maturing but still operationally expensive — running Hadoop required dedicated expertise. The API-first approach that Keen IO pioneered influenced how developer analytics tools were built afterward. The same pattern — complex infrastructure wrapped in a clean API — became the template for segment.com, Amplitude, Mixpanel, and eventually Snowflake's developer-focused data warehouse.

## Key points

- Keen IO: event analytics as an API — ingest arbitrary JSON events, query them with a flexible query language, visualize results without managing infrastructure.
- Developer-first positioning: the customer was the engineer who would rather call an API than configure a data warehouse.
- Market gap: Google Analytics covered web traffic; no good solution existed for custom application events without building your own pipeline.
- Business model: usage-based pricing on events stored and queries run — aligned with product growth.
- Historical pattern: Keen IO was early in the "analytics infrastructure as a service" category that Segment, Amplitude, and Snowflake later defined.

[Original](http://www.wired.com/business/2014/01/keen/)
