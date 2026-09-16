---
title: "GenomeBrowse: Free Tool for Visualizing DNA-seq and RNA-seq BAM Files"
date: 2013-01-28
categories:
  - genomics
  - bioinformatics
  - visualization
  - tools
  - bam
  - rna-seq
description: GenomeBrowse from Golden Helix — a free desktop genome browser for visualizing DNA-seq and RNA-seq BAM files. A 2013 alternative to IGV for exploring aligned sequencing data.
params:
  source: pinboard
  sourceUrl: http://www.goldenhelix.com/GenomeBrowse/
---

![GenomeBrowse: Free Tool for Visualizing DNA-seq and RNA-seq BAM Files](/images/notes/genomebrowse-visualization.png)

## Summary

GenomeBrowse is a desktop genome browser developed by Golden Helix for visualizing aligned sequencing data in BAM format. It was designed to compete with the Integrative Genomics Viewer (IGV) from the Broad Institute — the standard tool in 2013 for browsing aligned reads, coverage tracks, variants, and annotations alongside a reference genome.

A genome browser lets you navigate the reference genome as a coordinate space and overlay multiple data tracks: raw aligned reads (showing individual read pileups), coverage depth, variant calls (VCF files), gene annotations, and computational predictions. For RNA-seq data, you can see splice junctions (reads spanning exon-exon boundaries), alternative splicing, and coverage differences between samples. For DNA-seq, you see variant sites, read depth, and allele frequency.

Golden Helix positioned GenomeBrowse as faster and more accessible than IGV, which could struggle with large BAM files on modest hardware. The tool was free for personal use, which was unusual for commercial bioinformatics software and reflected the broader shift in the field toward free-at-the-point-of-use tools. IGV remained the standard tool for most researchers.

## Key points

- BAM file: Binary Alignment Map — compressed binary version of SAM; standard format for storing aligned sequencing reads
- Genome browser: software that lets you navigate the genome as a coordinate space, overlaying reads, coverage, variants, and annotations
- Golden Helix: bioinformatics software company based in Montana; known for SVS (statistical genetic analysis) and GenomeBrowse
- Competing tools: IGV (Broad Institute, free), UCSC Genome Browser (web-based), Ensembl (web-based)
- 2013 context: BAM files were routine for sequencing labs; visualization tools were critical for quality control and exploratory analysis

[Original](http://www.goldenhelix.com/GenomeBrowse/)
