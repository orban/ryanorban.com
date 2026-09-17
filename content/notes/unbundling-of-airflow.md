---
title: The Unbundling of Airflow
date: 2022-02-15
categories:
  - data-engineering
  - workflow-orchestration
  - airflow
  - mlops
  - infrastructure
description: fal.ai's analysis of why Apache Airflow is being unbundled by specialized tools — Prefect and Dagster for orchestration, dbt for transformation, Temporal for long-running workflows. The monolithic DAG orchestrator is fracturing along functional lines.
params:
  source: pinboard
  sourceUrl: https://blog.fal.ai/the-unbundling-of-airflow-2/
---

## Summary

Apache Airflow became the dominant workflow orchestration platform for data engineering over the 2017–2021 period — the default choice for scheduling ETL pipelines, ML training jobs, and data processing DAGs. But by 2022, fal.ai was diagnosing its unbundling: specialized tools were taking over specific parts of what Airflow does, often doing them better.

The breakdown follows the same pattern as other infrastructure unbundlings (like Craigslist being unbundled by vertical marketplaces): Airflow tried to do everything and newer tools optimize for specific use cases. Prefect and Dagster offer better Python-native orchestration with first-class support for dynamic DAGs and data artifacts. dbt owns the SQL transformation layer. Temporal handles long-running, stateful workflows better than Airflow's task model. Great Expectations handles data quality checks. Each tool does a narrower thing with much better ergonomics.

The broader thesis is that the data stack of 2022 was fragmenting into best-of-breed components connected by standard interfaces, rather than converging on monolithic platforms. This creates complexity for teams managing many tools, but better outcomes for teams that can compose the right pieces. This debate has continued — Astronomer (the Airflow company) has pushed back with Airflow 2.x improvements, but the specialization trend has held.

## Key points

- Apache Airflow's monolithic DAG model doesn't fit modern dynamic, Python-first workflows well.
- Dagster and Prefect offer better developer experience and data-aware orchestration.
- dbt captures the SQL transformation use case entirely; Spark / dbt combinations replace Airflow-managed transforms.
- Temporal handles stateful, long-running business workflows better than Airflow's task retry model.
- The [modern data stack](/notes/modern-data-stack/) trend: best-of-breed components over monolithic platforms.

[Original](https://blog.fal.ai/the-unbundling-of-airflow-2/)
