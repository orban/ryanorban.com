---
title: MLOps Notebooks Syllabus
date: 2022-03-05
categories:
  - mlops
  - machine-learning
  - data-engineering
  - education
  - reference
description: A Jupyter notebook curriculum for MLOps — covering model deployment, monitoring, CI/CD for ML, feature stores, and data versioning. Practical operational coverage for the gap between training a model and running it reliably in production.
params:
  source: pinboard
  sourceUrl: https://github.com/thejat/mlops-notebooks/blob/master/Syllabus.ipynb
---

## Summary

This MLOps curriculum by Arun J (University of Chicago) is a collection of Jupyter notebooks covering the full operational lifecycle of machine learning systems. Where most ML education ends at model training, this syllabus addresses what comes after: deploying models as services, tracking experiments, versioning data, monitoring production performance, and building CI/CD pipelines for ML workflows.

The syllabus covers the main MLOps concern areas: model serving (REST APIs, batch inference, streaming), experiment tracking with tools like MLflow and Weights & Biases, feature stores for consistent feature computation between training and serving, data versioning with DVC, and ML monitoring for detecting data drift and model degradation. The notebook format makes concepts executable — you can run the examples rather than just reading them.

This reflects the MLOps maturity model problem: in 2022, many teams had ML models but inconsistent practices around deploying and operating them. The field was consolidating around a set of tools (Kubeflow, MLflow, Seldon, Feast, Great Expectations) that together compose an ML platform, but knowing which piece to use when required conceptual orientation. The syllabus provides that orientation with hands-on examples.

## Key points

- Covers the post-training lifecycle: deployment, serving, monitoring, CI/CD, feature engineering consistency.
- Experiment tracking: MLflow / Weights & Biases for reproducibility and hyperparameter management.
- Feature store pattern: decouple feature computation from model training to ensure training/serving consistency.
- ML monitoring: detect data drift, model degradation, and pipeline failures in production.
- Notebook-based: concepts are runnable, not just readable.

[Original](https://github.com/thejat/mlops-notebooks/blob/master/Syllabus.ipynb) → REST API, GitHub
