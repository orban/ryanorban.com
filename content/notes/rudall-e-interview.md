---
title: How Sber Built ruDALL-E — Interview with Sergei Markov
date: 2021-12-31
categories:
  - machine-learning
  - nlp
  - generative-ai
  - large-language-models
  - research
description: Serokell's interview with Sergei Markov of SberDevices about building ruDALL-E — a 12B parameter Russian-language text-to-image model. Covers the engineering and research challenges of training massive multimodal models, plus the open-source culture argument in ML.
params:
  source: pinboard
  sourceUrl: https://serokell.io/blog/how-sber-built-rudall-e
---

## Summary

Sberbank (Russia's largest bank, branded as Sber) built ruDALL-E, a 12-billion parameter text-to-image model for Russian, inspired by OpenAI's DALL-E. The Serokell interview with Sergei Markov (head of SberDevices experimental ML systems) covers what it actually took to build a model at that scale — the compute requirements, training infrastructure, dataset construction, and the organizational decision to release it as open source.

The 12B parameter scale (equivalent to GPT-3's parameter count, which was revolutionary in 2020) requires massive GPU clusters and distributed training infrastructure. The Russian-language focus required building a separate training dataset — the DALL-E dataset was English-only, so Sber had to construct a Russian image-text pair dataset at comparable scale. This is the unglamorous part of large model research: dataset curation, cleaning, and quality filtering often take more engineering effort than the model architecture itself.

The open-source argument Markov makes: releasing models builds community, accelerates research iteration, and attracts talent. This was a live debate in 2021-2022 — OpenAI had pivoted away from full open release with GPT-3 (API-only), while EleutherAI was building open-source equivalents. Sber's choice to open-source ruDALL-E and related models (ruGPT-3, ruBERT) positioned them as participants in the open ML ecosystem rather than walled-garden API providers.

## Key points

- ruDALL-E: 12B parameter Russian text-to-image model; architecture based on DALL-E with Russian-specific training data
- Training compute challenge: 12B parameters requires weeks of training on large GPU clusters; distributed training across hundreds of GPUs
- Dataset construction: no existing Russian image-text pair dataset at scale — had to build from scratch (web crawl + filtering)
- Open-source rationale: community building, research acceleration, talent attraction — versus API-only approach
- Part of Sber's broader AI investment: ruGPT-3, ruBERT, and ruDALL-E formed a Russian-language large model family

[Original](https://serokell.io/blog/how-sber-built-rudall-e)
