---
title: What is TF-IDF? The 10 Minute Guide
date: 2015-09-29
categories:
  - nlp
  - information-retrieval
  - text-mining
  - data-science
  - machine-learning
description: A 10-minute introduction to TF-IDF — the classic term-weighting scheme that balances how often a word appears in a document against how rare it is across the corpus. Still one of the most useful baselines in text analysis despite being decades old.
params:
  source: pinboard
  sourceUrl: http://michaelerasm.us/tf-idf-in-10-minutes/
---

## Summary

TF-IDF (Term Frequency–Inverse Document Frequency) is the foundational text weighting scheme in information retrieval and NLP. The intuition: a word is important to a document if it appears frequently *in that document* but rarely *across the corpus*. "The" appears everywhere and carries no signal; synaptic appearing 12 times in one document is a strong indicator of that document's subject.

The formula combines two components. **TF** (term frequency) measures how often a term appears in a document, usually normalized by document length. **IDF** (inverse document frequency) measures how rare a term is across all documents — computed as log(N/df) where N is the number of documents and df is the number containing the term. Multiplying them gives each term in each document a score that rewards specificity.

TF-IDF vectors are the simplest useful representation of text for classical machine learning: convert each document to a vector of TF-IDF scores (one dimension per vocabulary term), and you can run cosine similarity, k-means clustering, logistic regression, or SVMs on it. It predates word embeddings by decades but remains competitive on many tasks — particularly for keyword extraction, document similarity, and search ranking where interpretability matters.

## Key points

- TF × IDF = term frequency × log(N/document frequency) — high score for terms that are frequent locally but rare globally.
- Produces sparse vectors (most terms score 0 in any given document) — efficient to compute and store.
- Cosine similarity on TF-IDF vectors is a standard baseline for document retrieval and duplicate detection.
- Predates word embeddings but still competitive on keyword extraction, search ranking, and short-text classification.
- Key limitation: no semantic understanding — car and automobile are unrelated in TF-IDF space.
- Superseded for many tasks by word2vec, GloVe, and then BERT — but still widely used in production for its speed and interpretability.

[Original](http://michaelerasm.us/tf-idf-in-10-minutes/)
