---
title: "Ploomber: Data Pipelines from Dev to Production"
date: 2022-01-23
categories:
  - data-science
  - data-pipelines
  - python
  - mlops
  - notebooks
  - open-source
description: Ploomber is a Python framework for building data pipelines that can develop in Jupyter notebooks and deploy to Kubernetes, Airflow, or AWS Batch without rewriting code. Solves the notebook-to-production gap by treating notebooks as first-class pipeline tasks.
params:
  source: pinboard
  sourceUrl: https://github.com/ploomber/ploomber
---

## Summary

Ploomber is an open-source Python framework for building data pipelines that close the gap between interactive development (Jupyter notebooks, IDEs) and production deployment. The distinctive capability: you can write pipeline tasks as Jupyter notebooks and Ploomber parameterizes and orchestrates them, or convert legacy monolithic notebooks into pipeline components automatically.

The caching behavior is a practical time-saver during development: Ploomber tracks which tasks have changed and only recomputes those parts of the pipeline, avoiding the re-run everything from scratch problem that makes large notebook-based workflows frustrating. The deployment story is the key selling point — the same pipeline definition runs locally or on Kubernetes, Apache Airflow, AWS Batch, or SLURM without code changes.

Ploomber and Kedro occupy similar territory (notebook-to-production data pipelines) but with different opinions. Kedro is more opinionated about project structure and data catalogs; Ploomber is more flexible about how you author tasks (notebooks, scripts, Python functions) and focuses more heavily on the deployment portability story. Both are responses to the same problem: data science code that works on a laptop and doesn't translate to production.

## Key points

- Treats Jupyter notebooks as first-class pipeline tasks — no rewrite needed to move from interactive to orchestrated.
- Smart caching: only re-runs tasks that changed, not the entire pipeline — critical for large multi-step workflows.
- Single pipeline definition runs locally, on Kubernetes, Apache Airflow, AWS Batch, or SLURM — true deployment portability.
- Converts existing monolithic notebooks into pipeline components automatically.
- Compared to Kedro: less opinionated on project structure, more flexible on task authoring format (notebooks, scripts, functions).

[Original](https://github.com/ploomber/ploomber) → GitHub
