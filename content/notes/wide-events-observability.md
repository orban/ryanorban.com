---
title: A Practitioner's Guide to Wide Events
date: 2024-11-13
categories:
  - observability
  - monitoring
  - logging
  - engineering
  - developer-tools
description: Jeremy Morrell's practitioner guide to wide events in observability — high-cardinality single-row records that capture the full context of a request in one place, rather than scattered low-cardinality metrics and fragmented logs. Covers implementation details that other wide-events explainers skip.
params:
  source: pinboard
  sourceUrl: https://jeremymorrell.dev/blog/a-practitioners-guide-to-wide-events/
---

![A Practitioner's Guide to Wide Events](/images/notes/wide-events-observability.png)

## Summary

Jeremy Morrell's guide fills a gap: existing articles on wide events define the concept well but leave the implementation details to the reader. Wide events are high-cardinality single-row observability records that capture everything relevant about a request or operation in one structured event — user ID, feature flags, timing, outcomes, error codes, business context — rather than scattering this information across metrics, logs, and traces.

The practical advantage: debugging requires correlating data across multiple signals when using traditional observability (a metric tells you something is slow, a log tells you what happened, a trace tells you where, but correlating them is manual and error-prone). A wide event has all the context in one place. Tools like Honeycomb are built around this model — the query interface assumes you have high-cardinality fields available to slice and group on.

Implementation considerations the article addresses: which fields to include without over-logging, when to emit events (request-level vs. operation-level), handling high-cardinality at scale, and integrating with existing OpenTelemetry instrumentation. These are the details that trip up teams trying to move from traditional logging to wide events.

## Key points

- Wide events: high-cardinality single-row records capturing full request context in one place.
- Eliminates cross-signal correlation during debugging — everything you need is in one event.
- Covers implementation details: which fields, event granularity, high-cardinality at scale.
- Integrates with OpenTelemetry instrumentation — not a wholesale replacement.
- Foundational to tools like Honeycomb — understanding wide events unlocks their query model.

[Original](https://jeremymorrell.dev/blog/a-practitioners-guide-to-wide-events/)
