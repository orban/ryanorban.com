---
title: Ex-Yahoo CEO Backs Genomics Big Data Startup Bina
date: 2013-07-31
categories:
  - genomics
  - big-data
  - bioinformatics
  - startup
  - sequencing
description: FierceBiotechIT covering Bina Technologies, a genomics big data startup backed by ex-Yahoo CEO Scott Thompson, building hardware-accelerated pipelines for processing whole-genome sequencing data. A 2013 marker of when genomics data volumes began requiring big data infrastructure at clinical scale.
params:
  source: pinboard
  sourceUrl: http://www.fiercebiotechit.com/story/ex-yahoo-ceo-backs-genomics-big-data-startup-bina/2013-07-30
---

## Summary

Bina Technologies was a startup building hardware-accelerated bioinformatics pipelines for processing whole-genome sequencing (WGS) data. Former Yahoo CEO Scott Thompson backed the company, and FierceBiotechIT covered the fundraise as evidence that the intersection of genomics and big data was attracting mainstream tech investment. Bina's pitch was reducing the time and cost to process a sequenced human genome from hours to minutes using custom FPGA-accelerated hardware paired with software pipelines.

A sequenced human genome is approximately 200GB of raw reads that must be aligned, sorted, variant-called, and annotated before producing clinically useful results. By 2013, Illumina had driven sequencing costs down dramatically (from $100M per genome in 2001 to under $5,000 by 2013), but the computational processing pipeline had become the bottleneck. BWA, GATK (Genome Analysis Toolkit from the Broad Institute), and downstream annotation tools were the standard pipeline — computationally intensive and slow on standard hardware.

Bina represented a class of genomics infrastructure companies betting that the sequencing cost curve would continue falling and that clinical genomics at scale (whole-genome sequencing for every hospital patient, population-scale biobanks) would require infrastructure specifically designed for this data type. Bina was acquired by Roche in 2014, validating the strategic value — Roche was building toward clinical genomics pipelines.

## Key points

- Whole-genome sequencing pipeline: raw reads → alignment (BWA) → variant calling (GATK) → annotation — each step computationally intensive, standard workflow in 2013.
- FPGA acceleration: field-programmable gate arrays configured to run specific genomics algorithms much faster than general-purpose CPUs or GPUs.
- Cost curve inflection: sequencing cost had dropped ~10,000x from 2001-2013; computational processing was becoming the new bottleneck.
- Broad Institute GATK: the standard variant-calling toolkit, originally resource-intensive enough to require cluster computing — a key target for acceleration.
- Roche acquisition (2014): validation that pharmaceutical and diagnostics companies saw genomics infrastructure as strategically important.
- 2013 context: clinical genomics was still early-stage; population genomics at scale (UK Biobank, All of Us) was years away — Bina was betting on the trajectory.

[Original](http://www.fiercebiotechit.com/story/ex-yahoo-ceo-backs-genomics-big-data-startup-bina/2013-07-30)
