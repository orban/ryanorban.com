---
title: "How Attention Got So Efficient: GQA, MLA, DSA explained"
date: 2025-12-01
categories:
  - machine-learning
  - transformers
  - attention
  - youtube
  - education
description: A YouTube explainer on how attention mechanisms evolved from full multi-head attention to the efficient variants powering modern LLMs — covering GQA (Grouped Query Attention), MLA (Multi-head Latent Attention from DeepSeek), and DSA (Dynamic Sparse Attention). Useful for understanding why modern inference is faster and cheaper than it was two years ago.
params:
  source: pinboard
  sourceUrl: https://m.youtube.com/watch?v=Y-o545eYjXM
---

![How Attention Got So Efficient: GQA, MLA, DSA explained](/images/notes/how-attention-got-efficient-youtube.png)

## Summary

This YouTube video traces the evolution of attention mechanisms in transformers from standard multi-head attention to the efficient variants that make modern LLM inference practical. The three techniques covered — Grouped Query Attention (GQA), Multi-head Latent Attention (MLA from DeepSeek), and Dynamic Sparse Attention (DSA) — each attack the same fundamental bottleneck: the KV cache grows with context length and dominates memory bandwidth at inference time.

Grouped Query Attention reduces the number of key-value heads relative to query heads, cutting KV cache size proportionally. Multi-head Latent Attention, used in DeepSeek-V2 and DeepSeek-V3, compresses key-value representations into a low-dimensional latent space — a more aggressive reduction that trades some representational capacity for a much smaller cache footprint. Dynamic Sparse Attention takes a different approach: instead of reducing the KV cache, it selectively attends to only the most relevant tokens rather than all tokens, making the computation sparse rather than dense.

Understanding this evolution matters for anyone working with or reasoning about LLM deployment. The difference between full attention and GQA explains a significant chunk of why Llama 2 vs Llama 3 inference costs differ. MLA is central to understanding why DeepSeek's models punch above their weight on cost.

## Key points

- GQA (Grouped Query Attention): fewer KV heads than Q heads — reduces cache with minimal accuracy loss, used in Llama 3, Mistral.
- MLA (Multi-head Latent Attention): compresses KV into low-dimensional latent — DeepSeek-V2/V3's core efficiency innovation.
- DSA (Dynamic Sparse Attention): attend to relevant tokens only — computation becomes sparse rather than $O(n^2)$.
- All three target the KV cache bottleneck — the dominant memory and bandwidth cost at inference time.
- Efficiency gains explain much of the cost reduction between 2023 and 2025 LLM inference.
- Companion to Physics of Language Models series for understanding transformer internals.

[Original](https://m.youtube.com/watch?v=Y-o545eYjXM)
