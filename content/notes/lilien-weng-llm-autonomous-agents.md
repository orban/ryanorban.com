---
title: LLM Powered Autonomous Agents
date: 2023-06-27
categories:
  - ai-agents
  - llm
  - research
  - planning
  - memory
description: Lilian Weng's survey post on LLM-powered autonomous agents — covering the planning, memory, and tool use components that compose into agent architectures. One of the most cited and comprehensive overviews of the agent design space from mid-2023.
params:
  source: pinboard
  sourceUrl: https://lilianweng.github.io/posts/2023-06-23-agent/
---

![LLM Powered Autonomous Agents](/images/notes/lilien-weng-llm-autonomous-agents.png)

## Summary

Lilian Weng's post LLM Powered Autonomous Agents is one of the most widely cited surveys of AI agent architectures using LLMs. Written in June 2023, it systematically breaks down the design space into three core components: planning (how the agent reasons about and decomposes tasks), memory (how the agent accesses and stores information), and tool use (how the agent interacts with external systems). This framework became canonical for thinking about LLM agent design.

**Planning** covers task decomposition techniques: chain-of-thought prompting, tree of thoughts for branching search, ReAct (interleaving reasoning and actions), and Reflexion (learning from past mistakes via self-reflection). The key challenge is that LLMs are prone to planning errors that compound — a wrong assumption early in a plan leads to cascading failures. Techniques like Reflexion address this by having the model critique its own outputs.

**Memory** distinguishes between in-context memory (the active context window — the fastest but smallest), external memory (vector stores for long-term retrieval), and parametric memory (what the model knows from training). The memory retrieval problem — given a large history, what's relevant right now — maps directly to RAG techniques. **Tool use** covers function calling, code execution, web search, and how agents can be given access to APIs to take real-world actions. The post synthesizes key papers including AutoGPT, Generative Agents, HuggingGPT, and ChemCrow as concrete architectures.

## Key points

- Three-component framework: Planning + Memory + Tool Use — still the standard vocabulary for agent design.
- Planning: chain-of-thought, ReAct, Reflexion, tree of thoughts — each addressing different failure modes.
- Memory: in-context (context window), external (RAG / vector store), parametric (trained knowledge).
- Tool use: function calling, code execution, web search — bridges LLM reasoning to real-world actions.
- Key risk: planning errors compound — small wrong assumption → cascading task failure.
- By Lilian Weng (then Head of Safety at OpenAI) — one of the most influential ML blog posts of 2023.

[Original](https://lilianweng.github.io/posts/2023-06-23-agent/)
 → GitHub
