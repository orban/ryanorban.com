---
title: Build a Support Bot with Supabase, OpenAI, and Windmill
date: 2023-06-29
categories:
  - llm
  - discord
  - supabase
  - openai
  - rag
  - developer-tools
description: Windmill's tutorial on building a Discord/Slack support bot using Supabase for vector storage and OpenAI for embeddings and generation — a worked RAG example for team documentation Q&A. Shows how to wire up the standard stack (embed, store, retrieve, generate) for a specific product use case.
params:
  source: pinboard
  sourceUrl: https://www.windmill.dev/blog/knowledge-base-discord-bot
---

![Build a Support Bot with Supabase, OpenAI, and Windmill](/images/notes/windmill-supabase-discord-bot.png)

## Summary

This tutorial from Windmill walks through building a Discord or Slack bot that answers support questions using your documentation as a knowledge base. The stack: Supabase with pgvector for storing document embeddings, OpenAI for generating embeddings and answers, and Windmill (an open-source workflow orchestration tool) to wire the pieces together. It's a concrete worked example of the RAG pattern applied to a specific product problem.

The workflow: ingest documentation pages → generate embeddings via OpenAI's embedding model → store in Supabase with pgvector → on Discord message, embed the query → retrieve nearest document chunks via vector similarity search → pass chunks + query to GPT-4 → post response in Discord. This is the canonical RAG architecture: embed-store-retrieve-generate, applied end-to-end.

The Windmill layer provides scheduling (re-ingest docs on change), workflow orchestration (coordinate the multi-step process), and a UI for monitoring — without requiring a separate backend service. The tutorial is valuable as a practical implementation guide for teams building similar bots for support, documentation Q&A, or internal knowledge retrieval. Supabase's pgvector extension is a particularly interesting choice: using your existing Postgres database for vector search rather than adding a separate vector store simplifies the infrastructure stack.

## Key points

- RAG pipeline: embed docs → store in Supabase with pgvector → retrieve on query → generate with GPT-4.
- pgvector: PostgreSQL extension for vector similarity search — vector storage in your existing Postgres.
- Windmill: open-source workflow orchestration — handles scheduling, coordination, and monitoring without a separate backend.
- Triggers on Discord / Slack messages — practical support bot pattern for documentation Q&A.
- Shows the full pipeline end-to-end: document ingestion through user-facing responses.
- Infrastructure advantage: pgvector keeps vector search in existing Supabase / Postgres rather than adding a dedicated vector database.

[Original](https://www.windmill.dev/blog/knowledge-base-discord-bot)
