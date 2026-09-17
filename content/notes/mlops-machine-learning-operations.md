---
title: "MLOps: Machine Learning Operations"
date: 2022-09-23
categories:
  - mlops
  - machine-learning
  - deployment
  - production
  - engineering
description: A comprehensive guide to MLOps — the practices, tools, and culture for deploying and maintaining machine learning models in production. Covers the full lifecycle from experiment tracking through model serving, monitoring, and retraining pipelines.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/MLops.pdf
---

## Summary

MLOps (Machine Learning Operations) applies DevOps principles to the machine learning lifecycle — the recognition that building a model is only a small fraction of the work needed to have that model deliver value in production. This document covers the full operational lifecycle: experiment tracking and reproducibility, model versioning, training pipelines, model serving infrastructure, data pipeline management, monitoring, drift detection, and retraining triggers. The analogy to DevOps is apt: just as DevOps industrialized software deployment with CI/CD, MLOps industrializes model deployment with ML-specific tooling.

The core problems MLOps addresses: (1) models are experiments and require experiment tracking (MLflow, Weights & Biases, DVC) to remain reproducible; (2) training data changes over time, causing concept drift and data drift that degrade model quality post-deployment; (3) model serving requires different infrastructure than web serving — latency/throughput tradeoffs, batch vs. online inference, hardware-specific optimizations; (4) ML code and ML artifacts (datasets, models) both need versioning, but the tooling differs.

The MLOps maturity model organizes teams into levels: Level 0 (manual, ad-hoc training and deployment), Level 1 (automated training pipeline, model versioning), Level 2 (full CI/CD for models, automated retraining). Most enterprise ML teams are at Level 0-1. Getting to Level 2 requires investment in feature stores, automated data quality checks, A/B testing infrastructure, and model registry tooling. The tools ecosystem covers Kubeflow, SageMaker, Vertex AI, BentoML, Seldon, and MLflow as the major platforms.

## Key points

- Experiment tracking: every run needs logged hyperparameters, metrics, code version, and data version — MLflow and Weights & Biases are standard; without this, experiments are unreproducible
- Model serving patterns: online serving (REST/gRPC endpoint, latency-sensitive), batch inference (scheduled jobs, throughput-optimized), streaming inference (Kafka-connected, event-driven)
- Data drift and concept drift monitoring: statistical tests (KS test, Population Stability Index) on input feature distributions; ground truth monitoring when labels arrive with delay
- Feature store: shared computation layer for features used in training and serving — prevents train-serve skew, enables feature reuse across models
- Deployment strategies: canary releases, shadow mode, A/B testing — same patterns as web services but with model-specific rollback criteria

[Original PDF →](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/MLops.pdf)
