---
title: "Banana Serverless Template: Stable Diffusion"
date: 2022-08-25
categories:
  - stable-diffusion
  - serverless
  - infrastructure
  - mlops
  - banana-dev
description: Banana.dev's serverless template for deploying Stable Diffusion as an API — package the model, push to Banana, get an API endpoint. One of the first practical paths to serving Stable Diffusion at scale without managing GPU infrastructure.
params:
  source: pinboard
  sourceUrl: https://github.com/bananaml/serverless-template-stable-diffusion
---

![Banana Serverless Template: Stable Diffusion](/images/notes/banana-serverless-stable-diffusion.png)

## Summary

Banana.dev (now defunct, acquired) offered a serverless GPU compute platform specifically targeting ML model deployment. This template repository provided the boilerplate to deploy Stable Diffusion as an API on Banana's infrastructure: define your model loading code, add an inference handler, and Banana handles provisioning GPU instances, scaling to zero when idle, and scaling up on demand. The template came out immediately after Stable Diffusion's open-source release in August 2022.

The problem it solved: running Stable Diffusion requires a GPU, and in August 2022, the options for serving it as an API were limited. You could rent a GPU VM (Lambda Labs, Vast.ai, AWS `p3` instances) and manage it yourself, use Replicate's model hosting platform, or use Banana. The serverless model was attractive for bursty workloads — pay only for inference time, not idle GPU time, and scale automatically. Banana positioned itself as the easiest path from model that runs locally to API endpoint anyone can call.

Banana.dev was part of a wave of MLOps infrastructure startups that emerged in 2021-2022 to fill the gap between training a model and running it in production. The category included Replicate (focus: reproducible model sharing), Modal (serverless Python with GPU support), RunPod (cheaper GPU cloud), and Beam Cloud. Banana specifically targeted the "I have a PyTorch model, I want an API" workflow. The platform was acquired in 2023 as the GPU cloud market consolidated.

## Key points

- Serverless GPU deployment template for Stable Diffusion on Banana.dev's infrastructure.
- Model-to-API in hours: load model, write inference handler, push to Banana, get an endpoint.
- Scale-to-zero billing — pay only for actual inference time, not idle GPU.
- Timed exactly with Stable Diffusion's August 2022 open-source release — immediate community adoption.
- Banana.dev was an early MLOps serverless GPU startup; acquired 2023.
- Part of the serverless ML category alongside Replicate, Modal, RunPod.

[Original](https://github.com/bananaml/serverless-template-stable-diffusion) → GitHub
