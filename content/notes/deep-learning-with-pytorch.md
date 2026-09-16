---
title: Deep Learning with PyTorch
date: 2022-04-05
categories:
  - deep-learning
  - pytorch
  - textbook
  - neural-networks
  - machine-learning
description: Manning's 2020 practical guide to deep learning with PyTorch by Stevens, Antiga, and Viehmann, covering tensors through CNNs, RNNs, generative models, and production deployment. The go-to book for practitioners who want to understand PyTorch from first principles rather than copy-paste patterns.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/ELI STEVENS, LUCA ANTIGA, AND THOMAS VIEHMANN - Deep Learning With PyTorch (2020, MANNING) - libgen.li.pdf
---

## Summary

*Deep Learning with PyTorch* by Eli Stevens, Luca Antiga, and Thomas Viehmann (Manning, 2020), with a foreword by Soumith Chintala (PyTorch's creator), is the canonical practical textbook for learning deep learning through PyTorch. Unlike tutorial-style introductions, the book builds understanding from the ground up: starting with tensors as the core data structure, then autograd for automatic differentiation, then progressively more complex architectures. The goal is to make readers comfortable building custom models rather than just adapting existing ones.

The first half covers the foundations. Tensors are explained with attention to memory layout, broadcasting semantics, and GPU transfer — the kind of mechanics that confuse practitioners who learned from high-level APIs. Autograd is demystified: the book explains the computational graph that gets built during the forward pass and how gradients flow backward through it, which makes debugging training failures much more tractable. The training loop is built from scratch, making the choices made by frameworks like [fast.ai](/notes/fastai/) and PyTorch Lightning legible.

The second half moves to applications: convolutional neural networks for image classification, recurrent neural networks and LSTMs for sequences, and generative models. Deployment chapters cover TorchScript for moving beyond Python and ONNX for cross-framework portability. The book also covers distributed training with torch.distributed, which is increasingly important as models grow. What distinguishes the book is that it consistently explains *why* things work the way they do — the backpropagation chapter actually derives the gradients rather than treating them as magic, and the CNN chapter grounds convolutions in signal processing intuition.

## Key points

- Tensors in PyTorch are not just arrays — memory layout (contiguous vs. non-contiguous), strides, and device placement have real performance implications that the book explains systematically
- Autograd builds a computational graph dynamically during the forward pass; understanding this graph is key to writing custom loss functions and debugging gradient flow
- TorchScript and ONNX represent two different paths to production: TorchScript for PyTorch-native deployment, ONNX for interoperability with TensorFlow Serving, TensorRT, and other inference runtimes
- The LSTM treatment connects sequence modeling to the vanishing gradient problem — why gating mechanisms exist and what they're guarding against
- Distributed training with torch.distributed follows a ring-allreduce pattern for gradient synchronization; understanding this is prerequisite for multi-GPU work

[Source](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/ELI%20STEVENS%2C%20LUCA%20ANTIGA%2C%20AND%20THOMAS%20VIEHMANN%20-%20Deep%20Learning%20With%20PyTorch%20(2020%2C%20MANNING)%20-%20libgen.li.pdf)
