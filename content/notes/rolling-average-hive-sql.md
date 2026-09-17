---
title: Rolling Average in Hive
date: 2013-10-28
categories:
  - hive
  - sql
  - hadoop
  - analytics
  - data-engineering
description: Brent Ozar's walkthrough of computing rolling averages in Hive — a problem that looks like a simple SQL query but requires window functions or self-joins in Hive's then-limited SQL dialect. A practical data engineering puzzle from the Hadoop era.
params:
  source: pinboard
  sourceUrl: http://www.brentozar.com/archive/2013/01/when-a-query-isnt-quite-a-query/
---

## Summary

Computing a rolling average (also called a moving average) in Hive was a harder problem than it sounds in 2013. Standard SQL window functions like `AVG() OVER (ORDER BY date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW)` weren't fully supported in early Hive versions, requiring workarounds through self-joins or UDFs.

Brent Ozar's framing — "when a query isn't quite a query" — captures the essential tension: Hive presented a SQL-like interface, but its MapReduce execution model meant certain query patterns that were simple in a traditional relational database were expensive or impossible. Rolling aggregations require ordered access across rows, which doesn't map cleanly to MapReduce's embarrassingly parallel model.

This was a practical problem for data analysts working with time-series data on Hadoop clusters — metrics smoothing, trend analysis, and anomaly detection all require sliding window aggregations. The solutions were often ugly: multiple map-reduce passes or pre-bucketing data into time windows in the ETL layer before the query hit Hive.

## Key points

- Rolling average requires ordered row access — fundamentally awkward in Hive on MapReduce, which favors independent record processing.
- Early Hive had incomplete SQL window function support; workarounds used self-joins or custom UDFs.
- Apache Spark and modern Hive versions (with Tez execution) later added full window functions, making this class of problem much simpler.
- Practical consequence for data engineering: push sliding window logic into ETL preprocessing when the query engine can't express it efficiently.
- Reflects the broader pattern of SQL-on-Hadoop tools gradually filling in the gaps between their surface SQL APIs and the underlying execution model.

[Original](http://www.brentozar.com/archive/2013/01/when-a-query-isnt-quite-a-query/)
