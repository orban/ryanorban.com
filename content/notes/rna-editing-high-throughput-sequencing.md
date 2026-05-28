---
title: Accurate Identification of RNA Editing Sites from High-Throughput Sequencing Data
date: 2012-04-17
categories:
  - genomics
  - rna
  - bioinformatics
  - sequencing
  - epigenetics
description: A Genomes Unzipped guest post on the bioinformatics challenge of accurately identifying RNA editing sites from high-throughput sequencing data — a technically demanding problem because RNA-DNA differences look similar to sequencing artifacts. Written at the height of the RNA editing research wave.
params:
  source: pinboard
  sourceUrl: http://www.genomesunzipped.org/2012/04/guest-post-accurate-identification-of-rna-editing-sites-from-high-throughput-sequencing-data.php
---

![Accurate Identification of RNA Editing Sites from High-Throughput Sequencing Data](/images/notes/rna-editing-high-throughput-sequencing.png)

## Summary

RNA editing is the post-transcriptional modification of RNA sequences — most commonly the enzymatic conversion of adenosine to inosine (A-to-I editing) by ADAR enzymes. The result is that the RNA sequence at an editing site differs from the underlying DNA template. This was known to be biologically important in a few cases, but the question in 2012 was: how widespread is it, and how do you find all the sites?

The Genomes Unzipped guest post addresses the central methodological challenge: RNA-DNA sequence differences can arise from RNA editing (real biological signal) or from sequencing errors, mapping artifacts, or SNPs (false positives). Naively identifying all positions where the RNA sequence differs from the genome gives a list dominated by noise. The 2011 paper by Li et al. had claimed thousands of RNA editing sites, but subsequent analysis showed that most were artifacts.

The bioinformatics challenge is essentially a false positive problem at scale. With high-throughput sequencing generating millions of reads, even a 0.1% error rate produces enormous numbers of apparent RNA-DNA differences that swamp the real signal. Proper identification requires careful quality filtering, strand-specific sequencing protocols, proper controls, and statistical methods that account for multiple testing.

## Key points

- A-to-I RNA editing by ADAR enzymes is the predominant form in mammals — adenosine reads as guanosine after editing.
- The challenge: distinguishing genuine RNA editing from sequencing error, SNPs, and alignment artifacts requires careful methodology.
- The 2011 Li et al. paper claiming widespread editing was largely retracted after the artifacts were identified — a cautionary tale about early sequencing analysis.
- Proper controls require: matched DNA sequencing from the same sample, strand-specific RNA-seq, duplicate read removal, rigorous variant calling pipelines.
- 2012 was the period when RNA-seq became affordable enough that these questions could be asked systematically, but methods hadn't caught up with the data scale.

[Original](http://www.genomesunzipped.org/2012/04/guest-post-accurate-identification-of-rna-editing-sites-from-high-throughput-sequencing-data.php)
