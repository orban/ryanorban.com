---
title: "The Utilization Gap: Big Data's Biggest Challenge"
date: 2013-03-17
categories:
  - big-data
  - strategy
  - analytics
  - business-intelligence
  - organizational
description: Forbes on the gap between data collection capability and actual data use in 2013 — organizations were investing heavily in Hadoop and data warehouses while most of the collected data sat unanalyzed. The insight that technology was not the bottleneck; talent and culture were.
params:
  source: pinboard
  sourceUrl: http://www.forbes.com/sites/christinemoorman/2013/03/17/the-utilization-gap-big-datas-biggest-challenge/
---

![The Utilization Gap: Big Data's Biggest Challenge](/images/notes/big-data-utilization-gap.png)

## Summary

By 2013, the big data narrative had shifted from "how do we store and process this data? to a harder question: why aren't we actually using it?" The Forbes piece identified what it called the utilization gap — the space between the data organizations were collecting and the decisions that data was actually informing. Most enterprises had invested in Hadoop clusters, data warehouses, and ETL pipelines, but the analysts and decision-makers who needed to act on the data were still working from gut feeling and spreadsheets.

The diagnosis was structural, not technological. The data was there; the query tools existed; Tableau and early business intelligence platforms made dashboards accessible. The bottleneck was organizational: most companies lacked data analysts who could bridge technical data infrastructure and business questions. SQL literacy was rare in business units; data teams were siloed from decision-makers; the cultural norm of showing your work with data hadn't taken hold outside of specific functions like finance and marketing.

The second bottleneck was time-to-insight. Hadoop MapReduce queries that ran for hours weren't useful for real-time operational decisions. Even the organizations with both the data and the analysts were constrained by infrastructure that made exploration slow and expensive. This is what made Impala, Presto, and eventually Apache Spark SQL important — they compressed the query feedback loop from hours to seconds, which changed the economics of exploratory analysis.

## Key points

- The utilization gap: organizations collecting exponentially more data while the fraction of that data informing decisions was growing much more slowly.
- Bottleneck in 2013 was **talent and culture**, not technology — data analysts who could translate business questions to queries were scarce.
- Time-to-insight as a second bottleneck: Hadoop MapReduce batch latency made exploratory analysis impractical; interactive SQL engines (Impala, Presto) were the response.
- Data literacy in business units was the missing layer — the gap between technical data teams and non-technical decision makers.
- The thesis proved durable: data-driven culture has been a management consulting topic for 15+ years precisely because it's hard to achieve.

[Original](http://www.forbes.com/sites/christinemoorman/2013/03/17/the-utilization-gap-big-datas-biggest-challenge/)
