---
title: iWantHue — Color Palette Generator
date: 2013-02-11
categories:
  - data-visualization
  - color
  - design
  - tools
description: iWantHue generates palettes of maximally distinct colors for data visualization — optimized in HCL color space for perceptual uniformity and colorblind accessibility. The go-to tool for assigning categorical colors to data categories.
params:
  source: pinboard
  sourceUrl: http://tools.medialab.sciences-po.fr/iwanthue/
---

![iWantHue — Color Palette Generator](/images/notes/iwanthue-color-palettes.png)

## Summary

iWantHue (from Sciences Po medialab) solves a specific data visualization problem: given N categories to display, what colors should you assign to maximize their distinctiveness to human viewers? This seems simple but is genuinely hard — human color perception is non-uniform (the HCL color space better approximates perceptual distance than RGB), and naive approaches like evenly-spaced hues produce palettes where some colors look similar.

The tool works by generating candidate colors in HCL (Hue-Chroma-Luminance) space — which more closely matches human perceptual distance than RGB — and then applying k-means clustering to select colors that maximize inter-cluster distance. The result is a palette where all colors are as visually distinct from each other as possible given the number of categories and the chroma/luminance constraints.

Key features: colorblind optimization mode (filters colors that would appear similar under various forms of color vision deficiency), export to JSON/CSS/JavaScript for direct use in code, and adjustable chroma/luminance ranges to match light or dark backgrounds. The tool was created by Alexis Jacomy and Guillaume Plique and became a standard resource for anyone doing information design with categorical color.

## Key points

- HCL color space (Hue-Chroma-Luminance) better models human color perception than RGB or HSV — perceptual distance in HCL correlates with perceived difference
- k-means clustering in color space: the algorithm selects colors that maximize perceptual distance between all palette members
- Colorblind accessibility: filters colors that would appear identical to viewers with deuteranopia, protanopia, or other color vision deficiencies
- Multiple export formats (JSON, CSS, JavaScript) make it directly usable in D3.js, web projects, or any charting library
- Still maintained as an open-source tool at Sciences Po medialab — the approach has been validated and adopted widely in data journalism

[Original](http://tools.medialab.sciences-po.fr/iwanthue/)
