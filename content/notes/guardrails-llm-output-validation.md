---
title: "Guardrails: Adding Structure and Validation to LLM Outputs"
date: 2023-03-13
categories:
  - llm
  - output-validation
  - structured-outputs
  - python
  - reliability
description: Guardrails adds structural and semantic validation to LLM outputs — defining schemas for what the model should return and automatically retrying or correcting when outputs don't conform. An early solution to LLM output reliability before JSON mode and structured outputs became standard.
params:
  source: pinboard
  sourceUrl: https://github.com/shreyar/guardrails
---

![Guardrails: Adding Structure and Validation to LLM Outputs](/images/notes/guardrails-llm-output-validation.png)

## Summary

Guardrails (by Shreya Rajpal) adds validation layers to LLM outputs — you define a schema (RAIL spec) describing what the model should return, and the library validates the output, asks the model to fix problems, and retries until the output conforms or a retry limit is hit. It addresses the fundamental problem that LLMs are probabilistic text generators, not reliable structured data producers.

The RAIL (Reliable AI Markup Language) format describes both the structure of the desired output (types, required fields, format constraints) and the instructions to include in the prompt to encourage that structure. Guardrails then post-processes model output: if the model returns malformed JSON, it prompts again with error context; if a field fails a validator (e.g., a URL format check), it asks the model to correct just that field.

At the time (March 2023), this was a significant gap — OpenAI had no JSON mode, no function calling, and no structured output guarantees. The only option was hoping the model followed format instructions, then parsing and handling failures in application code. Guardrails systematized that retry logic. The library directly influenced Instructor (the most widely used structured output library for Python) and anticipated OpenAI's native JSON mode and structured outputs features released in 2023-2024.

## Key points

- RAIL schema defines expected output structure + validators; library retries if output doesn't conform.
- Addresses pre-JSON-mode LLM output unreliability — systematic retry/correction logic.
- Python library; validators are composable (type checks, regex, custom functions).
- Directly influenced Instructor library and anticipated OpenAI JSON mode and structured outputs.
- One of the earliest tools to treat LLM output validation as a first-class engineering concern.

[Original](https://github.com/shreyar/guardrails) → GitHub
