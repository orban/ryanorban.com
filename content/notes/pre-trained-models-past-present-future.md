---
title: "Pre-Trained Models: Past, Present and Future"
date: 2022-07-19
categories:
  - nlp
  - pre-training
  - transfer-learning
  - bert
  - gpt
  - survey
  - language-models
description: "Comprehensive survey of large-scale pre-trained models (PTMs) tracing the evolution from BERT and GPT through four research frontiers: architecture, contextual use, efficiency, and interpretability. Required reading for understanding how self-supervised pre-training became the unified backbone of modern AI."
params:
  source: papers
  sourceUrl: https://arxiv.org/abs/2106.07139
---

## Summary

Large-scale pre-trained models (PTMs) like BERT and GPT have become the dominant paradigm in artificial intelligence, effectively replacing task-specific architectures by storing knowledge in huge parameter sets and adapting via fine-tuning. This survey from Tsinghua University traces the trajectory from early word embeddings like Word2Vec through contextual representations to the current era of billion-parameter models.

The paper argues that PTMs succeed because pre-training objectives — masked language modeling, causal language modeling, contrastive learning, and others — expose models to the statistical structure of language at a scale no task-specific dataset can match. Transfer learning then lets that general knowledge flow into downstream tasks with minimal labeled data. The authors identify four active research frontiers: designing more expressive architectures, leveraging context more effectively (e.g., few-shot prompting), reducing computational cost via knowledge distillation and pruning, and developing better theoretical understanding of what PTMs actually learn.

The survey situates PTMs within the broader arc of self-supervised learning, noting connections to contrastive self-supervised learning in vision and multimodal settings. The authors predict that the trend toward larger, more general models will continue, and that multi-modal pre-training (text, image, code) will increasingly unify previously separate research communities.

## Key points

- BERT introduced bidirectional masked language modeling as a pre-training objective, becoming the standard encoder; GPT showed that left-to-right autoregressive pre-training scales effectively for generation.
- Four open challenges: finding better pre-training objectives, efficient use of very long context, reducing the computational cost of pre-training and fine-tuning, and interpretability of learned representations.
- Parameter-efficient fine-tuning (prefix tuning, adapters) is highlighted as an emerging alternative to full fine-tuning for adapting large PTMs.
- The shift from task-specific architectures to general PTMs mirrors the shift in vision from hand-engineered features to ImageNet-pretrained convolutional neural networks in 2012.
- Multi-task learning and meta-learning are discussed as complementary approaches to transfer learning that can further reduce labeled data requirements.

[Original paper](https://arxiv.org/abs/2106.07139)
