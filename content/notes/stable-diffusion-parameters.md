---
title: Stable Diffusion Parameters Guide
date: 2022-10-29
categories:
  - stable-diffusion
  - generative-ai
  - prompt-engineering
  - image-generation
  - tutorial
description: A practical overview of the key parameters for controlling AI image generation in Stable Diffusion — steps, CFG scale, sampler, seed, and dimensions. A useful reference from the early days when these knobs were being collectively figured out.
params:
  source: pinboard
  sourceUrl: https://sagiodev.com/blog/stable_diffusion_parameters/
---

## Summary

This guide covers the essential knobs in Stable Diffusion — the parameters that shape what an image generation run produces beyond just the text prompt. In late 2022, these were being collectively discovered and documented by the community, and guides like this were among the primary ways practitioners learned what each parameter did.

The key parameters: **Steps** (how many denoising iterations to run — more steps generally improves quality up to a point, but with diminishing returns). **CFG scale** (Classifier-Free Guidance scale — how strictly to follow the prompt vs. allow creative freedom; too high produces oversaturated, distorted outputs). **Sampler** (the DDIM, DDPM, k-LMS, or other sampler algorithm — different samplers trade off speed vs. quality vs. reproducibility). **Seed** (random starting point — the same seed with the same prompt produces the same image). **Image dimensions** (powers of 2 near 512×512 for SD 1.x models, since that's what they were trained on).

Understanding these parameters became an important practical SKILL during the Stable Diffusion era. The community of practitioners sharing results on platforms like [Lexica](/notes/lexica/), Civitai, and Reddit collectively documented what values worked well. The parameter space also revealed something about how diffusion models work: CFG scale in particular makes the classifier-free guidance mechanism visible — it's how you steer the denoising process toward the prompt without conditioning on a separate classifier.

## Key points

- Key Stable Diffusion parameters: steps, CFG scale, sampler, seed, image dimensions.
- CFG scale (Classifier-Free Guidance): controls prompt adherence vs. creative freedom.
- **Steps**: denoising iterations — diminishing returns after ~20-30 for most samplers.
- **Seed**: reproducibility — same seed + same settings = same output.
- **Sampler**: DDIM, k-LMS, Euler, etc. — speed/quality tradeoffs in the denoising algorithm.
- Community-documented knowledge; essential for practitioners in the 2022 generative AI wave.

[Original](https://sagiodev.com/blog/stable_diffusion_parameters/)
