---
title: "CS231n: Convolutional Neural Networks for Visual Recognition"
date: 2021-01-25
categories:
  - machine-learning
  - deep-learning
  - computer-vision
  - education
  - stanford
  - courses
description: "Stanford CS231n: Convolutional Neural Networks for Visual Recognition — Andrej Karpathy's course that became the de facto entry point into deep learning for computer vision. The lecture notes remain among the best written explanations of CNNs, backprop, and training practice."
params:
  source: pinboard
  sourceUrl: https://cs231n.github.io/
---

## Summary

CS231n is Stanford's course on deep learning for computer vision, originally developed by Andrej Karpathy and Fei-Fei Li. The course notes, hosted publicly, became the gold standard reference for understanding convolutional neural networks. They cover the full stack: image classification, backpropagation derivation, batch normalization, dropout, regularization, transfer learning, and object detection architectures like YOLO and Faster R-CNN.

What makes CS231n stand out is the quality of writing. The backpropagation notes, for instance, explain the chain rule not as abstract calculus but as a computational graph where gradients flow backward through nodes — a framing that makes implementation feel natural rather than mysterious. The assignment sets (image classification from scratch, building a two-layer net, training a CNN on CIFAR-10) have been used by thousands of practitioners to build genuine intuition.

The course was designed around ImageNet and image classification, which explains its emphasis on CNN architectures. Though the field has since shifted toward transformer-based vision models (ViT, CLIP), the CNN fundamentals taught here remain essential for understanding residual networks, feature maps, and why spatial structure matters. Many practitioners who learned deep learning through CS231n went on to take [fast.ai](/notes/fastai/) or read deep learning papers independently.

## Key points

- Covers CNN fundamentals: convolution, pooling, receptive field, stride, and the architectural intuitions behind AlexNet, VGG, ResNet, Inception.
- The backpropagation notes are widely considered the clearest written explanation of gradient flow in computational graphs.
- Includes treatment of optimization methods: SGD, momentum, Adam, learning rate schedules.
- Transfer learning section explains how to reuse ImageNet-pretrained features for new tasks — still one of the most practical techniques in applied ML.
- Originally by Andrej Karpathy; co-taught with Justin Johnson and Serena Yeung in later editions.

[Original](https://cs231n.github.io/) → GitHub
