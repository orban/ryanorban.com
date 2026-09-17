---
title: We're All Using Airflow Wrong and How to Fix It
date: 2020-07-24
categories:
  - airflow
  - data-engineering
  - workflow-orchestration
  - antipatterns
description: "Bluecore Engineering's argument that most Airflow deployments misuse operators — using Python, Bash, and Spark operators that run code inside the Airflow worker, which breaks isolation and causes resource contention. The fix: use KubernetesPodOperator for everything."
params:
  source: pinboard
  sourceUrl: https://medium.com/bluecore-engineering/were-all-using-airflow-wrong-and-how-to-fix-it-a56f14cb0753
---

## Summary

Bluecore Engineering makes a pointed argument in this post: the standard way most teams use Apache Airflow — with PythonOperator, BashOperator, and other operators that run code directly in the Airflow worker processes — is architecturally wrong. The reason: these operators mix the execution environment of your task code with the Airflow worker infrastructure. This creates dependency conflicts (task A needs library version X, task B needs version Y), resource contention (a memory-heavy task starves the Airflow scheduler), and fragile deployments (task code must be deployed to every Airflow worker).

The proposed fix: use KubernetesPodOperator for almost everything. Each task runs in an isolated Kubernetes pod with its own Docker image, environment variables, and resource limits. Tasks become completely isolated, dependency conflicts disappear, and resource allocation is explicit per task. The Airflow worker just orchestrates pod lifecycle, not task execution.

This pattern aligns with how Affirm, Google, and other production Airflow users evolved their setups — the [Affirm Fargate Airflow](/notes/affirm-fargate-airflow/) post in the vault makes essentially the same argument for AWS Fargate instead of Kubernetes. The insight is the same: Airflow should be a scheduler/orchestrator, not an execution environment. Separating scheduling from execution is the right architectural decomposition.

## Key points

- PythonOperator / BashOperator antipattern: runs task code inside Airflow workers, causing dependency conflicts and resource contention.
- Fix: KubernetesPodOperator isolates each task in its own Docker container — clean dependencies, explicit resource limits.
- Airflow as orchestrator, not executor: scheduling and execution should be separated.
- Same architectural insight as [Affirm Fargate Airflow](/notes/affirm-fargate-airflow/) (uses Fargate instead of Kubernetes, same principle).
- Deployment simplification: each task has its own Docker image; no need to deploy task code to Airflow workers.
- Related vault notes: Airflow XCOM, [Affirm Fargate Airflow](/notes/affirm-fargate-airflow/), [Unbundling of Airflow](/notes/unbundling-of-airflow/), [Kedro data science framework](/notes/kedro-data-science-framework/).

[Original](https://medium.com/bluecore-engineering/were-all-using-airflow-wrong-and-how-to-fix-it-a56f14cb0753)
