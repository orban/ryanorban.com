---
title: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks
date: 2023-01-20
categories:
  - rag
  - nlp
  - retrieval
  - llm
  - research
description: Lewis et al. (Facebook AI, 2020) introduce Retrieval-Augmented Generation, a hybrid architecture that combines dense passage retrieval with seq2seq generation to ground language model outputs in a non-parametric knowledge store. RAG defined the template that most production knowledge-grounded LLM systems follow today.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.pdf
---

## Summary

Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, and colleagues at Facebook AI Research introduce retrieval-augmented generation (RAG) — a class of model that augments a parametric language model with a non-parametric memory component backed by a dense vector index of Wikipedia. The key insight: generative models suffer from the well-known knowledge boundary problem, where facts encoded in weights go stale and hallucinations fill gaps. A live, queryable index sidesteps this.

The architecture has two parts. A bi-encoder retriever (based on DPR, Dense Passage Retrieval) maps the input question to a query embedding, retrieves the top-k passages from a compressed Wikipedia index, and passes them to a seq2seq generator (based on BART). The generator conditions its output on both the question and all retrieved passages. Two variants are proposed: RAG-Sequence (which uses the same retrieved documents for the entire output) and RAG-Token (which allows different documents to contribute at each generation step). Both variants are trained end-to-end via marginalizing over the retrieved documents.

RAG outperforms all other approaches on three open-domain question answering benchmarks: Natural Questions, TriviaQA, and WebQuestions, while also showing strong results on abstractive QA and fact verification tasks. Importantly, the knowledge can be updated by swapping in a new document index without retraining — unlike purely parametric approaches that require expensive fine-tuning to incorporate new facts. This separation of knowledge storage from model weights became the architectural foundation for nearly all production RAG systems.

## Key points

- Retrieval-Augmented Generation (RAG) = parametric seq2seq generator + non-parametric dense retrieval over a live document corpus.
- DPR (Dense Passage Retrieval) retriever embeds question + document passages into the same vector space via a bi-encoder fine-tuned on Q&A.
- Two variants: RAG-Sequence (same docs per full output) and RAG-Token (per-token doc selection via marginalization).
- BART-based generator conditions on both the question and the retrieved passages; the model is trained end-to-end.
- Beats all previous approaches on Natural Questions, TriviaQA, WebQuestions; knowledge can be updated by swapping the index.
- Established the separation of **parametric memory** (model weights) vs **non-parametric memory** (index) as the standard framing for knowledge-intensive NLP.

[Original PDF](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/Retrieval-Augmented%20Generation%20for%20Knowledge-Intensive%20NLP%20Tasks.pdf)
