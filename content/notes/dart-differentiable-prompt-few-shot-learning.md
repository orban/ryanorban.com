---
title: "DART: Differentiable Prompt Makes Pre-Trained Language Models Better Few-Shot Learners"
date: 2022-07-30
categories:
  - llm
  - prompting
  - few-shot-learning
  - nlp
  - research
description: DART (Differentiable pRompT) trains prompt templates end-to-end via backpropagation, treating prompts as learnable continuous vectors rather than fixed text. It makes small pre-trained language models competitive few-shot learners without scaling to GPT-3 sizes — an important stepping stone between hand-crafted prompts and full fine-tuning.
params:
  source: papers
  sourceUrl: https://arxiv.org/abs/2108.13161
---

## Summary

Ningyu Zhang, Luoqiu Li, Xiang Chen, and collaborators at Zhejiang University and Alibaba (ICLR 2022, arXiv:2108.13161) propose DART (Differentiable pRompT) — a method for converting smaller pre-trained language models into better few-shot learners by making prompt templates and target label tokens directly optimizable via backpropagation. The motivation: GPT-3's impressive few-shot capabilities require 175B parameters, making deployment impractical. But GPT-3's success comes partly from in-context learning via prompts, not just scale. If the prompt itself were optimizable rather than hand-designed, smaller models might achieve comparable few-shot performance.

The core idea: rather than writing "The sentiment of [input] is [mask]" as a fixed string and hoping the model fills in "positive" or negative, DART treats the prompt template tokens as continuous vectors in embedding space and optimizes them jointly with a small labeled training set. The label mapping (what token at [mask] corresponds to which class) is also optimized. This is a form of soft prompting or prefix tuning — the prompt becomes a learned parameter rather than natural language, enabling gradient-based optimization while keeping the underlying model frozen.

DART is described as pluggable (works with any pre-trained LM) and extensible (handles diverse classification tasks by reformulating them as cloze completion). The approach sits in the tradition of prompt engineering automation — AutoPrompt, prefix tuning, and P-tuning all address the same core problem of making prompts learnable. The specific contribution of DART is its unified treatment of template tokens and label tokens as jointly optimizable, and its evaluation across standard NLP benchmarks showing consistent gains over hand-crafted prompts in low-data regimes.

## Key points

- DART optimizes prompt templates and label tokens jointly via backpropagation — continuous prompt vectors, not discrete text
- Makes small models competitive few-shot learners without scaling to GPT-3-scale
- Pluggable: works with any pre-trained LM by treating downstream tasks as cloze completion
- Related to soft prompting, prefix tuning, P-tuning, AutoPrompt — all tackle the same problem of learnable prompts
- Evaluated on standard NLP benchmarks in low-data regime; consistently outperforms discrete hand-crafted prompts
- Precedes instruction tuning era where prompt optimization gave way to large-scale data approaches

[Original](https://arxiv.org/abs/2108.13161)
