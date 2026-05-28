---
title: "Teaching a Computer to Read: NLP Hacking in Python"
date: 2013-09-27
categories:
  - nlp
  - python
  - text-analysis
  - machine-learning
  - tutorial
description: Scripted's NLP hacking tutorial in Python — covering tokenization, part-of-speech tagging, named entity recognition, and text classification with NLTK and scikit-learn. An applied introduction to NLP for data scientists.
params:
  source: pinboard
  sourceUrl: http://blog.scripted.com/staff/nlp-hacking-in-python/
---

## Summary

This post from Scripted (a content marketplace) walked through practical natural language processing (NLP) techniques in Python using NLTK and scikit-learn. The 2013 Python NLP stack was: NLTK for linguistics-oriented processing (tokenization, POS tagging, parse trees) and scikit-learn for the ML layer (feature extraction from text, classification models).

The tutorial likely covered the full pipeline from raw text to trained classifier: tokenization (splitting text into words/sentences), part-of-speech tagging (verb, noun, adjective labels), stemming or lemmatization (reducing words to root forms), TF-IDF or bag-of-words feature extraction, and fitting a classifier like Naive Bayes or logistic regression.

NLTK (Natural Language Toolkit) was the standard Python NLP library in 2013, developed at UPenn by Steven Bird and Edward Loper. It was comprehensive but slow; spaCy (released 2015) later displaced it for production use. The stack of NLTK + scikit-learn represented the state of practical Python NLP before word embeddings (word2vec, released 2013) and eventually transformers changed how text was represented.

## Key points

- 2013 Python NLP stack: NLTK for linguistic processing, scikit-learn for machine learning over text features.
- Core pipeline: tokenize → POS tag → extract features (TF-IDF, bag of words) → classify with Naive Bayes or logistic regression.
- NLTK was comprehensive but slow; spaCy later replaced it for production use after 2015.
- Pre-embeddings era: bag of words and TF-IDF were the standard text representations before word2vec and GloVe.
- Saved during Zipfian Academy period — NLP was a major application area for data science at the time.

[Original](http://blog.scripted.com/staff/nlp-hacking-in-python/)
