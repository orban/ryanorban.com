---
title: "AnythingLLM: Documents to Chatbot"
date: 2023-06-08
categories:
  - llm
  - rag
  - open-source
  - self-hosting
  - chatbot
description: AnythingLLM is a full-stack open-source application for turning any document collection into a chatbot — with a polished UI, workspace management, and multi-model support. The self-hosted alternative to ChatGPT Enterprise for teams wanting document Q&A over their own files.
params:
  source: pinboard
  sourceUrl: https://github.com/Mintplex-Labs/anything-llm
---

![AnythingLLM: Documents to Chatbot](/images/notes/anything-llm.png)

## Summary

AnythingLLM by Mintplex Labs is a full-stack open-source application that ingests document collections and exposes them as a RAG-powered chatbot. Documents go in (PDFs, Word docs, text files, URLs), get chunked and embedded, and the app provides a polished chat interface for asking questions over the document set. The key differentiator versus rolling your own RAG pipeline is the complete package: UI, document management, workspace organization, multi-user support, and multi-model flexibility.

The workspace model lets you create separate document collections — one workspace per project or topic, each with its own document set and chat history. This is a sensible UX for teams with multiple use cases: the support team's runbook workspace, the engineering team's API docs workspace, and the sales team's product docs workspace all live in the same installation with appropriate access controls.

AnythingLLM supports multiple LLM backends (cloud and local): OpenAI, Anthropic, Ollama (local models), and several others. The local model support means you can run the entire stack air-gapped — no data leaves your infrastructure. This positioning (open-source, self-hosted, local model support) made it one of the most-starred RAG application repos in 2023.

## Key points

- Full-stack RAG application: document ingestion → embedding → chat UI, all in one.
- Workspace model: separate document collections per project/team with independent chat histories.
- Multi-model support: OpenAI, Anthropic, Ollama (local) — fully air-gapped operation possible.
- Multi-user with access control — team-facing, not just individual use.
- Self-hosted alternative to ChatGPT Enterprise for document Q&A over private document collections.

[Original](https://github.com/Mintplex-Labs/anything-llm) → GitHub
