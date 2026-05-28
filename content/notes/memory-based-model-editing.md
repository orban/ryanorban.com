---
title: Memory-Based Model Editing at Scale
date: 2022-09-15
categories:
  - machine-learning
  - model-editing
  - research
  - language-models
  - icml
description: ICML 2022 paper on memory-based model editing at scale — a method for locally updating a neural network's factual knowledge without full retraining. Uses a cache of explicit edits that override the base model's predictions for targeted inputs.
params:
  source: pinboard
  sourceUrl: https://proceedings.mlr.press/v162/mitchell22a.html
---

![Memory-Based Model Editing at Scale](/images/notes/memory-based-model-editing.png)

## Summary

This ICML 2022 paper from Eric Mitchell, Charles Lin, Antoine Bosselut, Chelsea Finn, and Christopher Manning addresses a fundamental problem with large language models: once-correct predictions become wrong as the world changes, but retraining the full model for each update is prohibitively expensive.

The approach — SERAC (Semi-Parametric Editing with a Retrieval Augmented Counterfactual Model) — uses an explicit memory of edits rather than modifying model weights. When a query comes in, a scope classifier determines whether any stored edit applies. If yes, a small counterfactual model generates the corrected prediction. If no, the base model handles it normally. The memory is separate from the model parameters — you're not doing gradient descent into weights.

This is architecturally interesting because it sidesteps the catastrophic forgetting problem: storing edits in a separate cache doesn't risk degrading the base model's performance on unrelated queries. The downside is that at sufficient edit volume, you need efficient retrieval — the paper demonstrates this scales to thousands of edits while preserving both edit accuracy and base model performance.

The broader context: model editing research is motivated by knowledge editing for factual updates (a person's job title changed, a country's leader changed) as well as safety corrections. It pairs with papers like ROME (Rank-One Model Editing) which takes the weight-modification approach instead.

## Key points

- SERAC: store edits in explicit memory rather than modifying model weights.
- Scope classifier routes queries — edited fact vs. base model behavior.
- Avoids catastrophic forgetting: cache is separate from model parameters.
- Scales to thousands of edits with retrieval-based lookup.
- Relevant to knowledge editing, factual corrections, and safety interventions.
- Contrasts with ROME / MEMIT which directly edit transformer weights.

[Original](https://proceedings.mlr.press/v162/mitchell22a.html)
