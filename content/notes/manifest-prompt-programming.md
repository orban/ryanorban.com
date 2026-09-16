---
title: "Manifest: Prompt Programming with Foundation Models"
date: 2022-10-08
categories:
  - llm
  - prompt-engineering
  - python
  - research
  - hazyresearch
description: Manifest is a Python library from Stanford's HazyResearch lab for prompt programming with foundation models — a unified interface across providers with caching, batching, and structured output support. An early formalization of LLM programming patterns before LangChain dominated.
params:
  source: pinboard
  sourceUrl: https://github.com/HazyResearch/manifest
---

## Summary

Manifest is a Python library from HazyResearch (Stanford) for building applications on top of foundation models. Released in late 2022, it was one of the early attempts to create a systematic, reusable framework for prompt programming — before LangChain had taken hold as the dominant abstraction.

The core features: a unified client interface that works across multiple providers (OpenAI, AI21, Hugging Face models), automatic caching of model responses (identical prompts return cached results, reducing cost and latency during development), and support for batched queries. Manifest treats prompts as first-class objects and handles serialization, retry logic, and provider differences so calling code doesn't have to.

HazyResearch is the lab behind FlashAttention and other foundational ML systems work — Manifest reflects a systems-oriented perspective on LLM programming, focusing on efficiency and reproducibility. The caching alone was valuable: LLM development at the time involved running the same prompts dozens of times, and without caching, the iteration cost was high.

In retrospect, Manifest represents the pre-LangChain paradigm: smaller, more focused, less opinionated. It lost mindshare to LangChain's broader abstractions, but the design choices (caching, unified interface, batch support) are present in modern tooling.

## Key points

- Unified Python interface across LLM providers (OpenAI, AI21, Hugging Face).
- Automatic response caching — same prompt returns cached result, reducing iteration cost.
- Batching support for efficient parallel queries.
- From HazyResearch (Stanford) — systems-oriented perspective on LLM programming.
- Pre-dates LangChain dominance; represents early formalization of prompt programming patterns.
- Open source on GitHub under Apache 2.0 license.

[Original](https://github.com/HazyResearch/manifest)
