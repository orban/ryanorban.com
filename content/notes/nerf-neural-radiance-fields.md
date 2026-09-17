---
title: "NeRF: Neural Radiance Fields"
date: 2022-11-07
categories:
  - nerf
  - computer-vision
  - 3d
  - neural-rendering
  - research
description: The original NeRF (Neural Radiance Fields) project page from Matthew Tancik's site — the foundational 2020 paper that represents 3D scenes as neural functions and synthesizes novel views via volumetric rendering. A landmark that spawned a field.
params:
  source: pinboard
  sourceUrl: https://www.matthewtancik.com/nerf
---

## Summary

NeRF (Neural Radiance Fields) is the foundational technique for representing 3D scenes as continuous neural functions rather than explicit geometry. Introduced in the 2020 paper by Ben Mildenhall, Pratul Srinivasan, Matthew Tancik, Jonathan Barron, Ravi Ramamoorthi, and Ren Ng from UC Berkeley, it represents a scene as a function: given a 3D point and viewing direction, predict the color and density at that point. Volumetric ray marching integrates these predictions along camera rays to render novel views.

The key result: given a set of 2D photos of a scene taken from multiple angles, NeRF can synthesize photo-realistic views from arbitrary new camera positions — including positions where no photo was taken. The quality was dramatically better than previous novel view synthesis methods, and the implicit representation captured fine surface details, semi-transparency, and specular effects naturally.

NeRF spawned an entire research field. Immediate extensions addressed its slowness (training takes hours, rendering takes seconds per frame): [Instant NGP](/notes/instant-ngp/) (Müller et al., 2022) achieved real-time training with hash encoding; Mip-NeRF 360 improved unbounded scene handling; NeRF in the Wild handled varying lighting conditions. The technique was eventually partially superseded by 3D Gaussian Splatting for applications requiring real-time rendering, but remains central to the neural rendering field and influenced how Magic3D, DreamFusion, and similar text-to-3D systems work.

## Key points

- Represents 3D scenes as neural functions: given position + viewing direction → color + density.
- Enables photorealistic novel view synthesis from sparse 2D photos.
- Original paper from UC Berkeley (Mildenhall, Tancik, Barron et al.), 2020 — landmark in computer vision.
- Volumetric ray marching renders views by integrating the neural field along camera rays.
- Spawned a massive field: [Instant NGP](/notes/instant-ngp/), Mip-NeRF, NeRF in the Wild, and dozens of variants.
- Superseded in speed by 3D Gaussian Splatting but fundamental to neural rendering research.

[Original](https://www.matthewtancik.com/nerf)
