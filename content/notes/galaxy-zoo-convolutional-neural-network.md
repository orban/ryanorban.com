---
title: My Solution for the Galaxy Zoo Challenge — Sander Dieleman
date: 2014-04-08
categories:
  - deep-learning
  - convolutional-neural-networks
  - kaggle
  - astronomy
  - machine-learning
description: Sander Dieleman's winning solution for the Galaxy Zoo Kaggle challenge using convolutional neural networks to classify galaxy morphology from images. A landmark result showing CNNs achieving human-level performance on a citizen science dataset.
params:
  source: pinboard
  sourceUrl: http://benanne.github.io/2014/04/05/galaxy-zoo.html
---

## Summary

The Galaxy Zoo Kaggle challenge asked competitors to classify galaxy morphologies from telescope images — the same task that hundreds of thousands of human volunteers had done for the original Galaxy Zoo citizen science project. Sander Dieleman won by using convolutional neural networks, achieving a mean squared error that exceeded human annotation consistency on the test set.

The key technical insight in the solution was exploiting the rotational symmetry of galaxies: since a galaxy looks the same regardless of rotation angle, Dieleman's network applied multiple rotations and reflections to each input, averaging their predictions. This data augmentation with symmetry constraints acted as a strong regularizer. He also used the full Theano-based deep learning pipeline and carefully preprocessed the astronomical imaging data.

This was 2014, before Keras, TensorFlow, or PyTorch existed in usable form. Building and training CNNs required working directly with Theano or Caffe — significantly more effort than today. Dieleman's write-up was unusually transparent about the full pipeline, making it a reference point for the Kaggle community and demonstrating that deep learning could match human-level performance on image classification tasks outside standard benchmark datasets.

## Key points

- CNNs with data augmentation (rotation, reflection) for rotationally-symmetric galaxy images.
- Symmetry-based augmentation is a form of domain knowledge encoded as an inductive bias.
- Built in Theano — this was before Keras/TensorFlow and required significant low-level work.
- Winner of Kaggle Galaxy Zoo challenge with superhuman consistency on morphology labels.
- Demonstrated generalization of convolutional neural networks beyond ImageNet-style benchmarks.

[Original](http://benanne.github.io/2014/04/05/galaxy-zoo.html) → GitHub
