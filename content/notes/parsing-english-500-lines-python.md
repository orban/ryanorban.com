---
title: Parsing English with 500 Lines of Python
date: 2014-04-28
categories:
  - nlp
  - python
  - dependency-parsing
  - natural-language-processing
description: Matthew Honnibal's post describing a fast dependency parser for English implemented in 500 lines of Python — a precursor to spaCy. Demonstrates that a useful NLP system doesn't need a massive codebase if the algorithm is right.
params:
  source: pinboard
  sourceUrl: http://honnibal.wordpress.com/2013/12/18/a-simple-fast-algorithm-for-natural-language-dependency-parsing/
---

## Summary

Matthew Honnibal (later the creator of spaCy) wrote this post to demonstrate that dependency parsing — extracting the grammatical structure of a sentence — doesn't require a massive industrial system. The algorithm he describes is an arc-eager transition-based parser using a perceptron for scoring transitions. It produces good accuracy on standard benchmarks while fitting in a few hundred lines of readable Python.

The post is a deliberate contrast to the dominant NLP tools of the time (like the Stanford NLP pipeline or MaltParser), which were Java-based, heavyweight, and difficult to modify. By showing that the core algorithm fits in 500 lines, Honnibal was making the case that natural language processing could be accessible to practitioners who understood machine learning but weren't NLP specialists. This argument eventually became the founding premise of spaCy.

Dependency parsing is a core NLP task: given a sentence, draw directed edges between words indicating which words modify which. This dependency tree is the input to many downstream tasks — information extraction, named entity recognition, question answering. The transition-based approach represents parsing as a sequence of decisions (shift, reduce, left-arc, right-arc) that incrementally build the dependency tree.

## Key points

- Arc-eager transition-based dependency parsing with a perceptron classifier for transition scoring.
- 500 lines of Python achieving competitive accuracy — predecessor to spaCy's design philosophy.
- Matthew Honnibal wrote this while the field was dominated by slow, hard-to-extend Java tools.
- Transition-based parsing is O(n): each word is pushed/popped from a stack once, making it fast.
- Represents the argument that NLP systems can be both performant and comprehensible.

[Original](http://honnibal.wordpress.com/2013/12/18/a-simple-fast-algorithm-for-natural-language-dependency-parsing/)
