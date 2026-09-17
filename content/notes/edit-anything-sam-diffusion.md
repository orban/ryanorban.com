---
title: "EditAnything: Segment Anything + Stable Diffusion for Image Editing"
date: 2023-04-10
categories:
  - computer-vision
  - image-editing
  - stable-diffusion
  - segment-anything
  - open-source
description: EditAnything combines Meta's Segment Anything Model with Stable Diffusion to enable precise region-based image editing — click to select any object, then replace or transform it with a text prompt. One of the first practical applications of SAM.
params:
  source: pinboard
  sourceUrl: https://github.com/sail-sg/EditAnything
---

## Summary

EditAnything is an open-source tool from SAIL-SG that combines Meta's Segment Anything Model (SAM) with Stable Diffusion to enable segment-aware image editing. The workflow: use SAM to click-select any object or region in an image (SAM's zero-shot segmentation produces a precise mask for arbitrary objects without training), then apply a Stable Diffusion inpainting model constrained to that region using the mask. The result is text-driven editing that respects object boundaries naturally.

The power comes from SAM's remarkable zero-shot segmentation. Before SAM, precise masking required either manual painting or training a segmentation model on your specific objects. SAM segments anything — arbitrary objects, at multiple granularities — with a single click or bounding box. When you pipe that mask into an inpainting model, you get precise editing without bleeding into adjacent regions. A text prompt then controls what the selected region becomes.

EditAnything was one of the first practical demonstrations of the SAM + diffusion model combination that became a common pattern in 2023 computer vision tooling. Related systems include Grounded-SAM (text-driven segmentation), Inpaint Anything (fill/delete selected objects), and later integrations in tools like Adobe Photoshop's Generative Fill. The underlying pattern — use a powerful foundation model for spatial understanding, then apply generative control in the selected region — proved widely applicable.

## Key points

- Combines Segment Anything Model (SAM) for click-based segmentation with Stable Diffusion for text-driven inpainting.
- Zero-shot object selection: SAM works on arbitrary objects without domain-specific training.
- Text prompt controls what the selected region becomes — replace, transform, add texture.
- One of the first SAM + diffusion integrations; influenced Grounded-SAM and Inpaint Anything.
- Pattern later adopted by Adobe Photoshop Generative Fill and commercial image editing tools.
- ControlNet provides the bridge between the SAM mask and the diffusion generation process.

[Original](https://github.com/sail-sg/EditAnything) → GitHub
