---
title: "fast.ai: From Deep Learning Foundations to Stable Diffusion"
date: 2022-11-06
categories:
  - fast-ai
  - stable-diffusion
  - deep-learning
  - education
  - course
description: "fast.ai's Part 2 2022 course preview — the first two lessons of their deep learning foundations to Stable Diffusion curriculum, taught bottom-up from first principles. Jeremy Howard teaching diffusion models the way fast.ai teaches everything: by building it yourself."
params:
  source: pinboard
  sourceUrl: https://www.fast.ai/posts/part2-2022-preview.html
---

## Summary

[fast.ai](/notes/fastai/) released a preview of their Part 2 2022 course — "From Deep Learning Foundations to Stable Diffusion" — with the first two lessons available. The course is Jeremy Howard's characteristic approach: teach by building from first principles rather than treating neural networks as black boxes. Part 1 covers practical deep learning top-down; Part 2 goes back and builds the foundations bottom-up.

The timing was significant: Stable Diffusion had been released as open weights in August 2022, and this was among the first systematic educational treatments of how diffusion models work at the implementation level. Jeremy Howard built a working Stable Diffusion implementation from scratch using PyTorch, walking students through the math and code rather than just using the `diffusers` library as a black box.

The [fast.ai](/notes/fastai/) pedagogy — practical first, theory in service of implementation — is particularly well-suited to diffusion models, which have a rich mathematical underpinning (score matching, stochastic differential equations, DDPM) that can obscure the core ideas. By building it yourself and seeing it work, the math becomes interpretable. Hugging Face Diffusers had popularized the high-level API; this course taught you what was happening underneath.

## Key points

- [fast.ai](/notes/fastai/) Part 2 2022: deep learning foundations through Stable Diffusion, first two lessons previewed.
- Jeremy Howard builds Stable Diffusion from scratch in PyTorch — bottom-up, not top-down.
- Among the first serious educational treatments of diffusion model internals post-open-weights release.
- Covers DDPM, UNet, CLIP text conditioning — the stack beneath the `diffusers` API.
- Characteristic [fast.ai](/notes/fastai/) approach: learn by building, theory only once the intuition is established.
- Pairs well with Hugging Face Diffusers library for understanding what the high-level API abstracts.

[Original](https://www.fast.ai/posts/part2-2022-preview.html)
