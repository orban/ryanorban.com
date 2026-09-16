---
title: "Lucid Sonic Dreams: Audio-Reactive GAN Visualization"
date: 2022-08-17
categories:
  - generative-ai
  - music-visualization
  - stylegan
  - audio-reactive
  - creative-coding
description: Lucid Sonic Dreams syncs StyleGAN2-generated visuals to music, producing audio-reactive video from a song and style choice. Made GAN art accessible to musicians and VJs as a simple pip-installable Python package.
params:
  source: pinboard
  sourceUrl: https://github.com/mikaelalafriz/lucid-sonic-dreams
---

## Summary

[Lucid Sonic Dreams](/notes/lucid-sonic-dreams/) is a Python tool by Mikaela Alfriz that generates videos where StyleGAN2-based visuals animate in sync with music. Given an audio file and a style choice, the system analyzes the audio's rhythm and energy to drive the GAN's latent space traversal, producing audio-reactive video that pulses and morphs with the music. Output is an MP4 video file.

The tool uses pre-trained StyleGAN2 models from Justin Pinkney's consolidated repository — providing a variety of aesthetics (portraits, landscapes, abstract patterns) without training from scratch. The audio analysis maps beat onsets and spectral energy to movements in the latent space, creating synchronization between sound and image.

[Lucid Sonic Dreams](/notes/lucid-sonic-dreams/) sits at the intersection of creative coding and music visualization — a community of artists, VJs, and musicians producing live visuals and video art. It democratized GAN art for this audience: before tools like this, using StyleGAN2 required significant ML knowledge. The pip-installable package approach made it accessible to Python-comfortable creatives without deep ML backgrounds. It predates the Stable Diffusion wave and represents the GAN-era approach to generative video.

## Key points

- Syncs StyleGAN2 latent space traversal to music's beat and energy profile.
- Uses pre-trained models from Justin Pinkney's consolidated StyleGAN2 repository.
- Python package (pip install) with simple API — accessible to non-ML practitioners.
- Requires Python 3.6-3.7 and TensorFlow 1.15 (legacy; not compatible with TF2).
- GAN-era approach to generative video before Stable Diffusion-based video tools existed.
- Target audience: musicians, VJs, creative coding community wanting audio-reactive visuals.

[Original](https://github.com/mikaelalafriz/lucid-sonic-dreams) → GitHub
