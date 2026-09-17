---
title: Craiyon (formerly DALL-E mini)
date: 2022-08-11
categories:
  - generative-ai
  - text-to-image
  - dall-e
  - open-source
  - image-generation
description: Craiyon, formerly DALL-E mini, is a free web-based text-to-image generator that went viral before Stable Diffusion's release. It gave millions their first hands-on experience with AI image generation, despite producing lower-quality images than commercial alternatives.
params:
  source: pinboard
  sourceUrl: https://www.craiyon.com/
---

![Craiyon (formerly DALL-E mini)](/images/notes/craiyon.png)

## Summary

[Craiyon](/notes/craiyon/), originally released as DALL-E mini by Boris Dayma as a side project, is a free web interface for a smaller text-to-image model trained on public data. It went viral in mid-2022 — months before Stable Diffusion — giving millions of people their first experience with AI-generated images from text prompts. The original name referenced DALL-E 2 but wasn't affiliated with OpenAI, which eventually prompted the rename to [Craiyon](/notes/craiyon/).

The model quality was limited compared to DALL-E 2 or Midjourney — images were blurry, had distorted faces, and DALL-E mini hands became a meme. But the product was frictionless and free: anyone with a browser could type a prompt and get nine image variations in seconds. This viral simplicity made [Craiyon](/notes/craiyon/) the public's introduction to generative AI image synthesis, seeding the cultural moment that Stable Diffusion would later capitalize on with open-source weights.

The architecture combines a BART-based model for learning associations between text and image patches with VQGAN for generating images. It's smaller and less capable than the models it references, but its public accessibility made it significant as a cultural artifact of the early text-to-image era.

## Key points

- Free, browser-based text-to-image generator that went viral before Stable Diffusion's open release.
- Originally named "DALL-E mini" — not affiliated with OpenAI; renamed [Craiyon](/notes/craiyon/) after pushback.
- Uses BART + VQGAN architecture; lower quality than DALL-E 2 but freely accessible.
- "DALL-E mini hands" became a meme — a cultural marker of early AI image generation artifacts.
- Seeded public familiarity with prompt engineering for images before open-source models existed.
- Created by Boris Dayma as an open-source project hosted on Hugging Face.

[Original](https://www.craiyon.com/)
