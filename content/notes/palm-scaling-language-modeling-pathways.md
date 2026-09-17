---
title: "PaLM: Scaling Language Modeling with Pathways"
date: 2026-04-29
categories:
  - llm
  - scaling
  - google
  - transformers
  - research
description: PaLM is Google's 540B parameter language model trained across 6144 TPU v4 chips using the Pathways distributed training system. It achieved breakthrough performance on multi-step reasoning and BIG-Bench, and documented discontinuous capability gains at scale — capabilities that emerged suddenly with more compute.
params:
  source: papers
  sourceUrl: https://arxiv.org/abs/2204.02311
---

## Summary

PaLM (Pathways Language Model) is Google Research's 540-billion parameter transformer language model, presented in this 2022 paper by Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, and dozens of co-authors. It was trained on 6144 TPU v4 chips using the Pathways distributed training system — a new ML infrastructure framework enabling efficient training across multiple TPU pods. At the time of publication, PaLM was among the largest and best-performing LLMs.

The results established several important findings. PaLM achieved state-of-the-art few-shot learning results on hundreds of language understanding and generation benchmarks — and outperformed fine-tuned models on multi-step reasoning tasks, which was unusual. On BIG-Bench, it exceeded average human performance on a substantial fraction of tasks. Critically, the paper documented **discontinuous improvements**: many BIG-Bench tasks showed near-zero performance at smaller scales, then steep gains as scale reached 540B — direct evidence of emergent capabilities in language models.

PaLM demonstrated strong multilingual capabilities and code generation, alongside comprehensive analyses of bias and toxicity in model outputs. Its infrastructure contribution — the Pathways system — mattered as much as the model itself, because it enabled training a model of this scale across heterogeneous hardware without the fragility of previous distributed training approaches. PaLM prefigured later models like PaLM 2 (which powered Bard) and connected to the broader scaling hypothesis research program.

## Key points

- 540B parameters, 6144 TPU v4 chips, trained via Pathways distributed ML framework — a major infrastructure achievement.
- Discontinuous performance jumps on BIG-Bench tasks at scale = direct empirical evidence for emergent capabilities.
- Outperformed fine-tuned baselines on multi-step reasoning in few-shot learning settings — chain-of-thought prompting worked particularly well here.
- Strong multilingual and code generation capabilities evaluated across dozens of benchmarks.
- Bias and toxicity analysis included — one of the more thorough responsible AI evaluations in a scale paper at that time.
- Infrastructure precursor: Pathways enabled PaLM; its lessons influenced Google's subsequent ML training stack.

[Original](https://arxiv.org/abs/2204.02311)
