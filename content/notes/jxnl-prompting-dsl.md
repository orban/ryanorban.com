---
title: "Experimental Prompting DSL: Origin of Instructor"
date: 2023-06-29
categories:
  - llm
  - prompt-engineering
  - python
  - function-calling
  - structured-outputs
description: Jason Liu's experimental prompting DSL for structured LLM outputs via OpenAI function calling — an early version of what became the Instructor library. Shows the origin of the pydantic-based approach to reliable structured extraction from LLMs.
params:
  source: pinboard
  sourceUrl: https://github.com/jxnl/openai_function_call/pull/25
---

![Experimental Prompting DSL: Origin of Instructor](/images/notes/jxnl-prompting-dsl.png)

## Summary

This GitHub pull request by Jason Liu (jxnl) to the `openai_function_call` repository proposes an experimental prompting DSL (domain-specific language) for getting structured outputs from LLMs via OpenAI's function calling feature. This is the early precursor to what became Instructor — now one of the most widely used libraries for reliable structured output from LLMs.

The core insight Jason Liu was working toward: OpenAI's function calling feature (added in June 2023) lets you define a JSON schema that the model must produce. By using Pydantic models to define the expected output schema, you get Python type validation on the model's output, automatic retry logic when the model produces invalid output, and a clean interface that separates what I want (the Pydantic model) from how to get it (the prompt and function call machinery).

This pull request represents the moment where the approach crystallized. Instructor would go on to become a significant library in the LLM application development ecosystem — used anywhere developers need reliable structured data extraction (extracting entities from text, classifying inputs, generating structured responses). The Pydantic-as-schema approach influenced how people think about LLM output validation more broadly. Jason Liu is also known for his newsletter and writing on LLM application patterns.

## Key points

- Origin PR for what became the Instructor library — Pydantic models as OpenAI function calling schemas.
- OpenAI function calling (June 2023): model outputs conform to a provided JSON schema — enables structured outputs.
- Pydantic + function calling: define output schema in Python, get validated structured data from LLMs.
- Auto-retry on validation failure: if model output doesn't match Pydantic model, retry with error context.
- By Jason Liu (jxnl) — developer and writer known for practical LLM application engineering.
- Foundation for the broader pattern of using type systems to constrain and validate LLM outputs.

[Original](https://github.com/jxnl/openai_function_call/pull/25)
