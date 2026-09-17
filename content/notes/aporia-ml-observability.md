---
title: Aporia — ML Observability
date: 2022-11-25
categories:
  - machine-learning
  - mlops
  - monitoring
  - observability
  - data-drift
description: Aporia is a cloud-native ML observability platform for monitoring deployed models — drift detection, performance monitoring, and explainability tooling. Addresses the gap between training-time metrics and what models actually do in production.
params:
  source: pinboard
  sourceUrl: https://www.aporia.com/
---

## Summary

Aporia is an ML observability platform for monitoring machine learning models after deployment. The core problem it addresses: models trained on historical data degrade silently when the real-world distribution shifts. Data drift (input features changing) and concept drift (the relationship between inputs and outputs changing) are both common and hard to detect without dedicated monitoring infrastructure. A model can continue returning responses while producing subtly wrong predictions — there's no error thrown in the traditional software sense.

The platform centralizes model monitoring with dashboards for tracking feature drift, prediction drift, and custom metrics. It provides model explainability features — surfacing which input features most influenced predictions — which helps with debugging and compliance. The customized monitoring framing lets teams define domain-specific metrics rather than only statistical ones.

Aporia sits in the MLOps tooling space alongside Weights & Biases, Fiddler, Arize AI, and WhyLabs. The category emerged as organizations deployed more ML in production and realized that software engineering observability patterns (metrics, logs, traces) don't directly translate to model behavior monitoring. The harder question — whether centralized ML observability platforms are the right abstraction or whether model monitoring should be embedded into product analytics — remained open as the MLOps market fragmented.

## Key points

- ML observability for production models: detects data drift and concept drift before they cause silent failures.
- Customizable monitoring dashboards — domain-specific metrics beyond just statistical drift measures.
- Model explainability features for debugging and compliance.
- Competes with Arize AI, Fiddler, WhyLabs, Evidently AI in the MLOps monitoring space.
- Addresses the fundamental gap: ML models fail silently, unlike traditional software errors.

[Original](https://www.aporia.com/)
