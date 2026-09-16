---
title: OpenAI Codex TodoMVC Challenge
date: 2022-08-25
categories:
  - codex
  - openai
  - code-generation
  - llm
  - ai-tools
description: A walkthrough of using OpenAI Codex to build a TodoMVC app from natural language descriptions. Captures the pre-Copilot moment when Codex-powered code generation was the frontier of AI-assisted coding.
params:
  source: pinboard
  sourceUrl: https://codeball.ai/blog/codex-todo-mvc
---

## Summary

This article demonstrates OpenAI Codex — OpenAI's code-specialized derivative of GPT-3, fine-tuned on public code from GitHub — applied to building a standard [TodoMVC](/notes/todomvc/) application from natural language descriptions. Codex was the model underlying GitHub Copilot and OpenAI's Codex playground at the time.

The [TodoMVC](/notes/todomvc/) framework has long been the go-to benchmark for evaluating JavaScript frameworks — simple enough to implement quickly but complex enough to demonstrate real patterns. Using it as a Codex test case makes the output comparable: readers can judge quality against known reference implementations. The article walks through a four-phase workflow: project setup, code generation via prompt engineering, AI enhancement for task prioritization, and automated testing.

This captures an important moment in AI-assisted coding: 2022 was when Codex was the primary model for code generation, before GPT-4 and dedicated coding models raised the ceiling significantly. The pattern of describing a full application in natural language and iteratively prompting for code was novel and promising, even if results were rougher than today's equivalents.

## Key points

- Demonstrates OpenAI Codex building a [TodoMVC](/notes/todomvc/) app through natural language prompts.
- Codex is fine-tuned on GitHub code — the underlying model for GitHub Copilot at the time.
- Four-phase workflow: setup → code generation → AI enhancement → quality assurance.
- Early example of AI-assisted coding before ChatGPT made LLM coding assistance mainstream.
- [TodoMVC](/notes/todomvc/) as benchmark: standardized reference point that makes output quality comparable.
- Reduces development time for standard patterns — especially useful for those with limited programming experience.

[Original](https://codeball.ai/blog/codex-todo-mvc)
