---
title: Google Opens BigQuery Data Analytics to All
date: 2012-07-07
categories:
  - big-data
  - google
  - cloud
  - sql
  - data-analytics
description: GigaOM coverage of Google opening BigQuery to all developers in 2012 — the productization of Dremel as a cloud service. The moment when interactive SQL over petabyte datasets became a commercial product rather than a Google-internal tool.
params:
  source: pinboard
  sourceUrl: http://gigaom.com/cloud/google-opens-up-its-biq-query-data-analytics-service-to-all/
---

![Google Opens BigQuery Data Analytics to All](/images/notes/google-bigquery-opens-to-all.png)

## Summary

In July 2012, Google moved Google BigQuery from limited preview to general availability, making the Dremel-powered interactive query service accessible to any developer with a Google Cloud account. This was significant: before BigQuery, running SQL-like queries over petabyte-scale datasets required building and operating a distributed query infrastructure (like Apache Hive on Hadoop) or being inside Google. BigQuery offered the result — fast, interactive queries on massive datasets — as a managed cloud service.

The underlying technology was Dremel, Google's internal system for sub-second queries via columnar storage and a multi-level serving tree architecture. BigQuery exposed Dremel's query model (standard SQL subset over large tables stored in Google's infrastructure) as a pay-per-query API. The pricing model was novel: you didn't pay for cluster uptime, only for bytes processed per query. This made large-scale analytics more accessible to teams that couldn't justify dedicated Hadoop infrastructure.

In 2012, the competitive landscape was Hadoop/Apache Hive for batch analytics, with Amazon Redshift also launching the same year. BigQuery was positioned as the interactive alternative: slower than Redshift for complex joins but dramatically faster for scan-heavy analytical queries. It also required no schema management for ingestion — load JSON or CSV, run a query. The opening of BigQuery to all was an early marker in the shift from data warehousing as infrastructure (something you build and operate) to data warehousing as a service. Snowflake and others would extend this further, but BigQuery established the template.

## Key points

- Google BigQuery = Dremel as a cloud service — interactive SQL over petabyte data, no cluster management required.
- Pay-per-query (bytes processed) pricing model — made large-scale analytics accessible without dedicated infrastructure.
- Columnar storage and serving tree architecture: scans only columns touched by query; distributes across thousands of machines automatically.
- Launched publicly July 2012 alongside Amazon Redshift — both signaled the shift toward managed data warehousing in the cloud.
- BigQuery required no upfront schema optimization for ingestion — load data, query immediately.
- The direct product lineage: Google Dremel paper (VLDB 2010) → BigQuery limited preview → general availability 2012.

[Original](http://gigaom.com/cloud/google-opens-up-its-biq-query-data-analytics-service-to-all/)
