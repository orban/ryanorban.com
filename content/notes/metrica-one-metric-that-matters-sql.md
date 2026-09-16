---
title: Metrica — Finding Your One Metric That Matters Using SQL
date: 2013-04-17
categories:
  - analytics
  - metrics
  - sql
  - startups
  - product
description: Metrica's post on using SQL to identify your One Metric That Matters — the single KPI that best captures a startup's core health. A practical guide to distilling complex product data into a focus metric.
params:
  source: pinboard
  sourceUrl: http://blog.getmetrica.com/post/48153893395/finding-your-one-metric-that-matters-using-sql
---

## Summary

One Metric That Matters (OMTM) was a framework popularized in 2013 by Alistair Croll and Ben Yoskovitz in *Lean Analytics*. The idea: at any given stage, a startup should identify a single metric that best represents its current growth problem, focus everything on moving it, then pick a new one for the next stage. Metrica's post translated this concept into concrete SQL queries — showing how to build the metric from raw event logs or a relational analytics database.

The value of the OMTM framing is focus under uncertainty. Early-stage analytics produce hundreds of metrics: DAU, retention, conversion funnels, revenue, session length. When everything is tracked but nothing is prioritized, teams optimize for the wrong things or optimize nothing at all. OMTM forces a bet: right now, what is the one number that tells us if we're succeeding? That question cuts through noise and aligns product, engineering, and growth efforts.

The SQL angle is practical. Most analytics databases in 2013 lived in PostgreSQL, MySQL, or early columnar stores like Redshift. Writing OMTM queries in SQL meant product managers and analysts could compute the metric directly from raw data without needing a BI tool, and the query itself became a precise specification of what the metric meant — removing ambiguity about how it was calculated.

## Key points

- One Metric That Matters is a stage-gated framing: pick the single number that defines success for your current growth phase, move it, then pick the next one.
- SQL as a metric specification language: a query defines exactly what a metric means and how it's computed from raw data, eliminating definitional ambiguity.
- Common OMTM candidates: DAU/MAU ratio (engagement), retention curve slope (product-market fit), LTV:CAC ratio (unit economics), activation rate (onboarding).
- Metrica was a lightweight analytics platform aimed at making this kind of metric tracking accessible without a dedicated data team.
- The framework connects to pirate metrics (AARRR) and the broader 2013 lean analytics movement in the startup ecosystem.

[Original](http://blog.getmetrica.com/post/48153893395/finding-your-one-metric-that-matters-using-sql)
