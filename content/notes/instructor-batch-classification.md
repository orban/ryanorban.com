---
title: Batch classification with Instructor
date: 2024-01-31
categories:
  - llm
  - pydantic
  - structured-output
  - classification
  - python
description: An Instructor example showing how to classify multiple items in a single batched LLM call using Pydantic schemas — more efficient than sequential one-at-a-time classification, and type-safe by construction.
params:
  source: pinboard
  sourceUrl: https://jxnl.github.io/instructor/examples/batch_classification/
---

![Batch classification with Instructor](/images/notes/instructor-batch-classification.png)

## Summary

Instructor is Jason Liu's Python library that wraps LLM APIs to enforce Pydantic-validated structured outputs. This example from the Instructor docs demonstrates batch classification: using a single LLM call to classify multiple items simultaneously rather than sending one request per item — a significant efficiency gain when classifying large numbers of inputs.

The approach works by defining a Pydantic model that represents a list of classification results, then asking the LLM to fill in the schema for all items at once. The LLM returns a structured JSON response matching the schema, and Pydantic validates the types and values. Compared to one-at-a-time classification, batch classification reduces API latency and cost by amortizing the per-request overhead across multiple items.

Instructor handles the boilerplate of prompt-building, retry logic, and validation automatically. The user defines what the output should look like (via Pydantic) and Instructor handles making the LLM produce it reliably. This pattern — declarative output schemas for LLM tasks — is the core value proposition of Instructor and closely related to the goals of DSPy at a more structured level.

## Key points

- Batch multiple classification items in a single LLM call — reduces latency and cost vs. sequential calls.
- Instructor enforces Pydantic-validated structured outputs from any LLM API.
- Define the output schema with Pydantic; Instructor handles prompt construction and retry.
- From Jason Liu (jxnl), who runs the Instructor and related ML tooling projects.
- Part of the broader move toward type-safe, schema-driven LLM integrations.

[Original](https://jxnl.github.io/instructor/examples/batch_classification/) → GitHub
