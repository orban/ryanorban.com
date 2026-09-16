---
title: Transformer Inference Arithmetic
date: 2022-04-08
categories:
  - machine-learning
  - transformers
  - inference
  - performance
  - systems
description: Carol Chen (kipply) works through the arithmetic of transformer inference — compute vs. memory bandwidth, KV cache sizing, and how batch size shapes throughput/latency tradeoffs. Essential reference for anyone reasoning about LLM serving costs.
params:
  source: pinboard
  sourceUrl: https://carolchen.me/blog/transformer-inference-arithmetic/
---

## Summary

Carol Chen (kipply) walks through the mathematical skeleton of transformer inference — the kind of back-of-envelope reasoning that separates engineers who understand why LLM serving is expensive from those who just know that it is. The arithmetic starts with the observation that transformer inference is almost always memory bandwidth-bound, not compute-bound, which has deep implications for hardware selection and batching strategy.

The post derives the key bottleneck from first principles. Each forward pass must load model weights from HBM (high-bandwidth memory) on every token. For a model with P parameters stored in 16-bit floats, that's 2P bytes per token. With an A100's ~2 TB/s bandwidth, a 6.7B parameter model can generate roughly 150 tokens/sec at batch size 1. You're not limited by FLOPs — you're limited by how fast you can move weights through the memory bus. Increasing batch size amortizes this cost because you do the same weight loads but compute attention and FFN outputs for many sequences simultaneously.

The KV cache complicates the picture. Attention requires storing the key and value projections for all previous tokens, growing linearly with context length. For long contexts, KV cache can consume most of GPU memory — constraining max batch size and tipping the cost balance back toward attention, which does scale with sequence length. This tension between throughput and context length is why serving systems often offer context-length limits: they're memory constraints, not fundamental architectural ones.

## Key points

- Transformer inference is memory bandwidth-bound at batch size 1 — weight loading, not FLOPs, is the bottleneck.
- Batch size amortizes weight loading across sequences: doubling batch size doubles throughput until the compute/memory crossover point.
- KV cache memory scales as `2 * num_layers * num_heads * head_dim * context_length` per sequence — significant at long contexts.
- The compute-optimal vs. memory-optimal tradeoff explains why batch size, context length, and hardware type are coupled decisions.
- Prefill (processing prompt tokens in parallel) is compute-bound; decode (generating one token at a time) is memory-bound.
- By Carol Chen (kipply), formerly Cohere, known for clear ML systems writing.

[Original](https://carolchen.me/blog/transformer-inference-arithmetic/)
