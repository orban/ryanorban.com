---
title: An Introduction to Variational Autoencoders
date: 2026-04-29
categories:
  - generative-models
  - deep-learning
  - variational-inference
  - research
  - machine-learning
description: The canonical tutorial on Variational Autoencoders by Kingma and Welling — the original VAE inventors. Covers the ELBO, reparameterization trick, and extensions to deeper generative models. Essential background for anyone working with latent variable models or modern diffusion/flow models.
params:
  source: papers
  sourceUrl: https://arxiv.org/abs/1906.02691
---

## Summary

This tutorial by Diederik Kingma (Google) and Max Welling (University of Amsterdam / Qualcomm) is the authoritative introduction to Variational Autoencoders (VAEs) — written by the inventors of the model. Published in *Foundations and Trends in Machine Learning* (arXiv 1906.02691), it provides both the theoretical foundations and practical guidance for the model that became a cornerstone of generative deep learning.

The VAE frames generative modeling as a variational inference problem. A probabilistic encoder (the approximate posterior q(z|x)) maps data into a latent space; a probabilistic decoder p(x|z) generates data from latent codes. The training objective is the Evidence Lower Bound (ELBO), which balances reconstruction quality against regularization toward a prior (typically a standard Gaussian). The critical trick is the **reparameterization trick**: instead of sampling z from q(z|x), express z = μ + σ·ε where ε ~ N(0,1) — making sampling differentiable and enabling backpropagation through stochastic nodes.

The tutorial goes beyond the basic VAE to cover extensions: flexible normalizing flow posteriors via the Inverse Autoregressive Flow (IAF), hierarchical latent variable models with multiple latent layers, and connections to autoregressive models. These extensions addressed early VAE limitations like blurry samples and posterior collapse, and prefigure the design choices in modern generative models. The VAE's influence extends to diffusion models (which can be interpreted as deep hierarchical VAEs), VQ-VAE (discrete latent spaces), and DALL-E (which used a VAE for the discrete image tokens).

## Key points

- ELBO = reconstruction term + KL divergence penalty. Maximizing it trains both encoder and decoder jointly without computing the intractable marginal likelihood.
- Reparameterization trick: makes sampling differentiable by separating randomness (ε) from learned parameters (μ, σ). The key technical insight enabling end-to-end training.
- Posterior collapse: a failure mode where the encoder ignores the input and q(z|x) ≈ p(z). The tutorial discusses mitigations including annealing, free bits, and decoder weakening.
- Inverse Autoregressive Flow (IAF): normalizing flow that makes posterior more flexible while remaining computationally efficient for sampling.
- Foundation for modern generative models: diffusion models are deep hierarchical VAEs with fixed encoder noise schedules; VQ-VAE uses discrete latents.
- Connects variational inference from Bayesian statistics to neural network training — a key bridge between two communities.

[Original](https://arxiv.org/abs/1906.02691)
