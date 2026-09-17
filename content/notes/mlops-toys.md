---
title: "MLOps Toys: Curated List of Machine Learning Projects"
date: 2022-04-22
categories:
  - mlops
  - machine-learning
  - developer-tools
  - reference
  - curated-list
description: MLOps Toys is a curated directory of ML projects and tools — organized by category (data, model training, serving, monitoring, etc.). A snapshot of the MLOps ecosystem circa 2022, useful as a reference map of what tools existed before the category consolidated.
params:
  source: pinboard
  sourceUrl: https://mlops.toys/
---

## Summary

[MLOps Toys](/notes/mlops-toys/) is a curated directory of machine learning tools and projects organized by the stages of the ML lifecycle: data labeling and management, experiment tracking, model training, model serving, monitoring, feature stores, and orchestration. It serves as a reference map of the MLOps ecosystem — the set of practices and tools for operating machine learning in production, analogous to how DevOps tooling addresses software deployment.

The directory reflects the early-2022 state of the MLOps category, when the space was fragmented across many specialized tools with unclear winners. MLflow and Weights & Biases were emerging leaders in experiment tracking; Seldon, BentoML, and Ray Serve competed in model serving; Feast and Hopsworks in feature stores; Airflow, Prefect, and Metaflow in orchestration. The taxonomy itself was still being worked out — companies disagreed on what the distinct components of the ML stack were.

The practical value of a directory like this is pattern-matching across the stack: when you're building an ML system and realize you need experiment tracking, you can find the options rather than reinventing the wheel. The MLOps category emerged partly from the observation that ML systems fail in distinctive ways — data drift, training-serving skew, feature pipeline failures, model staleness — that require specific tooling beyond general software engineering practices.

## Key points

- Categorized directory of MLOps tools across the full ML lifecycle: data → training → serving → monitoring.
- Key categories: experiment tracking (MLflow, W&B), feature stores (Feast), serving (BentoML, Seldon), orchestration (Metaflow, Airflow).
- Captures the 2022 era of MLOps before the category consolidated — many competing tools, no clear standards.
- Useful reference map for building ML systems: find the tool for each lifecycle stage rather than building from scratch.
- Complements the Hidden Technical Debt in ML Systems paper in giving a structured view of ML system components.
- The toys framing is honest — many projects in this space are experimental or abandoned.

[Original](https://mlops.toys/)
