---
title: "LabML Neural Networks: Annotated Implementations"
date: 2021-01-30
categories:
  - machine-learning
  - deep-learning
  - education
  - pytorch
  - annotated-code
description: LabML Neural Networks is a collection of PyTorch implementations of ML papers with line-by-line annotations — making research papers readable by walking through the actual code. Covers transformers, diffusion models, GANs, and RL algorithms side-by-side with the paper math.
params:
  source: pinboard
  sourceUrl: https://nn.labml.ai/index.html
---

## Summary

[LabML Neural Networks](/notes/labml-neural-networks/) is a growing library of PyTorch implementations of influential machine learning papers, each annotated line-by-line in the style of The Annotated Transformer by Harvard NLP. The site renders code alongside explanations, making each file function as both a reference implementation and a reading guide. Papers covered include transformers, diffusion models, GANs, reinforcement learning algorithms, and optimization methods.

The annotation format bridges a gap that code-only implementations don't fill: reading a paper and then reading an implementation separately leaves you to mentally map one onto the other. By interleaving paper-level explanation with the corresponding code, LabML lets you verify that you understand both simultaneously. The PyTorch idioms are also pedagogically valuable — seeing how abstract tensor operations actually get written in practice.

This approach is similar to what Jeremy Howard promotes in [fast.ai](/notes/fastai/): read the code, not just the paper. The difference is that LabML targets paper implementations specifically, while [fast.ai](/notes/fastai/) targets practical applications. For someone who wants to implement a recent paper from scratch, LabML is a good starting point for understanding how standard architectures like VAEs, DDPMs, and attentions are typically coded.

## Key points

- Annotated PyTorch implementations of ML papers — line-by-line explanation alongside the code, eliminating the translation step between paper math and implementation.
- Covers transformers, diffusion models, DDPM, GANs, PPO, and other key architectures and algorithms.
- Inspired by The Annotated Transformer format, extended to a much broader range of papers.
- Useful for practitioners who want to implement papers themselves or verify their understanding of how key algorithms actually work in code.
- Complements Papers With Code for finding implementations; LabML goes deeper on explanation.

[Original](https://nn.labml.ai/index.html)
