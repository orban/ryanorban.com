---
title: "Visualizing Representations: Deep Learning and Human Beings"
date: 2015-01-16
categories:
  - deep-learning
  - neural-networks
  - visualization
  - representation-learning
  - interpretability
description: Christopher Olah's essay on visualizing what neural networks actually learn — using dimensionality reduction to show how deep networks transform data into progressively more separable representations. One of the most important early pieces on deep learning interpretability.
params:
  source: pinboard
  sourceUrl: http://colah.github.io/posts/2015-01-Visualizing-Representations/
---

## Summary

Christopher Olah is one of the clearest writers working at the intersection of neural network theory and visual communication. This 2015 post explores how deep networks learn by examining what their intermediate representations look like — using t-SNE and other dimensionality reduction techniques to visualize activations at different layers.

The core insight: deep networks don't directly transform inputs into outputs. They learn a series of intermediate representations, each more abstract than the last, until the final representation is linearly separable into the output classes. Visualizing these intermediate spaces — the geometry of what each layer has learned — makes this process legible. Points that started tangled in input space become progressively more organized as you move through the layers.

The post connects deep learning to a broader question about what it means for a machine to "understand" something. The representations learned by deep networks turn out to cluster by semantically meaningful categories, not just by statistical patterns in the training data. This is one of the early pieces that suggested deep networks learn something more like features than correlations — a hypothesis that has since been refined significantly through [mechanistic interpretability](/notes/mechanistic-interpretability/) research.

## Key points

- Deep networks learn a sequence of increasingly abstract representations — visualize each layer to understand what's learned.
- t-SNE visualization of layer activations shows geometric structure that corresponds to semantic categories.
- The tangled geometry metaphor: deep networks *untangle* complex decision boundaries across layers.
- By Christopher Olah — then an independent researcher, later at Google Brain and Anthropic.
- Precursor to his later work on neural network circuits, feature visualization, and [mechanistic interpretability](/notes/mechanistic-interpretability/).
- One of the early pieces suggesting neural networks learn semantically meaningful structure, not just statistical correlations.

[Original](http://colah.github.io/posts/2015-01-Visualizing-Representations/) → GitHub
