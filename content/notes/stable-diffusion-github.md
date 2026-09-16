---
title: "Stable Diffusion: CompVis Open-Source Release"
date: 2022-08-12
categories:
  - stable-diffusion
  - generative-ai
  - image-generation
  - open-source
  - latent-diffusion
description: The CompVis open-source release of Stable Diffusion — the text-to-image model that democratized AI image generation. This marked the moment state-of-the-art image synthesis left the walled gardens of DALL-E 2 and Midjourney and became freely runnable on consumer hardware.
params:
  source: pinboard
  sourceUrl: https://github.com/CompVis/stable-diffusion
---

## Summary

The `CompVis/stable-diffusion` repository is the original Stable Diffusion release by the Ludwig Maximilian University of Munich's CompVis Group, published in August 2022. It implements a latent diffusion model — a variant of diffusion models that operates in a compressed latent space rather than pixel space, making it dramatically more computationally efficient than prior approaches like DALL-E 2.

The release was a watershed moment for generative AI. Before Stable Diffusion, text-to-image generation was accessible only through rate-limited APIs (DALL-E 2 via OpenAI, Midjourney via Discord) with content restrictions. The CompVis release ran on a consumer GPU with 6GB VRAM, enabling local inference with no API key and no content policy. Within days, communities emerged, and an ecosystem of fine-tunes, GUIs (like AUTOMATIC1111), and extensions developed around it.

Technically, Stable Diffusion encodes images into a low-dimensional latent space using a variational autoencoder (VAE), then trains a diffusion process in that space conditioned on CLIP text embeddings. The denoising is done by a U-Net architecture. This is roughly 10x faster than pixel-space diffusion and fits in consumer VRAM — a critical practical advantage over contemporaries.

## Key points

- First open-source weights for a competitive text-to-image model; ran on consumer GPUs with 6GB VRAM.
- Uses latent diffusion in a compressed representation via VAE, conditioned on CLIP embeddings.
- Released under a non-commercial research license initially; later versions moved to more permissive terms.
- Spawned a massive ecosystem: AUTOMATIC1111, fine-tuning pipelines (DreamBooth, LoRA), and community model hubs.
- Marked the beginning of the open-source generative AI era — democratizing image generation as GPT-2 had for text.

[Original](https://github.com/CompVis/stable-diffusion) → GitHub
