---
title: "skift: scikit-learn Wrappers for fastText"
date: 2021-01-20
categories:
  - nlp
  - python
  - scikit-learn
  - fasttext
  - text-classification
description: skift wraps Facebook's fastText text classifiers in scikit-learn's estimator API, making fastText accessible as a drop-in component in scikit-learn pipelines and GridSearchCV. Useful for fast, production-grade text classification without leaving the sklearn ecosystem.
params:
  source: pinboard
  sourceUrl: https://github.com/shaypal5/skift
---

## Summary

skift (scikit-learn wrappers for fastText) bridges Facebook's fastText text classification library with scikit-learn's estimator API. fastText is notable for being extremely fast — training on millions of documents in seconds — and for its subword embeddings that handle out-of-vocabulary words gracefully by decomposing tokens into character n-grams. The scikit-learn wrapper lets you use fastText anywhere a scikit-learn classifier goes: in `Pipeline`s, with `GridSearchCV`, and alongside other estimators.

The core use case is text classification tasks where you need fastText's speed and subword embeddings but also want to use the scikit-learn ecosystem (cross-validation, preprocessing pipelines, feature union). Without a wrapper, fastText requires writing to disk and calling its CLI, which breaks pipeline composition. skift eliminates that friction.

fastText's character n-gram approach means it can handle morphologically rich languages and domain-specific vocabulary better than word-level models trained on standard corpora. This makes it useful for medical text, legal text, or any domain where unusual words appear frequently. Compared to BERT-based classifiers, fastText is orders of magnitude faster at both training and inference, making it viable for situations where latency or compute cost matter more than maximum accuracy.

## Key points

- fastText wrapped as a scikit-learn estimator — use it in `Pipeline`, `GridSearchCV`, `cross_val_score` like any other classifier.
- fastText trains in seconds on millions of documents and handles out-of-vocabulary words via subword embeddings (character n-grams).
- Trade-off: much faster than transformer-based text classifiers (BERT, RoBERTa) at the cost of accuracy on complex tasks.
- Useful for production text classification where latency and cost matter, especially with specialized vocabulary.
- Part of the scikit-learn ecosystem for NLP alongside tools like gensim and spaCy integrations.

[Original](https://github.com/shaypal5/skift) → GitHub
