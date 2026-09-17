---
title: Memorizing Transformers
date: 2022-08-25
categories:
  - transformers
  - memory
  - llm
  - inference
  - long-context
description: ICLR 2022 spotlight proposing memory-augmented transformers that use approximate k-NN lookup into stored (key, value) pairs at inference time, without weight updates. Scales to 262K token memory with consistent perplexity improvements — an early approach to giving language models dynamic, test-time-updateable knowledge stores.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/MEMORIZING TRANSFORMERS.pdf
---

## Summary

Yuhuai Wu, Markus Rabe, DeLesley Hutchins, and Christian Szegedy (Google) propose augmenting transformer language models with an external memory that can be read at inference time without weight updates. The mechanism is an approximate k-nearest neighbor (kNN) lookup into a stored set of (key, value) pairs from past inputs — effectively allowing the model to "remember" what it has seen before within a session or across a corpus, and retrieve relevant past context when processing new tokens.

The key insight is separating two kinds of knowledge: parametric knowledge (encoded in weights during training) and episodic knowledge (what the model has read recently in the current context). Standard transformers handle both through attention over a finite context window. [Memorizing Transformers](/notes/memorizing-transformers/) offload episodic knowledge to an external non-differentiable memory store, freeing the attention mechanism for local context while enabling much longer effective range. Memory is tested up to 262K tokens — far beyond context windows available at the time.

Performance improves consistently across diverse benchmarks: C4 webtext, arXiv papers, PG-19 books, GitHub code, and Isabelle formal theorems. The formal theorem result is notable: in code and math tasks, the model can retrieve and utilize newly-defined functions or theorems at test time, demonstrating that the memory is doing meaningful retrieval rather than just statistical correlation. The approach anticipates retrieval-augmented generation (RAG) but operates at the architectural level rather than as an inference pipeline.

## Key points

- kNN lookup into stored (key, value) pairs from past inputs — episodic memory read at inference time, no weight updates required
- Scales to 262K tokens of memory with consistent perplexity improvements across diverse domains
- Code and math results: model retrieves and uses newly-defined functions/theorems at test time — semantic retrieval, not just statistical overlap
- Non-differentiable memory: no gradient flows through the memory lookup, unlike differentiable memory approaches (Neural Turing Machine, etc.)
- ICLR 2022 spotlight — one of the early systematic demonstrations of external memory for transformer language models
- Architectural precursor to RAG; key difference is that [Memorizing Transformers](/notes/memorizing-transformers/) operates at the attention layer level rather than as a preprocessing step

[Original paper](https://arxiv.org/abs/2203.08913)
