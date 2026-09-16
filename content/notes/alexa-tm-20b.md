---
title: "AlexaTM 20B: Amazon's Few-Shot Language Model"
date: 2022-08-03
categories:
  - llm
  - few-shot-learning
  - amazon
  - multilingual
  - nlp
description: AlexaTM 20B is Amazon's 20B parameter seq2seq language model that outperforms PaLM 540B on one-shot summarization and sets state-of-the-art on multilingual translation — while training on one-fifth of GPT-3's carbon footprint. A strong argument for encoder-decoder architecture in few-shot settings.
params:
  source: pinboard
  sourceUrl: https://www.amazon.science/blog/20b-parameter-alexa-model-sets-new-marks-in-few-shot-learning
---

## Summary

AlexaTM 20B is Amazon's 20-billion-parameter language model, notable for using an encoder-decoder (seq2seq) architecture rather than the decoder-only design dominant in models like GPT-3 and PaLM. The research claims that for tasks like summarization and machine translation, bidirectional encoding is a structural advantage — and the results support this: AlexaTM 20B outperforms PaLM 540B (27x larger) on one-shot text summarization in English, German, and Spanish.

The few-shot learning angle is the headline. With a single example, AlexaTM generates better summaries than PaLM with 540B parameters. For machine translation, it achieves state-of-the-art on Flores-101 with especially large gains on low-resource language pairs — Arabic to Tamil jumps from 0.9 to 21.8 BLEU points compared to previous supervised models. The multilingual support (12 languages including Arabic, Hindi, Tamil, Telugu) reflects Alexa's need to work globally.

Efficiency is also notable: the training carbon footprint is approximately one-fifth of GPT-3's. The architecture choice matters here too — encoder-decoder models can be more parameter-efficient for the seq2seq tasks they're designed for. This was published in August 2022, before ChatGPT, when the dominant framing was still about raw benchmark performance rather than instruction following. AlexaTM didn't become a widely-used model, but the research makes a clear case that decoder-only is not the only viable architecture at scale.

## Key points

- 20B parameters, encoder-decoder (seq2seq) — not decoder-only like GPT-3
- One-shot summarization beats PaLM 540B in English, German, Spanish
- State-of-the-art on Flores-101 multilingual translation; dramatic gains on low-resource languages
- Supports 12 languages including Arabic, Hindi, Tamil, Telugu
- Carbon footprint ~1/5 of GPT-3 training
- Architecture argument: bidirectional encoding (BERT-style encoder) is better for seq2seq tasks than causal LM

[Original](https://www.amazon.science/blog/20b-parameter-alexa-model-sets-new-marks-in-few-shot-learning)
