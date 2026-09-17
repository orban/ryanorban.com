---
title: "Cube: The Semantic Layer for Data Applications"
date: 2023-05-01
categories:
  - data
  - analytics
  - open-source
  - developer-tools
  - api
description: Cube is an open-source semantic layer for building data applications — it sits between your data sources and your frontend, defining metrics, dimensions, and access control in a single place. Eliminates duplicated metric logic across BI tools, APIs, and embedded analytics.
params:
  source: pinboard
  sourceUrl: https://github.com/cube-js/cube
---

![Cube: The Semantic Layer for Data Applications](/images/notes/cube-js.png)

## Summary

Cube (formerly Cube.js) is an open-source semantic layer that sits between data sources and data consumers — BI tools, embedded analytics, APIs, notebooks. You define your metrics, dimensions, and access rules once in Cube's schema language, and Cube generates optimized SQL and exposes the results via a REST API, GraphQL API, or WebSocket connection. The goal is eliminating the proliferation of metric definitions scattered across Looker, Metabase, custom SQL queries, and app code.

The semantic layer concept is about single-source-of-truth for business logic: instead of monthly recurring revenue being defined five different ways in five different places, it's defined once in Cube and every consumer reads the same definition. Cube handles query optimization (including pre-aggregations for large datasets), caching, and multi-tenancy. This makes it valuable for organizations where data is consumed both by analysts using BI tools and by engineers building embedded analytics in products.

Cube competes with dbt Semantic Layer, LookML (in Looker), and Lightdash for the semantic layer space. It differentiates on being headless — no bundled BI tool — and on its API-first approach that works equally well for embedded analytics as for analyst tooling. The open-source core is solid; the cloud offering adds managed infrastructure, role-based access control, and integrations.

## Key points

- Semantic layer: define metrics/dimensions once, expose via REST API, GraphQL, or WebSocket.
- Handles pre-aggregations, query optimization, caching — not just routing queries through.
- Single source of truth for business logic across BI tools, embedded analytics, and application APIs.
- Headless and API-first — differentiates from BI-bundled semantic layers like LookML.
- Open source on GitHub (cube-js/cube); cloud managed offering available.
- Competes with dbt Semantic Layer and Lightdash for the standalone semantic layer space.

[Original](https://github.com/cube-js/cube)
