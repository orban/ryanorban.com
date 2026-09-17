---
title: "Sematic: Python-First ML Pipeline Orchestration"
date: 2022-08-10
categories:
  - mlops
  - pipeline
  - orchestration
  - machine-learning
  - open-source
description: Sematic is an open-source ML pipeline orchestration framework using Python decorators — no YAML, seamless local-to-cloud execution, built-in artifact tracking dashboard. Competes with MLflow and Kubeflow but stays in pure Python.
params:
  source: pinboard
  sourceUrl: https://www.sematic.dev/
---

![Sematic: Python-First ML Pipeline Orchestration](/images/notes/sematic.png)

## Summary

[Sematic](/notes/sematic/) is an open-source ML orchestration platform that lets practitioners define end-to-end training pipelines as pure Python functions decorated with `@sematic.func`. The philosophy: eliminate YAML templating and DSL overhead by keeping orchestration in the same Python environment as modeling code. Pipelines run identically whether executed locally or submitted to a Kubernetes cluster with specified GPU resources.

The architecture provides complete traceability: every pipeline step's inputs, outputs, logs, and metrics are persisted and viewable in a built-in dashboard. [Sematic](/notes/sematic/) supports dynamic DAGs — loops, conditional branching, nested pipelines — rather than requiring static graph definitions. Seamless local-to-cloud execution is a key selling point: the system packages and ships the local environment to cloud, avoiding environment mismatch bugs that plague other orchestration tools.

[Sematic](/notes/sematic/) was positioned as an alternative to MLflow (experiment tracking), Kubeflow (Kubernetes-native but complex), and Metaflow (Netflix's Python-first orchestration). Inspired by learnings from building systems at the number one robotaxi company (likely Waymo or similar). The MLOps problem it addresses is real: the overhead of stitching together experiment tracking, artifact storage, and cloud execution prevents rapid iteration.

## Key points

- Python-first ML pipeline orchestration: `@sematic.func` decorators, no YAML.
- Seamless local-to-cloud execution — packages environment automatically for Kubernetes.
- Built-in dashboard for artifact tracking, logs, metrics — MLOps observability out of the box.
- Supports dynamic DAGs: loops, conditionals, nested pipelines (beyond static graph DAGs).
- Competes with MLflow, Kubeflow, Metaflow in the MLOps tooling space.
- Open-source; targets ML teams who find Kubeflow too complex and Metaflow too opinionated.

[Original](https://www.sematic.dev/)
