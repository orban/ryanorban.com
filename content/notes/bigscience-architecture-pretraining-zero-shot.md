---
title: What Language Model Architecture and Pretraining Objective Work Best for Zero-Shot Generalization?
date: 2022-07-27
categories:
  - llm
  - pretraining
  - architecture
  - zero-shot
  - research
description: "Wang, Roberts, Scao et al. (BigScience Architecture Group) conduct a large-scale comparison of model architectures (causal decoder, non-causal decoder, encoder-decoder) and pretraining objectives (autoregressive, masked LM) for zero-shot generalization. The key finding: causal decoders + autoregressive LM win at zero-shot; non-causal decoders + masked LM + multitask fine-tuning win overall."
params:
  source: papers
  sourceUrl: https://arxiv.org/abs/2204.05832
---

## Summary

Thomas Wang, Adam Roberts, Teven Le Scao, Hyung Won Chung, Julien Launay, Colin Raffel, and the BigScience Architecture & Scaling Group (arXiv:2204.05832, Apr 2022) conduct a controlled large-scale study of the architectural and objective choices that drive zero-shot generalization in pretrained language models. By 2022, the field had GPT-3 (causal decoder, autoregressive), T5 (encoder-decoder, masked LM), and GLM (non-causal, various) — but no systematic comparison had been done at comparable scale.

The study trains six models with over 5 billion parameters each, systematically varying three factors: **architecture** (causal decoder, non-causal decoder, encoder-decoder), **pretraining objective** (autoregressive language modeling, masked language modeling), and **whether multitask prompted finetuning** is applied (as in T0/FLAN). The key findings: (1) causal decoder + autoregressive LM produces the strongest zero-shot performance after purely unsupervised pretraining; (2) non-causal decoder + masked LM + multitask finetuning performs best overall. The GPT-style architecture is the natural zero-shot generalizer; the T5-style architecture needs instruction tuning to realize its potential.

The paper also explores **cross-architecture adaptation**: pretrained non-causal decoder models can be adapted into causal decoders using autoregressive LM as a downstream task, and vice versa. This suggests that pretraining and architecture choices are more separable than previously assumed — you can adapt architectures across training regimes rather than starting from scratch. The paper is a contribution to understanding *why* the GPT paradigm (causal decoder + autoregressive LM) became dominant: it's empirically superior for zero-shot generalization, the most practically valuable regime for large-scale deployment.

## Key points

- Causal decoder + autoregressive LM = strongest zero-shot generalization after unsupervised pretraining
- Non-causal decoder + masked LM + multitask finetuning = best overall — but requires the finetuning step
- Cross-architecture adaptation is feasible: non-causal → causal and causal → non-causal with targeted adaptation
- Controlled comparison at 5B+ parameters makes conclusions more likely to transfer to larger scales
- Explains the dominance of the GPT paradigm: best zero-shot regime, most useful for large-scale deployment without task-specific tuning

[Original](https://arxiv.org/abs/2204.05832)
