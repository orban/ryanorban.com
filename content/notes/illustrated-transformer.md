---
title: The Illustrated Transformer
date: 2021-01-08
categories:
  - machine-learning
  - transformers
  - education
  - visualization
  - deep-learning
description: Jay Alammar's illustrated walkthrough of the Transformer architecture — the most widely cited visual explainer of attention, encoder-decoder structure, and multi-head attention. A must-read before diving into any BERT, GPT, or T5 paper.
params:
  source: pinboard
  sourceUrl: https://jalammar.github.io/illustrated-transformer/
---

## Summary

The Illustrated Transformer by [Jay Alammar](/notes/jay-alammar/) is the canonical visual explainer for the transformer architecture introduced in Attention Is All You Need (Vaswani et al., 2017). It breaks down every component — self-attention, multi-head attention, positional encoding, the encoder-decoder stack — using step-by-step diagrams that show exactly what the tensors look like at each stage. This post is probably the single most linked explanation of how transformers work among practitioners.

The key insight Alammar communicates is that self-attention allows each token in a sequence to directly attend to every other token, bypassing the sequential bottleneck of RNNs. Instead of processing left-to-right and compressing all context into a fixed hidden state, every position gets direct access to every other position, with learned weights determining relevance. This fundamentally changed what NLP models could do.

The post is part of a broader series on [Jay Alammar](/notes/jay-alammar/)'s blog that also covers BERT, GPT-2, and word embeddings. It's the natural companion to Chris Olah's more theoretical writing — Alammar goes wide on architecture intuition, Olah goes deep on theory. For practitioners coming from a deep learning background, this is the fastest path to a solid mental model of modern LLMs.

## Key points

- Self-attention computes query, key, value vectors for each token and uses dot-product similarity to weight which tokens to attend to — the core of the transformer.
- Multi-head attention runs several attention operations in parallel, letting the model attend to different relationships simultaneously (e.g., syntax and semantics).
- Positional encoding injects sequence order via sinusoidal functions, since attention itself is order-agnostic.
- The encoder reads an input sequence; the decoder generates the output while attending to the encoder's output via cross-attention.
- The post predates BERT and GPT-2 but remains the foundational explainer — everything downstream (including vision transformers and diffusion transformers) shares this core structure.

[Original](https://jalammar.github.io/illustrated-transformer/) → GitHub
