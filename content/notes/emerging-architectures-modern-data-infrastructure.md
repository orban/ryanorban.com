---
title: Emerging Architectures for Modern Data Infrastructure
date: 2020-10-18
categories:
  - data-engineering
  - data-infrastructure
  - cloud
  - architecture
  - machine-learning
description: Andreessen Horowitz maps the emerging stack for modern data infrastructure — separating analytics, ML, and operational workloads into distinct architectural patterns. A useful taxonomy of the data tooling landscape circa 2020.
params:
  source: pinboard
  sourceUrl: https://a16z.com/2020/10/15/the-emerging-architectures-for-modern-data-infrastructure/
---

## Summary

Andreessen Horowitz (a16z) published this landmark analysis of the data infrastructure landscape in late 2020, providing a framework for how the modern data stack had evolved from the monolithic data warehouse into distinct, composable architectural layers. The thesis: software systems are increasingly data-driven, and new tool categories have emerged to serve both analytics and operational AI/ML workloads that the old stack couldn't handle well.

The framework describes three core architectural patterns: **modern business intelligence** (cloud-native analytics with data replication, cloud data warehouses like Snowflake and Databricks, and SQL modeling via dbt), **multimodal data processing** (evolved data lakes that serve both analytical and operational workloads), and **AI/ML** (specialized stack for model development, testing, and deployment). These aren't competing — most organizations use elements of all three depending on use case.

The unified layer taxonomy runs: ingestion (Fivetran, Airbyte) → storage (Snowflake, Databricks) → processing → transformation (dbt) → applications (Looker, Tableau, Hex). Supporting infrastructure includes data observability tools (Monte Carlo, Bigeye), reverse ETL (Hightouch, Census), and feature stores (Tecton). The emergent concept is the **data platform** — a consolidated backend where third-party applications build atop standardized infrastructure, creating network effects.

## Key points

- dbt (data build tool) emerged as the transformation layer missing from the classic stack — SQL-first, version-controlled, testable.
- Reverse ETL is a category flip: instead of data flowing into the warehouse for analytics, it flows back out to operational systems (CRM, marketing automation). Hightouch and Census defined this category.
- Feature stores (Tecton, Feast) solve the train-serve skew problem in ML: the same feature definitions used in training need to be served at prediction time.
- The data lakehouse pattern (Delta Lake, Apache Iceberg) merges data lake flexibility with data warehouse reliability — ACID transactions on object storage.
- Data observability as a distinct category acknowledges that data pipelines fail silently in ways that code failures don't — schema drift, null rates, volume anomalies need monitoring too.

[Original](https://a16z.com/2020/10/15/the-emerging-architectures-for-modern-data-infrastructure/)
