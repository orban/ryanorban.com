---
title: State-of-the-Art Image Generative Models (2021)
date: 2021-03-05
categories:
  - generative-ai
  - image-generation
  - gans
  - deep-learning
  - research
description: Aran Komatsuzaki's March 2021 survey of state-of-the-art image generative models — covering BigGAN, VQVAE-2, DALL-E, CLIP, and diffusion models just as they were emerging. A historical snapshot of the field one year before diffusion models took over.
params:
  source: pinboard
  sourceUrl: https://arankomatsuzaki.wordpress.com/2021/03/04/state-of-the-art-image-generative-models/
---

![State-of-the-Art Image Generative Models (2021)](/images/notes/image-generative-models-sota.png)

## Summary

Aran Komatsuzaki's March 2021 survey captures the field of image generation at a pivotal transition moment. GAN-based models (BigGAN, StyleGAN2) had been the dominant approach, producing high-resolution photorealistic images but requiring careful training and suffering from mode collapse. The survey covers these alongside the newly emerging alternatives.

Key models covered: VQ-VAE-2 (Vector Quantized VAE) from DeepMind — a two-stage approach using discrete codebooks and autoregressive priors, competitive with GANs without adversarial training instability. DALL-E (OpenAI) — the first broadly capable text-to-image model, using a transformer over a discrete image token vocabulary. CLIP — trained on image-text pairs, powerful as a feature extractor and increasingly as a guidance signal for generation. And the earliest diffusion model results (DDPM) — denoising-based generation that would within a year come to dominate the field.

From 2026, this reads as a snapshot taken at the exact moment diffusion models were about to displace GANs. DDPM is mentioned but not yet recognized as the paradigm that would power Stable Diffusion, DALL-E 2, Midjourney, and Imagen. The survey is historically valuable for understanding why diffusion models won: GANs are harder to train, harder to scale, and more prone to failure modes.

## Key points

- March 2021: GANs still dominant, diffusion models just emerging (DDPM results just published).
- VQ-VAE-2: autoregressive over discrete image codes — stable alternative to adversarial training.
- DALL-E v1: transformer over discrete image tokens — first broadly capable text-to-image model.
- CLIP: cross-modal embeddings — became the guidance backbone for text-to-image tools like Deep Daze.
- Historical inflection: within 18 months, diffusion models (Stable Diffusion, DALL-E 2) superseded GANs.

[Original](https://arankomatsuzaki.wordpress.com/2021/03/04/state-of-the-art-image-generative-models/)
