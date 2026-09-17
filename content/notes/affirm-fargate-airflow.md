---
title: How Affirm Uses AWS Fargate and Apache Airflow for Batch Jobs
date: 2021-01-07
categories:
  - data-engineering
  - airflow
  - aws
  - batch-processing
  - fintech
description: Affirm's engineering blog post on running Apache Airflow DAGs on AWS Fargate for batch job management — serverless task execution without persistent workers. A practical architecture case study for ML and data pipeline orchestration at a fintech scale.
params:
  source: pinboard
  sourceUrl: https://aws.amazon.com/blogs/containers/how-affirm-uses-aws-fargate-and-apache-airflow-to-manage-batch-jobs/
---

## Summary

Affirm's engineering team describes their batch job infrastructure built on Apache Airflow and AWS Fargate. The core architectural choice: instead of running persistent Celery workers that idle between tasks, Fargate spins up containers on demand per Airflow task and terminates them when done. This eliminates the cost and operational overhead of managing worker fleets — a meaningful win for a batch workload where jobs are bursty rather than continuous.

Apache Airflow handles the DAG definition and scheduling; Fargate provides the serverless compute layer where each task runs. The integration is through Airflow's `ECSOperator` (Fargate is part of Amazon ECS). Each Airflow task maps to a container invocation with its own resource allocation — different tasks can have different CPU/memory settings without worker specialization.

The fintech context matters: Affirm runs large-scale credit risk models and payment processing pipelines where correctness and auditability are critical. Fargate's per-task isolation makes failures clean (a stuck container doesn't affect other tasks), and the container registry stores exact version history of what ran. This architecture is widely applicable beyond fintech — any ML training, ETL, or report generation pipeline that has variable, bursty compute needs fits this pattern.

## Key points

- Apache Airflow for orchestration (DAG definition, scheduling, dependency management) + AWS Fargate for serverless per-task execution.
- Eliminates persistent workers: tasks run in ephemeral containers, reducing idle compute cost and worker management overhead.
- Each Airflow task gets its own Fargate task definition with independent CPU/memory settings.
- Per-task container isolation makes failures clean and provides exact reproducibility via container image versioning.
- ECSOperator is the Airflow integration point — this pattern applies to any Airflow deployment targeting AWS.

[Original](https://aws.amazon.com/blogs/containers/how-affirm-uses-aws-fargate-and-apache-airflow-to-manage-batch-jobs/)
