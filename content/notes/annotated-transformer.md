---
title: The Annotated Transformer
date: 2025-08-27
categories:
  - machine-learning
  - transformers
  - attention
  - education
  - nlp
description: The Annotated Transformer by Sasha Rush is a line-by-line annotated implementation of the 'Attention is All You Need' paper, reorganized for pedagogical clarity. One of the most important educational resources for understanding transformers in practice.
params:
  source: pinboard
  sourceUrl: https://nlp.seas.harvard.edu/annotated-transformer/
---

![The Annotated Transformer](/images/notes/annotated-transformer.png)

## Summary

The Annotated Transformer is an educational resource by Sasha Rush (Harvard NLP, 2018, updated 2022) that re-presents the Attention Is All You Need paper as an annotated, working code implementation. Rather than just summarizing the paper, it reorganizes the content so that each concept is immediately followed by the code that implements it — bridging the gap between mathematical notation and what the model is actually doing.

The transformer architecture introduced in Attention Is All You Need (Vaswani et al., 2017) became the foundational architecture for modern LLMs, BERT, GPT, and essentially all of current deep learning NLP. Understanding it at the implementation level — not just conceptually — matters for anyone building or reasoning about these systems. The Annotated Transformer makes this accessible by pairing equations with working PyTorch code in a readable, navigable format.

The resource has been updated as the community's understanding evolved and has become a standard reference point — often assigned in university deep learning courses alongside the original paper. It's the clearest path from I've heard of transformers to "I understand how they actually work at the code level."

## Key points

- Line-by-line PyTorch implementation of the original transformer architecture.
- Reorganizes Attention Is All You Need (Vaswani et al. 2017) for pedagogical clarity.
- Pairs mathematical notation with the code that implements each concept.
- By Sasha Rush (Harvard NLP); updated in 2022 with community contributions.
- Standard deep learning education reference, often used alongside the original paper.
- The clearest path from reading to understanding transformers at implementation level.

[Original](https://nlp.seas.harvard.edu/annotated-transformer/)
