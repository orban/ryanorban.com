---
title: Google Talk to Books
date: 2022-08-11
categories:
  - google
  - books
  - semantic-search
  - nlp
  - ai-tools
description: Google's Talk to Books lets you search a large corpus of books using natural language statements, returning passages that respond semantically to your query. An early public demonstration of semantic search over a curated corpus, predating the vector database era.
params:
  source: pinboard
  sourceUrl: https://books.google.com/talktobooks/
---

![Google Talk to Books](/images/notes/google-talk-to-books.png)

## Summary

[Google Talk to Books](/notes/google-talk-to-books/) is an experimental Google product that lets users search a large corpus of books using natural language statements or questions, returning passages that semantically respond to the query. Rather than keyword matching, the system uses sentence embeddings to find passages that are conversationally responsive — a precursor to the semantic search approaches that became mainstream with dense retrieval and vector databases.

The system was trained on a large dataset of book text paired with dialog-style responses, teaching the model what a good response to a statement looks like. This predates GPT-3 and large language models for question answering — it's a dedicated retrieval system, not a generative one. The results show which published authors have addressed your question or made a related argument.

Talk to Books was part of Google's People + AI Research (PAIR) lab — experimenting with novel search interfaces before the LLM-powered search paradigm arrived. The book corpus gives it a distinctive property: rather than finding web pages optimized for SEO, it surfaces considered, edited thinking from published works. That remained distinctive even as general semantic search improved.

## Key points

- Semantic search over a large book corpus using natural language statements or questions.
- Returns passages that "respond" conversationally — not keyword-matched excerpts.
- Uses sentence embeddings trained on dialog + book text pairs — a retrieval model, not generative.
- From Google PAIR — Google's experimental AI product and research lab.
- Predates the vector database era; an early public-facing semantic search demonstration.
- Book corpus is distinctive: finds considered, edited arguments rather than SEO-optimized content.

[Original](https://books.google.com/talktobooks/)
