---
title: "JARVIS / HuggingGPT: LLM as AI Model Orchestrator"
date: 2023-04-09
categories:
  - ai-agents
  - llm
  - tool-use
  - microsoft
  - multi-model
description: Microsoft JARVIS (also published as HuggingGPT) uses ChatGPT as a task planner that routes subtasks to specialized Hugging Face models — an early demonstration that LLMs could orchestrate other AI models as tools. A prototype of the multi-model agent pattern.
params:
  source: pinboard
  sourceUrl: https://github.com/microsoft/JARVIS
---

## Summary

JARVIS (also known as HuggingGPT) is a Microsoft Research system that treats ChatGPT as a planning and orchestration layer over the broader Hugging Face model ecosystem. The core idea: for any complex request, ChatGPT decomposes the task, selects appropriate specialized Hugging Face models for each subtask, executes them via API, and synthesizes the results. The LLM becomes a task planner and coordinator rather than the only model doing work.

A user request like "analyze the sentiment of this audio clip's transcript" gets decomposed into: (1) run Whisper for speech-to-text, (2) run a sentiment classifier on the transcript, (3) return the result with explanation. ChatGPT handles the decomposition, dispatching, and synthesis; the specialized models handle the execution. This separation lets the system use purpose-built models for vision, audio, code, and other tasks where they outperform a general LLM.

JARVIS was published as a paper in early 2023 and became one of the first concrete demonstrations of the multi-model orchestration pattern — what would later be generalized in frameworks like LangChain agents, LlamaIndex pipelines, and tool-use APIs from OpenAI and Anthropic. The pattern proved highly influential: the insight that an LLM can serve as a controller over heterogeneous AI tools is now foundational to modern AI agent architectures.

## Key points

- Uses ChatGPT as a task planner that routes to specialized Hugging Face models for execution.
- Separates planning/synthesis (LLM) from domain-specific inference (specialized models).
- Handles multimodal tasks: vision, audio, text by routing to the right model for each subtask.
- Published as the HuggingGPT paper — precursor to modern AI agent tool-use frameworks.
- Pattern adopted by LangChain, AutoGPT, and later OpenAI function calling.
- Demonstrates that LLM value can be as the controller, not just the compute doing the work.

[Original](https://github.com/microsoft/JARVIS) → GitHub
