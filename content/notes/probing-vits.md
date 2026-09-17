---
title: Probing Vision Transformers
date: 2022-08-18
categories:
  - vision-transformers
  - vit
  - interpretability
  - deep-learning
  - research
description: "A research repository probing the internal representations and attention mechanisms of Vision Transformers (ViT, DeiT, DINO). Notable finding: self-supervised DINO produces more salient attention maps than supervised models, suggesting better spatial semantics from self-supervision."
params:
  source: pinboard
  sourceUrl: https://github.com/sayakpaul/probing-vits
---

## Summary

This repository by Sayak Paul implements analysis techniques for understanding what Vision Transformers (ViTs) learn internally. Probing is a standard interpretability methodology: examine the representations learned at different layers by analyzing attention patterns and learned embeddings, rather than just measuring task accuracy.

The repo covers three ViT families — the original ViT (Google Brain, 2020), DeiT (Facebook AI Research's data-efficient variant), and DINO (self-supervised learning via self-distillation). For each, it implements attention visualization (which image regions each head attends to), mean attention distance (how far attention propagates), attention rollout (tracing flow through layers), positional embedding visualization, and projection filter visualization.

The notable finding: DINO produces more salient attention maps than supervised equivalents. DINO learns without labels via self-distillation, yet its attention clearly segments objects in scenes — often better than a model trained with supervision. This matters for understanding the relationship between training objective and representation quality in ViTs, and suggests self-supervised learning learns more semantically meaningful spatial representations than supervised classification.

## Key points

- Probing techniques for Vision Transformers: attention visualization, mean attention distance, attention rollout, positional embedding analysis.
- Covers ViT, DeiT, and DINO model families.
- Notable: DINO (self-supervised) produces more salient attention maps than supervised models.
- Implemented in TensorFlow with interactive demos on Hugging Face Spaces.
- Sayak Paul is a Hugging Face contributor known for TF/Keras ML implementations.
- Connects to broader work on [mechanistic interpretability](/notes/mechanistic-interpretability/) — understanding what learned representations encode.

[Original](https://github.com/sayakpaul/probing-vits) → GitHub
