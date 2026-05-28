---
title: "Stanford CoreNLP: Free Text Analysis Pipeline"
date: 2014-02-06
categories:
  - nlp
  - stanford
  - text-analysis
  - java
  - open-source
description: Stanford's CoreNLP — the Java-based NLP pipeline from Stanford's NLP Group offering tokenization, POS tagging, NER, parsing, coreference resolution, and sentiment analysis in one tool. The dominant academic NLP pipeline before deep learning NLP models took over.
params:
  source: pinboard
  sourceUrl: http://nlp.stanford.edu/software/corenlp.shtml
---

## Summary

Stanford CoreNLP is the integrated NLP pipeline from Stanford NLP Group — a suite of Java-based tools for processing English (and later multilingual) text. The pipeline chains together: tokenization, sentence splitting, part-of-speech tagging, named entity recognition (NER), dependency parsing, coreference resolution, and sentiment analysis. Each step builds on the previous one, making it possible to run a full linguistic analysis on a document with a single API call.

The Prismatic share (framed as "Stanford scientists put free text-analysis tool on the web") reflects the launch of a web interface that made CoreNLP accessible without setting up the Java environment locally. The underlying tools had existed as research releases for years, but packaging them as a web demo lowered the friction for journalists, researchers, and product teams who wanted NLP capabilities without Java setup overhead.

Stanford CoreNLP's dominance in 2013-2014 was about the breadth of its pipeline and the quality of its trained models — both products of Stanford's NLP research program, which had pioneered conditional random fields for NER, probabilistic context-free grammars (PCFGs) for parsing, and recursive neural networks for sentiment analysis. spaCy (Python, industrial-grade, fast) and AllenNLP (Python, PyTorch-based, research-grade) later displaced it for most practitioners, but Stanford CoreNLP remained the reference system for many years.

## Key points

- Stanford CoreNLP: Java pipeline — tokenization → POS tagging → NER → parsing → coreference → sentiment, chainable in one call.
- Named entity recognition (NER): identifies persons, organizations, locations, dates in text — foundational for information extraction.
- Coreference resolution: links pronouns and mentions to the entities they refer to — enables understanding "he as referring to President Obama" earlier in the document.
- Web interface: lowered friction for exploration without Java environment — signals the democratization pressure on academic NLP tools.
- Historical position: the pre-BERT gold standard for English NLP pipelines, eventually displaced by deep learning-based alternatives from spaCy and Hugging Face.

[Original](http://nlp.stanford.edu/software/corenlp.shtml)
