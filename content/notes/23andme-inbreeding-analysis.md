---
title: "Using Your 23andMe Data: How Inbred Are You?"
date: 2013-01-09
categories:
  - genomics
  - 23andme
  - population-genetics
  - ancestry
  - bioinformatics
description: Razib Khan's guide to analyzing your 23andMe raw data for runs of homozygosity — a proxy for inbreeding coefficient. Part of the early era when direct-to-consumer genomics made population genetics analyses available to anyone.
params:
  source: pinboard
  sourceUrl: http://blogs.discovermagazine.com/gnxp/2013/01/using-your-23andme-data-how-inbred-are-you/
---

## Summary

Razib Khan (Gene Expression blog, then at Discover Magazine) wrote this guide during the early direct-to-consumer genomics era when 23andMe was expanding access to personal genomic data. The specific analysis: using your raw SNP data to calculate a runs of homozygosity (ROH) metric — an empirical measure of how many long stretches of your genome have identical alleles on both chromosomes, which indicates common ancestry on both sides of your family.

Runs of homozygosity are a proxy for the inbreeding coefficient — not just immediate inbreeding but the accumulated effect of distant common ancestors over many generations. All humans have some ROH; the question is how much. Populations with historically small effective sizes (island populations, isolated ethnic groups, populations that went through founder effects) tend to have more. The analysis is done on the raw 23andMe data using tools like PLINK or custom scripts.

The 2013 context: 23andMe was offering $99 genetic tests that produced raw SNP data that users could download and analyze themselves. Razib Khan was one of the most prolific writers explaining what you could actually learn from that data — beyond the health risk estimates provided in the 23andMe interface. This was a genuinely new form of personal science: people analyzing their own genomes with population genetics tools.

## Key points

- Runs of homozygosity: stretches of genome where both chromosomes carry identical alleles — indicates autozygosity from common ancestors
- Inbreeding coefficient: probability that an individual's two copies of a locus are identical by descent — estimated from ROH length distribution
- 23andMe raw data: downloadable SNP genotype file; analyzed with PLINK or custom scripts to compute population genetics statistics
- Direct-to-consumer genomics opened population genetics to personal analysis — the 2013 version of what ancestry services now make automated
- Razib Khan / GNXP: a major node in the early personal genomics and population genetics writing community

[Original](http://blogs.discovermagazine.com/gnxp/2013/01/using-your-23andme-data-how-inbred-are-you/)
