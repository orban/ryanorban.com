---
title: Deep Learning Tutorials — DeepLearning.net
date: 2013-12-29
categories:
  - deep-learning
  - neural-networks
  - theano
  - tutorial
  - education
description: The canonical deep learning tutorial site from the Montreal group — code-first walkthrough of core architectures (RBM, DBN, CNN, LSTM) using Theano. Written by the lab around Yoshua Bengio and became the standard reference before fast.ai existed.
params:
  source: pinboard
  sourceUrl: http://deeplearning.net/tutorial/
---

## Summary

The Deep Learning Tutorials site from LISA Lab at Université de Montréal was the definitive practical resource for learning deep learning in 2013. Written by researchers in Yoshua Bengio's group, it provided code-first walkthroughs of core architectures using Theano — the Python framework the lab developed for symbolic math and GPU computation that preceded TensorFlow and PyTorch.

The tutorial sequence built from first principles through a pedagogically sound path: logistic regression, Multi-Layer Perceptrons (MLPs), Convolutional Neural Networks (CNNs) for image classification, Denoising Autoencoders, Stacked Denoising Autoencoders, Restricted Boltzmann Machines (RBMs), Deep Belief Networks (DBNs), and LSTM networks for sequence modeling. Each tutorial included working Python/Theano code alongside the theory.

This site is historically significant: it was where most practitioners in 2013 actually learned how to implement deep learning systems. The code was written against the MNIST benchmark, making it easy to verify implementations. Before [fast.ai](/notes/fastai/), Coursera, or any of the current educational infrastructure existed, this was the curriculum.

## Key points

- From Yoshua Bengio's LISA Lab — the Montreal group that alongside Geoffrey Hinton and Yann LeCun drove the deep learning revolution.
- Uses Theano for all implementations — the symbolic differentiation library that introduced the GPU computation paradigm later adopted by TensorFlow.
- Tutorial sequence: logistic regression → MLP → CNN → denoising autoencoder → RBM → Deep Belief Network → LSTM.
- All examples benchmark against MNIST digit recognition — reproducible and verifiable.
- Historically the primary educational resource for deep learning before the current Coursera/fast.ai era.
- Theano is now deprecated but its design heavily influenced modern deep learning frameworks.

[Original](http://deeplearning.net/tutorial/)
