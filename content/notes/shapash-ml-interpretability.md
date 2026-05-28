---
title: "Shapash: Making Machine Learning Models Transparent"
date: 2021-03-06
categories:
  - machine-learning
  - interpretability
  - explainability
  - python
  - open-source
description: Shapash is MAIF's Python library for making ML models interpretable to non-technical stakeholders — wrapping SHAP and LIME with better visualizations and business-friendly explanations. Targets the gap between data scientists and decision-makers.
params:
  source: pinboard
  sourceUrl: https://github.com/MAIF/shapash
---

![Shapash: Making Machine Learning Models Transparent](/images/notes/shapash-ml-interpretability.png)

## Summary

Shapash is an open-source Python library from MAIF (a French insurance cooperative) designed to make machine learning models interpretable not just for data scientists, but for business stakeholders who need to understand and trust model decisions. It wraps lower-level interpretability methods (SHAP, LIME) with better visualizations and terminology that non-technical users can understand.

The library generates interactive HTML reports showing feature contributions, a stability plot showing how predictions change as inputs vary, and local explanations for individual predictions — all with the ability to map technical feature names to human-readable labels. The goal is to close the gap between the data scientist who builds the model and the business analyst or compliance officer who needs to verify it makes sense.

This addresses a real deployment problem: ML models may perform well on metrics but fail to gain trust from stakeholders who can't inspect them. In regulated industries like insurance (MAIF's context), explainability is often a legal requirement — models that affect customers must be able to provide explanations. Shapash competes with Alibi, SHAP's native visualization tools, and InterpretML in this space.

## Key points

- Wraps SHAP and LIME with better visualizations and business-readable labels.
- Generates interactive HTML reports for local (individual prediction) and global (model-level) explanations.
- Targets the communication gap between data scientists and non-technical stakeholders.
- From MAIF — insurance context means explainability is a legal/compliance requirement, not just nice-to-have.
- Competes with Alibi, InterpretML, and SHAP's native tools in the XAI (Explainable AI) space.

[Original](https://github.com/MAIF/shapash) → GitHub
