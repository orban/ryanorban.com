---
title: Finally a Nanopore Sequencer That Works
date: 2013-04-02
categories:
  - genomics
  - sequencing
  - nanopore
  - biology
  - hardware
description: CoreGenomics blog covering Oxford Nanopore's MinION — the first nanopore sequencer that actually worked reliably in practice. A 2013 milestone post documenting the moment nanopore sequencing moved from theoretical promise to real instrument.
params:
  source: pinboard
  sourceUrl: http://core-genomics.blogspot.nl/2013/03/finally-nanopore-sequencer-that-works.html
---

## Summary

Oxford Nanopore Technologies announced the MinION in 2012 and began its early access program in 2013 — the first commercial nanopore sequencing instrument to demonstrate reliable real-world performance. The CoreGenomics blogger, a sequencing core director, wrote this post from the perspective of someone who had watched many next-generation sequencing promises fail to deliver: nanopore sequencing had been theoretically attractive for over a decade, but the error rates and throughput had never reached practical utility.

The core technology: nanopore sequencing passes a DNA strand through a protein nanopore embedded in a membrane. As each nucleotide transits the pore, it causes a characteristic change in electrical current — the current signal is decoded to identify the base sequence. Unlike Illumina sequencing (which relies on fluorescent dye imaging of short synthesized fragments), nanopore generates long reads directly from native DNA — no amplification required. The potential advantages: read lengths of tens of kilobases (vs. 150bp for Illumina), real-time sequencing output, and a device small enough to hold in your hand.

The practical catch: nanopore signals are noisy, and base-calling (converting current traces to DNA sequence) had high error rates compared to Illumina's sub-1% error rate. The MinION early access program was explicitly a research collaboration — Oxford Nanopore wanted academic users to develop the base-calling algorithms and wet-lab protocols that would improve accuracy. The tradeoff was real: accept higher error rates in exchange for long reads and portability. This was the beginning of a technology arc that by 2020 would make nanopore sequencing genuinely competitive for many genomics applications.

## Key points

- Nanopore sequencing: DNA strand passes through a protein pore; current changes identify each nucleotide in real time without fluorescent labels.
- MinION: Oxford Nanopore's hand-held USB-connected sequencer — the first sequencer designed for field deployment rather than core labs.
- Long read advantage: kilobase-scale reads vs. 150bp short reads from Illumina — critical for resolving repetitive regions and structural variants.
- Error rate tradeoff: 2013 MinION error rates (~15–20%) were high compared to Illumina (~0.1%) — accepted in exchange for length and portability.
- Direct sequencing: no PCR amplification or fluorescent labeling required — enables detection of base modifications (methylation) that Illumina misses.
- Path from 2013 to maturity: error rates improved dramatically over the next 7 years; by 2020 nanopore was production-quality for many applications.

[Original](http://core-genomics.blogspot.nl/2013/03/finally-nanopore-sequencer-that-works.html)
