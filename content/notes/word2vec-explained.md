---
title: Word2Vec Explained
date: 2022-03-27
categories:
  - machine-learning
  - nlp
  - word-embeddings
  - education
  - deep-learning
description: A clear walkthrough of Word2Vec's intuition and mechanics — skip-gram vs. CBOW, negative sampling, and why the king-queen analogy works. Good primer before reading papers on later embedding methods.
params:
  source: pinboard
  sourceUrl: https://towardsdatascience.com/word2vec-explained-49c52b4ccb71
---

## Summary

Word2Vec is the 2013 breakthrough by Tomas Mikolov and team at Google that made word embeddings a standard tool in NLP. The core idea: train a shallow neural network to predict words from context (or context from words), then discard the prediction task and keep the learned weights as dense vector representations of words. These representations encode semantic relationships as geometric structure — the famous example being that `king − man + woman ≈ queen` in the embedding space.

Two architectures were introduced: CBOW (Continuous Bag of Words) predicts the center word from surrounding context words; Skip-gram predicts surrounding context words from the center word. Skip-gram generally performs better on rare words since it treats each context word as a separate training example. Training on a large corpus produces embeddings where words with similar distributions end up close together in the vector space — proximity encodes shared semantic context.

Negative sampling is the training trick that made Word2Vec practical. The full softmax over a vocabulary of millions of words is expensive. Negative sampling instead trains a binary classifier: given a (word, context) pair, is this a real pair from the corpus or a randomly sampled "negative" pair? By sampling ~5-20 negative examples per positive, training becomes tractable without approximating softmax. The approach works because embeddings for frequently co-occurring words are pushed together while embeddings for random pairs are pushed apart.

## Key points

- Skip-gram: predict context from center; CBOW: predict center from context — both learn useful embeddings as a byproduct.
- Negative sampling replaces expensive softmax with a binary classification task against random "negative" word samples.
- Distributed representation: meaning encoded in activation patterns across dimensions, not single neurons.
- Semantic relationships emerge as vector arithmetic — synonym clusters, gender analogies, country-capital relationships.
- Word2Vec embeddings became the foundation for later methods like GloVe, FastText, and eventually BERT contextualized embeddings.
- By Tomas Mikolov et al. at Google (2013); the paper "Distributed Representations of Words and Phrases" is the main reference.

[Original](https://towardsdatascience.com/word2vec-explained-49c52b4ccb71)
