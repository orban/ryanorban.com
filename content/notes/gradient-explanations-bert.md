---
title: Gradient Explanations for HuggingFace BERT Classification
date: 2022-05-30
categories:
  - machine-learning
  - explainability
  - bert
  - huggingface
  - nlp
description: A tutorial by Victor Dibia on generating gradient-based explanations for HuggingFace BERT text classification models in TensorFlow 2.0 — visualizing which tokens most influenced the model's prediction. Explainability for transformer classifiers was a practical gap in 2022 since attention maps alone are insufficient.
params:
  source: pinboard
  sourceUrl: https://victordibia.com/blog/explain-bert-classification/
---

## Summary

This tutorial by Victor Dibia demonstrates how to generate gradient-based explanations for text classification models built with HuggingFace and BERT in TensorFlow 2.0. The core technique is Integrated Gradients — computing how much each input token's embedding contributes to the final classification score by integrating gradients along a path from a baseline (usually a zero or mask token) to the actual input.

The appeal of gradient methods over plain attention visualization is that attention weights don't directly measure feature importance — a token can receive high attention without actually influencing the output. Integrated Gradients satisfies axiomatic properties (completeness, sensitivity, implementation invariance) that make it a rigorous measure of input attribution rather than a heuristic proxy. For a text classifier, this means you get a score per token that tells you: "removing this token would change the prediction by approximately this much."

The HuggingFace Transformers library made BERT fine-tuning accessible, but the explanability story lagged behind. Tools like Captum (PyTorch) and tf-explain (TensorFlow) attempted to fill this gap. Victor Dibia's tutorial is a practical end-to-end example showing how to wire GradientTape in TF2 with a fine-tuned BERT model to produce attribution heatmaps for individual predictions.

## Key points

- Integrated Gradients measures token-level attribution to model output — more rigorous than attention visualization
- BERT embeddings are continuous, so gradient attribution makes sense: small perturbations in token embeddings trace how they affect the prediction
- HuggingFace abstractions make it easy to get logits; the trick is unwrapping the model to access intermediate embeddings for gradient computation
- Baseline choice matters: a zero embedding baseline vs. a mask token baseline produces different attribution patterns
- Related tools: Captum (PyTorch-based attribution library), LIME, SHAP for NLP
- GradCAM is the analogous technique for computer vision — gradient of class score w.r.t. feature maps

[Original](https://victordibia.com/blog/explain-bert-classification/)
