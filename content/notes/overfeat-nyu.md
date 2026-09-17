---
title: "OverFeat: Integrated Recognition, Localization, and Detection"
date: 2014-01-05
categories:
  - deep-learning
  - computer-vision
  - object-recognition
  - convolutional-networks
  - nyu
description: OverFeat is NYU CILVR lab's deep learning framework for object recognition, localization, and detection using convolutional networks — won the ImageNet 2013 localization task. An important 2014 artifact of Yann LeCun's group.
params:
  source: pinboard
  sourceUrl: http://cilvr.nyu.edu/doku.php?id=software:overfeat:start
---

## Summary

OverFeat is a deep learning framework from Yann LeCun's CILVR Lab at NYU (Computational Intelligence, Learning, Vision, and Robotics) for object recognition, localization, and detection using convolutional neural networks. It won the ImageNet 2013 localization competition. The key contribution was showing that a single CNN trained for classification could be repurposed for localization and detection by applying it at multiple scales with a sliding window approach.

The framework used Torch (then NYU's preferred deep learning framework before PyTorch existed) and provided pre-trained models that others could use without training from scratch — still a significant barrier in 2014 given GPU requirements.

## Key points

- Won ImageNet LSVRC 2013 localization task — an early demonstration that the same CNN backbone could handle classification, localization, and detection
- Multiscale sliding window: applies the network at multiple image scales and aggregates predictions — the predecessor of modern feature pyramid approaches
- Pre-trained model release was significant: allowed the community to do transfer learning without training from scratch on ImageNet
- Used Torch as the framework — Yann LeCun and CILVR were advocates for Torch/Lua before PyTorch superseded it
- The OverFeat approach was quickly superseded by R-CNN (Girshick et al., 2014) but was an important stepping stone in object detection methodology

[Original](http://cilvr.nyu.edu/doku.php?id=software:overfeat:start)
