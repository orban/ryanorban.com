---
title: Colah's Blog — Chris Olah on Neural Networks
date: 2022-07-16
categories:
  - machine-learning
  - visualization
  - education
  - neural-networks
  - research
description: Chris Olah's personal blog is foundational reading for anyone trying to understand deep learning from first principles — his LSTM explainer, neural network topology post, and attention posts have shaped how a generation of researchers think about these models. Olah went on to co-found Anthropic's interpretability team, and the blog reflects his interest in mechanistic understanding.
params:
  source: pinboard
  sourceUrl: https://colah.github.io/
---

## Summary

Chris Olah (colah) is a deep learning researcher whose personal blog has influenced how the field talks about its own models. Writing in a style that prioritizes geometric and topological intuition, Olah treats neural networks as mathematical objects worth understanding deeply rather than black boxes to be benchmarked. He later co-founded Anthropic and leads [mechanistic interpretability](/notes/mechanistic-interpretability/) research there.

The most-referenced post is Understanding LSTMs (2015), which explained long short-term memory networks through diagrams that became the standard illustration in courses and textbooks worldwide. His Neural Networks, Manifolds, and Topology post frames classification as learning to untangle manifolds in high-dimensional space — a framing that informs how people think about representation learning. The attention posts preceded the transformer era and set up intuitions that became essential.

Olah's interest in interpretability — understanding *what* a model computes and *why* — runs through the blog's later work. Posts on feature visualization, circuits, and superposition in neural networks laid the groundwork for the [mechanistic interpretability](/notes/mechanistic-interpretability/) field. This blog is as much a research journal as a teaching resource.

## Key points

- Understanding LSTMs (2015) — still cited as the definitive visual explanation of gated recurrent units and LSTM cell state flow
- Neural Networks, Manifolds, and Topology — frames deep learning as learning continuous transformations between topological spaces
- Attention and Augmented Recurrent Neural Networks — early explainer on attention mechanisms before transformers
- Feature Visualization (with Distill team) — interactive neural feature visualization using activation maximization
- Companion to [Jay Alammar](/notes/jay-alammar/)'s blog; Olah goes deeper on theory while Alammar covers more architectures

[Original](https://colah.github.io/) → GitHub
