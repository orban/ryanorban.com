---
title: Practical Deep Learning for Coders — fast.ai
date: 2017-07-23
categories:
  - deep-learning
  - education
  - machine-learning
  - python
  - fast-ai
description: "fast.ai's Practical Deep Learning for Coders — Jeremy Howard and Rachel Thomas's free course that inverted the standard pedagogy: start with working image classifiers, then learn the theory underneath. Democratized deep learning at a moment when most education assumed a PhD on-ramp."
params:
  source: pinboard
  sourceUrl: http://course.fast.ai/lessons/lesson1.html
---

## Summary

[fast.ai](/notes/fastai/) was founded by Jeremy Howard and Rachel Thomas with the explicit mission of making deep learning accessible to anyone with coding ability and a year of experience. Their flagship course, "Practical Deep Learning for Coders," launched free in 2016-2017 and became one of the most influential ML education resources of the decade. The course URL saved here is the first lesson of the 2017 edition.

The pedagogical approach was deliberately counter to the standard curriculum. Most deep learning courses at the time (including Andrew Ng's) taught bottom-up: linear algebra, calculus, backpropagation, then simple toy models, and eventually real applications. fast.ai did the opposite — start with a working image classifier (cats vs. dogs using ResNet with transfer learning) on lesson 1, then work backward to understand what the model is actually doing. This top-down or whole game approach was borrowed from how sports and music are taught: you play the game first, then learn to refine specific skills.

The course used Python, Jupyter notebooks, and originally Theano before moving to PyTorch (which fast.ai helped popularize for research). Howard's central message: you don't need a PhD to get state-of-the-art results on many practical problems. Transfer learning — taking a model pre-trained on ImageNet and fine-tuning it on your specific dataset — could achieve competitive accuracy with very little data and compute. This was genuinely surprising to many practitioners in 2017, when the assumption was that deep learning required massive datasets and Google-scale resources.

## Key points

- Top-down pedagogy: working image classifier in lesson 1, theory second — the inversion of standard deep learning curricula.
- Transfer learning as the central message: fine-tune ResNet (pre-trained on ImageNet) on your dataset; competitive accuracy with small data.
- Used PyTorch (after switching from Theano) and built the `fastai` library on top of it — fast.ai significantly contributed to PyTorch's adoption.
- Free, international students — the course was taken by hundreds of thousands of practitioners globally.
- Later produced research too: ULMFiT (transfer learning for NLP, 2018), tabular deep learning, and DAIN.

[Original](http://course.fast.ai/lessons/lesson1.html)
