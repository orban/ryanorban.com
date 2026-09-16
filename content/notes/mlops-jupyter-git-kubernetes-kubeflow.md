---
title: "Data Science Meets DevOps: MLOps with Jupyter, Git, and Kubernetes"
date: 2020-08-05
categories:
  - mlops
  - kubernetes
  - jupyter
  - git
  - machine-learning
  - data-engineering
description: Kubeflow's blog post on MLOps practices combining Jupyter notebooks, Git, and Kubernetes — the infrastructure side of making ML reproducible, collaborative, and deployable. Establishes the canonical MLOps stack for Kubernetes-based ML teams.
params:
  source: pinboard
  sourceUrl: https://blog.kubeflow.org/mlops/
---

## Summary

Kubeflow's blog post on MLOps lays out the argument for bringing DevOps practices to machine learning workflows. The core problem: ML experiments run in Jupyter notebooks are hard to reproduce, hard to version, and hard to deploy. Git version-controls code but not data or model artifacts. Traditional CI/CD pipelines assume stateless applications, not stateful trained models. MLOps is the practice of addressing this gap.

The proposed stack: Jupyter notebooks for interactive exploration (with nbconvert and Papermill for parameterized execution), Git for code version control, DVC or similar for data and model artifact versioning, and Kubernetes (via Kubeflow) for scalable training and deployment. The workflow: experiment in notebooks → refactor into modular Python pipeline code → version with Git → execute on Kubernetes → serve the model with a REST API.

Kubeflow specifically provides: KFServing (now KServe) for model serving, Kubeflow Pipelines for orchestrating multi-step ML workflows as DAGs, Katib for hyperparameter tuning, and notebook spawning with GPU resource allocation. The ecosystem addresses the full ML lifecycle rather than just training.

## Key points

- MLOps bridges DevOps practices and machine learning — reproducibility, versioning, CI/CD for models.
- Stack: Jupyter for exploration → Git for code → DVC for data → Kubernetes / Kubeflow for execution.
- Kubeflow Pipelines: ML workflow orchestration as DAGs on Kubernetes — complements Apache Airflow.
- KServe: model serving layer on Kubernetes with canary deployments and auto-scaling.
- Key insight: ML systems have extra artifacts (data, models, hyperparameters) that standard DevOps pipelines don't handle.
- Related vault notes: [Kedro data science framework](/notes/kedro-data-science-framework/), Ploomber pipelines, [Affirm Fargate Airflow](/notes/affirm-fargate-airflow/).

[Original](https://blog.kubeflow.org/mlops/)
