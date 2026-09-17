---
title: A Visual Guide to Vision Transformers
date: 2024-04-16
categories:
  - deep-learning
  - vision
  - transformers
  - education
  - computer-vision
description: A visual guide to Vision Transformers (ViT) — explains how the transformer architecture is adapted for images, covering patch embeddings, position encodings, and attention in visual domains with diagrams. Good complement to the original ViT paper for building intuition.
params:
  source: pinboard
  sourceUrl: https://blog.mdturp.ch/posts/2024-04-05-visual_guide_to_vision_transformer.html
---

![A Visual Guide to Vision Transformers](/images/notes/visual-guide-vision-transformers.png)

## Summary

Vision Transformers (ViT) adapt the transformer architecture — designed for sequential text tokens — to image data. The key challenge is that images don't have a natural token sequence. The solution ViT uses: divide the image into fixed-size patches, flatten each patch into a vector, and treat those patch vectors as tokens. From there, standard self-attention mechanisms apply, with position encodings tracking where in the image each patch came from.

This visual guide explains the adaptation step-by-step with diagrams — patch embedding (turning 16×16 pixel patches into 768-dimensional vectors), position encoding (appended so the model knows spatial layout), and the CLS token (a learnable token prepended to the sequence, whose output representation is used for classification). The guide makes the "attend to all other patches at once" property concrete: each patch can directly attend to any other patch in the image, unlike CNNs which process local neighborhoods.

ViT has become foundational to modern computer vision — CLIP, DINO, SAM, and most vision-language models use transformer-based image encoders. Understanding the ViT architecture is now a prerequisite for reading current computer vision research. This guide targets someone who already understands self-attention in the text domain and needs to map that understanding to images.

## Key points

- ViT treats image patches as tokens — each 16×16 region becomes a fixed-size vector input to a standard transformer.
- Position encoding preserves spatial information; CLS token accumulates global representation for classification head.
- Each patch attends to all others simultaneously — unlike CNNs which process local neighborhoods.
- Underpins modern vision models: CLIP, DINO, SAM, vision-language models.
- Prerequisite knowledge: self-attention mechanics in the text domain.

[Original](https://blog.mdturp.ch/posts/2024-04-05-visual_guide_to_vision_transformer.html)
