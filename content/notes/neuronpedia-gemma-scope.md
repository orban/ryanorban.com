---
title: "Neuronpedia Gemma Scope: interactive mechanistic interpretability for Gemma 2"
date: 2026-02-15
categories:
  - mechanistic-interpretability
  - machine-learning
  - sparse-autoencoders
  - gemma
  - research
description: Neuronpedia's Gemma Scope microscope lets you scan Gemma 2's internal features using Sparse Autoencoders — activating features, steering behavior, browsing SAE decompositions. Interactive mechanistic interpretability for a production model.
params:
  source: pinboard
  sourceUrl: https://www.neuronpedia.org/gemma-scope#microscope
---

![Neuronpedia Gemma Scope: interactive mechanistic interpretability for Gemma 2](/images/notes/neuronpedia-gemma-scope.png)

## Summary

Neuronpedia is an open-source platform for mechanistic interpretability research that provides interactive tools for exploring the internal mechanisms of language models. The Gemma Scope project on Neuronpedia focuses specifically on Google DeepMind's Gemma 2 2B model, offering a \microscope\ that lets researchers — and curious developers — scan the model's internals.

The core mechanic is Sparse Autoencoders (SAEs). SAEs are a technique for decomposing dense model activations into interpretable sparse feature representations. When you apply an SAE to a model layer's activations, you get a set of features that fire for specific semantic concepts. Neuronpedia's microscope makes this interactive: you can select a feature, see what text activates it most, understand its function, and then steer model behavior by amplifying or suppressing specific features. This is one of the primary tools in the mechanistic interpretability toolkit.

The significance: most LLMs are trained (\grown\, in Neuronpedia's framing) rather than designed, which makes their internals opaque by default. SAE-based analysis has become one of the most productive approaches to understanding what's actually happening inside these models — Anthropic has published major work on features in Claude using the same approach. Neuronpedia's Gemma Scope makes that analysis accessible without needing to run the research infrastructure yourself.

## Key points

- Sparse Autoencoders (SAEs) decompose model activations into interpretable sparse features.
- Interactive microscope: activate features, understand their function, steer model behavior.
- Specifically covers Gemma 2 2B from Google DeepMind.
- Part of Neuronpedia, an open-source mechanistic interpretability research platform.
- Anthropic has done parallel work applying SAEs to Claude — this makes similar methods available for Gemma.
- Key tool for the safety and interpretability research community.

[Original](https://www.neuronpedia.org/gemma-scope#microscope)
