---
title: Timeline of Transformer Models and Large Language Models
date: 2023-05-01
categories:
  - llm
  - transformers
  - reference
  - history
  - visualization
description: A visual timeline of transformer models and large language models from 2017 through the present, mapping the lineage of architectures from the original Attention Is All You Need paper through GPT-4 and beyond. A useful reference for understanding model genealogy.
params:
  source: pinboard
  sourceUrl: https://ai.v-gar.de/ml/transformer/timeline/
---

![Timeline of Transformer Models and Large Language Models](/images/notes/transformer-timeline.png)

## Summary

This visual timeline by Vincent Garbe maps the development of transformer models and large language models from the original 2017 Attention Is All You Need paper through the 2023 frontier. It shows model lineage — which architectures descended from which — and lets you see the branching tree of BERT-style encoder models, GPT-style decoder models, encoder-decoder models like T5, and the subsequent explosion of fine-tuned variants and specialized models.

Timelines like this are useful for understanding how today's models got here. The transformer architecture has been remarkably stable as a foundation — the key innovations over 2017–2023 were mostly training data scale, parameter count, instruction fine-tuning techniques (RLHF, InstructGPT), and architectural refinements (attention efficiency, positional encodings). Seeing models plotted against time shows how the capability jumps correlated with scale increases vs. architectural changes.

By May 2023, the timeline captured a field that had moved from one dominant player (OpenAI's GPT family) to a diverse landscape including Google's PaLM and Gemini work, Meta's LLaMA, EleutherAI's GPT-NeoX, BigCode's [StarCoder](/notes/starcoder/), and dozens of fine-tuned community models. The timeline makes the proliferation visible in a way that reading individual paper announcements doesn't.

## Key points

- Visual mapping of transformer architecture lineage from 2017 (Attention Is All You Need) onward.
- Covers encoder models (BERT, RoBERTa), decoder models (GPT family), encoder-decoder (T5, BART).
- Shows model family relationships — which LLMs descended from which base architectures.
- Captures the 2023 moment when open-source models (LLaMA, [MPT-7B](/notes/mpt-7b/), Falcon) proliferated alongside closed frontier models.
- Useful reference for understanding capability jumps in terms of scale vs. architectural changes.

[Original](https://ai.v-gar.de/ml/transformer/timeline/)
