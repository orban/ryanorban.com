---
title: "Flamingo: A Visual Language Model for Few-Shot Learning"
date: 2022-05-09
categories:
  - vision-language
  - multimodal
  - few-shot-learning
  - deepmind
  - language-models
description: DeepMind's Flamingo (2022) bridges a frozen vision encoder and a frozen large language model with cross-attention layers, enabling powerful few-shot vision-language capabilities without retraining either component. It set new few-shot records on image captioning and VQA benchmarks by treating visual inputs as just another type of context for an LM.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/flamingo.pdf
---

## Summary

Jean-Baptiste Alayrac, Jeff Donahue, Pauline Luc, Antoine Miech, Iain Barr, Yana Hasson, Karel Lenc, and colleagues at DeepMind introduce Flamingo, a family of Visual Language Models (VLMs) that achieve strong few-shot performance on vision-language tasks by efficiently bridging a frozen vision encoder with a frozen large language model through lightweight cross-attention layers. The core insight is that separately pre-trained vision and language experts can be kept frozen — protecting their learned representations — while only the connecting layers are trained on interleaved image-text data.

The architecture has three key components. First, a frozen Normalizer-Free ResNet (NFNet) vision encoder processes images into visual features. Second, a Perceiver Resampler compresses the variable-length visual features into a fixed number of visual tokens (64), making the interface to the LM computationally feasible. Third, cross-attention layers are interleaved into the layers of a frozen Chinchilla-scale autoregressive language model, letting the LM attend to visual tokens at every text generation step. These cross-attention layers are the only components trained during Flamingo training.

The training data consists of interleaved sequences of images and text scraped from the web, plus curated image-text pairs and video-text pairs. This interleaved format allows Flamingo to be prompted with few-shot examples: "here's image 1, here's a caption; here's image 2, here's a caption; now describe image 3." This few-shot prompting achieves state-of-the-art results on captioning and Visual Question Answering (VQA) benchmarks including COCO, VQAv2, and OK-VQA. The Flamingo-80B model sets new records across most benchmarks, demonstrating that the frozen-components approach scales well. This architecture directly influenced BLIP-2 and other subsequent multimodal models.

## Key points

- Frozen vision encoder + frozen LM + learned cross-attention: Flamingo avoids catastrophic forgetting of either encoder by never updating their weights.
- Perceiver Resampler compresses variable-length image features to a fixed 64-token visual representation — crucial for keeping the interface to the LM tractable.
- Interleaved image-text training data enables in-context few-shot vision-language prompting — treating image understanding as a few-shot learning problem.
- Sets new records on captioning (COCO), VQA (VQAv2, OK-VQA), and video QA benchmarks with only 4-32 in-context examples, often matching fine-tuned models.
- Directly influenced BLIP-2's Q-Former approach and established the template for modular multimodal architectures that preserve frozen pre-trained experts.

[Original PDF](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/flamingo.pdf)
