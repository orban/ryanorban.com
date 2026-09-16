---
title: Noise in Creative Coding
date: 2021-04-22
categories:
  - generative-art
  - creative-coding
  - graphics
  - mathematics
  - javascript
description: Varun Vachhar's deep dive into noise functions for creative coding — covering Perlin noise, simplex noise, domain warping, and fractal Brownian motion with beautiful visual examples. The go-to reference for understanding how noise generates organic, natural-looking patterns.
params:
  source: pinboard
  sourceUrl: https://varun.ca/noise/
---

## Summary

Varun Vachhar's essay is one of the most comprehensive visual explanations of noise functions in creative coding. Noise functions generate smooth, pseudo-random values that look natural rather than jagged — the mathematical substrate for procedural textures, terrain generation, organic motion, and countless effects in generative art.

The essay walks through the progression from basic random values to Perlin noise (developed by Ken Perlin for the film *Tron* in 1982, later winning him an Academy Award) to simplex noise (a later Perlin improvement with better isotropy in higher dimensions). Each is illustrated with interactive visual examples that make the mathematical difference tangible — you can see how Perlin noise's grid structure creates subtle directional artifacts that simplex noise eliminates.

More advanced techniques covered: fractional Brownian motion (layering multiple noise octaves at different frequencies and amplitudes to create detail at multiple scales), domain warping (feeding noise output back as input to create flowing, turbulent effects), and curl noise (noise-based vector fields for particle systems that naturally maintain density). These techniques appear throughout generative art, game development (Minecraft's terrain uses 3D Perlin noise), and visual effects.

## Key points

- Perlin noise generates smooth pseudo-random values — natural-looking compared to pure randomness.
- Simplex noise: improved version with less directional bias and better scaling to higher dimensions.
- Fractional Brownian motion (fBm): layering noise at multiple octaves creates multi-scale detail.
- Domain warping: feeding noise output back as input coordinate produces turbulent, organic-looking flows.
- By Varun Vachhar — interactive visualizations throughout, excellent reference for creative coding.

[Original](https://varun.ca/noise/)
