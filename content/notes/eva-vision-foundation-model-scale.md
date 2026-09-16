---
title: "EVA: Exploring the Limits of Masked Visual Representation Learning at Scale"
date: 2022-11-14
categories:
  - vision
  - foundation-models
  - deep-learning
  - clip
  - masked-image-modeling
description: EVA is a 1-billion-parameter vision foundation model from BAAI that achieves state-of-the-art on image classification, detection, and segmentation by pretraining a ViT to reconstruct masked CLIP features. Initializing CLIP's vision tower from EVA dramatically stabilizes training — an important practical finding for building large multimodal systems.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/2211.07636.pdf
---

## Summary

EVA (Explore the limits of Visual representation At scale) from the Beijing Academy of Artificial Intelligence is a 1-billion-parameter Vision Transformer (ViT) pretrained through a novel masked image modeling (MIM) objective: reconstructing CLIP image-text aligned features from visible patches. Rather than predicting raw pixel values (as in MAE) or discrete tokens, EVA predicts the CLIP feature space — which encodes both visual and semantic information.

The model sets new records on image classification, video action recognition, object detection, instance segmentation, and semantic segmentation — all without heavy supervised pretraining. A particularly notable finding: EVA exhibits qualitative performance jumps as it scales that aren't seen in other models. On LVIS large-vocabulary instance segmentation (1000+ categories), EVA nearly matches COCO performance despite the massive category count difference — suggesting scale and the right pretraining objective unlock generalization that smaller models don't exhibit.

Beyond standalone vision tasks, EVA demonstrates that initializing the vision tower of a giant CLIP model from EVA rather than random weights stabilizes training and requires fewer samples. This is a practical finding with real implications for anyone building large multimodal models — cold-starting the vision encoder from a strong visual foundation significantly reduces training cost.

## Key points

- 1B parameter ViT pretrained to predict masked CLIP features (not pixels) — the pretraining target encodes semantic alignment from CLIP.
- Sets SOTA on image classification, video, detection, segmentation using only 30M public images with 150 training epochs.
- Qualitative scaling behavior: EVA shows emergent generalization on LVIS that smaller models don't exhibit.
- Initializing CLIP vision towers from EVA stabilizes training and outperforms random initialization with much less data and compute.
- Released with full code and model weights; code at GitHub.com/baaivision/EVA.

[Original paper](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/2211.07636.pdf)
