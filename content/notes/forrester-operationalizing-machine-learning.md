---
title: "Operationalizing Machine Learning: Forrester Research Report"
date: 2021-12-06
categories:
  - mlops
  - machine-learning
  - enterprise
  - model-deployment
  - research
description: Forrester Research report on operationalizing machine learning in enterprise settings, covering the organizational and technical requirements for moving models from development into production reliably. Useful snapshot of where enterprise ML practice stood in late 2021 and the key gaps between experimentation and production.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/Operationalize-Machine-Learning-Forrester-.pdf
---

## Summary

This Forrester Research report (likely 2021, consistent with the save date) surveys the state of enterprise machine learning operationalization — the set of processes, tools, and organizational structures required to reliably deploy ML models into production and keep them performing well. The core finding is that most organizations are better at building ML models than at running them: data science teams can produce interesting prototypes, but the handoff to engineering for production deployment, monitoring, and maintenance is a persistent source of failure.

The report identifies the main gaps in enterprise MLOps practice circa 2021: lack of reproducibility (models trained on ephemeral notebook environments that can't be rebuilt), insufficient model monitoring (no systematic detection of data drift or concept drift post-deployment), fractured tooling (data engineers, data scientists, and ML engineers all use different platforms with poor integration), and unclear ownership (who is responsible when a deployed model degrades?). Continuous integration and deployment patterns from software engineering apply to ML, but require adaptation — data versioning, model versioning, and pipeline orchestration are not native to DevOps toolchains.

The recommended architecture involves four layers: data and feature management (feature store), model development and experimentation (tracked with experiment management tools), deployment and serving (online/batch inference endpoints), and monitoring and governance (drift detection, explainability, audit logs). The report profiles platforms like MLflow, Kubeflow, SageMaker, Databricks, and emerging vendors in the MLOps space. Organizations are rated on a maturity model from ad-hoc experimentation to fully automated ML pipelines with closed-loop retraining.

## Key points

- Primary gap in enterprise ML: model building is easy; production deployment, monitoring, and maintenance are the hard parts.
- Data drift and concept drift detection are the most commonly neglected aspect of deployed ML — models silently degrade.
- Four-layer MLOps architecture: data/feature management → development/experimentation → deployment/serving → monitoring/governance.
- Feature stores resolve the training/serving skew problem (features computed differently offline vs. online).
- Key tools profiled: MLflow, Kubeflow, AWS SageMaker, Databricks, Weights & Biases.
- Maturity model: ad-hoc → repeatable → managed → optimizing (automated retraining with drift-triggered pipelines).

[Original PDF](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/Operationalize-Machine-Learning-Forrester-.pdf)
