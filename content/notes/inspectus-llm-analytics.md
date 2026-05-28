---
title: "Inspectus: LLM Analytics and Visualization"
date: 2024-06-09
categories:
  - llm
  - interpretability
  - visualization
  - research
  - machine-learning
  - open-source
description: Inspectus is labml.ai's tool for visualizing LLM internals — attention maps, token distributions, and model analytics rendered as interactive visualizations in Jupyter notebooks. Makes transformer attention patterns inspectable without custom code.
params:
  source: pinboard
  sourceUrl: https://github.com/labmlai/inspectus
---

![Inspectus: LLM Analytics and Visualization](/images/notes/inspectus-llm-analytics.png)

## Summary

Inspectus is labml.ai's open-source library for visualizing LLM internals, particularly attention patterns and token-level analytics. It renders interactive visualizations inside Jupyter notebooks — attention heatmaps across layers and heads, token probability distributions, and other internal state — so researchers and practitioners can inspect what a model is attending to without writing custom visualization code.

The core visualization is the attention map: a matrix showing which tokens attend to which other tokens at each layer and head. In transformer models, attention is one of the most interpretable internal mechanisms — it directly shows the information-gathering pattern. Inspectus makes it easy to pull these maps out of any HuggingFace Transformers model and render them interactively. You can hover, zoom, filter by head, and compare attention across layers.

Beyond attention, Inspectus includes token distribution visualizations (probability distributions over the vocabulary at each step), useful for understanding why a model chose one token over another, and for spotting cases where the probability mass is unexpectedly distributed. This is directly useful for [mechanistic interpretability](/notes/mechanistic-interpretability/) research, prompt engineering refinement, and debugging unexpected model outputs. The tool sits in the same space as BertViz (attention visualization) and TransformerLens (more full-featured interpretability), but is simpler to drop into an existing Jupyter workflow.

## Key points

- Interactive attention map visualization across layers and heads in Jupyter.
- Token probability distribution visualization for debugging generation decisions.
- Works with HuggingFace Transformers models out of the box.
- Simpler entry point than TransformerLens for quick attention inspection.
- Useful for [mechanistic interpretability](/notes/mechanistic-interpretability/) research and prompt engineering debugging.
- By labml.ai, which also makes experiment tracking tools.

[Original](https://github.com/labmlai/inspectus) → GitHub
