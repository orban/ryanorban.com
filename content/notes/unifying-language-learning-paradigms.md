---
title: Unifying Language Learning Paradigms (UL2)
date: 2022-06-07
categories:
  - nlp
  - pre-training
  - language-models
  - google-research
  - t5
  - architecture
description: Google Research's UL2 paper proposes Mixture-of-Denoisers (MoD), a unified pre-training objective that combines span corruption, prefix LM, and causal LM into a single framework — and separates architecture choices from pre-training objectives, which were previously conflated. The insight that objective and architecture are orthogonal opened the door to mixing paradigms that were previously treated as distinct camps.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/Unifying Language Learning Paradigms.pdf
---

## Summary

Yi Tay, Mostafa Dehghani, and colleagues at Google Research present a unified framework for pre-training language models that disentangles two concepts researchers had long conflated: architectural choices and pre-training objectives. The paper's central argument is that questions like "should I use an encoder-decoder or a decoder-only architecture?" are separate from questions like "what self-supervised objective should I train with?" — and that treating them as the same question has led to unnecessary fragmentation in the field.

The core contribution is Mixture-of-Denoisers (MoD), a pre-training objective that blends three distinct paradigms: (1) span corruption as in T5, where contiguous token spans are masked and reconstructed; (2) Extreme Span Corruption (X-Denoisers), with longer and more aggressive masking; and (3) Prefix Language Modeling (R-Denoisers), where the model sees a prefix and generates the rest causally. Rather than committing to one paradigm, MoD trains a single model on all three simultaneously. The paper also introduces mode switching, where different fine-tuning setups (called R, S, and X modes) correspond to the pre-training scheme best matched to the downstream task type — generative tasks prefer causal mode, classification tasks prefer the bidirectional mode.

The resulting model, UL2 (20B parameters), achieves state-of-the-art or competitive results on a wide range of NLP benchmarks. Crucially, it beats models that had been pre-trained with a single objective, suggesting that the multi-paradigm pre-training provides a richer internal representation that generalizes better across task types. The paper connects to earlier work on multi-task learning but frames it more specifically around the objective-architecture orthogonality insight.

## Key points

- Mixture-of-Denoisers (MoD) is the central contribution: a single pre-training objective blending span corruption, extreme span corruption, and prefix language modeling simultaneously.
- Architecture and pre-training objective are orthogonal — conflating them led to the false dichotomy between T5-style encoder-decoder models and GPT-style decoder-only models.
- Mode switching associates downstream tasks with the pre-training scheme best suited to them (R/S/X modes), improving few-shot and fine-tuned performance.
- UL2 (20B) outperforms GPT-3 and T5 on many benchmarks despite matching or exceeding much larger models, suggesting objective diversity is more important than scale alone.
- Connects to instruction tuning and FLAN-style research — unified objectives make it easier to train models that generalize across task formats.

[Original PDF](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/Unifying%20Language%20Learning%20Paradigms.pdf)
