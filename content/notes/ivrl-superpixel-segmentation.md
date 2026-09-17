---
title: Superpixel Segmentation — IVRL
date: 2017-08-11
categories:
  - computer-vision
  - image-processing
  - machine-learning
  - research
  - epfl
description: The IVRL lab at EPFL's research page on superpixel segmentation — home of the SLIC algorithm, which became the dominant superpixel method due to its speed and perceptual uniformity. Superpixels are a fundamental preprocessing step in classical computer vision pipelines.
params:
  source: pinboard
  sourceUrl: http://ivrl.epfl.ch/research/superpixels
---

## Summary

The Image and Visual Representation Lab (IVRL) at EPFL in Lausanne, Switzerland, produced some of the most widely used algorithms in classical computer vision, particularly in image segmentation. Their superpixel research page is the home of SLIC (Simple Linear Iterative Clustering), introduced by Radhakrishna Achanta and colleagues in a 2012 paper that became one of the most-cited works in computer vision.

Superpixels are small, perceptually coherent regions of an image — groups of pixels that share similar color and spatial proximity. Rather than operating on individual pixels (which is slow and ignores local structure), many computer vision algorithms first over-segment an image into ~100-1000 superpixels, then operate on those compact regions. This dramatically reduces computational complexity while preserving the image's perceptual structure. Superpixels are used as building blocks in semantic segmentation, object detection, saliency maps, and graph-based image analysis.

SLIC generates superpixels using a modified k-means clustering in a 5-dimensional space: CIELAB color (3 channels) + spatial coordinates (x, y). The number of clusters k controls the number of superpixels. The algorithm is fast because it restricts each pixel's candidate cluster centers to a local search window, making it O(n) rather than O(nk). By 2017, SLIC had become the default superpixel algorithm in practice. The IVRL page also documented earlier methods (SLIC's predecessors like Turbopixels, Quickshift, and FH segments) and comparisons.

## Key points

- SLIC (Simple Linear Iterative Clustering): k-means in 5D CIELAB+spatial space, restricted to local search windows — O(n), fast and perceptually uniform.
- Superpixels reduce pixel-level computation to region-level computation while preserving perceptual boundaries.
- IVRL at EPFL — Swiss research group led by Sabine Süsstrunk, producing foundational color science and image processing research.
- SLIC is used as a preprocessing step in semantic segmentation, saliency detection, and many graph-based computer vision methods.
- By 2018-2019, deep learning end-to-end segmentation methods (like Mask R-CNN) had largely displaced superpixel-based pipelines for high-accuracy tasks, though superpixels remain useful for edge cases requiring interpretable intermediate representations.

[Original](http://ivrl.epfl.ch/research/superpixels)
