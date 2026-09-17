---
title: "ART: Questions Are All You Need to Train a Dense Passage Retriever"
date: 2022-07-07
categories:
  - information-retrieval
  - nlp
  - machine-learning
  - dense-retrieval
  - unsupervised-learning
description: ART (Autoencoding-based Retriever Training) trains dense retrievers without labeled question-passage pairs — only questions and an unpaired document collection. This removes the main bottleneck for deploying dense retrieval in new domains where annotation is expensive.
params:
  source: pinboard
  sourceUrl: https://arxiv.org/abs/2206.10658
---

## Summary

ART (Autoencoding-based Retriever Training) is a paper by Devendra Singh Sachan et al. introducing an unsupervised approach to training dense passage retrieval models. The key challenge in dense retrieval is that standard training requires labeled (question, relevant passage) pairs — expensive to collect for new domains. ART removes this dependency: you only need a collection of questions and an unpaired document corpus.

The method frames retrieval as an autoencoding task. A language model generates a question from a document passage. The retriever is then trained to recover that passage given the generated question — effectively teaching it to find documents that would naturally give rise to the observed questions. This creates a self-supervised training signal without any human-labeled pairs. The approach is grounded in the Mutual Information Maximization perspective on representation learning.

At the time (mid-2022), dense retrieval models like DPR (Dense Passage Retrieval) had shown that learned embeddings outperformed BM25 sparse retrieval on standard QA benchmarks. But DPR required large labeled datasets like Natural Questions or TriviaQA. ART's unsupervised signal makes dense retrieval viable in low-resource domains — a significant practical advance for building retrieval-augmented generation (RAG) systems without annotation budgets.

## Key points

- Unsupervised: trains a dense retriever using only questions + unpaired documents, no labeled pairs
- Autoencoding objective: model generates a question from a passage, retriever is trained to recover that passage
- Outperforms zero-shot BM25 retrieval and matches supervised DPR in many settings
- Opens dense retrieval to low-resource domains where labeled (question, passage) pairs are unavailable
- Relevant to RAG pipelines where the domain-specific retriever is the performance bottleneck

[Original](https://arxiv.org/abs/2206.10658)
