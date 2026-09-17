---
title: TextSynth Playground
date: 2022-04-27
categories:
  - llm
  - language-models
  - inference
  - developer-tools
  - playground
description: TextSynth is a web playground and API for running large language models efficiently — built by Fabrice Bellard (of ffmpeg and QuickJS fame) using his GGML-based inference engine. In 2022 it was one of the few accessible ways to experiment with GPT-J, GPT-NeoX, and similar open models.
params:
  source: pinboard
  sourceUrl: https://textsynth.com/playground.html
---

## Summary

TextSynth is a web playground and API for running open-weight large language models, built and maintained by Fabrice Bellard — the programmer behind FFmpeg, QEMU, and QuickJS, known for implementing historically complex software in extraordinarily lean code. TextSynth was notable in 2022 because it offered one of the few accessible ways to experiment with then-state-of-the-art open models — GPT-J (6B parameters), GPT-NeoX (20B), CODEGEN, and Fairseq models — via a simple web UI and API without setting up your own GPU infrastructure.

The technical engine behind TextSynth is Bellard's custom inference implementation (libnc / his tensor library, predecessor to what became known in the GGML ecosystem). Bellard optimized the transformer inference heavily, achieving efficient CPU-based inference that made it practical to serve these models affordably. This was early work in the direction that Georgi Gerganov's GGML and llama.cpp would later popularize — making large model inference run on commodity hardware.

The historical context: in April 2022, GPT-3 was API-only and expensive; there was no Stable Diffusion yet; ChatGPT was months away. TextSynth was one of a handful of places (alongside EleutherAI's Discord and Hugging Face Spaces) where a developer could interact with a genuinely capable language model without a waitlist or a large API bill. It was a quiet but important piece of infrastructure in the pre-democratization era of open LLMs.

## Key points

- Web playground and API for open-weight language models — GPT-J, GPT-NeoX, CODEGEN accessible without GPU setup.
- Built by Fabrice Bellard (FFmpeg, QEMU, QuickJS) using his custom tensor inference engine.
- Efficient CPU-based inference: predecessor work to the GGML / llama.cpp approach to commodity model serving.
- April 2022: one of very few accessible open LLM interfaces before ChatGPT, Stable Diffusion, llama.cpp.
- API available for programmatic access — developers could integrate models without training infrastructure.
- The era it represents: EleutherAI models, pre-Meta AI LLaMA, when "open" LLMs meant 6B-20B parameter models.

[Original](https://textsynth.com/playground.html)
