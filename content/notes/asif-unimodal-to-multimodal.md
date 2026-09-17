---
title: "ASIF: Coupled Data Turns Unimodal Models to Multimodal Without Training"
date: 2022-10-05
categories:
  - multimodal
  - zero-shot
  - representation-learning
  - contrastive-learning
  - research
description: Norelli, Fumero, Maiorca, Rodolà et al. (Sapienza University, arXiv:2210.01738, 2022) show that any two unimodal models can be composed into a zero-shot multimodal system by finding approximate shared nearest neighbors across their embedding spaces, given only a small set of coupled pairs. The result challenges the assumption that multimodal capability requires joint training.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/2210.01738.pdf
---

## Summary

Norelli, Fumero, Maiorca, Rodolà and colleagues (Sapienza University, arXiv:2210.01738, 2022) introduce ASIF (Approximate Shared Information Finder), a method for composing two pretrained unimodal models into a zero-shot multimodal system without any joint training. The key insight is that any two independently trained encoders — a text encoder and an image encoder, for instance — produce embedding spaces that are approximately compatible given a small set of coupled pairs (image-caption pairs that bridge the modalities).

ASIF works by identifying approximate nearest neighbors across the two embedding spaces using the coupled anchor pairs as a bridge. Given a query in one modality, it finds the nearest anchors in that modality's space, then retrieves the corresponding anchors in the other modality's space, and returns their neighbors as the cross-modal matches. This is a non-parametric retrieval approach — no new parameters are trained, and the unimodal models are entirely frozen. The approach scales with the number of coupled pairs: more anchors yield better cross-modal alignment.

The paper demonstrates zero-shot image-text retrieval competitive with CLIP — a model trained end-to-end on hundreds of millions of image-text pairs — despite using no multimodal training at all. This is a striking result because it suggests that unimodal representation spaces trained independently on different data can share sufficient geometric structure for cross-modal retrieval via nearest-neighbor bridging. The connection to broader work on contrastive learning and multimodal learning is clear: CLIP's joint training is one way to achieve cross-modal alignment, but ASIF shows it isn't the only way. The result also echoes findings from research on representational similarity across independently trained networks.

## Key points

- Any two pretrained unimodal encoders can be composed into a zero-shot multimodal retrieval system using only a small set of coupled anchor pairs
- Zero-shot image-text retrieval competitive with CLIP without any joint multimodal training
- Non-parametric: uses approximate nearest neighbors across embedding spaces, no new parameters trained
- Implies that independently trained representation learning models share enough geometric structure for cross-modal bridging
- Connects to work on multimodal learning, zero-shot learning, and the geometry of learned embedding spaces

[Source](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/2210.01738.pdf)
