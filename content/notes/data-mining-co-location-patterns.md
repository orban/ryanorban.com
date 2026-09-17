---
title: Data Mining for Co-Location Patterns
date: 2022-04-04
categories:
  - data-mining
  - spatial-data
  - pattern-recognition
  - textbook
description: Guoqing Zhou's CRC Press book on co-location pattern mining, a spatial data mining problem concerned with finding features that frequently appear together in geographic proximity. A specialized but valuable topic for anyone working with geospatial data analysis.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/Guoqing Zhou - Data Mining for Co-location Patterns_ Principles and Applications-CRC Press (2022).pdf
---

## Summary

Guoqing Zhou's 2022 CRC Press textbook addresses co-location pattern mining, a specialized problem in spatial data mining: identifying sets of spatial features that tend to appear in geographic proximity to each other. Unlike association rule mining in market basket analysis (where co-occurrence is transactional), co-location is inherently spatial — distance matters, not just co-presence in a transaction.

The problem originated from Zhou's PhD dissertation at Virginia Tech (2001), expanded over two decades into this book. Co-location pattern discovery has applications in ecology (species co-occurrence), urban analytics (retail clustering), epidemiology (disease-environment correlations), and geospatial business intelligence. The challenge is defining participation ratios and interest measures that respect the continuous nature of geographic space.

The book bridges mathematical and statistical foundations with practical case studies from retail, telecommunications, banking, and manufacturing — following the Manning MEAP approach of grounding abstractions in real datasets. Python implementation examples accompany the case studies.

## Key points

- Co-location patterns are the spatial analog of association rules: features near each other rather than features bought together
- Key challenge is defining proximity in continuous space — unlike transactions, spatial relationships don't have natural discrete boundaries
- Applications span ecology, urban analytics, retail site selection, epidemiology, and geospatial intelligence
- Based on Zhou's Virginia Tech dissertation, so the theoretical contributions are original research, not survey material
- Cluster analysis and pattern recognition over geospatial data are the core algorithmic techniques

[Original PDF](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/Guoqing%20Zhou%20-%20Data%20Mining%20for%20Co-location%20Patterns_%20Principles%20and%20Applications-CRC%20Press%20(2022).pdf)
