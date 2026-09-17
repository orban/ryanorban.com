---
title: "hue.tools: Color Utility Suite"
date: 2022-02-16
categories:
  - design
  - color
  - tools
  - developer-tools
description: hue.tools is a color utility suite for designers and developers — format conversion, harmony generation, palette tools, and color manipulation in one place. A no-frills reference tool when you need quick color work.
params:
  source: pinboard
  sourceUrl: https://hue.tools/
---

## Summary

hue.tools is a browser-based color toolkit that consolidates the common operations designers and developers need: converting between color formats (hex, RGB, HSL, HSV, CMYK, Lab), generating color harmonies (complementary, triadic, analogous, split-complementary), inspecting color properties, and mixing colors.

The distinguishing quality is breadth over depth — it covers the full range of daily color operations in one place rather than specializing in one area. This differentiates it from Huetone (which specifically generates accessible design token palettes in OKLCH) and from code-focused tools like the chroma.js library. It's more of a calculator than a design workflow tool — useful when you have a hex code and need to know its HSL equivalent, or when you're picking a color scheme and want to see harmonious variants.

The practical use case for developers: quickly checking whether a proposed color meets WCAG contrast requirements, generating the full HSL range for a design token scale, or finding a complementary color for a UI accent. For designers without access to Figma at a given moment, or who want quick sanity checks, it fills a similar role to coolors.co or the CSS Color Module spec reference.

## Key points

- Color format conversion: hex ↔ RGB ↔ HSL ↔ HSV ↔ CMYK ↔ Lab in one interface.
- Harmony generation: complementary, analogous, triadic, split-complementary palettes from a base color.
- Contrast checker: verify WCAG AA/AAA compliance for foreground/background combinations.
- Complementary to Huetone (design tokens) and coolors.co (palette generation) — a general utility.
- No install required — browser-based, fast to reach when you need a quick color operation.

[Original](https://hue.tools/)
