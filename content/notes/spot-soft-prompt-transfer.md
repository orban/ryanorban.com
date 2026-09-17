---
title: "SPoT: Better Frozen Model Adaptation through Soft Prompt Transfer"
date: 2022-07-24
categories:
  - prompt-tuning
  - parameter-efficient-finetuning
  - transfer-learning
  - nlp
  - research
description: Vu, Constant, Al-Rfou, Cer, and Lester (Google Research/UMass, 2022) show that initializing soft prompts from a related source task dramatically improves prompt tuning, achieving near fine-tuning performance while keeping the base model frozen. The result reveals that prompt initialization is a critical and underappreciated factor in parameter-efficient adaptation.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/SPOT prompt tuning 2.0.pdf
---

## Summary

Tu Vu, Constant, Al-Rfou, Cer, and Brian Lester (Google Research/UMass, 2022) introduce SPoT (Soft Prompt Transfer), a method for improving prompt tuning by leveraging source task knowledge. Standard prompt tuning — learning a small set of continuous soft prompt tokens prepended to the input while keeping the base model frozen — is highly sensitive to prompt initialization. Random initialization often leads to poor convergence, especially on smaller models and low-resource target tasks. SPoT addresses this by initializing the target task's soft prompt from a prompt already trained on a related source task.

The transfer mechanism is straightforward: train a soft prompt on a source task (e.g., a large multi-task mixture), then use those learned tokens as the starting point for gradient-based optimization on the target task. This warm-start improves both final performance and optimization stability. The paper evaluates source tasks from SuperGLUE and T5 multitask mixtures, showing that even a prompt from a loosely related source task outperforms random initialization by a substantial margin. SPoT achieves near fine-tuning performance on many benchmarks while updating only the soft prompt tokens — the T5 backbone remains entirely frozen.

A secondary contribution is showing that source task selection matters: prompts from semantically related tasks transfer better, and a small meta-learning approach (trying a few source prompts on a validation set) can identify good candidates automatically. This connects SPoT to the broader transfer learning literature on task similarity and task embeddings, applied here to the novel setting of soft prompt initialization. SPoT sits in the ecosystem of parameter-efficient fine-tuning (PEFT) methods alongside prefix tuning, LoRA, and adapters, and shares with those methods the motivation of adapting large frozen models without full fine-tuning. The result that initialization quality dominates random prompting is a durable finding that applies across PEFT methods.

## Key points

- Warm-starting soft prompt tokens from a source task dramatically improves prompt tuning — initialization matters more than previously recognized
- Near fine-tuning performance on SuperGLUE while keeping the T5 backbone entirely frozen
- Source task relevance matters: semantically related sources transfer better, and a validation-based source selection strategy works well
- Sits in the parameter-efficient fine-tuning family alongside LoRA, prefix tuning, and adapters
- Result generalizes: good prompt initialization is a durable finding applicable across PEFT methods, not specific to SPoT's setup

[Source](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/SPOT%20prompt%20tuning%202.0.pdf)
