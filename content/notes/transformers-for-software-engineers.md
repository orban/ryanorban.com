---
title: Transformers for Software Engineers
date: 2022-04-02
categories:
  - machine-learning
  - transformers
  - education
  - software-engineering
  - deep-learning
description: Nelson Elhage's explainer on transformers pitched at software engineers — treats the architecture as a data structure rather than mysterious ML magic. Grounding for anyone who codes but hasn't internalized what attention actually does.
params:
  source: pinboard
  sourceUrl: https://blog.nelhage.com/post/transformers-for-software-engineers/
---

## Summary

Nelson Elhage's post on transformer architecture from the blog Made of Bugs takes an unusual approach: it treats the transformer as a system to be understood through the lens of data structures and information flow, not statistics. For engineers comfortable with systems thinking but unfamiliar with ML, this framing makes the architecture legible in a way that papers and ML-first explanations often don't.

The central mental model Elhage offers is the residual stream: a high-dimensional vector (the model's working memory for each token position) that gets read and written by each layer. Attention heads read from it to compute what to attend to, write their outputs back into it; MLP layers do the same. No single layer owns the representation — it's a collaborative accumulation across the full depth of the model. This view makes layer residuals feel natural (you're adding to an existing state, not transforming it) and makes representation learning more concrete.

Self-attention gets explained as a routing mechanism: each token queries the other tokens to decide what information to pull into its representation. The query, key, value matrices are learned projections that determine what am I looking for, what do I advertise, and "what do I actually send if selected." Dot-product similarity between queries and keys produces the attention weights; the weighted sum of values is what gets added to the residual stream. Crucially, this is fully differentiable, so the model learns what to attend to end-to-end. The MLP layers then process each position independently — they're the model's lookup table that maps combinations of features to new features.

## Key points

- The residual stream is the right mental model: a shared state vector each layer reads and writes into additively.
- Self-attention = learned routing: queries ask questions, keys advertise, values deliver.
- MLP layers are position-wise: they don't mix information across tokens, only attention does.
- Layer normalization stabilizes training by normalizing activations before each sub-layer.
- Multi-head attention runs multiple attention operations in parallel with different projections, enabling different types of relationships to be captured simultaneously.
- By Nelson Elhage (Anthropic), who is also known for [mechanistic interpretability](/notes/mechanistic-interpretability/) research.

[Original](https://blog.nelhage.com/post/transformers-for-software-engineers/)
