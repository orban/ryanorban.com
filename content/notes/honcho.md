---
title: "Honcho: continual learning memory for AI agents"
date: 2026-02-04
categories:
  - memory
  - ai-agents
  - context-management
  - developer-tools
  - stateful
description: Honcho is an AI-native memory platform that gives agents continual, reasoned learning rather than raw retrieval — 60-90% token savings by surfacing only essential context. Background 'Dreaming' keeps understanding current without runtime overhead.
params:
  source: pinboard
  sourceUrl: https://app.honcho.dev/login
---

![Honcho: continual learning memory for AI agents](/images/notes/honcho.png)

## Summary

[Honcho](/notes/honcho/) is a memory platform for AI agents and applications, built around a key distinction from standard RAG approaches: instead of storing and retrieving raw data, it runs custom reasoning models that continually learn from each message. The result is curated context — not transcripts — delivered in about 200ms via a `context()` function call.

The 60-90% token savings claim comes from this curation. A naive memory system retrieves the N most similar past interactions; [Honcho](/notes/honcho/) delivers only what's actually essential, reducing noise and cost. The `Dreaming` feature runs asynchronously in the background, continuously refining understanding without hitting runtime performance.

The tiered reasoning model is interesting: a `.chat()` method with levels from $0.001 (minimal) to $0.50 (research-grade). Developers can dial in computation based on the query — cheap lookups for routine context, deeper reasoning for nuanced situations. [Honcho](/notes/honcho/) also models multiple entity types (users, agents, NPCs, groups) via a Peers system, allowing it to represent relationships rather than just individual histories.

## Key points

- Custom reasoning models learn continually from messages — delivers curated context, not raw data.
- `context()` returns essential context + conversation history in ~200ms.
- 60-90% token savings vs naive retrieval by filtering to what actually matters.
- Tiered reasoning via `.chat()`: $0.001–$0.50 per call based on depth needed.
- Dreaming: async background learning that doesn't impact runtime performance.
- "Peers" system supports users, agents, NPCs, and groups — models relationships, not just individuals.
- Integrates with Claude Code, OpenClaw, and other AI agent frameworks.

[Original](https://www.honcho.dev/)
