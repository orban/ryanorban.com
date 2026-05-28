---
title: "ChatRWKV: ChatGPT Powered by an RNN"
date: 2023-01-20
categories:
  - llm
  - rnn
  - open-source
  - architecture
  - research
description: ChatRWKV is a ChatGPT-like chatbot built on the RWKV architecture — a language model that achieves transformer-level performance using an RNN design, enabling constant memory inference regardless of sequence length. A significant architectural alternative to attention-based transformers.
params:
  source: pinboard
  sourceUrl: https://github.com/BlinkDL/ChatRWKV
---

![ChatRWKV: ChatGPT Powered by an RNN](/images/notes/chatrwkv-rnn-language-model.png)

## Summary

ChatRWKV is a ChatGPT-style conversational model built on [RWKV](/notes/rwkv/) — an architecture by BlinkDL (Bo Peng) that achieves transformer-level language modeling performance while using a recurrent neural network design rather than self-attention. The key property: [RWKV](/notes/rwkv/) inference uses constant memory and constant compute per token regardless of context length, unlike transformers where KV cache memory grows linearly with sequence length.

[RWKV](/notes/rwkv/) (Receptance Weighted Key Value) reformulates the attention mechanism into a linear recurrence that can be computed efficiently both as a sequential RNN (for inference) and as a parallel scan (for training, similar to transformer parallelism). This gives it the best of both worlds: parallelizable training and constant-time inference. The architecture is an alternative to efforts like Mamba and [RWKV](/notes/rwkv/) 5/6 that similarly try to escape the quadratic attention cost.

The significance at the time of release (early 2023) was demonstrating that the transformer wasn't the only viable architecture for large language models. [RWKV](/notes/rwkv/) matched GPT performance on standard benchmarks while offering fundamentally different inference characteristics — a promising result that helped motivate the broader research direction of linear attention and state space models, later expanded by Mamba (2023) and H3.

## Key points

- [RWKV](/notes/rwkv/) architecture: transformer-quality LM performance with constant memory RNN inference
- No KV cache growth with sequence length — significant advantage for long-context inference
- Parallelizable during training (scan-based), sequential during inference (RNN-style)
- By BlinkDL (Bo Peng) — a single-researcher open-source alternative to transformer LLMs
- Precursor to the broader linear attention / state space model research wave (Mamba, H3)

[Original](https://github.com/BlinkDL/ChatRWKV)
 → GitHub
