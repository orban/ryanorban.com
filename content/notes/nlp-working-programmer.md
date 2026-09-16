---
title: Natural Language Processing for the Working Programmer
date: 2013-02-11
categories:
  - nlp
  - natural-language-processing
  - haskell
  - machine-learning
  - books
description: Natural Language Processing for the Working Programmer — a free online book teaching NLP concepts using Haskell. Unusual choice of language for NLP education; valuable for functional programming practitioners interested in text processing.
params:
  source: pinboard
  sourceUrl: http://nlpwp.org/book/
---

![Natural Language Processing for the Working Programmer](/images/notes/nlp-working-programmer.png)

## Summary

"Natural Language Processing for the Working Programmer" was a free online book at nlpwp.org that taught NLP concepts using Haskell as the implementation language. This made it distinctive in a field dominated by Python tutorials: using a functional programming language to teach NLP aligned naturally with the mathematical structures underlying the field (probability distributions, transformations, composition of text processing steps).

The choice of Haskell was deliberate and pedagogically interesting. Many NLP operations (tokenization, stemming, n-gram extraction, probabilistic model evaluation) map cleanly to functional abstractions — higher-order functions, lazy evaluation for stream processing, strong typing to prevent category errors. A text corpus is essentially a lazy stream, and Haskell's lazy I/O makes working with large corpora natural.

The book likely covered foundational NLP: tokenization and normalization, part-of-speech tagging, n-gram language models, naive Bayes classification, and possibly more advanced topics like hidden Markov models. In 2013, deep learning hadn't yet transformed NLP — the field was still dominated by feature-engineered models with probabilistic graphical structure.

## Key points

- Haskell for NLP: functional abstractions (maps, folds, lazy streams) align naturally with text processing pipelines — an unusual but illuminating approach
- Pre-deep learning NLP (2013): tokenization, n-gram models, naive Bayes, HMMs — statistical approaches with hand-crafted features
- Free online book format: following the tradition of accessible programming books that made knowledge freely available (SICP, LYAH, Learn You a Haskell)
- The NLP landscape shifted dramatically after 2015 with word2vec, and again after 2017 with Transformer architectures — this book represents the classical era
- Complementary reading: NLTK book for Python practitioners, Jurafsky & Martin for the comprehensive academic reference

[Original](http://nlpwp.org/book/)
