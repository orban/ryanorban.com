---
title: "SE-ML: Software Engineering Practices for Machine Learning"
date: 2022-10-03
categories:
  - machine-learning
  - software-engineering
  - mlops
  - best-practices
description: SE-ML is a catalog of software engineering practices adapted for machine learning systems — covering data management, model training, deployment, and monitoring. A structured reference for treating ML development with the same rigor as traditional software engineering.
params:
  source: pinboard
  sourceUrl: https://se-ml.github.io/practices/
---

## Summary

SE-ML is a research project and catalog documenting software engineering best practices specifically adapted for machine learning systems. The site emerged from academic research studying how ML teams handle the unique engineering challenges that don't arise in traditional software: data versioning, experiment tracking, model reproducibility, and the fact that bugs often manifest as subtle degradations in model quality rather than explicit errors.

The catalog organizes practices across the full ML lifecycle: data management (versioning datasets, documenting lineage), model development (experiment tracking, reproducibility), deployment (serving infrastructure, monitoring), and organizational practices (team structure, documentation). Each practice is grounded in survey data from ML practitioners rather than being prescriptive theory.

The underlying tension the project addresses is that MLOps as a field is still maturing — many practices that are standard in traditional DevOps (CI/CD, automated testing, version control) don't map cleanly to ML systems, and the tooling is fragmented. SE-ML tries to document what actually works in practice before the field converges on standards.

## Key points

- Catalog of software engineering practices adapted for machine learning development.
- Covers data versioning, experiment tracking, model reproducibility, and deployment monitoring.
- Research-backed: practices derived from surveys of ML practitioners, not just prescriptive theory.
- Addresses the MLOps maturity gap — ML teams often lack engineering rigor that traditional software teams have.
- Complements tools like MLflow, DVC, and Weights & Biases which automate some of these practices.
- Free resource; part of academic research on the intersection of SE and ML.

[Original](https://se-ml.github.io/practices/) → GitHub
