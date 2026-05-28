---
title: Data Engineering Zoomcamp
date: 2022-01-20
categories:
  - data-engineering
  - education
  - free-course
  - docker
  - spark
  - kafka
  - dbt
description: DataTalksClub's free 9-week data engineering course — builds an end-to-end pipeline covering Docker, Terraform, BigQuery, dbt, Spark, and Kafka. One of the better free paths from zero to production data engineering.
params:
  source: pinboard
  sourceUrl: https://github.com/DataTalksClub/data-engineering-zoomcamp
---

![Data Engineering Zoomcamp](/images/notes/data-engineering-zoomcamp.png)

## Summary

The [Data Engineering Zoomcamp](/notes/data-engineering-zoomcamp/) by DataTalksClub is a free 9-week course that builds an end-to-end data pipeline from scratch, covering the full stack of modern data engineering tooling. No prior data engineering experience required — basic Python and SQL familiarity is the starting point.

The curriculum is deliberately practical: each module introduces a tool by building something with it, rather than teaching concepts in isolation. Week 1 starts with Docker and Terraform for containerization and infrastructure. The middle modules cover workflow orchestration (Kestra), data warehousing (BigQuery), and analytics engineering (dbt). The later weeks address batch processing (Apache Spark) and streaming (Apache Kafka with Avro schema management). The capstone project requires integrating these tools end-to-end.

This is a course that reflects current production data engineering more accurately than most: dbt for transformation, BigQuery or DuckDB for the warehouse, Kafka for streaming, Spark for large-scale batch. The choice of Kestra for orchestration (over the incumbent Airflow) is a forward-looking bet. The free, cohort-based format with Slack community gives it accountability structure that pure self-paced courses lack.

## Key points

- Free, 9-week, project-based curriculum — builds an end-to-end pipeline across all major data engineering domains.
- Module stack: Docker, Terraform, Kestra (orchestration), BigQuery, dbt, Apache Spark, Apache Kafka.
- DuckDB used for local development; Bruin for end-to-end pipeline testing — forward-looking tool choices.
- Capstone project applies all modules in an integrated pipeline — not just tutorial exercises.
- Hosted by DataTalksClub with free cohort runs; companion to their ML Zoomcamp and MLOps Zoomcamp.

[Original](https://github.com/DataTalksClub/data-engineering-zoomcamp) → GitHub
