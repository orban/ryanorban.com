---
title: Editable Neural Networks
date: 2022-09-15
categories:
  - machine-learning
  - model-editing
  - research
  - neural-networks
  - iclr
description: ICLR paper proposing 'editable neural networks' — a method for making targeted modifications to a model's behavior on specific inputs without disrupting performance elsewhere. An early formalization of the model editing problem.
params:
  source: pinboard
  sourceUrl: https://openreview.net/forum?id=HJedXaEtvS
---

![Editable Neural Networks](/images/notes/editable-neural-networks.png)

## Summary

This ICLR paper formalizes the problem of editing neural networks — making targeted changes to a model's predictions on specific inputs while preserving performance on everything else. The key tension is locality: a gradient descent update to fix a wrong prediction tends to ripple through the network and affect unrelated predictions in unpredictable ways.

The proposed approach learns to make local edits by training an auxiliary network (an editor) that can modify the base model's hidden states in a targeted way. The editor is trained to be a surgeon — adjusting exactly the representation needed for the target input without disturbing the base network's behavior elsewhere. This is conceptually different from fine-tuning, which adjusts weights globally.

The model editing framing has since become a significant research area, branching into approaches like ROME (rank-one weight edits), SERAC (memory-based edits), and MEMIT (mass editing). This paper is an early contribution to the formal definition of what an edit is: it should affect the target input, generalize to semantically equivalent paraphrases of the target, and leave unrelated inputs unchanged.

## Key points

- Formalizes model editing as a problem: targeted prediction changes without global side effects.
- Auxiliary editor network modifies hidden states rather than fine-tuning weights directly.
- Three desiderata for a valid edit: target accuracy, generalization to paraphrases, locality for unrelated inputs.
- Early formal contribution to a problem that became major research focus 2022–2024.
- Precursor to ROME, MEMIT, SERAC — the dominant 2022-2023 model editing methods.
- Relevant to factual knowledge correction in LLMs without full retraining.

[Original](https://openreview.net/forum?id=HJedXaEtvS)
