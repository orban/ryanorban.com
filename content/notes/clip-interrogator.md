---
title: CLIP Interrogator
date: 2022-09-05
categories:
  - clip
  - stable-diffusion
  - prompt-engineering
  - image-generation
  - tools
description: CLIP Interrogator by pharmapsychotic is a Google Colab tool that reverse-engineers what prompt would produce a given image — using CLIP to describe an image in terms that Stable Diffusion understands. The go-to tool in 2022 for figuring out how to replicate an image style.
params:
  source: pinboard
  sourceUrl: https://colab.research.google.com/github/pharmapsychotic/clip-interrogator/blob/main/clip_interrogator.ipynb
---

## Summary

[CLIP Interrogator](/notes/clip-interrogator/) by pharmapsychotic is a tool that analyzes an input image and produces a text prompt that would generate a similar image in Stable Diffusion. It works by using CLIP (Contrastive Language-Image Pretraining, the text-image model from OpenAI that powers Stable Diffusion's text conditioning) to compare the image against a large database of known artists, styles, movements, and modifiers, selecting the combination that best matches the image's visual characteristics.

The output is typically something like: "portrait of a woman by Greg Rutkowski, octane render, artstation, intricate details, 8k" — a structured concatenation of artist names, rendering keywords, and quality modifiers that the Stable Diffusion community had empirically found to improve results. [CLIP Interrogator](/notes/clip-interrogator/) automated the process of identifying which combination of these terms best characterized an image, making it easier to replicate or riff on a style.

pharmapsychotic was a prominent figure in the early Stable Diffusion community, maintaining a well-known list of artist names and style modifiers that worked well with CLIP-conditioned generation. [CLIP Interrogator](/notes/clip-interrogator/) became one of the most-used tools in the image generation workflow: generate an image you like (or find one online), run it through [CLIP Interrogator](/notes/clip-interrogator/), get a prompt, and use that prompt as a starting point for variations. It ran as a Google Colab notebook to avoid local GPU requirements.

## Key points

- Reverse-engineers a text prompt from an image using CLIP embeddings and a curated style database.
- Compares image against artist names, styles, and quality modifiers; outputs the best-matching prompt combination.
- Built on CLIP — same text-image model used as conditioning in Stable Diffusion.
- Made by pharmapsychotic, a prominent Stable Diffusion community figure; ran as a Google Colab notebook.
- Primary use: replicating or riffing on a style found in an existing image.
- Embodies the 2022 prompt engineering culture: empirical keyword lists, artist names as style tokens.

[Original](https://colab.research.google.com/github/pharmapsychotic/clip-interrogator/blob/main/clip_interrogator.ipynb) → GitHub
