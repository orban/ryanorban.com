---
title: Linear Representations and Superposition in LLMs
date: 2026-02-15
categories:
  - mechanistic-interpretability
  - machine-learning
  - research
  - llm
  - linear-algebra
description: A clear explainer on how LLMs encode thousands of features in relatively small embedding spaces via superposition — the Johnson-Lindenstrauss lemma applied to neural representations. Good primer on the theoretical foundations behind SAE-based interpretability.
params:
  source: pinboard
  sourceUrl: https://ternarysearch.blogspot.com/2026/02/linear-representations-and-superposition.html
---

![Linear Representations and Superposition in LLMs](/images/notes/linear-representations-superposition.png)

## Summary

This blog post from ternarysearch explains how large language models compress thousands of semantic features into their embedding spaces through a phenomenon called superposition — and why this matters for mechanistic interpretability.

Linear representations are the observation that conceptual differences in LLMs manifest as consistent directional shifts in the embedding space. The classic example from Word2Vec: king − man + woman ≈ queen. The Park et al. framework formalizes this: concepts are represented as directions in the geometry of the embedding space. You can do arithmetic on meanings because meanings are vectors.

Superposition addresses a tension: models have thousands of meaningful features to represent, but embedding spaces are only 2K-16K dimensional. Perfect orthogonality (independent directions for each feature) would require dimensionality equal to the number of features. The Johnson-Lindenstrauss lemma provides the escape hatch: exponentially many nearly-orthogonal vectors can coexist in high-dimensional spaces. The trick is that real features are sparse — most features don't fire simultaneously — so the interference between superimposed features stays manageable, especially with ReLU-style nonlinearities that can route around it.

Understanding superposition is what motivated Sparse Autoencoders (SAEs) as an interpretability tool: SAEs learn to decompose superimposed activations back into sparse interpretable features. This is the same mechanism behind Neuronpedia's Gemma Scope microscope and Anthropic's interpretability research.

## Key points

- Linear representations: semantic concepts encoded as directions in embedding space — enables vector arithmetic on meaning.
- Superposition: models encode exponentially more features than dimensions by exploiting the Johnson-Lindenstrauss lemma and feature sparsity.
- ReLU nonlinearities help manage interference between superimposed sparse features.
- This is the theoretical foundation behind Sparse Autoencoders (SAEs) used in mechanistic interpretability.
- Understanding superposition is essential for understanding tools like Neuronpedia and Anthropic's interpretability work.

[Original](https://ternarysearch.blogspot.com/2026/02/linear-representations-and-superposition.html)
