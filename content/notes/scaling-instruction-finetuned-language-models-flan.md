---
title: Scaling Instruction-Finetuned Language Models
date: 2022-10-27
categories:
  - llm
  - instruction-tuning
  - fine-tuning
  - scaling
  - chain-of-thought
description: The FLAN-T5 and Flan-PaLM paper (2022) showing that instruction finetuning across 1.8K tasks improves performance on zero-shot, few-shot, and chain-of-thought prompting across multiple model families. Established instruction finetuning as a general-purpose method and released Flan-T5 checkpoints that shaped the open-source LLM ecosystem.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/Scaling Instruction-Finetuned Language Models.pdf
---

## Summary

Hyung Won Chung, Le Hou, Shayne Longpre et al. (Google Research, 34 authors) systematically study three dimensions of instruction finetuning: task quantity (how many diverse tasks), model scale, and inclusion of chain-of-thought (CoT) training data. The paper is the technical report behind Flan-PaLM and Flan-T5 — models that became reference points for instruction-following capability throughout 2022–2023.

The headline results: Flan-PaLM 540B achieves 75.2% 5-shot accuracy on MMLU (then state-of-the-art) and +9.4% average improvement over base PaLM across a broad evaluation suite. More importantly, the scaling analysis shows that all three dimensions matter and interact: more tasks help, larger scale helps, and including CoT data specifically improves reasoning-oriented tasks without hurting others. The released Flan-T5 checkpoints (80M to 11B parameters) provide a public-release artifact that influences much downstream work, including use as a backbone for RLHF and instruction-following research.

The paper formalizes a recipe that was implicitly understood but not systematically validated: curate a diverse set of tasks as natural-language instructions, finetune on them in a multi-task fashion, and the resulting model generalizes better to new tasks in zero-shot or few-shot settings. This establishes instruction finetuning as a general-purpose technique rather than task-specific fine-tuning. The CoT component is especially significant: it demonstrates that training on reasoning traces generalizes to held-out reasoning tasks, anticipating later work on RLVR and reasoning models.

## Key points

- Three-way scaling study: task quantity (1.8K tasks), model scale (PaLM 8B to 540B), and chain-of-thought data — all three matter and interact
- Flan-PaLM 540B: 75.2% MMLU (5-shot), +9.4% average over base PaLM — then state-of-the-art
- Released Flan-T5 checkpoints (80M–11B) became a key open-source baseline for instruction-following research
- CoT training data generalizes to held-out reasoning tasks — reasoning-capability transfer across tasks
- Established instruction finetuning as a general method, not a task-specific trick — significant paradigm shift
- Precursor to RLHF-based alignment: demonstrates the value of natural-language supervision before reward modeling becomes dominant

[Original paper](https://arxiv.org/abs/2210.11416)
