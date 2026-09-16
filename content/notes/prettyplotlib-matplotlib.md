---
title: "prettyplotlib: Painlessly Create Beautiful Matplotlib Plots"
date: 2013-11-18
categories:
  - python
  - matplotlib
  - visualization
  - data-science
  - plotting
description: Olga Botvinnik's prettyplotlib — a Python library that wraps matplotlib with better defaults (ColorBrewer palettes, no chartjunk) to produce publication-quality plots without manual style configuration. The answer to 'why does matplotlib look so bad by default?'
params:
  source: pinboard
  sourceUrl: http://blog.olgabotvinnik.com/post/58941062205/prettyplotlib-painlessly-create-beautiful-matplotlib
---

## Summary

Olga Botvinnik (computational biologist, then at UCSD Salk Institute) created prettyplotlib to solve a daily frustration: matplotlib's default visual output is ugly, and making it look good requires boilerplate configuration that every data scientist copies from Stack Overflow. The library wraps matplotlib's API with sensible defaults drawn from Edward Tufte's data visualization principles and ColorBrewer palettes.

The core changes: replace the default blue-orange-green color cycle with perceptually distinct ColorBrewer palettes, remove top and right axis spines (chartjunk), use a white background instead of gray, and adjust font sizes to be readable. These are the specific changes that make ggplot2 (R's visualization library) look so much better than base matplotlib — prettyplotlib brings the same philosophy to Python.

The library's `ppl` module replaces standard matplotlib calls (`plt.bar`, `plt.scatter`, `plt.plot`) with wrapped versions that apply the style automatically. You swap in `ppl.bar` for `plt.bar` and get a cleaner plot immediately. This made it an easy adoption: no learning curve, just drop-in replacement.

## Key points

- Wraps matplotlib with better defaults: ColorBrewer palettes, no chartjunk spines, white background.
- Drop-in replacements: `ppl.bar`, `ppl.scatter`, `ppl.plot` mirror the matplotlib API exactly but apply style automatically.
- Tufte principles applied: remove everything that doesn't encode data (top/right spines, gray background, garish colors).
- ColorBrewer palettes: designed by cartographer Cynthia Brewer to be perceptually distinct and colorblind-friendly.
- prettyplotlib was later superseded by seaborn (which took the same philosophy further) and matplotlib's built-in style sheets.
- Olga Botvinnik is a well-known figure in the Python scientific computing community, also contributed to pandas and bioinformatics tools.

[Original](http://blog.olgabotvinnik.com/post/58941062205/prettyplotlib-painlessly-create-beautiful-matplotlib)
