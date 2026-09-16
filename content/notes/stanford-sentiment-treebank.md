---
title: Recursive Deep Models for Semantic Compositionality
date: 2013-09-05
categories:
  - nlp
  - sentiment-analysis
  - deep-learning
  - recursive-neural-networks
  - stanford
description: Stanford's Recursive Neural Tensor Network paper and Sentiment Treebank dataset — Richard Socher's EMNLP 2013 work that used tree-structured recursive neural networks to predict fine-grained sentiment at every node of a parse tree. A landmark paper that pushed NLP models toward compositionality.
params:
  source: pinboard
  sourceUrl: http://nlp.stanford.edu/sentiment/index.html
---

## Summary

Richard Socher and colleagues at Stanford NLP published this work introducing the [Stanford Sentiment Treebank](/notes/stanford-sentiment-treebank/) and a Recursive Neural Tensor Network (RNTN) that achieved state-of-the-art sentiment analysis results by operating on constituency parse trees. Rather than treating a sentence as a bag of words or a flat sequence, the RNTN computed sentiment at every internal node of a parse tree — capturing how negation, intensifiers, and compositional structure change meaning.

The key insight was semantic compositionality: the meaning of not terrible is not simply the average of "not" and "terrible" but depends on how they compose. Word embeddings at the time (this predates word2vec by a few months) couldn't capture this well; operating over parse trees let the model learn how syntactic composition affects sentiment. The Stanford Sentiment Treebank annotated 11,855 sentences with fine-grained sentiment labels (1–5 scale) at every tree node — a much richer dataset than binary positive/negative labels.

This paper appeared at EMNLP 2013 and was part of Richard Socher's influential streak of recursive neural network papers applying deep learning to structured linguistic data. It preceded the dominance of LSTMs and transformers for NLP — the tree-structured approach was a serious alternative before sequence models proved more scalable and easier to train.

## Key points

- Recursive Neural Tensor Network: applies a neural network at each node of a constituency parse tree to model compositional semantics.
- [Stanford Sentiment Treebank](/notes/stanford-sentiment-treebank/): 11,855 sentences, sentiment labeled at every parse tree node — enables learning how composition affects sentiment, not just bag-of-words classification.
- Compositionality problem: negation (not good), degree modifiers (very bad), and contrastive clauses (good but boring) require understanding structure, not just word co-occurrence.
- Predecessor to sequence-based NLP: LSTMs, attention mechanisms, and eventually transformers largely replaced tree-structured approaches by 2016.
- Richard Socher's work — alongside word2vec (Mikolov, 2013) and later GloVe — was foundational to the distributed representations era of NLP.
- The treebank dataset itself remained a standard sentiment analysis benchmark for years after.

[Original](http://nlp.stanford.edu/sentiment/index.html)
