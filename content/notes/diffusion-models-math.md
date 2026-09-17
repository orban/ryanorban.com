---
title: "How Diffusion Models Work: The Math from Scratch"
date: 2022-10-04
categories:
  - diffusion-models
  - machine-learning
  - math
  - deep-learning
  - education
description: AI Summer's mathematical walkthrough of how diffusion models work from scratch — covering the forward noising process, reverse denoising, DDPM training objective, and score matching. The most math-forward accessible introduction to the field.
params:
  source: pinboard
  sourceUrl: https://theaisummer.com/diffusion-models/
---

## Summary

AI Summer's deep-dive into the mathematics underlying diffusion models. This is a step above explainers like [Jay Alammar](/notes/jay-alammar/)'s illustrated guide — it derives the DDPM (Denoising Diffusion Probabilistic Models) training objective from first principles rather than just describing what happens.

The forward process is a Markov chain that gradually adds Gaussian noise to data over T timesteps, until the original data is indistinguishable from pure noise. The key mathematical insight is that you can sample from any intermediate step directly (no need to run T steps of noising) using the reparameterization trick — this makes training efficient.

The reverse process learns to denoise at each step by training a neural network to predict the noise that was added. The ELBO (evidence lower bound) connects this to variational inference: the training objective is to maximize the likelihood of the data under the model. Score matching and DDPM arrive at the same place from different theoretical starting points — both ultimately train a model to estimate the score function (gradient of log probability).

Understanding the math explains design choices that seem arbitrary from the outside: why the U-Net architecture, why cosine vs. linear noise schedules matter, and why DDIM (Denoising Diffusion Implicit Models) can generate images in fewer steps.

## Key points

- Diffusion models = forward noising Markov chain + learned reverse denoising.
- Reparameterization trick allows sampling any noisy step without running all prior steps.
- Training objective derived from the ELBO — equivalent to maximizing data likelihood.
- Score matching connects to DDPM: both estimate the score function.
- DDIM replaces the DDPM Markov chain with a deterministic process — fewer steps, same quality.
- Noise schedules (linear vs. cosine) significantly affect training stability and output quality.

[Original](https://theaisummer.com/diffusion-models/)
