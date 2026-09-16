---
title: Generative Pretraining from Pixels (iGPT)
date: 2020-06-01
categories:
  - deep-learning
  - vision
  - self-supervised-learning
  - transformers
  - generative-models
description: The iGPT paper from OpenAI (ICML 2020) showing that a GPT-2-scale transformer trained to autoregressively predict pixels learns strong image representations — 96.3% accuracy on CIFAR-10 with a linear probe. It's a direct transposition of NLP pretraining ideas to the image domain, predating CLIP and DALL-E.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/chen20s.pdf
---

## Summary

Mark Chen, Alec Radford, Rewon Child, Jeff Wu, Heewoo Jun, David Luan, and Ilya Sutskever from OpenAI ask a direct question: can the same self-supervised pretraining approach that works for language work for images? The answer is yes. They train a GPT-2-scale sequence transformer to autoregressively predict pixels — left to right, top to bottom — without encoding any 2D spatial structure. The resulting model, iGPT, learns strong visual representations measurable by linear probing and fine-tuning.

The results are compelling: 96.3% accuracy on CIFAR-10 with a linear probe (beating a supervised Wide ResNet), 99.0% with fine-tuning, and competitive self-supervised benchmarks on ImageNet using VQVAE encoding. This was published at ICML 2020, before CLIP and Vision Transformer (ViT) arrived and shifted the field toward contrastive and masked image modeling approaches. iGPT is the pixel-prediction branch of that tree.

The paper is historically significant for demonstrating that generative pretraining — the GPT paradigm — generalizes beyond text. It predates DALL-E and image generation approaches that explicitly use autoregressive pixel prediction, and anticipates the now-standard recipe of "pretrain on unlabeled data, fine-tune on downstream tasks" applied to vision.

## Key points

- A GPT-2-scale transformer trained to predict the next pixel achieves CIFAR-10 linear probe accuracy of 96.3%, outperforming supervised baselines.
- Training operates on raw pixel sequences; no spatial structure (e.g., 2D convolution, positional encodings tied to patches) is used.
- Substituting VQVAE encodings for raw pixels on ImageNet achieves 69% top-1 accuracy — competitive with self-supervised learning methods of the era.
- Bridges NLP language modeling and visual representation learning, generalizing the GPT pretraining idea to images.
- Work predates ViT, MAE, and CLIP — the later approaches that dominated vision SSL; iGPT is the alternative road not taken.

[Original paper](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/chen20s.pdf)
