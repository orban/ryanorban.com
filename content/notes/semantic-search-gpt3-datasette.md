---
title: Semantic Search and Q&A with GPT-3 and Datasette
date: 2023-01-22
categories:
  - semantic-search
  - gpt3
  - embeddings
  - tutorial
  - simon-willison
description: Simon Willison's tutorial on building Q&A over documentation using GPT-3, embeddings, and Datasette — an early practical guide to semantic search that Willison built for his own blog. One of the first clearly explained end-to-end RAG implementations from a respected practitioner.
params:
  source: pinboard
  sourceUrl: https://simonwillison.net/2023/Jan/13/semantic-search-answers/
---

![Semantic Search and Q&A with GPT-3 and Datasette](/images/notes/semantic-search-gpt3-datasette.png)

## Summary

Simon Willison's post documents how he implemented semantic search and Q&A over his own documentation using GPT-3, OpenAI embeddings, and Datasette (his own open-source tool for exploring SQLite databases). The post is both a tutorial and a working system description — Willison built this for his own blog and documentation, then wrote up exactly how it worked.

The system embeds content (blog posts, documentation) using OpenAI's embedding API, stores embeddings in a SQLite database via Datasette, and at query time retrieves the most similar content chunks by cosine similarity, then passes them to GPT-3 to generate a natural language answer. It's the minimal RAG pipeline applied to personal documentation — no external vector database required, just SQLite and NumPy.

Simon Willison is a well-respected practitioner and creator of Django; his posts carry weight because they document real systems rather than toy examples. Publishing this in January 2023, when the RAG pattern was still novel enough that most practitioners hadn't implemented it, gave the post significant reach. It became a reference for people trying to understand the RAG pattern from a practitioner who had built and tested it rather than explained it theoretically.

## Key points

- End-to-end RAG implementation: embed content → store in SQLite/Datasette → cosine similarity → GPT-3 answer
- By Simon Willison (Django creator) — a real production system for his own blog, not a toy
- No external vector database needed — SQLite + NumPy for small corpora
- One of the earliest clearly-explained semantic search + LLM answer generation tutorials
- Published January 2023 — influential early documentation of the RAG pattern before it became standard terminology

[Original](https://simonwillison.net/2023/Jan/13/semantic-search-answers/)
