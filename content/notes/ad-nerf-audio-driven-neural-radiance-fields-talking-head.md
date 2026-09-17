---
title: "AD-NeRF: Audio Driven Neural Radiance Fields for Talking Head Synthesis"
date: 2021-11-09
categories:
  - nerf
  - talking-head
  - generative-ai
  - audio-visual
  - neural-rendering
  - computer-vision
description: AD-NeRF generates photorealistic talking-head video directly from audio using neural radiance fields, bypassing the 2D landmarks or 3D face model intermediaries used by prior methods. By conditioning an implicit neural function on audio features and rendering via volume rendering, it achieves both head and upper body generation with free-viewpoint control.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/AD-NeRF.pdf
---

## Summary

AD-NeRF (Audio Driven Neural Radiance Fields) is a 2021 paper from University of Science and Technology of China and Zhejiang University that takes a fundamentally different approach to talking head synthesis than prior methods. While earlier work used intermediate representations — 2D facial landmarks, 3D morphable face models, or optical flow — as a bridge between audio and video, AD-NeRF feeds audio features directly into a conditional implicit neural function that generates a NeRF scene for each audio frame.

The model learns two separate neural radiance fields: one for the head (including hair) and one for the upper body. At inference time, given an audio signal, the system queries these fields to synthesize a frame using standard volume rendering. This architecture enables free control over viewing direction (you can change the camera angle) and background images, capabilities that 2D-landmark-based methods can't cleanly support because they're locked to the training camera angle.

This work sits at the intersection of neural scene representation and audio-visual synthesis, both of which were rapidly evolving at the time. NeRF had been introduced the prior year and was gaining traction as an approach for view synthesis; AD-NeRF is one of the first to apply it to the dynamic, audio-conditioned domain. The results are significantly more photorealistic than GAN-based talking head methods for the person-specific case (a single person is trained per model).

## Key points

- AD-NeRF generates talking-head video by conditioning a neural radiance field directly on audio features, removing the need for 2D landmarks or 3D face models as intermediate representations.
- Two separate NeRF models handle head+hair and upper body independently, enabling synthesis of both regions (prior methods typically only handled the face).
- Volume rendering gives free control over viewpoint and background — camera angle can be changed at inference time without retraining.
- Person-specific training is required (one model per person); this enables high fidelity but limits generalization across identities.
- The approach demonstrates that implicit neural representations are applicable to dynamic, conditioned synthesis tasks, opening a research direction that later includes [instant-ngp](/notes/instant-ngp/) and gaussian splatting successors.

[Original paper](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/AD-NeRF.pdf)
