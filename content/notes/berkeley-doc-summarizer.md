---
title: Berkeley Document Summarizer
date: 2021-06-26
categories:
  - nlp
  - summarization
  - machine-learning
  - research
  - open-source
description: The Berkeley Document Summarizer is a learning-based extractive summarization system that uses syntactic compression and coreference constraints. Academic research code from Greg Durrett, representing the pre-neural era of NLP summarization work.
params:
  source: pinboard
  sourceUrl: https://github.com/gregdurrett/berkeley-doc-summarizer
---

## Summary

The Berkeley Document Summarizer is an open-source, learning-based extractive summarization system developed by Greg Durrett and colleagues at UC Berkeley. Unlike abstractive summarization systems that generate new text, it works by selecting and compressing existing sentences from the source document — making the output faithful to the original by construction.

The system exploits syntactic compression to shorten selected sentences: it parses sentences into dependency trees and drops non-essential subtrees according to learned deletion rules. Coreference resolution constraints ensure consistency — if a pronoun in a selected sentence refers to an entity already introduced, that reference is maintained correctly. This combination of extraction and compression was a state-of-the-art approach for single-document summarization at the time of publication.

From a historical perspective, this represents the statistical NLP era — feature engineering, structured learning, and constraint-based inference — before transformer-based models (BERT, PEGASUS, T5) largely superseded these approaches. The techniques it uses (syntactic parsing, coreference, compression) remain conceptually important even if neural end-to-end models now dominate the leaderboards.

## Key points

- Extractive summarization: selects and compresses source sentences rather than generating new text.
- Uses syntactic compression via dependency parse trees to shorten sentences while preserving meaning.
- Coreference resolution constraints maintain entity reference consistency in summaries.
- Pre-neural, statistical NLP approach — contrasts with modern transformer-based summarization.
- By Greg Durrett (UC Berkeley) — research code, single-document summarization task.

[Original](https://github.com/gregdurrett/berkeley-doc-summarizer) → GitHub
