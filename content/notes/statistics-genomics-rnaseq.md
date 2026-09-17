---
title: "Statistics for Genomics: Introduction to RNA-seq"
date: 2013-01-28
categories:
  - genomics
  - rna-seq
  - statistics
  - bioinformatics
  - education
description: A YouTube lecture series on statistical methods for RNA-seq analysis — covering the mathematical foundations behind differential expression analysis, normalization, and count modeling. A bioinformatics education resource from the early RNA-seq era.
params:
  source: pinboard
  sourceUrl: https://www.youtube.com/watch?v=C8RNvWu7pAw
---

![Statistics for Genomics: Introduction to RNA-seq](/images/notes/statistics-genomics-rnaseq.png)

## Summary

RNA-seq (RNA sequencing) was becoming the dominant method for transcriptome analysis by 2013, replacing microarray technology. Where microarrays measure hybridization intensity for a fixed set of probes, RNA-seq counts actual sequencing reads mapping to transcripts — giving digital counts rather than analog intensities, with better dynamic range and the ability to discover novel transcripts not represented on any array.

This lecture series covers the statistical foundations: why raw read counts can't be compared directly across samples (library size differences require normalization), why count data fits a negative binomial distribution better than a Poisson (overdispersion is ubiquitous in biological data), and how differential expression analysis (finding genes that change between conditions) accounts for variability in biological replicates. Tools like DESeq2 and edgeR implement these statistical models.

The landscape in 2013 was still early: reference genomes for model organisms were good but annotation was incomplete, alignment tools (STAR, TopHat) were new, and best practices for RNA-seq analysis pipelines were still being established. The statistical questions were genuine research problems, not settled methodology — this lecture series was filling a gap between sequencing becoming affordable and statisticians catching up with how to analyze the data properly.

## Key points

- RNA-seq: sequence-based transcriptome quantification — reads mapped to reference genome, counted per gene; replaced microarray for most transcriptomics
- Normalization: required before comparing counts across samples; methods include TMM, DESeq2 size factor estimation, RPKM/FPKM/TPM
- Negative binomial model: appropriate for count data with overdispersion (variance > mean); Poisson underestimates variability in biological replicates
- Differential expression: statistical testing for count differences between conditions; DESeq2 and edgeR are the standard tools, both R packages
- Bioinformatics pipeline: fastq → align (STAR/HISAT2) → count (HTSeq/featureCounts) → normalize → differential expression

[Original](https://www.youtube.com/watch?v=C8RNvWu7pAw)
