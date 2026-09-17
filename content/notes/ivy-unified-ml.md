---
title: "Ivy: The Unified Machine Learning Framework"
date: 2022-08-07
categories:
  - machine-learning
  - framework-agnostic
  - pytorch
  - tensorflow
  - jax
description: Ivy is a unified machine learning framework that transpiles code between NumPy, PyTorch, TensorFlow, and JAX — write once, run anywhere across ML backends. An ambitious attempt to solve the framework fragmentation problem that plagues ML research and production.
params:
  source: pinboard
  sourceUrl: https://lets-unify.ai/
---

## Summary

Ivy is a framework created by Daniel Lenton and the lets-unify.ai team that wraps NumPy, PyTorch, TensorFlow, and JAX under a single unified API. The idea: write your ML code once in Ivy, and it transpiles to whichever backend you need. This attacks a genuine pain point — ML code written in PyTorch can't run on TPUs (which require JAX or TF), code written in TensorFlow doesn't compose nicely with the PyTorch-native research ecosystem, and model weights often can't be shared across frameworks.

The transpilation approach is technically ambitious. Ivy intercepts function calls and rewrites them to the target backend's operations, managing the semantic differences between frameworks (e.g., how they handle in-place operations, broadcasting, random number generation). This is harder than it looks: the frameworks differ not just in API surface but in execution semantics, gradient computation, device handling, and memory management.

The framework-fragmentation problem Ivy targets is real, and the ML community had already built partial solutions: ONNX for model export, Hugging Face for pretrained model sharing, TorchScript for PyTorch deployment. Ivy aimed at a more ambitious unification at the development level rather than just the model exchange level. The project attracted significant open-source attention and VC interest. Whether the full transpilation vision is achievable at production quality remains contested, but the problem it's solving — that PyTorch, TensorFlow, and JAX are islands — is real.

## Key points

- Single unified API over NumPy, PyTorch, TensorFlow, and JAX — write once, run on any backend
- Transpilation (not just wrapping): converts operations to native backend code
- Problem: ML frameworks are islands — research in PyTorch, production in TF, TPUs need JAX
- Existing partial solutions: ONNX (model export), Hugging Face (model sharing) — Ivy targets the development layer
- Created by Daniel Lenton and team; attracted open-source community and research interest
- Technically hard: frameworks differ in in-place ops, grad computation, device semantics

[Original](https://lets-unify.ai/)
