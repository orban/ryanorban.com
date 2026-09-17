---
title: The Illustrated Stable Diffusion
date: 2022-10-04
categories:
  - stable-diffusion
  - diffusion-models
  - machine-learning
  - explainer
  - image-generation
description: Jay Alammar's visual explainer of how Stable Diffusion works under the hood — covering latent diffusion, the CLIP text encoder, and the U-Net denoiser. Alammar's illustrated series is one of the best entry points for building intuition about complex ML architectures.
params:
  source: pinboard
  sourceUrl: https://jalammar.github.io/illustrated-stable-diffusion/
---

## Summary

[Jay Alammar](/notes/jay-alammar/)'s illustrated explainer of Stable Diffusion — part of his long-running series that makes deep learning architectures visually comprehensible. The post walks through all the components that make up a Stable Diffusion image generation pipeline: the CLIP text encoder that converts your prompt to a vector, the latent diffusion space where the denoising happens, and the U-Net that does the actual denoising work.

The key insight Alammar surfaces is that Stable Diffusion doesn't operate in pixel space — it operates in a compressed latent space produced by a VAE (variational autoencoder). This is what makes it computationally tractable: the U-Net denoises a much smaller representation (64×64 latents rather than 512×512 pixels), and the VAE decoder expands it at the end. The latent diffusion approach is what separates Stable Diffusion architecturally from DALL-E 2, which at the time operated in pixel space.

The diffusion model process itself: start from pure Gaussian noise, then iteratively denoise guided by the text embedding. Classifier-free guidance (CFG) is what makes the text conditioning strong — the model generates both a conditioned and unconditioned sample, then steers toward the conditioned result. Higher CFG scales push more strongly toward the text prompt but sacrifice diversity.

## Key points

- Stable Diffusion runs in latent space via a VAE — computationally cheaper than pixel-space diffusion.
- The CLIP text encoder produces the conditioning signal from your prompt.
- U-Net performs denoising at each step, conditioned on the text embedding via cross-attention.
- Classifier-free guidance (CFG) controls text adherence vs. image diversity trade-off.
- Stable Diffusion was released open-source by Stability AI in August 2022 — the open release is what made the model proliferate.
- Part of [Jay Alammar](/notes/jay-alammar/)'s illustrated series that also covers Transformers, BERT, and GPT.

[Original](https://jalammar.github.io/illustrated-stable-diffusion/) → GitHub
