---
title: Deep Learning Systems (CMU 10-414/714)
date: 2024-11-13
categories:
  - machine-learning
  - deep-learning
  - courses
  - systems
  - education
  - cmu
description: "10-414/714: Deep Learning Systems at CMU — a publicly available course on building the components of a deep learning framework from scratch, including automatic differentiation, optimization, and hardware acceleration. One of the best resources for understanding how frameworks like PyTorch actually work."
params:
  source: pinboard
  sourceUrl: https://dlsyscourse.org/lectures/
---

![Deep Learning Systems (CMU 10-414/714)](/images/notes/deep-learning-systems-cmu.png)

## Summary

10-414/714: Deep Learning Systems is a publicly available CMU course that teaches students to build the components of a deep learning framework from scratch — automatic differentiation, neural network layers, optimization algorithms, and hardware acceleration. The lecture videos, slides, and assignments are all freely available at dlsyscourse.org.

The course fills a critical gap between "use PyTorch" and "understand PyTorch." Most deep learning education teaches you to use existing frameworks; this course teaches you how those frameworks are built. By implementing autodiff, you understand what gradients actually are at the computation graph level. By implementing a GPU kernel, you understand why certain operations are fast or slow.

Instructors Tianqi Chen (creator of TVM and XGBoost) and Zico Kolter bring systems and ML expertise respectively. The course covers: numpy-style operations from scratch, automatic differentiation via computation graphs, backpropagation implementation, convolutional neural networks, recurrent neural networks, and how to write code that runs efficiently on GPUs.

## Key points

- Build a deep learning framework from scratch — autodiff, layers, optimizers, GPU kernels.
- Free: lectures, slides, and assignments available at dlsyscourse.org.
- Teaches *how* PyTorch/TensorFlow work, not just how to use them.
- Instructors: Tianqi Chen (TVM, XGBoost) and Zico Kolter.
- Essential for anyone who wants to work on ML infrastructure rather than just apply models.

[Original](https://dlsyscourse.org/lectures/)
