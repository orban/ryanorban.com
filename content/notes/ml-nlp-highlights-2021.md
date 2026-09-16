---
title: ML and NLP Research Highlights of 2021
date: 2022-01-25
categories:
  - machine-learning
  - nlp
  - research
  - "2021"
  - review
  - foundation-models
description: Sebastian Ruder's annual ML/NLP research highlights for 2021 — covering foundation models, the prompting revolution, AlphaFold 2, diffusion models, and the growing focus on efficiency and responsible AI. The most useful single-document summary of where the field moved that year.
params:
  source: pinboard
  sourceUrl: https://ruder.io/ml-highlights-2021/
---

## Summary

Sebastian Ruder's annual review of machine learning and NLP research is one of the most useful year-end retrospectives in the field — synthesizing 15+ research areas into a coherent picture of where things moved and why. The 2021 edition captured a year that felt like a genuine inflection point across multiple directions simultaneously.

The dominant theme was foundation models and scale: pre-trained models grew larger and were applied across modalities (speech, vision, language, code). But the more interesting story was what happened around the edges of scale: prompting emerged as a viable alternative to fine-tuning, with a well-chosen prompt worth thousands of labeled examples. Parameter-efficient fine-tuning (adapters, prefix tuning) addressed the cost of adapting giant models to new tasks without full retraining. And retrieval-augmented generation scaled to trillion-token corpora — the first signs of what would later become RAG pipelines everywhere.

The landmark results that year: AlphaFold 2 solved protein structure prediction in a way the field considered years away, Codex and GitHub Copilot demonstrated practical code generation at a level that changed developer workflows, and diffusion models produced near-photorealistic image generation that would lead directly to Stable Diffusion and DALL-E 2 the following year.

## Key points

- Foundation models: massive pre-trained models generalized across modalities — the year scale proved its worth empirically.
- Prompting revolution: a good prompt worth up to 3,500 labeled examples — shifted fine-tuning vs. prompting calculus significantly.
- AlphaFold 2: solved protein structure prediction; Codex/GitHub Copilot: practical code generation; diffusion models: photorealistic image generation.
- Parameter-efficient fine-tuning (adapters, LoRA, prefix tuning) — adapt large models cheaply without full retraining.
- Retrieval-augmented generation (RAG) scaled to trillion-token corpora — seeds of the RAG pipeline pattern that would become ubiquitous.
- Growing research focus on benchmark quality, data quality, bias, and responsible deployment — the field's methodological self-reflection.

[Original](https://ruder.io/ml-highlights-2021/) → GitHub
