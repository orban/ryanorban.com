---
title: "Huetone: Accessible Color Palette Tool"
date: 2022-02-18
categories:
  - design
  - color
  - accessibility
  - tools
  - ui-design
description: Huetone is a color palette tool for UI design that generates WCAG-accessible palettes using the OKLCH color space for perceptually uniform lightness scaling. Solves the practical problem of creating design tokens that meet contrast requirements across all shade steps.
params:
  source: pinboard
  sourceUrl: https://huetone.ardov.me/
---

## Summary

Huetone by Alexey Ardov is a tool for creating accessible color palettes for UI design systems. The key technical decision is using OKLCH (Oklch chroma-hue) color space instead of HSL — OKLCH is perceptually uniform, meaning that equal numeric steps in lightness actually correspond to equal perceived brightness differences. In HSL, a step from 90% to 100% lightness looks very different visually than a step from 50% to 60%.

This matters practically for design systems because you want palette shades (e.g., primary-100 through primary-900) to scale predictably and meet WCAG contrast requirements. With HSL-based palettes, designers often have to hand-tweak individual shades because the math doesn't match human perception. OKLCH-based generation produces more consistent, just works palettes.

The tool is relevant to the broader shift toward perceptual color spaces in design tooling — Figma added OKLCH support in 2023, and the CSS Color Level 4 spec added `oklch()` to the browser. Huetone was ahead of mainstream adoption and reflects the kind of sophisticated color thinking that good design systems (like Radix UI's palette or Tailwind CSS's gray scales) require.

## Key points

- OKLCH color space: perceptually uniform lightness scaling, unlike HSL which has visual inconsistencies.
- Generates palettes that meet WCAG contrast ratios out of the box — contrast checking is built in.
- Useful for building design token systems where shade naming (100–900) should mean something consistent.
- Contrasts with HSL-based palette generators that produce visually inconsistent scales.
- Part of the industry shift toward perceptual color spaces (OKLCH, OKLCH, P3) in design tooling.

[Original](https://huetone.ardov.me/)
