---
title: ONNX Stable Diffusion Exporter for Hugging Face Diffusers
date: 2022-09-08
categories:
  - stable-diffusion
  - onnx
  - hugging-face
  - inference
  - open-source
description: The pull request adding ONNX export and an ONNX inference pipeline to Hugging Face Diffusers — enabling Stable Diffusion to run via ONNX Runtime on hardware accelerators beyond CUDA, including DirectML for Windows GPUs and optimized CPU inference.
params:
  source: pinboard
  sourceUrl: https://github.com/huggingface/diffusers/pull/399
---

## Summary

This GitHub pull request by `anton-l` adds ONNX export support and an ONNX Runtime inference pipeline to the Hugging Face Diffusers library. ONNX (Open Neural Network Exchange) is an interoperability format for neural network models — exporting Stable Diffusion to ONNX allows it to run via ONNX Runtime rather than PyTorch, which opens up hardware targets beyond NVIDIA CUDA: AMD GPUs via DirectML on Windows, CPU inference with optimizations, and specialized accelerators.

The practical significance in September 2022: Stable Diffusion had just been released open-source, and most guides assumed NVIDIA CUDA hardware. Users with AMD GPUs, Apple Silicon (before the `mps` backend was stable), or CPU-only machines had limited options. ONNX Runtime offered a path to running Stable Diffusion on non-CUDA hardware with reasonable performance through backend-specific optimizations.

Diffusers became the canonical Python library for running diffusion models — the `diffusers` library abstractions (pipeline, scheduler, UNet, VAE) defined how the community packaged and distributed Stable Diffusion variants. Adding ONNX export to Diffusers meant every model in the ecosystem could potentially be exported to ONNX, not just the base model. This PR is historically significant as an early step in making Stable Diffusion broadly accessible across hardware.

## Key points

- Adds ONNX export and ONNX Runtime inference pipeline to Hugging Face Diffusers.
- Enables Stable Diffusion on non-CUDA hardware: AMD via DirectML, CPU optimized inference.
- ONNX = interoperability format; ONNX Runtime provides hardware-specific execution backends.
- Timed with Stable Diffusion's August 2022 open-source release — addressed the CUDA hardware requirement.
- Part of making Diffusers the canonical SD inference library with broad hardware support.
- DirectML specifically addressed the large user base on Windows with AMD/Intel GPUs.

[Original](https://github.com/huggingface/diffusers/pull/399)
