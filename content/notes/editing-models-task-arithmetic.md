---
title: Editing Models with Task Arithmetic
date: 2026-04-29
categories:
  - model-editing
  - fine-tuning
  - weight-space
  - research
  - llm
description: Task Arithmetic shows that fine-tuning deltas (task vectors) can be added, subtracted, and combined arithmetically to edit model behavior — without any additional training. Negation forgets a task; addition combines capabilities; analogical transfer works across tasks.
params:
  source: papers
  sourceUrl: https://arxiv.org/abs/2212.04089
---

## Summary

Task Arithmetic (arXiv 2212.04089, December 2022) from Gabriel Ilharco, Mitchell Wortsman, Suchin Gururangan, and collaborators at University of Washington, Microsoft Research, and Allen Institute for AI introduces **task vectors** — directions in a model's weight space that encode everything needed to perform a specific task. A task vector is computed simply: subtract the pre-trained model weights from the fine-tuned weights on a task. The result is a vector you can manipulate arithmetically.

The key operations are negation and addition. **Negation** (subtracting a task vector from the base model) makes the model *forget* a task — useful for unlearning unwanted behaviors or removing biased capabilities — while leaving unrelated behaviors intact. **Addition** (adding multiple task vectors to the base model) combines capabilities, effectively creating a multi-task model without joint training. Remarkably, when tasks form an analogy relationship ("A is to B as C is to D"), combining three task vectors can improve performance on the fourth task even with no training data for it.

This connects to a broader line of work on model merging and weight interpolation (like WiSE-FT). The key insight is that fine-tuning moves models in structured directions in weight space — and those directions are semantically meaningful. The analogy to Word2Vec's king − man + woman ≈ queen is intentional: the same algebraic structure appears to hold in weight space as in embedding space. This framing turns model editing from an art into something closer to arithmetic.

## Key points

- Task vector = fine-tuned weights − pre-trained weights. A direction in weight space encoding task-specific knowledge.
- Negation removes task capability surgically; addition combines tasks — both without additional training.
- Analogical transfer: if A:B::C:D, combining task vectors from A, B, C improves performance on D with no D training data.
- Experiments across vision, language, and multimodal models — not a domain-specific trick.
- Foundation for later work on model merging, TIES merging, DARE, and sparse model merging methods.
- Simple and computationally cheap: arithmetic operations on weight tensors, no gradient computation needed.

[Original](https://arxiv.org/abs/2212.04089)
