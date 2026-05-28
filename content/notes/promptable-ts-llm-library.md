---
title: "Promptable.js: TypeScript Library for LLM Apps"
date: 2023-02-14
categories:
  - llm
  - typescript
  - library
  - open-source
  - prompt-engineering
description: Promptable.js is an early TypeScript library for building LLM apps with Prompt, Search, Chain, and Trace primitives — a TypeScript analogue to LangChain that appeared in February 2023 before LangChain's own TypeScript support matured. Historically significant as one of the first LLM frameworks for TypeScript developers.
params:
  source: pinboard
  sourceUrl: https://docs-promptable.vercel.app/docs/introduction
---

![Promptable.js: TypeScript Library for LLM Apps](/images/notes/promptable-ts-llm-library.png)

## Summary

Promptable.js was one of the first TypeScript libraries for building LLM-powered applications, appearing in February 2023 when LangChain's TypeScript support was still immature. The library organized LLM application primitives into four core concepts: Prompt (prompt templates with variable interpolation), Search (embedding and retrieval), Chain (composing prompts and retrieval into pipelines), and Trace (logging and debugging LLM calls).

The four-primitive design maps cleanly to the building blocks that every LLM application needs. Prompt handles the template management problem — constructing prompts dynamically with data. Search handles the retrieval problem — finding relevant chunks from a document store. Chain handles orchestration — connecting retrieval outputs to prompt inputs. Trace handles observability — recording what the system actually sent and received for debugging.

Promptable.js positioned itself as "the world's first library for building AI apps in TypeScript" in early promotional materials. In practice, LangChain shipped TypeScript support shortly after and dominated the market with its larger ecosystem and community. Promptable.js captures the moment of intense competition in the LLM framework space — multiple teams building similar abstractions simultaneously, with the winner determined more by community momentum than technical differentiation.

## Key points

- Four primitives: Prompt (templates), Search (embeddings + retrieval), Chain (orchestration), Trace (observability).
- Early TypeScript-native LLM library — appeared when LangChain's TS support was minimal.
- First TypeScript LLM library framing — accurate at the time, surpassed by LangChain's ecosystem growth.
- `npm install promptable` — designed for Node.js and browser JS environments.
- Historical artifact: captures the framework competition phase of early 2023 LLM tooling.

[Original](https://docs-promptable.vercel.app/docs/introduction)
