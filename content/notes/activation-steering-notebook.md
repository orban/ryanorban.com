---
title: Activation Steering Notebook (concentration_notebooks)
date: 2024-12-18
categories:
  - mechanistic-interpretability
  - activation-steering
  - llm
  - research
  - jupyter
description: A Jupyter notebook exploring activation steering in neural networks from the concentration_notebooks repo. Saved as a reference in the mechanistic interpretability and model steering space.
params:
  source: pinboard
  sourceUrl: https://github.com/Elluran/concentration_notebooks/blob/main/steering.ipynb
---

![Activation Steering Notebook (concentration_notebooks)](/images/notes/activation-steering-notebook.png)

## Summary

This is a Jupyter notebook (steering.ipynb) from the concentration_notebooks repository by Elluran, exploring activation steering in large language models. Activation steering is the technique of adding or subtracting activation vectors at specific layers during inference to systematically shift model behavior — steering the model toward or away from concepts, behaviors, or styles without fine-tuning.

Activation steering has become a key tool in mechanistic interpretability research. The basic idea: identify the direction in activation space that corresponds to a concept (e.g., "anger" or French language), then add a scaled version of that vector during inference. The model starts generating text that reflects the steered concept more or less strongly depending on the scaling factor. Related techniques include Contrastive Activation Addition (CAA), representation engineering, and feature steering using sparse autoencoder (SAE) features.

The "concentration" framing in the repo name may relate to attention concentration studies or to feature concentration in activation space — areas of active mechanistic interpretability research. The notebook format makes it a practical exploration resource alongside more formal papers in the steering/interpretability literature.

## Key points

- Activation steering: add/subtract direction vectors in activation space to shift model behavior.
- Related to representation engineering and Contrastive Activation Addition (CAA).
- Sparse autoencoder features can be used as more precise steering targets than hand-crafted vectors.
- Jupyter notebook format — exploratory, hands-on reference in the mechanistic interpretability tradition.
- Connected to the broader project of understanding and controlling LLM internals.

[Original](https://github.com/Elluran/concentration_notebooks/blob/main/steering.ipynb) → GitHub
