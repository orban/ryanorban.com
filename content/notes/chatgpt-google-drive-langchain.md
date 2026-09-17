---
title: ChatGPT + Google Drive with LangChain
date: 2023-06-05
categories:
  - llm
  - langchain
  - google-drive
  - rag
  - python
description: A tutorial for connecting ChatGPT to Google Drive using LangChain and Python in 30 lines of code — an early canonical example of the document Q&A pattern using LangChain's document loaders and retrieval chain.
params:
  source: pinboard
  sourceUrl: https://www.haihai.ai/gpt-gdrive/
---

![ChatGPT + Google Drive with LangChain](/images/notes/chatgpt-google-drive-langchain.png)

## Summary

This tutorial by Haihai demonstrates the document Q&A pattern using LangChain and Google Drive as the document source — one of the early canonical examples of RAG in practice before the acronym became standard. The promise: 30 lines of Python to ask questions over your Google Drive documents using ChatGPT.

The pattern uses LangChain's document loaders (specifically the Google Drive loader), which authenticate via OAuth and pull document content. Documents are chunked, embedded, and stored in an in-memory vector store. A retrieval chain retrieves the relevant chunks for each question and passes them to OpenAI for synthesis. The 30-line claim is roughly accurate — LangChain abstracts all the chunking, embedding, and retrieval machinery.

This tutorial was influential in 2023 for demonstrating that connecting an LLM to your own documents was achievable by a developer in an afternoon, not a months-long engineering project. The accessibility of LangChain's abstraction layer (document loaders → text splitter → embeddings → vector store → retrieval chain → LLM chain) was the message as much as the specific Google Drive integration.

## Key points

- Uses LangChain document loaders + retrieval chain for Google Drive Q&A in ~30 lines.
- Full RAG pipeline: OAuth doc fetch → chunk → embed → vector store → retrieve → LLM synthesis.
- Early canonical tutorial for the document Q&A pattern before "RAG" became common terminology.
- Demonstrates LangChain's abstraction layer — high-level chains hide chunking and retrieval mechanics.
- Influential for showing developers that personal document Q&A was an afternoon project, not months.

[Original](https://www.haihai.ai/gpt-gdrive/)
