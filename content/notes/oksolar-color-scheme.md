---
title: OKSolar — Perceptually Uniform Color Scheme
date: 2022-11-21
categories:
  - color
  - terminal
  - design
  - developer-tools
  - accessibility
description: OKSolar is a perceptually uniform terminal and editor color scheme built in the OKLab color space, updating the classic Solarized with better perceptual balance. Addresses the color inconsistency problems of older schemes like Solarized and Monokai.
params:
  source: pinboard
  sourceUrl: https://meat.io/oksolar
---

## Summary

OKSolar is a terminal and editor color scheme built using the OKLab color space rather than sRGB. The premise: classic color schemes like Solarized were designed by eye in sRGB, which means colors that look equally bright perceptually aren't actually equal in the underlying math. OKLab is a perceptually uniform color space where equal numerical distances correspond to equal perceived differences — designed specifically for color manipulation that looks right to human eyes.

The project takes Solarized's design philosophy (warm background, carefully chosen accent colors, good contrast in both light and dark modes) and rebuilds it with OKLab to fix the perceptual inconsistencies. Colors that are supposed to have equal weight — say, yellow and cyan used for different syntax highlights — actually have equal perceived lightness rather than just equal sRGB values.

OKLab was designed by Björn Ottosson and released in 2020 as an improvement over CIE Lab for use cases like color picking, gradients, and palette design. OKSolar is one of the more visible applications of it to developer tooling. The theme is named for the combination of "OK (from OKLab) and Solar" (from Solarized). Ports exist for common terminals (Alacritty, iTerm2, Windows Terminal) and editors (Vim, Neovim, VS Code).

## Key points

- Terminal/editor color scheme built in OKLab — perceptually uniform, so colors with equal weight actually look equal.
- Reimplements Solarized's design philosophy with correct perceptual math.
- OKLab (by Björn Ottosson) is a 2020 color space designed specifically for color manipulation.
- Fixes sRGB's perceptual inconsistency problem: colors with equal sRGB values look unequal to human eyes.
- Ports available for major terminals and editors.

[Original](https://meat.io/oksolar)
