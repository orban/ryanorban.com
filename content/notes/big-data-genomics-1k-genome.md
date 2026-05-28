---
title: "Big Data: The Power of Petabytes (Genomics Edition)"
date: 2015-11-05
categories:
  - genomics
  - big-data
  - bioinformatics
  - science
  - healthcare
description: Nature's supplement on big data in genomics, covering the arrival of the $1,000 genome and what it means for medicine — the data storage, analysis, and clinical interpretation challenges of a world where genome sequencing is routine. A milestone in the convergence of biology and data infrastructure.
params:
  source: pinboard
  sourceUrl: http://www.nature.com/nature/journal/v527/n7576_supp/full/527S2a.html
---

![Big Data: The Power of Petabytes (Genomics Edition)](/images/notes/big-data-genomics-1k-genome.png)

## Summary

This Nature supplement examines what happened to biology when genome sequencing became cheap enough that cost was no longer the constraint. The $1,000 genome milestone — reached around 2014 — meant the bottleneck shifted from sequencing to storage, processing, and interpretation. A single human genome is roughly 3 gigabytes raw; a hospital running routine genomic diagnostics generates petabytes per year. This is the moment biology became a big data problem.

The data challenge in genomics is compound: not just volume but complexity. Genome analysis requires comparing sequences across populations to find meaningful variants; the relevant signal (disease-causing mutations) is buried in a vast background of benign variation. Bioinformatics pipelines had been built for the era of expensive, sparse sequencing data — they needed to be rebuilt for continuous high-volume throughput. This created opportunities for both cloud infrastructure companies and specialized genomics analytics firms.

The deeper implication is clinical: when sequencing is cheap enough to be routine, the question becomes whether the medical system can use the data. Interpreting a genome requires connecting variant data to population-scale clinical outcomes — a fundamentally machine learning problem requiring enormous labeled datasets. This is why precision medicine initiatives (like the US All of Us program and the UK Biobank) were racing to build training corpora. The bottleneck moved upstream from data generation to data interpretation.

## Key points

- "$1,000 genome" milestone: shifted the bottleneck from sequencing cost to data storage, processing, interpretation.
- Single human genome ~3GB raw; hospital-scale genomics generates petabytes annually.
- Bioinformatics pipelines designed for sparse sequencing had to be rebuilt for continuous high-volume data.
- Clinical interpretation requires population-scale machine learning — rare variants need massive labeled datasets.
- Convergence with cloud computing and ML made precision medicine computationally feasible for the first time.

[Original](http://www.nature.com/nature/journal/v527/n7576_supp/full/527S2a.html)
