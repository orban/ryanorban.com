---
title: "Teaching a Computer to Read: NLP Hacking in Python"
date: 2013-12-16
categories:
  - nlp
  - python
  - text-processing
  - nltk
  - machine-learning
description: Scripted blog's introduction to NLP in Python — using NLTK for tokenization, part-of-speech tagging, named entity recognition, and sentiment analysis. A practical hands-on introduction to text processing written for a content-tech company's engineering blog.
params:
  source: pinboard
  sourceUrl: http://blog.scripted.com/scripted-updates/nlp-hacking-in-python/
---

## Summary

This post from Scripted (a content marketplace company) demonstrates natural language processing techniques in Python, written from the perspective of an engineering team that actually processes text for a living. The framing — teaching a computer to read — reflects where NLP was in 2013: moving from academic research into applied engineering.

The tutorial covers the core NLTK toolkit operations: tokenization (splitting text into words and sentences), part-of-speech tagging (marking words as nouns, verbs, etc.), named entity recognition (identifying people, places, organizations), and sentiment analysis via a simple Naive Bayes classifier trained on labeled text. These were the standard NLP primitives before word embeddings (word2vec, published in early 2013) and neural language models transformed the field.

The practical context matters: Scripted processed large volumes of written content and needed these techniques to assess quality, extract topics, and identify entities. The blog post bridges the gap between the NLTK Book (comprehensive but academic) and actually deploying text processing in a production Python application.

## Key points

- Core NLTK workflow: tokenize → tag → parse → classify. The standard 2013 NLP pipeline.
- Part-of-speech tagging with NLTK's averaged perceptron tagger — identifies grammatical roles of words.
- Named entity recognition: chunking tagged text to identify PERSON, ORGANIZATION, LOCATION entities.
- Sentiment analysis via Naive Bayes classifier: fast, works surprisingly well on bag-of-words features.
- This predates word2vec (2013) and the neural NLP revolution — NLTK-based rule/statistical methods were the practical state of the art.
- Written for engineers using text processing in production, not academic researchers.

[Original](http://blog.scripted.com/scripted-updates/nlp-hacking-in-python/)
