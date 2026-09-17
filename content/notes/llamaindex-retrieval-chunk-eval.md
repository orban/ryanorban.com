---
title: LlamaIndex Retrieval and Chunk Evaluation Notebook
date: 2023-10-07
categories:
  - rag
  - llamaindex
  - evaluation
  - retrieval
  - notebooks
description: A LlamaIndex Google Colab notebook for evaluating retrieval quality and chunk size in RAG pipelines — demonstrating how to measure retrieval hit rate and MRR across different chunk sizes. Practical tooling for the underappreciated problem of RAG evaluation.
params:
  source: pinboard
  sourceUrl: https://colab.research.google.com/drive/1Siufl13rLI-kII1liaNfvf-NniBdwUpS?usp=sharing
---

![LlamaIndex Retrieval and Chunk Evaluation Notebook](/images/notes/llamaindex-retrieval-chunk-eval.png)

## Summary

This Google Colab notebook from LlamaIndex demonstrates how to evaluate retrieval quality and chunk size in a RAG pipeline — a practical tool for answering the question "how does my chunk size affect retrieval accuracy?" The notebook uses LlamaIndex's evaluation utilities to run systematic experiments with different chunking strategies and measures the results.

The evaluation metrics the notebook targets: hit rate (does the relevant document appear anywhere in the top-k retrieved results?) and MRR (Mean Reciprocal Rank — how highly is the relevant document ranked?). These are retrieval-specific metrics that let you evaluate the retrieval component independently of the generation quality. Separating these concerns is important: a well-designed RAG evaluation should distinguish between "the retriever failed to find the relevant chunk and the LLM failed to use the context correctly."

The notebook approach: create a test set of question-answer pairs from your documents, run retrieval with different configurations (chunk size: 128, 256, 512, 1024 tokens), measure retrieval metrics for each configuration, and pick the chunk size that optimizes for your use case. Smaller chunks improve precision but may miss necessary context; larger chunks improve recall but introduce noise. This empirical testing approach is more reliable than theoretical rules about chunk size.

## Key points

- Evaluates RAG retrieval independently of generation — isolates retrieval failure modes.
- Metrics: hit rate and MRR across top-k retrieved results per query.
- Tests multiple chunk sizes empirically rather than relying on rules of thumb.
- Smaller chunks: better precision, may miss context; larger chunks: better recall, more noise.
- Part of LlamaIndex's evaluation toolkit — pairs with their `RetrieverEvaluator` module.
- Demonstrates the eval-first approach to RAG improvement rather than intuition-based tuning.

[Original](https://colab.research.google.com/drive/1Siufl13rLI-kII1liaNfvf-NniBdwUpS?usp=sharing) → LlamaIndex
