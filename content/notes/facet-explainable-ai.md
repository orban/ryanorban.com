---
title: "FACET: Human-Explainable AI"
date: 2021-02-28
categories:
  - machine-learning
  - interpretability
  - explainability
  - python
  - open-source
description: FACET is BCG Gamma's Python library for human-explainable AI — extending SHAP with interaction effects and redundancy-aware feature importance, plus simulation tools for model-based what-if analysis. More sophisticated than vanilla SHAP for understanding feature relationships.
params:
  source: pinboard
  sourceUrl: https://github.com/BCG-Gamma/facet
---

![FACET: Human-Explainable AI](/images/notes/facet-explainable-ai.png)

## Summary

FACET is an open-source Python library from BCG Gamma (BCG's data science unit) for machine learning model inspection and explanation. It extends SHAP values with additional analysis layers: synergy (how features interact to jointly influence predictions), redundancy (when features carry overlapping information), and independence (when features contribute independently). These decompositions go beyond standard SHAP to explain *how* features relate to each other.

The library also provides simulation tools — given a fitted model, you can run what-if scenarios (what happens to predicted churn probability if we increase customer tenure by 1 year?) using the model as a simulator. This is positioned for business stakeholders who need to reason about interventions, not just understand historical patterns.

FACET sits in the same space as Shapash and InterpretML but targets a more analytical audience comfortable with statistical decompositions. The synergy/redundancy decomposition is particularly useful for feature selection — if two features are highly redundant (measuring the same underlying signal), keeping both may not improve the model while adding complexity. Understanding this structure before building final models can improve both performance and interpretability.

## Key points

- Extends SHAP with synergy, redundancy, and independence decomposition — explains feature *relationships*, not just importance.
- Redundancy analysis: identifies features that carry overlapping information — guides feature selection.
- Synergy analysis: identifies feature pairs whose joint contribution exceeds their individual contributions.
- Simulation tools: run what-if scenarios using the model as a causal simulator.
- From BCG Gamma — targets practitioners who need both model explanation and business scenario analysis.

[Original](https://github.com/BCG-Gamma/facet) → GitHub
