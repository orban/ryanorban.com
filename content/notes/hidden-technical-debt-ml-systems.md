---
title: Hidden Technical Debt in Machine Learning Systems
date: 2022-01-06
categories:
  - machine-learning
  - software-engineering
  - technical-debt
  - mlops
  - google
description: "Sculley, Holt, Golovin et al. at Google extend the software engineering concept of technical debt to ML systems, identifying ML-specific forms that accumulate invisibly at the system level: boundary erosion, entanglement, hidden feedback loops, undeclared consumers, and data dependencies. The canonical paper explaining why ML systems are uniquely expensive to maintain."
params:
  source: papers
  sourceUrl: https://proceedings.neurips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html
---

## Summary

D. Sculley, Gary Holt, Daniel Golovin, Eugene Davydov, and colleagues at Google (NeurIPS 2015) apply Ward Cunningham's concept of technical debt to machine learning systems and find that ML has an extraordinary capacity to accumulate invisible debt at the system level. Unlike code-level debt — which is visible in messy functions and missing tests — ML technical debt lives in the interactions between components and is often invisible until it causes expensive failures.

The paper catalogs ML-specific risk factors that compound over time. **Boundary erosion** occurs when ML components tempt re-use in contexts they weren't designed for, gradually corrupting abstraction boundaries. **Entanglement** is the CACE problem (Changing Anything Changes Everything): in ML, changing one feature, one data source, or one hyperparameter can silently change the behavior of the entire model in unpredictable ways. **Hidden feedback loops** arise when ML systems influence the data they're later trained on — a recommendation system shapes user behavior, which shapes the training set, which shapes future recommendations, creating feedback dynamics that are hard to detect or analyze. **Undeclared consumers** happen when model outputs get consumed by downstream systems without formal API contracts, coupling tightly coupled to specific model behaviors. **Data dependencies** accumulate like code dependencies but are harder to clean up because removing a data feature requires retraining and re-evaluation.

The paper's impact was to give the MLOps community a vocabulary for the maintenance burden of production ML — making it possible to have principled conversations about when technical debt should be paid down vs. accepted. It's cited extensively in production ML literature and remains the canonical reference for why deploying a model is the beginning of the maintenance cost, not the end of it.

## Key points

- ML systems have all the technical debt of traditional software **plus** ML-specific forms that accumulate at the system level
- **CACE principle**: Changing Anything Changes Everything in ML — no feature is truly independent
- **Hidden feedback loops**: production ML systems influence their own future training data, creating hard-to-detect dynamics
- Data dependencies are more expensive than code dependencies — removing a data feature requires full retraining and evaluation
- Established the vocabulary for MLOps conversations about maintenance costs; still the canonical reference on this topic

[Original](https://proceedings.neurips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html)
