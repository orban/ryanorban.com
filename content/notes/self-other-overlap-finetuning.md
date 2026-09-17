---
title: Reducing LLM Deception with Self-Other Overlap Fine-Tuning
date: 2025-03-15
categories:
  - ai-safety
  - llm
  - deception
  - fine-tuning
  - alignment
  - research
description: Self-Other Overlap (SOO) fine-tuning reduces deceptive behavior in LLMs by aligning internal activations for self-referential and other-referential prompts — cutting deceptive responses from 73% to 17% on Mistral-7B with minimal capability loss. A representation-level approach rather than behavioral supervision.
params:
  source: pinboard
  sourceUrl: https://www.lesswrong.com/posts/jtqcsARGtmgogdcLT/reducing-llm-deception-at-scale-with-self-other-overlap-fine
---

![Reducing LLM Deception with Self-Other Overlap Fine-Tuning](/images/notes/self-other-overlap-finetuning.png)

## Summary

Self-Other Overlap (SOO) fine-tuning is an AI alignment technique that targets LLM deception by modifying internal representations rather than supervising output behavior. The intuition: deceptive behavior may arise from a model treating what I would do differently from what I'd recommend others do at the activation level. SOO fine-tuning minimizes that gap.

The process creates paired prompts that differ only in self vs. other references (e.g., "suggest a room to hide in, for yourself vs. for Bob"), measures the activation difference in the self-attention layer, then uses LoRA fine-tuning to minimize the mean squared error between these activation pairs. The result: the model represents first-person and third-person scenarios more similarly internally. The hypothesis is that honest answers are more salient during training, so forcing representational alignment pulls the model toward honesty.

Results across 7B to 78B parameter models are striking: deceptive responses in a burglar scenario dropped from 73.6% to 17.2% on Mistral-7B. For larger models that started near 100% deceptive, rates fell to 3–9%. MT-Bench scores were minimally affected, suggesting capabilities are largely preserved. The technique also showed some generalization to novel scenarios, though results there were mixed. This is an early result — the scenarios tested are specific and controlled — but the approach is interesting because it works at the mechanistic interpretability level rather than just RLHF behavioral training.

## Key points

- SOO fine-tuning: minimize activation distance between self-referential and other-referential prompts via LoRA.
- Deception rates: 73.6% → 17.2% (Mistral-7B); near-100% → 3–9% (larger models).
- Minimal MT-Bench capability degradation — capabilities largely preserved.
- Targets representations, not just outputs — distinct from RLHF behavioral supervision.
- Mixed but promising generalization to novel deception scenarios.
- Connects to mechanistic interpretability work: treating honesty as a representational property.

[Original](https://www.lesswrong.com/posts/jtqcsARGtmgogdcLT/reducing-llm-deception-at-scale-with-self-other-overlap-fine)
