---
title: "Deep Daze: Text to Image with CLIP and Siren"
date: 2021-03-29
categories:
  - generative-ai
  - clip
  - text-to-image
  - machine-learning
  - open-source
description: Deep Daze is Phil Wang's early text-to-image tool combining OpenAI's CLIP with Siren (implicit neural representations) — one of the first accessible open-source implementations of text-guided image generation, predating DALL-E and Stable Diffusion by over a year.
params:
  source: pinboard
  sourceUrl: https://github.com/lucidrains/deep-daze
---

## Summary

Deep Daze is an early text-to-image generation tool by Phil Wang (lucidrains), combining OpenAI's CLIP model with Siren (Sinusoidal Representation Networks — a type of implicit neural representation that represents images as continuous functions rather than pixel grids). It was one of the first accessible command-line tools for generating images from text descriptions, appearing in early 2021.

The mechanism: CLIP is a multimodal model trained to align text and image embeddings — it can score how well an image matches a text prompt. Siren provides a differentiable image generator. Deep Daze optimizes the Siren network via gradient descent to produce an image that CLIP scores highly for the given text description. No dataset, no diffusion process — just optimization against CLIP's cross-modal embedding space.

This approach predates DALL-E 2, Stable Diffusion, and Midjourney by over a year. At the time, it was remarkable that a text prompt could produce coherent (if dreamlike and blurry) imagery at all. Phil Wang's GitHub (lucidrains) became a hub for early implementations of these techniques — he also published early versions of DALL-E recreation attempts, Imagen reproductions, and Perceiver implementations. Deep Daze is now mostly of historical interest, superseded by diffusion-based models with far better image quality.

## Key points

- Combines CLIP (text-image alignment) with Siren (implicit neural representation) for text-to-image.
- Optimization-based, not generative: gradient descent on a neural image to maximize CLIP score for a text prompt.
- Early 2021 — predates DALL-E 2, Stable Diffusion, and Midjourney by 12-18 months.
- By Phil Wang (lucidrains) — prolific open-source ML researcher who reproduced many early generative models.
- Now superseded; historical interest as a step in the evolution of text-to-image generation.

[Original](https://github.com/lucidrains/deep-daze)
