---
title: Textual Inversion for Stable Diffusion
date: 2022-08-29
categories:
  - stable-diffusion
  - textual-inversion
  - fine-tuning
  - image-generation
  - open-source
description: A patch enabling textual inversion in Stable Diffusion — the technique of learning a new text token that represents a custom concept (a person, style, or object) from just 3-5 example images. Textual inversion was the first practical method for personalizing Stable Diffusion without full fine-tuning.
params:
  source: pinboard
  sourceUrl: https://github.com/hlky/sd-enable-textual-inversion
---

![Textual Inversion for Stable Diffusion](/images/notes/sd-textual-inversion.png)

## Summary

Textual inversion is a technique for personalizing Stable Diffusion by learning a new token in the CLIP text encoder's embedding space. Given 3-5 images of a concept — a specific person, a particular artistic style, a custom object — textual inversion optimizes a new embedding vector that, when used in a prompt (typically written as `S*` or a special token), causes the model to generate images incorporating that concept. No modification of the model weights is required; only the embedding is learned.

The original paper (An Image Is Worth One Word: Personalizing Text-to-Image Generation using Textual Inversion, Gal et al., Weizmann Institute, August 2022) demonstrated the technique just as Stable Diffusion was released open-source. This repository by `hlky` adapted it to work with the community Stable Diffusion codebase that people were already using. The timing mattered: the open-source community adopted textual inversion rapidly because it ran locally without cloud infrastructure and didn't require fine-tuning the full model.

Textual inversion is more parameter-efficient than full fine-tuning but less flexible: it can't change the model's behavior, only inject a concept that the existing model can represent. It was eventually supplanted by DreamBooth (fine-tunes the full model, higher quality) and LoRA (Low-Rank Adaptation, computationally cheaper fine-tuning that became the dominant approach). Together, these three techniques defined the landscape of Stable Diffusion personalization through 2022-2023.

## Key points

- Textual inversion learns a new CLIP embedding token from 3-5 images — no model weight changes required.
- Enables generating a custom concept (person, style, object) by using the learned token in prompts.
- From Gal et al. (Weizmann Institute) August 2022; this repo adapted it to the community SD codebase.
- More efficient than full fine-tuning; less flexible — can only express concepts the model can already represent.
- Later displaced by DreamBooth (higher quality) and LoRA (dominant approach for personalization).
- Part of the Stable Diffusion personalization trifecta: textual inversion → DreamBooth → LoRA.

[Original](https://github.com/hlky/sd-enable-textual-inversion) → GitHub
