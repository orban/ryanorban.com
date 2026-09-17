---
title: Differentiable Prompt Makes Pre-trained Language Models Better Few-Shot Learners
date: 2022-07-30
categories:
  - nlp
  - prompting
  - few-shot-learning
  - fine-tuning
  - research
description: DifferentiablePrompt (DPT) replaces discrete token prompts with optimized continuous embeddings, enabling gradient-based prompt tuning for few-shot learning. Published at ICLR 2022, it established that soft prompts can match full fine-tuning with far fewer parameters.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/differentiable.pdf
---

## Summary

Ningyu Zhang, Luoqiu Li, Xiang Chen, Shumin Deng, Zhen Bi, Chuanqi Tan, Fei Huang, and Huajun Chen at Zhejiang University and Alibaba (arXiv 2108.13161, ICLR 2022) present DifferentiablePrompt (DPT), a method for few-shot learning with pre-trained language models that combines soft prompt tuning with verbalizer optimization. Rather than engineering hand-crafted discrete prompts, DPT learns continuous prompt embeddings jointly with the mapping from model outputs to task labels.

The key insight is that prompt tuning can be made end-to-end differentiable by replacing the discrete tokens of a template with continuous vectors in the model's embedding space. These vectors have no corresponding words — they're soft tokens that the model treats as input but that exist only as real-valued vectors optimized by backpropagation. This allows gradient-based optimization of the prompt while keeping the pre-trained model weights frozen (parameter-efficient) or fine-tuning only a small set of parameters. DPT also learns a differentiable verbalizer mapping that determines which output tokens correspond to which task labels, removing another manual design choice from the pipeline.

On standard few-shot NLP benchmarks (SuperGLUE, relation extraction, text classification), DPT matches or exceeds methods that fully fine-tune the model, despite only updating a small number of parameters. This was an early demonstration that parameter-efficient fine-tuning (PEFT) methods could be competitive with full fine-tuning — a finding that later motivated LoRA, prefix tuning, and the entire PEFT landscape.

## Key points

- Replaces discrete prompt tokens with continuous soft prompt embeddings optimized by backpropagation — making prompts differentiable.
- Both the prompt template and the verbalizer (label mapping) are learned jointly, removing manual design.
- Parameter-efficient: only soft tokens are updated, the pre-trained model is frozen.
- Matches full fine-tuning on SuperGLUE and relation extraction in few-shot settings.
- Early demonstration that PEFT methods are competitive — precursor to LoRA, prefix tuning, prompt tuning.
- Limitation: soft prompts are not human-readable and don't transfer across model architectures.

[Original paper](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/differentiable.pdf)
