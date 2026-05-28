---
title: From Deep to Long Learning?
date: 2023-04-09
categories:
  - machine-learning
  - long-context
  - state-space-models
  - research
  - transformers
description: Stanford Hazy Research argues the next frontier is moving from deep networks to networks that can process very long sequences — motivating state space models like Mamba as a shift away from transformer attention's O(n²) complexity. A prescient 2023 post about where sequence modeling was headed.
params:
  source: pinboard
  sourceUrl: https://hazyresearch.stanford.edu/blog/2023-03-27-long-learning
---

## Summary

Hazy Research at Stanford argues that the next architectural challenge for machine learning is handling very long sequences — not just going deeper in layers, but extending effective context to millions of tokens. The framing: the field spent a decade learning to build "deep" networks that process fixed-length inputs through many layers; the next era requires "long" networks that maintain useful state across extremely long sequences.

The post motivates state space models (SSMs) like H3 and the subsequent Mamba as alternatives to transformer attention. The core problem with transformers: the self-attention mechanism is O(n²) in sequence length — it scales quadratically, making long-context processing expensive. SSMs handle long sequences in linear time by maintaining a compressed state representation rather than attending over all past tokens. The tradeoff is recall quality (transformers can retrieve from anywhere in context; SSMs must compress the past), but for many tasks the efficient long-sequence processing is worth it.

This post was published in March 2023, before Mamba (December 2023) popularized SSMs for language modeling. It captures the intellectual foundation of the shift from transformer-centric to hybrid architectures, connecting work from Hazy Research (FlashAttention, H3) to the broader question of whether transformers are the right architecture for long-context tasks. The long learning framing proved accurate: by 2024-2025, context window length had become a primary competitive dimension for LLM providers, and hybrid SSM/transformer architectures like Jamba were being deployed at scale.

## Key points

- Argues for "long" networks that handle extended sequences as the next ML frontier, beyond just "deep" networks.
- Transformers scale O(n²) in attention — prohibitively expensive for million-token contexts.
- State space models (SSMs) scale linearly but compress context — tradeoff between efficiency and recall.
- From Hazy Research (Stanford) — the lab behind FlashAttention, H3, and early SSM language modeling work.
- Published March 2023, before Mamba — prescient framing of the SSM vs. transformer debate.
- By 2024, context length had become a primary competitive dimension, validating the "long learning" thesis.

[Original](https://hazyresearch.stanford.edu/blog/2023-03-27-long-learning)
