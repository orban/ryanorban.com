---
title: "An Image is Worth One Word: Personalizing Text-to-Image Generation Using Textual Inversion"
date: 2022-11-08
categories:
  - generative-ai
  - text-to-image
  - diffusion-models
  - personalization
  - research
description: Tel Aviv University and NVIDIA paper introducing Textual Inversion — learning a single new text embedding token that represents a user-provided concept, enabling that concept to be composed into any text prompt. Showed that the embedding space of text-to-image models is richly structured and can be expanded with just 3-5 example images.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/2208.01618.pdf
---

## Summary

Rinon Gal, Yuval Alaluf, Yuval Atzmon, Or Patashnik, Amit Bermano, Gal Chechik, and Daniel Cohen-Or at Tel Aviv University and NVIDIA propose Textual Inversion — a method for personalizing text-to-image generation by learning a new pseudo-word embedding that represents a user-provided concept. Given 3–5 images of an object or style, the method optimizes a single new text token (like `S*`) in the text encoder's embedding space so that the model, when prompted with that token, generates images containing that concept.

The key insight is that large text-to-image models (specifically Stable Diffusion and related latent diffusion models) have learned a rich semantic embedding space where concepts can be composed freely via text. Rather than fine-tuning the entire model (expensive and prone to catastrophic forgetting), Textual Inversion only updates one new embedding vector. This vector can then be combined with any existing text description: "a painting of S* in the style of Van Gogh or S* sitting on a beach at sunset."

The method demonstrated that personalization in generative models doesn't require retraining — the model already contains the compositional machinery, and you just need to locate the right point in embedding space. This opened a large research area: subsequent methods like DreamBooth (fine-tuning the full model for better fidelity) and LoRA-based personalization built on this insight, and the Stable Diffusion community embraced word embeddings as the most lightweight personalization primitive.

## Key points

- Textual Inversion: learn one new embedding token from 3-5 images, usable in any text prompt without model fine-tuning
- Exploits the compositionality of text encoder embedding space — the model can already compose concepts, you just need to inject a new one
- Only updates ~768 floats (one embedding vector) — extremely parameter-efficient personalization
- Enables concept placement into novel contexts: style transfer, attribute modification, scene composition
- Foundational for the Stable Diffusion custom embedding ecosystem — directly used in AUTOMATIC1111 and similar
- Preceded by DreamBooth (same period) — that method fine-tunes the full model; Textual Inversion is lighter but less faithful

[Original (arXiv 2208.01618)](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/2208.01618.pdf)
