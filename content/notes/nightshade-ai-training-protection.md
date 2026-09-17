---
title: "Nightshade: Protecting Copyright Through Adversarial Poisoning"
date: 2024-06-10
categories:
  - ai-safety
  - art
  - copyright
  - adversarial
  - research
  - machine-learning
description: Nightshade is a tool that lets artists poison AI training data by adding imperceptible perturbations to images — images look normal to humans but cause AI models trained on them to produce corrupted outputs. An offensive countermeasure for artists against unauthorized scraping.
params:
  source: pinboard
  sourceUrl: https://nightshade.cs.uchicago.edu/whatis.html
---

![Nightshade: Protecting Copyright Through Adversarial Poisoning](/images/notes/nightshade-ai-training-protection.png)

## Summary

Nightshade is a research tool from the University of Chicago (the Glaze team, led by Ben Zhao) that lets artists add imperceptible perturbations to their images before posting them online. The perturbations are designed as data poisoning attacks: the images look visually normal to humans, but when scraped and used to train image generation models, they corrupt the model's ability to generate images in that style or category. An artist posting Nightshade-processed images is polluting the training data that would otherwise be used without consent.

The technical mechanism: Nightshade uses adversarial examples targeted at the CLIP vision-language model embeddings that underpin most diffusion model training pipelines. The perturbations shift the semantic representation of the image in the embedding space — making a painting of a dog look like a cat to the model's feature extractor, while remaining visually a dog to humans. When enough poisoned images appear in a training dataset, the model learns corrupted associations: dog → cat-like outputs, fantasy art → broken outputs.

The tool is part of a broader artist response to AI scraping. Glaze (the earlier tool from the same team) applies style cloaking that makes it harder for models to learn an artist's specific style. Nightshade is more aggressive — rather than protecting the artist's style, it actively corrupts the model trained on their work. The asymmetry is notable: a handful of artists using Nightshade can potentially degrade a model trained on millions of images, because poisoned samples disproportionately affect learned associations.

## Key points

- Adds imperceptible adversarial perturbations to images that poison AI training when scraped.
- Targets CLIP embeddings that underlie Stable Diffusion and similar diffusion model pipelines.
- Works asymmetrically: a few hundred poisoned images can corrupt model outputs at scale.
- By the Glaze team at University of Chicago — same group doing style-cloaking research.
- Artist countermeasure against unauthorized training data scraping.
- Related to adversarial ML, data poisoning, and the ongoing AI copyright debate.

[Original](https://nightshade.cs.uchicago.edu/whatis.html)
