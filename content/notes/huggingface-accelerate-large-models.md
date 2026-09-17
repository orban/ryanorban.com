---
title: How Hugging Face Accelerate Runs Very Large Models
date: 2022-12-29
categories:
  - hugging-face
  - large-models
  - pytorch
  - gpu
  - model-parallelism
description: Hugging Face's technical guide to running very large models using Accelerate — covers device_map, model parallelism across GPUs, CPU offloading, and the mechanics of loading models that don't fit in a single GPU's VRAM. Essential reading for anyone self-hosting large LLMs.
params:
  source: pinboard
  sourceUrl: https://huggingface.co/blog/accelerate-large-models
---

## Summary

This Hugging Face blog post explains the technical mechanisms behind running models that are too large to fit in a single GPU's VRAM using the Accelerate library. The key innovation is the `device_map` parameter: pass `device_map="auto"` and Accelerate automatically shards the model across available GPUs, CPU RAM, and disk storage, deciding which layers go where based on available memory.

The mechanics are worth understanding. PyTorch normally assumes a model fits entirely on one device. Accelerate intercepts the forward pass and manages layer-by-layer movement between devices — a process called "model parallelism with CPU offloading." The speed cost is significant (data has to transfer between GPU VRAM and CPU RAM for each layer that's offloaded), but it makes inference possible on hardware that would otherwise run out of memory entirely.

The post explains three main strategies: multi-GPU parallelism (split model across multiple GPUs — fast), CPU offloading (overflow to RAM — slower), and disk offloading (overflow to disk — very slow but possible for enormous models). Accelerate handles the bookkeeping automatically, making it possible to run a 70B parameter model on a machine with two 24GB GPUs and some RAM without manually managing the sharding. This was especially relevant in late 2022 as open-source LLMs like OPT, BLOOM, and early LLaMA precursors were becoming accessible for self-hosting.

## Key points

- `device_map="auto"` in Accelerate auto-shards models across GPUs, CPU, and disk.
- Enables running models larger than single-GPU VRAM via automatic model parallelism.
- Three strategies: multi-GPU (fast), CPU offload (slower), disk offload (possible but slow).
- Published late 2022 as open-source LLMs were first becoming self-hostable.
- Prerequisite understanding for anyone self-hosting 7B-70B parameter models on consumer hardware.

[Original](https://huggingface.co/blog/accelerate-large-models)
