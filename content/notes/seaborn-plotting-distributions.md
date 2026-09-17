---
title: Seaborn — Plotting Distributions Notebook
date: 2014-11-25
categories:
  - python
  - seaborn
  - data-visualization
  - statistics
  - jupyter
description: Seaborn's official distribution-plotting example notebook — demonstrates the library's statistical visualization API for histograms, KDE plots, rug plots, and joint distributions. The reference for anyone learning to visualize data distributions in Python.
params:
  source: pinboard
  sourceUrl: http://nbviewer.ipython.org/github/mwaskom/seaborn/blob/master/examples/plotting_distributions.ipynb
---

## Summary

Seaborn is Michael Waskom's Python statistical visualization library built on top of Matplotlib. Where Matplotlib is a general-purpose plotting engine requiring explicit specification of every visual element, Seaborn provides opinionated defaults for the most common statistical graphics — with the tradeoff that it handles the common cases beautifully and the unusual cases awkwardly.

The distribution-plotting notebook demonstrates the core Seaborn distribution API from 2014 (later reorganized in v0.11+): `distplot()` for histograms with kernel density estimate overlay, `kdeplot()` for pure KDE, `rugplot()` for individual observation marks, and `jointplot()` for paired distributions with marginals. These are the functions you reach for when asking what does my data look like? before any modeling.

Kernel density estimation (KDE) is the key statistical concept behind several of these functions. A KDE is a non-parametric estimate of the probability density function of a continuous variable — it places a kernel (typically Gaussian) at each data point and sums the contributions, producing a smooth curve that approximates the underlying distribution without assuming a parametric form. The bandwidth parameter controls smoothing: too small → jagged, too large → oversmoothed.

## Key points

- Seaborn wraps Matplotlib with statistical defaults — the standard library for exploratory data visualization in Python.
- `distplot()`: histogram + KDE overlay in one call — the default first look at any continuous variable.
- `jointplot()`: scatter of two variables with marginal distributions on each axis — reveals correlation and individual distributions simultaneously.
- Kernel density estimation: non-parametric smooth density estimate — bandwidth controls smoothing tradeoff.
- `pairplot()` (not in this notebook but related): pairwise distributions across all feature columns — standard EDA tool.
- Notebooks on `nbviewer.ipython.org` (now `nbviewer.jupyter.org`) were the primary way to share executable Python examples in 2014.

[Original](http://nbviewer.ipython.org/github/mwaskom/seaborn/blob/master/examples/plotting_distributions.ipynb) → GitHub
