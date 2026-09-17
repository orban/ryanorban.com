---
title: "Image as a Foreign Language: BEIT-3 Pretraining for All Vision and Vision-Language Tasks"
date: 2022-09-08
categories:
  - multimodal
  - vision-language
  - pretraining
  - microsoft
  - research
description: Wang, Bao, Dong et al. at Microsoft introduce BEIT-3, a general-purpose multimodal foundation model that treats images as a 'foreign language' and applies masked language modeling uniformly across images, text, and image-text pairs. BEIT-3 achieves state-of-the-art across seven vision and vision-language benchmarks including COCO, ImageNet, VQA, and NLVR2.
params:
  source: papers
  sourceUrl: https://arxiv.org/abs/2208.10442
---

## Summary

Wenhui Wang, Hangbo Bao, Li Dong, Johan Bjorck, Zhiliang Peng, Furu Wei, and colleagues at Microsoft (arXiv:2208.10442, Aug 2022) introduce BEIT-3, a general-purpose multimodal foundation model built around a single unifying pretraining objective. The key conceptual move is to treat images as a foreign language (Imglish) and apply masked language modeling uniformly across images, text, and image-text pairs — the same training procedure, the same architecture, three modalities.

The architecture uses **Multiway Transformers**: a shared backbone with modality-specific expert layers, enabling both deep fusion (shared computation across modalities) and modality-specific encoding. This avoids the common design choice between full parameter sharing (which forces the model to handle all modalities with one representation) and separate encoders (which prevents cross-modal knowledge transfer). The pretraining data includes large-scale image-only, text-only, and paired image-text corpora, with masking applied independently to each modality.

BEIT-3 achieves state-of-the-art performance across seven diverse benchmarks: COCO object detection, ADE20K semantic segmentation, ImageNet classification, NLVR2 visual reasoning, VQAv2 visual question answering, COCO image captioning, and Flickr30K cross-modal retrieval. The improvements are consistent and meaningful — +5.6% on NLVR2, +1.7% on VQAv2, +2.3% CIDEr on image captioning. The paper demonstrates that the vision-language convergence story is empirically real: a single pretraining recipe and architecture can achieve state-of-the-art across tasks that previously required specialized models for each domain.

## Key points

- Treats images as a "foreign language" (Imglish): applies masked language modeling to all three data types (images, text, image-text pairs) with the same objective
- **Multiway Transformers**: shared backbone + modality-specific expert layers enables deep fusion without forcing full parameter sharing
- State-of-the-art on 7 benchmarks: COCO, ADE20K, ImageNet, NLVR2, VQAv2, image captioning, retrieval
- A single foundation model that outperforms specialized models on diverse vision and vision-language tasks
- Empirical validation of the big convergence thesis: language modeling objectives work across modalities

[Original](https://arxiv.org/abs/2208.10442)
