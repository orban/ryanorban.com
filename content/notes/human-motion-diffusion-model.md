---
title: Human Motion Diffusion Model (MDM)
date: 2022-12-05
categories:
  - diffusion-models
  - motion-generation
  - computer-vision
  - transformers
  - research
description: Tevet et al. (Tel Aviv University, arXiv:2209.14916, 2022) apply diffusion models to human motion generation, producing MDM — a transformer-based denoiser that generates realistic motion sequences from text descriptions or action labels. It matters because it extends the generative power of diffusion to a structured temporal domain, enabling controllable motion editing that prior methods couldn't match.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/Human Motion Diffusion.pdf
---

## Summary

Guy Tevet, Raab, Gordon, Shafir, Daniel Cohen-Or, and Amit Bermano (Tel Aviv University, arXiv:2209.14916, 2022) introduce MDM (Motion Diffusion Model), which adapts diffusion models to the problem of human motion generation. Instead of operating on images or tokens, MDM's denoiser works directly on motion sequences — arrays of joint positions over time — and is conditioned on text descriptions or action class labels. The backbone is a transformer, which processes the full motion sequence at each denoising step rather than applying convolutions along the time axis.

The conditioning mechanism is straightforward: text or action labels are encoded and injected as additional inputs to the transformer at each denoising timestep. This lets the model attend jointly to the noisy motion state and the conditioning signal, producing outputs that align with the description while remaining physically plausible. MDM reports state-of-the-art results on HumanML3D and HumanAct12 benchmarks, outperforming prior autoregressive and VAE-based approaches on both quality and diversity metrics.

A significant contribution beyond generation quality is MDM's support for editing and in-betweening. Because the diffusion reverse process is iterative, it can be seeded with partial motion constraints — fix the starting and ending pose, fill in the middle — or guided to edit a specific body part while holding the rest fixed. This compositional flexibility doesn't require separate models or fine-tuning; it falls out of the diffusion framework naturally. The approach connects to broader work on controllable generation and anticipates later methods that use classifier-free guidance for motion conditioning.

## Key points

- MDM applies diffusion models to motion sequences using a transformer-based denoiser that operates directly on joint positions over time
- Conditioned on text descriptions or action labels — the same model handles both text-to-motion and action-conditioned generation
- State of the art on HumanML3D and HumanAct12 benchmarks at time of publication
- Supports motion editing and in-betweening as natural capabilities of the iterative denoising process
- Demonstrates that diffusion's strength in image generation transfers to structured temporal data with appropriate architecture choices

[Source](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/Human%20Motion%20Diffusion.pdf)
