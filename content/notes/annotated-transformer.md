---
title: The Annotated Transformer
date: 2022-08-03
categories:
  - transformer
  - deep-learning
  - nlp
  - education
  - pytorch
description: The Annotated Transformer walks through the 'Attention Is All You Need' paper with working PyTorch code alongside every equation — the canonical resource for understanding transformer architecture from first principles. Published by Harvard NLP.
params:
  source: pinboard
  sourceUrl: http://nlp.seas.harvard.edu/annotated-transformer/
---

![The Annotated Transformer](/images/notes/annotated-transformer.png)

## Summary

The Annotated Transformer is a line-by-line implementation of the original transformer architecture from Attention Is All You Need (Vaswani et al., 2017), written by Sasha Rush and the Harvard NLP group. Every equation in the paper is accompanied by working PyTorch code that implements it directly — multi-head attention, positional encoding, layer normalization, the encoder-decoder stack, and beam search decoding. The presentation interleaves paper content with code so you can see exactly what each mathematical operation becomes in practice.

This is one of the most read technical documents in ML. The transformer architecture underlies essentially all modern NLP — BERT, GPT, T5, LLaMA — and understanding it at the implementation level is the prerequisite for modifying, debugging, or reasoning about any of these models. The annotated version solved a real problem: the original paper is dense and leaves implementation choices implicit, making it hard to go from equations to code without multiple readings.

The format (Jupyter notebook rendered as a webpage, code and prose interleaved) became influential. Andrej Karpathy's later works like nanoGPT and his educational notebooks follow a similar philosophy: the best way to understand a model is to implement it yourself from the math, with clear derivations at each step. The Annotated Transformer is the original template for this style of ML pedagogy.

## Key points

- Implements Attention Is All You Need with PyTorch code alongside every equation
- Covers full architecture: multi-head attention, positional encoding, layer normalization, beam search
- By Sasha Rush / Harvard NLP — the canonical transformer implementation reference
- Understanding the transformer from this level enables real reasoning about BERT, GPT, T5, etc.
- Format influenced later educational implementations: [nanoGPT](/notes/nanogpt/), minGPT, LLaMA educational ports
- Updated in 2022 to reflect modern PyTorch conventions (original was 2018)

[Original](http://nlp.seas.harvard.edu/annotated-transformer/)
