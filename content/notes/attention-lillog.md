---
title: Attention? Attention! (Lilian Weng)
date: 2022-09-17
categories:
  - attention-mechanism
  - machine-learning
  - deep-learning
  - transformers
  - nlp
description: Lilian Weng's canonical blog post on attention mechanisms — written in 2018, it covers sequence-to-sequence attention, self-attention, and multi-head attention. Still the clearest single-page reference for understanding how attention works before reading the Transformer paper.
params:
  source: pinboard
  sourceUrl: https://lilianweng.github.io/posts/2018-06-24-attention/
---

![Attention? Attention! (Lilian Weng)](/images/notes/attention-lillog.png)

## Summary

Lilian Weng's 2018 blog post on attention mechanisms is one of the most-referenced ML explainers on the internet. It covers the evolution from seq2seq models with fixed-size bottleneck vectors to attention-augmented models, then through self-attention to the full Transformer architecture. The writing style is precise and comprehensive — this became the go-to reference before the Attention Is All You Need paper was as widely read.

The historical framing matters: attention mechanisms were first developed for machine translation to let decoders focus on relevant parts of the input sequence rather than compressing everything into one vector. Bahdanau attention was the first major formulation. Self-attention generalized this — instead of encoder-decoder attention, every position attends to every other position in the same sequence.

Multi-head attention runs several attention operations in parallel across different linear projections of the input. Each "head" can specialize in attending to different aspects of the representation — some heads track syntactic structure, others semantic relationships. Concatenating and projecting the outputs combines these perspectives.

The post connects attention to memory networks, neural Turing machines, and other external memory approaches — establishing attention as one instance of a broader class of differentiable soft-addressing mechanisms.

## Key points

- Attention mechanisms solve the bottleneck problem in seq2seq models by letting decoders look at all encoder states.
- Bahdanau attention (2015) was the first prominent formulation for machine translation.
- Self-attention generalizes this: each position attends to all positions in the same sequence.
- Multi-head attention runs parallel attention with different projections — enables specialization.
- Scaled dot-product attention divides by sqrt(d_k) to prevent softmax saturation in high dimensions.
- By Lilian Weng (OpenAI research, formerly), who maintains one of the best technical ML blogs.

[Original](https://lilianweng.github.io/posts/2018-06-24-attention/) → GitHub
