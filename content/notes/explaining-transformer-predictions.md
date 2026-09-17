---
title: Explaining Transformer Model Predictions
date: 2022-08-18
categories:
  - transformers
  - interpretability
  - shap
  - machine-learning
  - explainability
description: "A practical comparison of SHAP, Transformers Interpret, and Ferret for explaining Hugging Face transformer predictions. Key takeaway: different methods give different results for the same prediction — all require careful interpretation."
params:
  source: pinboard
  sourceUrl: https://medium.com/@rajistics/explaining-predictions-from-transformer-models-55ab9c6cab24
---

## Summary

This article introduces and compares three Python packages for explaining transformer model predictions: SHAP (using Partition SHAP for text), Transformers Interpret (using Integrated Gradients from Captum), and Ferret (a benchmarking framework that incorporates multiple methods). Each assigns importance scores to input tokens, showing which words drove a particular prediction.

The core practical challenge: "explanations for text are complicated and need to be appropriately caveated." Different methods return different token importance rankings for the same prediction. SHAP uses hierarchical clustering and Shapley values (slower but theoretically grounded); Transformers Interpret uses Integrated Gradients (faster, gradient-based); Ferret runs multiple methods and compares them. No method is universally correct — they proxy different aspects of importance.

The use cases are concrete: diagnosing why a transformer is making wrong predictions, explaining model behavior to non-technical stakeholders, and satisfying regulatory requirements for explainability in NLP deployments. This was a live concern in 2022 as Hugging Face models were being deployed in production and AI regulation discussions were heating up.

## Key points

- Three packages for explaining transformer predictions: SHAP, Transformers Interpret, Ferret.
- SHAP: Partition Shapley values, hierarchical clustering — slower, theoretically grounded.
- Transformers Interpret: Integrated Gradients via Captum — faster, gradient-based.
- Ferret: benchmarks multiple methods — useful for comparing explanation approaches side by side.
- Key caveat: different methods disagree — explanation results need interpretation, not blind trust.
- Use cases: model debugging, stakeholder communication, AI explainability compliance.

[Original](https://medium.com/@rajistics/explaining-predictions-from-transformer-models-55ab9c6cab24)
