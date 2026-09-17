---
title: "Kedro: Production-Ready Data Science Pipelines"
date: 2022-01-23
categories:
  - data-science
  - mlops
  - python
  - data-pipelines
  - kedro
  - open-source
description: Kedro is an open-source Python framework for building reproducible, maintainable, and modular data science pipelines — applying software engineering principles (catalogs, pipelines, project templates) to ML workflows. The answer to 'how do data science teams write production-grade code.'
params:
  source: pinboard
  sourceUrl: https://github.com/kedro-org/kedro
---

## Summary

Kedro is an open-source Python framework for building data pipelines that are reproducible, maintainable, and modular — applying software engineering discipline to the historically messy world of data science code. The project is now maintained by the LF AI & Data Foundation and has over 10,000 GitHub stars.

The core abstractions are the Data Catalog (a configuration-driven registry of datasets with connectors for local files, cloud storage, databases, and custom formats), the Pipeline (a DAG of Python functions with automatic dependency resolution), and a project template based on Cookiecutter for standardized structure. These three pieces together address the most common problems in data science codebases: data access scattered across scripts, unclear dependencies between steps, and no consistent project structure that new team members can navigate.

Kedro-Viz provides visualization of pipeline DAGs. The framework is designed to deploy to common ML infrastructure: Apache Airflow, Kubeflow, Vertex AI, AWS SageMaker, and Prefect, among others. This is a meaningful design goal — write once, run anywhere in the pipeline orchestration ecosystem. The comparison to Ploomber is natural: both address the notebook-to-production gap, with Kedro being more opinionated about project structure and Ploomber being more flexible about where pipelines come from.

## Key points

- Data Catalog: config-driven dataset registry with connectors for S3, GCS, local, databases, and custom formats — eliminates scattered data loading code.
- Pipeline as a Python function DAG with automatic dependency resolution and Kedro-Viz visualization.
- Project template (Cookiecutter-based) enforces consistent structure across data science projects.
- Deploys to Apache Airflow, Kubeflow, Vertex AI, SageMaker, Prefect — portable across orchestrators.
- Moves data science from Jupyter notebook-to-script archaeology toward repeatable, testable, version-controlled engineering practice.

[Original](https://github.com/kedro-org/kedro)
