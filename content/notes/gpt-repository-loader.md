---
title: "gpt-repository-loader: Pack a Repo for GPT"
date: 2023-03-18
categories:
  - llm
  - code-understanding
  - developer-tools
  - gpt
  - context-packing
description: gpt-repository-loader concatenates a git repository into a single text file formatted for GPT ingestion — solving the context-packing problem for code understanding before embeddings-based retrieval became standard.
params:
  source: pinboard
  sourceUrl: https://github.com/mpoon/gpt-repository-loader
---

![gpt-repository-loader: Pack a Repo for GPT](/images/notes/gpt-repository-loader.png)

## Summary

[gpt-repository-loader](/notes/gpt-repository-loader/) is a simple tool by mpoon that concatenates a git repository into a single text file, with file paths as headers, formatted for feeding into GPT models. Given a repo, it outputs a single document you can paste into a prompt — enabling questions like explain this codebase or find the bug in this system against the entire repo at once.

The problem is real: GPT-4's 8K token context window (in March 2023) made it impossible to naively paste a whole repository. [gpt-repository-loader](/notes/gpt-repository-loader/) optimizes the formatting — respecting `.gitignore`, using concise file-path headers, stripping unnecessary whitespace — to fit as much relevant code as possible into the context. It also supports an output tokens budget so you can target a specific model's limit.

This approach predates RAG-based code search. RAG over code (embedding files, retrieving relevant chunks per query) is more scalable and handles larger repos. But the brute-force pack everything into context approach works well for small-to-medium repos and avoids retrieval quality issues — if the code is in context, the model can reason over it directly. [gpt-repository-loader](/notes/gpt-repository-loader/) was one of the first tools to make this easy, alongside autodoc and Adrenaline in the early code-understanding cluster.

## Key points

- Concatenates a repo into a single GPT-ready text file — file paths as headers, gitignore respected.
- Predates RAG-based code search; brute-force context packing works well for small-to-medium repos.
- Supports token budget targeting so output fits within a specific model's context window.
- Paired well with ChatGPT Plus subscribers who had GPT-4 access and wanted to ask about their code.
- Part of the early 2023 code-understanding tooling cluster with autodoc, Adrenaline, llama_index.

[Original](https://github.com/mpoon/gpt-repository-loader) → GitHub
