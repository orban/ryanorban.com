---
title: "SLED: Efficient Long-Text Understanding with Short-Text Models"
date: 2022-08-02
categories:
  - nlp
  - long-context
  - transformers
  - research
  - efficiency
description: SLED (Sliding-Encoder and Decoder) lets you apply short-context pretrained models to arbitrarily long documents by chunking input with overlap and fusing representations in the decoder. Competitive with specialized long-context models without the expensive custom pretraining.
params:
  source: pinboard
  sourceUrl: https://mivg.github.io/publication/sled
---

## Summary

SLED (Sliding-Encoder and Decoder) addresses a fundamental limitation of transformer models: their quadratic attention complexity makes processing long documents computationally expensive and practically impossible beyond a few thousand tokens. Rather than building a new long-context architecture from scratch, SLED reuses existing short-context pretrained models by splitting the input document into overlapping chunks, encoding each chunk independently with the pretrained encoder, and then using the pretrained decoder to fuse information across all the encoded chunks.

The key insight is that long-context pretraining is expensive and rare — models like Longformer, BigBird, and LED require custom architectures and large-scale pretraining from scratch or from extensive fine-tuning. SLED sidesteps this by treating the chunked encoding as a form of retrieval: the decoder can attend to all the chunk representations, so important information from any part of the document is theoretically accessible. The overlapping chunks ensure that context at chunk boundaries isn't lost.

Evaluated on the SCROLLS benchmark (seven long-document understanding datasets including summarization, QA, and classification), SLED is competitive with specialized long-context models despite being significantly simpler and cheaper. Published in TACL 2023 and presented at ACL 2023, the work by Maor Ivgi and collaborators is a good example of the "don't pretraining from scratch, extend existing models cleverly" school of efficiency research.

## Key points

- SLED: chunk document → encode chunks with short-context model → decoder fuses across chunks
- Avoids expensive custom pretraining: works with any existing encoder-decoder pretrained model (T5, BART)
- Overlapping chunks preserve context at boundaries — key engineering detail
- Competitive with Longformer, BigBird, LED on SCROLLS benchmark
- Published TACL 2023 / ACL 2023 — by Maor Ivgi et al.
- Broader pattern: extending short-context models to long inputs is often better than training specialized models

[Original](https://mivg.github.io/publication/sled) → GitHub
