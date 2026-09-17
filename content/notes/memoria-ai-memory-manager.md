---
title: "Memoria: structured memory management for AI agents"
date: 2024-04-07
categories:
  - memory
  - ai-agents
  - llm
  - context-management
  - open-source
description: Memoria is a memory manager for AI agents that routes information to appropriate memory types (episodic, semantic, procedural) to enable dynamic, context-aware responses. An attempt to implement a structured cognitive architecture for LLM memory.
params:
  source: pinboard
  sourceUrl: https://github.com/balajivis/Memoria
---

![Memoria: structured memory management for AI agents](/images/notes/memoria-ai-memory-manager.png)

## Summary

Memoria is a memory management system for AI agents that organizes information across multiple memory types — [episodic memory](/notes/episodic-memory/) (specific experiences and events), semantic memory (general facts and concepts), and procedural memory (how-to knowledge). Rather than dumping everything into a flat vector store, Memoria routes incoming information to the appropriate memory type and retrieves from the right type based on the query context.

The structured approach to memory maps onto theories of human memory from cognitive science. [Episodic memory](/notes/episodic-memory/) handles time-stamped specific events ("when the user mentioned they prefer Python"); semantic memory handles general knowledge ("Python is a dynamically typed language"); procedural memory handles skills and routines ("how to format a code block for this user"). Different retrieval patterns apply to each type.

This connects to the broader agent memory design space alongside Mastra's Observational Memory, [Honcho](/notes/honcho/)'s continual-learning approach, and [EchoVault](/notes/echovault/)'s local-first storage. The key differentiation of Memoria is the cognitive-science-inspired typing system: most memory frameworks treat memory as a uniform store, while Memoria claims the retrieval quality improves when information is organized by its epistemic type.

## Key points

- Three memory types: [episodic memory](/notes/episodic-memory/) (events), semantic memory (facts), procedural memory (skills/routines).
- Intelligent routing: incoming information is classified and stored in the appropriate memory type.
- Context-aware retrieval: queries pull from the right memory type based on what kind of information is needed.
- Cognitive science framing: mirrors theories of human memory architecture.
- Part of the AI agent memory tooling cluster: compare [Honcho](/notes/honcho/), Mastra, [EchoVault](/notes/echovault/), Supermemory.

[Original](https://github.com/balajivis/Memoria) → GitHub
