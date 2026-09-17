---
title: All Dashboards Should be Feeds
date: 2013-01-09
categories:
  - information-architecture
  - dashboards
  - feeds
  - product-design
  - anil-dash
description: Anil Dash's 2013 argument that dashboards should be replaced by feeds — because feeds are scannable, show change over time, and can be subscribed to, while dashboards require active navigation and miss temporal context. A prescient critique of how enterprise analytics was being designed.
params:
  source: pinboard
  sourceUrl: http://dashes.com/anil/2013/01/all-dashboards-should-be-feeds.html
---

## Summary

Anil Dash argued in January 2013 that the dashboard metaphor for data display was fundamentally inferior to the feed metaphor for most information consumption. A dashboard is a static snapshot: you navigate to it, look at current state, and leave. A feed is a stream of events ordered by time: it comes to you, shows what changed, and gives you temporal context without requiring navigation.

The practical case: when you visit a dashboard, you're trying to detect change ("has anything significant happened?"). But dashboards present state, not change — you have to mentally diff the current view against your memory of the last visit. Feeds surface change directly, are scannable rather than requiring attention to every metric, and can be subscribed to with different urgency levels. They also naturally preserve history rather than overwriting it.

Dash's framing was particularly aimed at enterprise analytics and monitoring tools — the Salesforce dashboards, BI suites, and business reporting systems of 2013 that required people to remember to visit and then mentally reconstruct what had changed. The activity feed model from social networks (Facebook, Twitter) had proved better for this — people checked feeds constantly precisely because feeds surfaced what mattered without requiring active comparison.

This argument is still relevant: modern dashboards in observability (Datadog, Grafana) and product analytics (Mixpanel, Amplitude) add alerting and change detection precisely because static dashboards fail to surface anomalies.

## Key points

- Dashboard vs feed mental models: dashboards show state, feeds show change — change is almost always what you actually care about
- Scannability: feeds are designed to be scanned quickly; dashboards require attention to each metric
- Temporal context: feeds preserve history naturally; dashboards show only the latest state
- The alerting workaround: most dashboards require bolted-on alerts because they don't surface change — feeds make change the primary signal
- Modern observability tools have converged on this: alerts, incident timelines, and deployment feeds are how engineers actually stay aware

[Original](http://dashes.com/anil/2013/01/all-dashboards-should-be-feeds.html)
