---
title: "MLC-LLM: LLMs on Every Device"
date: 2023-05-01
categories:
  - llm
  - on-device
  - inference
  - mobile
  - open-source
description: MLC-LLM enables running large language models natively on any device — laptops, phones, browsers — without a server, by compiling models through the Apache TVM compiler stack. One of the earliest frameworks to make on-device LLM inference practical across diverse hardware.
params:
  source: pinboard
  sourceUrl: https://github.com/mlc-ai/mlc-llm
---

![MLC-LLM: LLMs on Every Device](/images/notes/mlc-llm.png)

## Summary

[MLC-LLM](/notes/mlc-llm/) (Machine Learning Compilation for LLMs) is a framework from MLC AI for running large language models natively on any device — iPhones, Android phones, laptops, web browsers — without a server or cloud API. It works by compiling models through Apache TVM, an ML compiler stack that generates optimized native code for diverse hardware backends (Metal, CUDA, Vulkan, WebGPU, OpenCL).

The approach separates model architecture from hardware-specific optimization: you define the model once, and the compiler handles generating efficient code for each target. This makes deploying LLaMA, Vicuna, and other open models to mobile devices practical — the generated code is fast enough for interactive use on consumer hardware. By May 2023, MLC-LLM could run LLaMA-7B on an iPhone 14 Pro and in a web browser via WebGPU.

[MLC-LLM](/notes/mlc-llm/) is significant because it shifts the inference paradigm from model as a remote API to model as a local application. This enables privacy-preserving deployment (data never leaves the device), offline-first applications, and eliminates per-query API costs. The same team is behind TVM, TensorIR, and the broader MLC research agenda on universal ML deployment — connecting this to academic work on compiler-based ML optimization.

## Key points

- Compiles LLMs to native code for any hardware via Apache TVM — iPhone, Android, browser (WebGPU), desktop.
- Ran LLaMA-7B on iPhone 14 Pro at interactive speed — a milestone for on-device LLM inference in 2023.
- Model-hardware separation: define once, compile to any target without architecture changes.
- Privacy + offline benefits: model runs entirely on-device, no API calls.
- Related: llama.cpp (CPU-focused), Ollama (local server), [llamafile](/notes/llamafile/) — different approaches to the same problem.
- Academic lineage: Apache TVM, TensorIR, MLC research from CMU/UW.

[Original](https://github.com/mlc-ai/mlc-llm) → GitHub
