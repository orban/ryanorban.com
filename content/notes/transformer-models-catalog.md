---
title: "Transformer Models: An Introduction and Catalog"
date: 2022-07-22
categories:
  - transformer
  - llm
  - survey
  - nlp
  - reference
description: Xavier Amatriain's catalog of transformer models covers the full landscape of architecture variants and named models as of mid-2022 — encoder-only, decoder-only, encoder-decoder, and multimodal. A useful orientation map for the pre-ChatGPT era of rapid model proliferation.
params:
  source: pinboard
  sourceUrl: https://amatriain.net/blog/transformer-models-an-introduction-and-catalog-2d1e9039f376/
---

![Transformer Models: An Introduction and Catalog](/images/notes/transformer-models-catalog.png)

## Summary

Xavier Amatriain (formerly CTO of Curai, Netflix ML research) published this catalog to map the proliferating landscape of transformer architectures in 2022. By mid-2022, the number of named transformer models had grown fast enough that keeping track of them, understanding the architectural differences, and knowing which to use for what task had become genuinely difficult. The catalog organizes models taxonomically: encoder-only (BERT family), decoder-only (GPT family), encoder-decoder (T5, BART), and multimodal (DALL-E, CLIP, Flamingo).

The article explains the core design choices that differentiate these model families: bidirectional vs. unidirectional attention, masked language modeling vs. causal language modeling, prefix language models, and how these choices affect what the model is good for. Encoder-only models like BERT are strong for classification and understanding tasks; decoder-only models like GPT are strong for generation; encoder-decoder models like T5 are strong for sequence-to-sequence tasks. These are not subtle distinctions — they determine what training data you need and what tasks the model can do.

The catalog form makes it useful as a reference rather than just a read-once piece. As new models appeared through 2022 and 2023, Amatriain updated it. It became a community resource for practitioners needing to orient in the field quickly.

## Key points

- Taxonomy of transformer architectures: encoder-only (BERT), decoder-only (GPT), encoder-decoder (T5/BART), multimodal
- Key design choice: bidirectional attention (BERT) vs causal attention (GPT) determines task suitability
- Covers BERT, RoBERTa, GPT-3, T5, BART, DALL-E, CLIP, and dozens of variants
- By Xavier Amatriain — updated as new models appeared, maintained as a living reference
- Useful for practitioners needing to choose architectures or understand what a model name refers to
- Published July 2022 — snapshot of the field right before ChatGPT and the RLHF-tuned model wave

[Original](https://amatriain.net/blog/transformer-models-an-introduction-and-catalog-2d1e9039f376/)
