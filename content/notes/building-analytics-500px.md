---
title: Building Analytics at 500px
date: 2015-06-22
categories:
  - analytics
  - data-engineering
  - data-warehouse
  - amazon-redshift
  - etl
description: A first-person account of building 500px's analytics infrastructure from scratch — Amazon Redshift data warehouse, Luigi ETL, Periscope BI. The 20% evangelism rule and 'don't bake your own ETL' lesson make it one of the most practical early data engineering retrospectives.
params:
  source: pinboard
  sourceUrl: https://medium.com/@samson_hu/building-analytics-at-500px-92e9a7005c83
---

## Summary

Samson Hu's retrospective on building 500px's analytics infrastructure is one of the best early accounts of the data engineering challenges small-to-mid-size startups faced in 2015. The stack: Amazon Redshift as the data warehouse ($4,000/year for 2TB), Luigi (Spotify's Python workflow framework) for ETL orchestration with 200+ nodes, and Periscope for self-service SQL analysis. Data flowed nightly from MySQL production databases and 20GB/day log files through Luigi pipelines into Redshift.

The key architectural decision was dimensional modeling — separating fact and dimension tables so that end users writing SQL queries didn't need to understand the production database schema. This mirrors the Kimball methodology and made the warehouse genuinely usable by non-engineers. The lesson that "dimensional models hide complexity from end users" is one of the most durable principles of analytics engineering.

Two hard-earned lessons stand out. First: "I will not bake my own ETL solution." Custom ETL systems become unmaintainable quickly; using established frameworks (Luigi, later Airflow, dbt) is the right default. Second: allocate 20% of effort to evangelism. Hu underestimated the time needed for training, communicating metric definitions, and building organizational trust in the data — and found the analytics effort partly failed because of adoption, not technical quality. Accurate data that nobody uses is worthless.

## Key points

- Stack: Amazon Redshift + Luigi ETL + Periscope BI — a canonical 2015 data stack.
- Dimensional modeling (Kimball-style) made the warehouse usable by non-engineers.
- 80% confidence at most — data quality monitoring against external sources (Google Analytics) is a permanent requirement, not a launch task.
- **Rule**: don't build custom ETL — use frameworks.
- **Rule**: 20% of effort on evangelism — adoption is as important as technical quality.
- Partner with engineering from day one: event logging schema must be designed upfront, not retrofitted.

[Original](https://medium.com/@samson_hu/building-analytics-at-500px-92e9a7005c83)
