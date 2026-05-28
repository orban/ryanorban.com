---
title: "LLM Course: Roadmaps and Notebooks for Large Language Models"
date: 2023-12-02
categories:
  - llm
  - education
  - fine-tuning
  - rag
  - reference
  - awesome-list
description: A comprehensive GitHub repository by Maxime Labonne with roadmaps, notebooks, and articles for learning about LLMs — from fundamentals through fine-tuning and deployment. One of the most starred LLM learning resources, covering the full practitioner pipeline.
params:
  source: pinboard
  sourceUrl: https://github.com/mlabonne/llm-course
---

![LLM Course: Roadmaps and Notebooks for Large Language Models](/images/notes/llm-course.png)

## Summary

[LLM Course](/notes/llm-course/) by Maxime Labonne is a structured learning resource for LLM practitioners, organized around three tracks: the LLM Fundamentals track (math, Python, neural networks), the LLM Scientist track (architecture, pre-training, fine-tuning, evaluation), and the LLM Engineer track (RAG, inference optimization, deployment, agents). The GitHub repository links out to Colab notebooks, articles, and papers for each topic.

The Scientist track is the densest and most useful for researchers: it covers transformer architecture, tokenization, pre-training data pipelines, supervised fine-tuning (SFT), RLHF, and preference learning (DPO). The Engineer track is practical: how to quantize models, run efficient inference with vLLM or llama.cpp, build RAG pipelines, and deploy to production. This dual-track structure makes it useful for both people building models and people building applications on top of them.

By late 2023 when this was bookmarked, the LLM space was moving faster than most courses could track, but Maxime Labonne was maintaining it actively. The repository's high star count (40k+) reflects that it filled a gap: enough depth for practitioners without requiring a PhD, with runnable notebooks rather than just theory.

## Key points

- Three tracks: Fundamentals, LLM Scientist (pre-training, fine-tuning), LLM Engineer (RAG, deployment).
- Runnable Colab notebooks for each topic — not just reading material.
- Covers QLoRA, DPO, RLHF, quantization, vLLM, RAG pipeline, and agent patterns.
- Maintained by Maxime Labonne (quantization researcher at Hugging Face).
- Companion to the book "Hands-on Large Language Models."
- Useful as a curriculum for internal team upskilling on LLM engineering.

[Original](https://github.com/mlabonne/llm-course) → AI agent
