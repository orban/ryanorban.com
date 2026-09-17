---
title: "Voynich Manuscript: Word Vectors and t-SNE Visualization"
date: 2016-01-19
categories:
  - nlp
  - word-vectors
  - t-sne
  - visualization
  - cryptography
  - unsolved-mysteries
description: Christian Perone applies word2vec embeddings and t-SNE visualization to the Voynich Manuscript — an undeciphered 15th-century text — to surface structural patterns in its unknown script. A creative application of NLP tools to a centuries-old mystery.
params:
  source: pinboard
  sourceUrl: http://blog.christianperone.com/2016/01/voynich-manuscript-word-vectors-and-t-sne-visualization-of-some-patterns/
---

## Summary

Christian Perone applied word2vec embeddings and t-SNE visualization to the Voynich Manuscript — the famous 15th-century illustrated codex that remains undeciphered. The experiment treats the manuscript's words (sequences of glyphs separated by whitespace) as a vocabulary, trains word2vec on the corpus, and uses t-SNE to project the resulting high-dimensional embeddings into two dimensions. The resulting clusters reveal structural patterns in the text even without knowing what any of it means.

The approach is genuinely revealing: if the manuscript is a language (or language-like encoding), words with similar distributional contexts should cluster together in the embedding space. If it's purely random or a substitution cipher, the clusters would be meaningless. Perone found that the embeddings do show meaningful groupings — consistent with the manuscript having some form of underlying grammar or semantic structure — even if the specific content remains unknown.

This is a creative demonstration of what distributional semantics can and can't do. Word2vec learns from co-occurrence patterns without any knowledge of meaning. Applied to an unknown script, it can detect whether the text has language-like structure without decoding it. The t-SNE visualization makes the structure visible. The manuscript remains unsolved, but tools like this constrain the hypothesis space.

## Key points

- word2vec applied to an unknown script: learns embeddings from co-occurrence without knowing semantics.
- t-SNE projects high-dimensional embeddings to 2D, revealing cluster structure.
- Clusters suggest language-like distributional structure in the manuscript.
- Demonstrates distributional semantics: meaning derived from context, not content.
- Voynich Manuscript remains undeciphered — this analysis constrains, but doesn't solve, the mystery.

[Original](http://blog.christianperone.com/2016/01/voynich-manuscript-word-vectors-and-t-sne-visualization-of-some-patterns/)
