---
title: "Block-NeRF: City-Scale Neural Neighborhoods"
date: 2022-02-11
categories:
  - nerf
  - computer-vision
  - machine-learning
  - 3d
  - waymo
description: Block-NeRF from Waymo and UC Berkeley extends Neural Radiance Fields to city-scale scenes by dividing them into individually trained blocks that stitch together. A step toward photorealistic neural reconstruction of entire neighborhoods from street-level imagery.
params:
  source: pinboard
  sourceUrl: https://www.unite.ai/the-new-cgi-creating-neural-neighborhoods-with-block-nerf/
---

![Block-NeRF: City-Scale Neural Neighborhoods](/images/notes/block-nerf-neural-neighborhoods.png)

## Summary

Block-NeRF is a Waymo and UC Berkeley research paper (2022) that extends Neural Radiance Fields (NeRF) from single objects or rooms to city-scale scene reconstruction. The core challenge: standard NeRF can't handle large scenes because it trains a single neural network on all images and the scale makes it intractable. Block-NeRF's solution is to divide a city block into sub-regions, train separate NeRF models for each block, then compose them at render time.

The results were striking for 2022: photo-realistic reconstruction of entire San Francisco street blocks from drive-by imagery, navigable at the pixel level. The technique also handles the practical challenges of real-world data — appearance variation from different lighting conditions, transient objects (pedestrians, vehicles), and the inconsistent overlap between camera positions.

This work sits at the intersection of autonomous driving research (Waymo's core mission) and 3D reconstruction methods. For Waymo, the ability to create accurate neural representations of road environments enables simulation without expensive physical re-driving — you can generate synthetic training data for edge cases by rendering novel viewpoints of real environments. The broader implication: photorealistic neural rendering at city scale becomes a tool for autonomous vehicle training pipelines.

## Key points

- Divides large scenes into overlapping blocks; each block trains its own NeRF model.
- Block merging: at render time, nearby blocks are blended based on camera proximity.
- Handles appearance variation (time of day, weather) via per-image appearance embeddings.
- Waymo use case: neural simulation environments for autonomous driving training data.
- Extends the NeRF research trajectory from objects → rooms → city blocks.

[Original](https://www.unite.ai/the-new-cgi-creating-neural-neighborhoods-with-block-nerf/)
