---
title: Self-Organising Textures
date: 2022-04-25
categories:
  - neural-cellular-automata
  - generative-art
  - machine-learning
  - distill
  - self-organization
description: Distill's 2021 interactive article on Neural Cellular Automata for texture synthesis — a small local rule, learned via gradient descent, produces complex global textures through iteration. One of the clearest demos that local rules can encode rich global structure.
params:
  source: pinboard
  sourceUrl: https://distill.pub/selforg/2021/textures/
---

## Summary

[Self-Organising Textures](/notes/self-organising-textures/) is a 2021 Distill article by Alexander Mordvintsev and collaborators that applies Neural Cellular Automata (NCAs) to the problem of texture synthesis. The core idea: instead of designing a texture generator top-down, you learn a tiny local rule — a small neural network that each cell applies to its neighborhood — and let iteration produce the global texture. The result looks remarkably like biological pattern formation.

The approach extends the earlier Growing Neural Cellular Automata work (which grew and repaired MNIST digits) into the texture domain. Here, the NCA learns to reproduce a target texture from a single example image. Each cell only sees its 3×3 neighborhood, yet after many iterations the entire grid exhibits the target pattern. This works because the gradient of texture loss with respect to the local rule is backpropagated through the unrolled iterations — essentially training the CA rule end-to-end with backpropagation.

What makes this compelling beyond the visual results is the theoretical connection to reaction-diffusion systems and Turing patterns — the biological mechanisms behind animal skin patterns, coral growth, and shell markings. The NCA framework lets you explore a continuous space of rules that connects the hand-designed reaction-diffusion equations to data-driven texture models. The Distill interactive format lets you modify the target texture and watch the NCA adapt, which makes the mechanism intuitively clear.

## Key points

- Neural Cellular Automata learn a local rule via backpropagation through unrolled CA steps — gradient descent finds the rule, not the texture.
- Each cell applies a 3×3 neighborhood rule; global texture emerges from iterated local interactions.
- Connects to Turing patterns and reaction-diffusion systems — a differentiable version of biological pattern formation.
- Part of the broader selforg Distill series on differentiable self-organization, alongside Growing Neural Cellular Automata and Learning to See work.
- The NCA rule generalizes across initialization — any seed grows into the target texture, not just a specific starting state.
- Distill interactive format: adjust the target texture live and watch re-optimization in the browser.

[Original](https://distill.pub/selforg/2021/textures/)
