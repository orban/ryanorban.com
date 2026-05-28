---
title: "Outlines: Guided Text Generation"
date: 2023-11-13
categories:
  - llm
  - structured-output
  - python
  - open-source
  - inference
description: Outlines is a Python library for guided LLM text generation — constraining model outputs to match JSON schemas, regex patterns, or context-free grammars. It was one of the first production-quality structured generation libraries before OpenAI's own structured outputs feature.
params:
  source: pinboard
  sourceUrl: https://github.com/outlines-dev/outlines
---

![Outlines: Guided Text Generation](/images/notes/outlines-guided-generation.png)

## Summary

Outlines (outlines-dev) is a Python library for structured LLM generation — constraining model outputs to match specific formats like JSON schemas, regex patterns, or context-free grammars. Rather than prompting the model to output valid JSON and hoping it complies, Outlines modifies the sampling process itself: at each token position, it masks logits for tokens that would violate the target grammar, making invalid outputs structurally impossible.

This is a fundamentally different approach from prompt-based output constraining. With prompt engineering alone, you get probabilistic compliance — the model usually outputs valid JSON but occasionally produces malformed output that breaks downstream parsing. With Outlines' token-level masking, the model cannot produce invalid output; the constraint is enforced at inference time.

The library integrates with transformers, llama.cpp, and vLLM backends. You define a Pydantic model or JSON schema and get back guaranteed-valid structured data. This was the leading open-source solution for structured generation before OpenAI added native structured outputs to their API in 2024.

## Key points

- Token-level logit masking ensures structurally valid output — not just probabilistic compliance.
- Supports JSON schema, Pydantic models, regex, and context-free grammars as constraints.
- Works with transformers, llama.cpp, and vLLM — not locked to any one backend.
- Precursor to instructor (prompt-based) and OpenAI structured outputs (API-level).
- Essential for tool use, function calling, and any pipeline requiring structured LLM output.
- Related: lm-format-enforcer, guidance (Microsoft) — different approaches to the same problem.

[Original](https://github.com/outlines-dev/outlines) → GitHub
