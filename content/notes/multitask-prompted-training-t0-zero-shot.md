---
title: Multitask Prompted Training Enables Zero-Shot Task Generalization
date: 2022-07-27
categories:
  - llm
  - zero-shot
  - instruction-tuning
  - multi-task
  - huggingface
  - research
description: T0 shows that training a language model on 2000+ diverse human-authored prompts across 170+ NLP tasks dramatically improves zero-shot generalization to unseen tasks. An 11B T0 model outperformed 175B GPT-3 zero-shot — proving prompt diversity during training matters more than raw scale for generalization.
params:
  source: papers
  sourceUrl: https://arxiv.org/abs/2110.01691
---

## Summary

T0 (T-Zero) is a BigScience / Hugging Face paper demonstrating that training on a diverse collection of explicitly-prompted tasks dramatically improves zero-shot generalization to unseen task families. The authors built P3 (Public Pool of Prompts), a dataset of 2,000+ prompts across 170+ NLP tasks, and fine-tuned T5 (11B parameters) on a large subset.

The central finding: T0 substantially outperformed the much larger GPT-3 (175B) on held-out zero-shot benchmarks despite being 16× smaller. This established that instruction tuning with diverse prompt coverage is the key driver of zero-shot generalization — more impactful than raw model scale for out-of-domain transfer.

The work sits at the intersection of instruction tuning, prompt engineering, and multi-task learning, and directly influenced FLAN, InstructGPT, and the entire wave of aligned LLMs that followed. P3 became a community resource enabling reproducible comparisons of instruction tuning approaches.

## Key points

- Multitask prompted training on 2,000+ diverse prompts causes emergent zero-shot generalization — not interpolation within training tasks, but transfer to new task families
- T0 (11B) outperformed GPT-3 (175B) zero-shot, showing that aligned instruction coverage dominates raw parameter count for held-out generalization
- P3 (Public Pool of Prompts) became a shared resource enabling reproducible instruction tuning research — a community infrastructure contribution as important as the model
- Prompt diversity across task *families* matters more than volume within any single family; the ablations show variety is the key variable
- Directly influenced FLAN, FLAN-T5, InstructGPT, and the modern paradigm of instruction-tuned LLMs as the default deployment format

[Original paper](https://arxiv.org/abs/2110.01691)
