---
title: "DeepDream: How Alexander Mordvintsev Excavated the Computer's Hidden Layers"
date: 2020-08-03
categories:
  - machine-learning
  - neural-networks
  - visualization
  - computer-vision
  - creativity
description: The story behind Google's DeepDream — how researcher Alexander Mordvintsev discovered that running gradient ascent on a convolutional network's hidden layers produces psychedelic imagery that reveals what features the network learned. A landmark moment in neural network interpretability.
params:
  source: pinboard
  sourceUrl: https://thereader.mitpress.mit.edu/deepdream-how-alexander-mordvintsev-excavated-the-computers-hidden-layers/
---

## Summary

DeepDream began as a visualization research technique in 2015. Alexander Mordvintsev, a Google researcher, was trying to understand what a trained convolutional neural network (CNN) had learned. The approach he took: instead of feeding an image through the network forward to get a classification, run it in reverse — use gradient ascent to maximize the activation of a particular layer's neurons. The result was that the network would modify an input image to contain more of whatever that layer responds to strongly.

What emerged was visually shocking. The hidden layers of GoogLeNet trained on ImageNet responded to eyes, animals, buildings, and abstract textures in ways that, when amplified through gradient ascent, produced surreal, layered imagery — dogs inside clouds, eyes embedded in architectural details. The psychedelic quality wasn't a design choice; it was a direct window into the representational geometry of a deep neural network. The patterns revealed that networks learn highly compositional features: early layers detect edges and textures, middle layers detect parts, deep layers detect objects and scenes.

Google published the technique and code in 2015, and it went viral outside the ML community as an art phenomenon. But the underlying technical contribution was significant: feature visualization through gradient ascent became a foundational method in neural network interpretability. Mordvintsev's technique established that you could interrogate what a network sees by asking it to hallucinate images that maximally activate its neurons. This lineage connects directly to later work in [mechanistic interpretability](/notes/mechanistic-interpretability/), activation patching, and tools like Distill.pub's feature visualization articles.

## Key points

- DeepDream uses gradient ascent on a trained CNN to amplify what individual layers respond to — effectively asking the network to dream images that trigger its neurons.
- Reveals the hierarchical feature learning in deep learning: edges → textures → parts → objects.
- Alexander Mordvintsev's technique is foundational to the field of neural network interpretability.
- The visual output went viral culturally (2015) and made neural network internals legible to non-researchers.
- Feature visualization via gradient ascent connects to modern [mechanistic interpretability](/notes/mechanistic-interpretability/) research.
- Trained on ImageNet, the network hallucinates dogs, eyes, and buildings because those dominate the training data.

[Original](https://thereader.mitpress.mit.edu/deepdream-how-alexander-mordvintsev-excavated-the-computers-hidden-layers/)
