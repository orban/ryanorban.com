---
title: "GAN Lab: Interactive GANs in the Browser"
date: 2022-02-25
categories:
  - machine-learning
  - visualization
  - education
  - gans
  - interactive
description: GAN Lab is an interactive browser-based tool for playing with Generative Adversarial Networks — visualizing the generator and discriminator training dynamics in real time. One of the best tools for building intuition about how GANs work and fail.
params:
  source: pinboard
  sourceUrl: https://poloclub.github.io/ganlab/
---

## Summary

GAN Lab is an interactive visualization tool from the Polo Club of Data Science at Georgia Tech, running entirely in the browser using TensorFlow.js. It lets you train a Generative Adversarial Network (GAN) on simple 2D distributions and watch the generator and discriminator compete in real time, with animated visualizations of the probability landscapes, loss curves, and generated samples.

GANs are notoriously difficult to understand from equations alone — the adversarial training dynamic, where the generator learns to fool the discriminator while the discriminator learns to detect fakes, is easy to state but hard to internalize. GAN Lab makes the dynamics visible: you can watch the generator's samples converge toward the real distribution, see the discriminator boundary shift in response, and observe instabilities like mode collapse (where the generator produces only a few types of samples and ignores the rest of the distribution).

The tool lets you modify hyperparameters (learning rate, network size, step count) and select from several 2D target distributions (ring, grid, random). The immediate visual feedback turns hyperparameter tuning from abstract configuration into something you can observe directly. This design philosophy connects to TensorFlow Playground (for basic neural networks) and the broader interactive machine learning education movement — building intuition through direct manipulation rather than passive reading.

## Key points

- Runs in the browser — no setup required; uses TensorFlow.js for in-browser training.
- Real-time animation of generator and discriminator competing — makes the adversarial dynamic visible.
- Demonstrates common GAN failure modes like mode collapse interactively.
- Selectable 2D target distributions (ring, grid, random) and adjustable hyperparameters.
- Part of the interactive machine learning education genre alongside TensorFlow Playground and Neural Network Playground.
- From Polo Club of Data Science at Georgia Tech — same group behind CNN Explainer and other visualization tools.

[Original](https://poloclub.github.io/ganlab/) → GitHub
