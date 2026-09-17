---
title: Patterns for Building LLM-based Systems & Products
date: 2023-08-02
categories:
  - llm
  - engineering
  - patterns
  - rag
  - production
description: Eugene Yan's comprehensive guide to patterns for building LLM-based systems — covering evals, RAG, fine-tuning, caching, guardrails, defensive UX, and user feedback collection. One of the most referenced practical engineering posts of 2023.
params:
  source: pinboard
  sourceUrl: https://eugeneyan.com/writing/llm-patterns/
---

![Patterns for Building LLM-based Systems & Products](/images/notes/patterns-building-llm-systems.png)

## Summary

Eugene Yan published this post as a systematic catalog of patterns that emerge when building LLM applications for production. Where most 2023 content was either theoretical (here's what LLMs can do) or tutorial-level (here's how to call the API), this is engineering-level: what design patterns work, what problems each pattern solves, and what tradeoffs to expect.

The patterns covered span the full production stack:

**Evals**: How do you know if your LLM application is working? Human evaluation, model-based evaluation, and behavioral testing — each has different cost, speed, and reliability tradeoffs. Without evals, you're flying blind.

**RAG**: Retrieval-Augmented Generation as a pattern for grounding LLM responses in external knowledge — when to use it, how to structure the retrieval, and how retrieval quality affects generation quality.

**Fine-tuning**: When it's appropriate, what data quality requirements it imposes, and why it's often not the right first tool.

**Caching**: Semantic caching of LLM responses — different from traditional caching because similar queries should hit the same cache entry even without exact string matches.

**Guardrails**: Input and output validation to prevent misuse, reduce hallucination surface, and constrain outputs to safe/appropriate content.

**Defensive UX**: Designing interfaces that degrade gracefully when LLM outputs are wrong or uncertain — user-facing patterns that maintain trust even when the model errs.

**User feedback**: Collecting signal from users (thumbs up/down, corrections) to build datasets for evals and future fine-tuning.

## Key points

- Evals are the foundation — without measuring quality, you can't improve or catch regressions.
- RAG quality depends primarily on retrieval quality, not generation quality — fix retrieval first.
- Semantic caching with vector search enables cache hits on paraphrased queries, not just exact repeats.
- Guardrails operate at input (intent classification, topic filtering) and output (format validation, toxicity detection).
- Defensive UX treats model fallibility as a design constraint, not an exception.

[Original](https://eugeneyan.com/writing/llm-patterns/)
