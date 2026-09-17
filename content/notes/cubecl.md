---
title: "CubeCL: Multi-Platform GPU Compute for Rust"
date: 2025-04-24
categories:
  - rust
  - gpu
  - compute
  - deep-learning
  - tracel
description: CubeCL is a multi-platform GPU compute language extension for Rust — write one kernel that targets CUDA, ROCm, Vulkan/WebGPU, and Metal. The foundation for the Burn deep learning framework's backend abstraction.
params:
  source: pinboard
  sourceUrl: https://github.com/tracel-ai/cubecl
---

![CubeCL: Multi-Platform GPU Compute for Rust](/images/notes/cubecl.png)

## Summary

[CubeCL](/notes/cubecl/) is a high-performance compute language extension for Rust that compiles to multiple GPU backends from a single kernel definition. Write your GPU kernel once, target CUDA (NVIDIA), ROCm (AMD), Vulkan/WebGPU, and Metal (Apple Silicon). The project comes from Tracel AI, the team behind the Burn deep learning framework.

The abstraction layer is the key engineering challenge: GPU compute languages (CUDA C, WGSL, Metal Shading Language) differ enough that writing portable compute code is painful. [CubeCL](/notes/cubecl/) raises the abstraction to a Rust-native DSL that generates the backend-specific shader code. This is the same problem solved by WebGPU/WGSL for graphics, but targeting the compute/AI workload specifically.

For the deep learning use case, this is significant: the Burn framework uses [CubeCL](/notes/cubecl/) so that models written in Burn can run on any GPU hardware without platform-specific kernel implementations. This matters especially as AI workloads spread beyond NVIDIA — AMD ROCm and Apple Silicon users gain first-class GPU support without waiting for framework-specific ports.

## Key points

- Single Rust kernel definition compiles to CUDA, ROCm, Vulkan/WebGPU, and Metal.
- Core infrastructure for the Burn deep learning framework's multi-platform backend.
- Solves the GPU compute portability problem: write once, run anywhere.
- Rust-native DSL — type-safe, integrated with Rust's ownership model.
- From Tracel AI, makers of Burn.
- Important for running AI workloads on non-NVIDIA hardware (AMD, Apple Silicon).

[Original](https://github.com/tracel-ai/cubecl) → GitHub
