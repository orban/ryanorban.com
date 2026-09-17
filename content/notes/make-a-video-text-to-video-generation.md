---
title: "Make-A-Video: Text-to-Video Generation without Text-Video Data"
date: 2022-09-29
categories:
  - video-generation
  - text-to-video
  - diffusion
  - computer-vision
  - research
description: Singer et al. (Meta AI, 2022) introduce Make-A-Video, a text-to-video generation system that learns spatiotemporal motion from unlabeled video while keeping semantic knowledge from paired image-text data. It sidesteps the absence of large-scale video-caption datasets by decoupling what to generate from how things move.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/Make-A-Video.pdf
---

## Summary

Uriel Singer, Adam Polyak, and the Meta AI team present Make-A-Video — a system for generating short video clips from text prompts, trained without paired text-video data. The key insight is a clever decomposition of the problem: the model learns *what the world looks like* from large-scale text-image pairs (where paired data is abundant), then separately learns *how things move* from unlabeled video footage. This avoids the fundamental data bottleneck that had stalled text-to-video generation research: video paired with captions is expensive to collect at scale, but raw video and image-caption datasets exist in enormous quantities.

The architecture extends a pre-trained text-to-image diffusion model (based on DALL-E 2-style hierarchical generation with CLIP embeddings) by inserting temporal attention layers and temporal convolutional layers into the U-Net backbone. The spatial layers stay frozen from the image model; only temporal layers are trained on video. A spatiotemporal decoder and frame interpolation network round out the pipeline. The model can generate 16 frames at 300×300 resolution and interpolate to 76 frames at 768×768 resolution.

Make-A-Video produced qualitatively impressive results when released in September 2022, generating coherent motion for prompts like "a teddy bear painting a portrait or a dog playing in a field." It also supports one-shot variation (take an image, generate related video) and video variation (take a video, generate a stylistically similar one). The decoupled training approach proved highly influential: contemporaneous papers like Imagen Video and Phenaki followed similar paradigms, and the idea of learning motion from video while learning semantics from image-text has become standard in the field.

## Key points

- Text-to-video generation without paired video-caption data — separates semantic learning (from image-text pairs) from temporal/motion learning (from unlabeled video).
- Architecture: pre-trained text-to-image diffusion model extended with temporal attention + temporal convolutional layers; spatial weights frozen from image model.
- CLIP text embeddings drive the semantic content; temporal layers trained on raw video learn motion dynamics.
- Generates 16-76 frames at up to 768×768 resolution using frame interpolation post-processing.
- Also supports image-to-video variation and video-to-video stylization from a single example.
- Concurrent with Imagen Video (Google) and Phenaki (Google); established the decoupled training paradigm for video generation.

[Original PDF](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/Make-A-Video.pdf)
