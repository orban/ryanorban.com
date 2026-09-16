---
title: "Haystack: Question Answering at Scale"
date: 2022-04-02
categories:
  - machine-learning
  - nlp
  - question-answering
  - information-retrieval
  - open-source
description: Haystack by deepset is an open-source NLP framework for building question-answering and search systems at scale — Retriever-Reader pipelines over large document corpora. An early entrant in what became the RAG ecosystem.
params:
  source: pinboard
  sourceUrl: https://haystack.deepset.ai/overview/intro
---

## Summary

Haystack is deepset's open-source NLP framework for building question answering systems over large document collections. The core abstraction is a pipeline: you configure a sequence of components — document stores, retrievers, readers, and generators — that together take a natural language question and return answers extracted from your corpus. In 2022, this was the leading open-source framework for what the field now calls RAG (Retrieval-Augmented Generation).

The Retriever-Reader pipeline is the foundational pattern. The Retriever does fast approximate search over a document store to find candidate passages — using BM25, dense passage retrieval (DPR), or embedding similarity. The Reader then does fine-grained extractive QA on those candidates, finding the exact span that answers the question. This two-stage approach is necessary at scale: you can't run a slow neural reader over millions of documents, but you can run it over the 10-50 candidate passages the retriever selects. Elasticsearch, FAISS, and Milvus are supported document stores.

Haystack also supports generative QA: instead of extracting spans, a seq2seq model generates an answer given the retrieved passages as context. This is the pattern that became RAG — the document store and retriever are the retrieval component, the generative model is the "augmented generation" component. In 2022, the generative models were smaller (BART, T5, early GPT variants); today the same Haystack pipeline could use Claude or GPT-4 as the reader. The framework abstracted over these choices, which is why it remained relevant through the LLM transition.

## Key points

- Haystack pioneered the Retriever-Reader pipeline — the architecture that became modern RAG.
- Document stores: Elasticsearch, FAISS, OpenSearch, Milvus — pluggable backends.
- Dense passage retrieval (DPR) enables semantic search over passages; BM25 handles keyword retrieval.
- Supports both extractive QA (find the span) and generative QA (generate the answer given context).
- deepset (Berlin-based) built Haystack as both a product and a community contribution to the NLP ecosystem.
- Precursor to LangChain and LlamaIndex in the document QA space — Haystack was the go-to framework before those emerged.

[Original](https://haystack.deepset.ai/overview/intro)
