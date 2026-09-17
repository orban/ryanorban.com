---
title: The DALL-E 2 Prompt Book
date: 2022-07-26
categories:
  - ai-art
  - generative-ai
  - prompt-engineering
  - image-generation
description: Unofficial visual reference guide by Guy Parsons (dallery.gallery) covering how to prompt DALL-E 2 across photography, illustration styles, art history movements, 3D artwork, and editing techniques. A practical taxonomy of the prompt space for the first widely-accessible diffusion image model.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/The-DALL·E-2-prompt-book-v1.01.pdf
---

## Summary

This document (v1.01, July 2022) by Guy Parsons of dallery.gallery is an unofficial visual guide to prompting DALL-E 2, OpenAI's text-to-image model released earlier that year. Rather than documenting a formal API, the book maps the emergent behavior of a model trained on 650 million image-caption pairs — so nothing in it was explicitly programmed in by the developers. The core premise is that effective prompting requires discovering what the model has absorbed, not following documented rules. The guide covers six major domains: vibes/mood vocabulary, photography, illustration, art history, 3D artwork, and advanced editing techniques.

The photography section is particularly systematic, covering framing (extreme close-up through extreme wide shot), camera angles, lens choices (telephoto, macro, fisheye, tilt-shift), shutter speed effects, outdoor and indoor lighting conditions, and film stocks (Kodachrome, Polaroid, cameraphone, etc.). The key insight is that specifying a camera or lens (Sigma 85mm f/1.4) doesn't just mimic that optical profile — it more broadly signals "the kind of professional photo where the photographer names their equipment," which tends to produce higher-quality outputs. Similarly, film-and-TV-show prompts ("film still from Blade Runner 2049") allow borrowing entire aesthetic vocabularies without knowing the technical terminology.

The editing techniques section covers DALL-E 2 inpainting and outpainting: replacing details, subjects, or backgrounds in existing images; simple uncropping/outpainting via an image editor to extend the canvas; and combining two separate images into a single scene. The book documents that iterating — variations of variations — leads to unexpected aesthetic territory that language prompts alone couldn't produce, and includes a community showcase of notable creative work.

## Key points

- Prompt structure for photography: subject + framing + camera angle + lens + lighting + film type + usage context (e.g., "editorial fashion photography from Vogue") combines to produce coherent, specific aesthetics
- Emotional vocabulary is organized across two axes: valence (positive/negative) and energy (high/low) — useful for controlling mood without specifying explicit content
- Art historical styles can be invoked with period + movement + artist names (e.g., "Surrealist painting by Magritte, 1929") but DALL-E struggles to reliably replicate specific artists' styles due to training data heterogeneity
- Outpainting requires moving the source image off-center in an image editor, erasing at least one pixel to trigger DALL-E 2's edit mode, then prompting for the surrounding area
- Using a process reward model for iteration — making variations of variations — allows exploring aesthetic neighborhoods that can't be reached by text prompting alone

[Original](file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/The-DALL·E-2-prompt-book-v1.01.pdf)
