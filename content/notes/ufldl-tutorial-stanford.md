---
title: UFLDL Tutorial — Stanford
date: 2014-01-03
categories:
  - deep-learning
  - neural-networks
  - unsupervised-learning
  - stanford
  - tutorial
description: Andrew Ng's Stanford UFLDL Tutorial — the primary self-study resource for deep learning before MOOCs existed. Teaches sparse autoencoders, PCA, CNNs, and deep belief networks with mandatory from-scratch implementation exercises.
params:
  source: pinboard
  sourceUrl: http://deeplearning.stanford.edu/wiki/index.php/UFLDL_Tutorial
---

## Summary

The UFLDL Tutorial (Unsupervised Feature Learning and Deep Learning) from Andrew Ng's group at Stanford was the primary self-study resource for deep learning before [fast.ai](/notes/fastai/) and dedicated MOOCs existed. The wiki covers sparse autoencoders, PCA, whitening, convolutional neural networks, and deep belief networks, with MATLAB and Octave exercises included.

The tutorial is notable for requiring students to implement backpropagation from scratch before using any library. In 2013-2014 this was a rite of passage: most practitioners learned gradient descent and backpropagation by implementing them manually on toy problems before scaling to real architectures. That hands-on requirement is why many people from this cohort have unusually strong intuitions about what's happening inside the forward and backward passes.

## Key points

- Starts with logistic regression and builds to sparse autoencoders, PCA, and convolutional neural networks
- Each module includes a programming exercise — implement first, verify against numerical gradient check
- Covers sparse coding, restricted Boltzmann machines, and deep belief networks — historical context for understanding modern architectures
- Originally in MATLAB/Octave; community Python translations emerged as Python became the standard
- Stanford CS231n (computer vision) and CS224n (NLP) are its successors for domain-specific deep learning

[Original](http://deeplearning.stanford.edu/wiki/index.php/UFLDL_Tutorial)
