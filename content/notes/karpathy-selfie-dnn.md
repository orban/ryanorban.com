---
title: What a Deep Neural Network Thinks About Your Selfie
date: 2015-11-03
categories:
  - deep-learning
  - computer-vision
  - neural-networks
  - convolutional-networks
  - social-media
description: Andrej Karpathy trained a VGGNet on 2 million Instagram selfies to learn what makes a selfie 'good' — using likes-per-follower as the quality signal. Beyond the entertainment value, it's a sharp demonstration of how supervised learning can proxy for human aesthetic judgment at scale.
params:
  source: pinboard
  sourceUrl: http://karpathy.github.io/2015/10/25/selfie/
---

## Summary

Andrej Karpathy built a convolutional neural network (specifically VGGNet, with 140 million parameters) to classify selfies as "good" or bad. The training signal was likes-per-follower on Instagram — a noisy but scalable proxy for human aesthetic preference. The dataset: ~5 million images tagged #selfie, filtered to 2 million with detected faces, then split into 1 million positive and 1 million negative examples based on engagement.

The technical approach is straightforward: transfer learning wasn't used — VGGNet was trained from scratch on the selfie task. The network learned to detect visual patterns that correlated with engagement, rather than being told what to look for. This is classic supervised learning applied to a subjective aesthetic task, and the fact that it works at all is the interesting result.

What the network learned: female subjects ranked higher, faces filling roughly one-third of the frame, slightly tilted with forehead cropping, longer hair, oversaturation or black-and-white filters, and visible borders. Poor lighting and overly close framing hurt scores. The key insight is that *style* — not raw attractiveness — explained most of the variance. This connects to deeper questions about what computer vision models actually learn: are they encoding aesthetics, or just encoding cultural norms present in the training data?

## Key points

- Trained VGGNet (140M parameters) from scratch on 2M selfie images labeled by likes-per-follower.
- Engagement metrics as weak supervision — a scalable, if noisy, label source.
- Network learned style signals (filter, framing, lighting) over raw attractiveness.
- Female subjects consistently ranked higher — raises questions about training data bias.
- By Andrej Karpathy at Stanford (before his Tesla AI and OpenAI roles) — part of his run of sharp blog posts on applied deep learning.
- One of the early examples of using social media engagement as a training signal, a pattern now central to RLHF and content recommendation.

[Original](http://karpathy.github.io/2015/10/25/selfie/) → GitHub
