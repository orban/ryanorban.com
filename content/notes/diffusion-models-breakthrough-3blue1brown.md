---
title: "The breakthrough behind modern AI image generators: diffusion models (3Blue1Brown)"
date: 2025-02-10
categories:
  - machine-learning
  - diffusion-models
  - education
  - video
  - 3blue1brown
description: "3Blue1Brown's visual explanation of diffusion models — part 1 covering the core breakthrough behind modern AI image generators. Classic 3B1B treatment: intuition-first, mathematically grounded, visually clear."
params:
  source: pinboard
  sourceUrl: https://www.youtube.com/watch?v=1pgiu--4W3I
---

![The breakthrough behind modern AI image generators: diffusion models (3Blue1Brown)](/images/notes/diffusion-models-breakthrough-3blue1brown.png)

## Summary

This is Part 1 of 3Blue1Brown's visual explanation of diffusion models — the technology powering Stable Diffusion, DALL-E, Midjourney, and similar image generation systems. 3Blue1Brown (Grant Sanderson) is known for building intuition visually before introducing formalism, making this an excellent entry point for understanding how diffusion works.

Diffusion models work by learning to reverse a noise-adding process. Training adds Gaussian noise incrementally to images until they become pure noise; the model learns to denoise — to predict what was removed at each step. Generation then starts from pure noise and iteratively denoises toward a coherent image. The key insight is that this denoising objective is tractable to train and produces remarkably high-quality samples.

The breakthrough framing is accurate. Before diffusion models, GANs (Generative Adversarial Networks) were the dominant approach — producing sharp images but prone to mode collapse and training instability. Diffusion models achieved better sample quality, more diverse outputs, and more stable training, enabling the wave of image generation tools that emerged from 2022 onward. DDPM (Denoising Diffusion Probabilistic Models) is the foundational paper; later work added DDIM for faster sampling and classifier-free guidance for conditioning on text prompts.

## Key points

- Diffusion models learn to reverse a noise-adding process — training on denoising, generating via iterative denoising from noise.
- 3Blue1Brown treatment: visual intuition before formalism, Part 1 of multi-part series.
- Superseded GANs as the dominant image generation approach due to better quality and training stability.
- DDPM is the foundational paper; DDIM adds fast sampling; classifier-free guidance enables text conditioning.
- Basis for Stable Diffusion, DALL-E 2/3, Midjourney, and Imagen.

[Original](https://www.youtube.com/watch?v=1pgiu--4W3I)
