---
title: "DIYHarappaWorld: Population Genetics for Personal Genomes"
date: 2012-05-08
categories:
  - genomics
  - diy-bio
  - ancestry
  - population-genetics
  - open-source
description: DIYHarappaWorld let people run the Harappa Ancestry Project's South Asian population genetics analysis on their own genetic data. An early example of citizen science genomics — taking academic ADMIXTURE tools and making them accessible to personal genome hobbyists.
params:
  source: pinboard
  sourceUrl: http://www.harappadna.org/2012/05/diy-harappaworld/
---

## Summary

Harappa Ancestry Project released DIYHarappaWorld — a tool that let individuals run the same ADMIXTURE population genetics analysis used by the project on their own raw genetic data (from services like 23andMe or deCODEme). The tool was modeled on DIYDodecad, a similar project by Dienekes Pontikos focused on European ancestry analysis. Both were part of a wave of citizen science genomics that emerged around 2010-2012 as personal genome services became affordable.

The underlying method: ADMIXTURE (or similar tools like STRUCTURE) takes a person's SNP genotype data and computes what proportion of their ancestry comes from different ancestral population clusters. The HarappaWorld reference clusters were derived from South Asian populations — the project was specifically interested in the genetic structure of the Indian subcontinent, Pakistan, Sri Lanka, and related populations. For South Asians using 23andMe (which had poor South Asian reference panels at the time), projects like Harappa offered much more granular ancestry analysis.

The DIY aspect mattered because it democratized a computational method that had previously required academic access. You could download the tool, run it on your raw genotype file, and get population cluster assignments that the commercial services didn't provide. This was early personal genomics infrastructure — before GnomAD had standardized reference panels, before 23andMe had South Asian-specific ancestry reports, and while academic population geneticists were still debating how to handle consumer genomics data ethically.

## Key points

- Based on ADMIXTURE software for population genetics — computes ancestry proportions from SNP data.
- Harappa Ancestry Project focused on South Asian population structure (India, Pakistan, Bangladesh, Sri Lanka).
- Modeled on DIYDodecad by Dienekes Pontikos — citizen science personal genomics analysis.
- Filled a gap: 23andMe had weak South Asian reference panels in 2012; Harappa offered more granular results.
- Part of broader open source genomics movement: genome hobbyists running academic-grade tools on personal data.

[Original](http://www.harappadna.org/2012/05/diy-harappaworld/)
