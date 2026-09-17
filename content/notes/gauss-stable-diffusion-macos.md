---
title: "Gauss: Native macOS Stable Diffusion App"
date: 2022-12-28
categories:
  - stable-diffusion
  - macos
  - image-generation
  - desktop-app
  - apple-silicon
description: Gauss is a native macOS app for running Stable Diffusion locally — built by Jake Teton-Landis using Swift/SwiftUI and Apple's Core ML stack to run image generation on Apple Silicon without Python. One of the early native Mac SD apps before AUTOMATIC1111 and ComfyUI dominated.
params:
  source: pinboard
  sourceUrl: https://github.com/justjake/Gauss
---

## Summary

Gauss is a native macOS application for running Stable Diffusion locally, built by Jake Teton-Landis using Swift and SwiftUI. Rather than running a Python-based web UI like AUTOMATIC1111 or InvokeAI, Gauss is a proper native Mac app that uses Apple Core ML to accelerate inference on Apple Silicon (M1/M2) chips.

The technical approach mattered for Apple Silicon users in late 2022: the standard Stable Diffusion stack was built for CUDA/NVIDIA GPUs. Running it on a Mac required either CPU inference (slow) or converting models to Apple's Core ML format to use the Neural Engine and GPU acceleration. Gauss handled this conversion and wrapped the whole stack in a native UI, giving Mac users a local image generation experience without needing to understand Python environments.

By mid-2023, the landscape had shifted: Diffusers added MPS backend support for Apple Silicon, and tools like DiffusionBee and Draw Things became the dominant Mac-native options. Gauss predates this ecosystem maturation — it's a snapshot of the moment when early adopters were figuring out how to run SD on hardware that wasn't the intended target. The open-source code is also useful as an example of how to integrate Core ML models into a SwiftUI app.

## Key points

- Native macOS app for Stable Diffusion — SwiftUI + Core ML, no Python required.
- Designed specifically for Apple Silicon — uses Neural Engine and GPU acceleration.
- December 2022: one of the earliest native Mac SD apps, predating DiffusionBee dominance.
- Converts Stable Diffusion models to Core ML format for Apple-optimized inference.
- Open source on GitHub — useful reference for Core ML + SwiftUI integration.

[Original](https://github.com/justjake/Gauss)
