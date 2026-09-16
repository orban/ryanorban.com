---
title: "SeqAlign: Sequence Alignment Visualization"
date: 2013-10-06
categories:
  - bioinformatics
  - sequence-alignment
  - visualization
  - algorithms
  - dna
description: SeqAlign is a browser-based DNA/protein sequence alignment visualization tool by Chris Fenton. A clean interface for a foundational bioinformatics algorithm — useful for understanding how pairwise alignment works visually.
params:
  source: pinboard
  sourceUrl: http://www.chrisfenton.com/seqalign/
---

## Summary

SeqAlign by Chris Fenton is a web-based visualization tool for sequence alignment — the fundamental bioinformatics algorithm for comparing DNA, RNA, or protein sequences to find regions of similarity. The tool makes the dynamic programming matrix used in alignment algorithms (like Needleman-Wunsch for global alignment or Smith-Waterman for local alignment) visible and interactive.

Sequence alignment underlies much of modern genomics: finding where a sequenced read maps to a reference genome, identifying homologous genes across species, detecting mutations relative to a reference. The algorithms use dynamic programming to fill a matrix of match/mismatch/gap scores and then trace back the optimal alignment path. Visualizing this matrix helps build intuition for how the alignment is computed rather than treating it as a black box.

Saved during a period when Ryan was exploring the intersection of data science and biological applications — bioinformatics was an area where machine learning and statistical methods were being actively applied. The sequence alignment problem also illustrates general dynamic programming principles applicable beyond biology.

## Key points

- Sequence alignment: finding the optimal match between two sequences accounting for substitutions, insertions, and deletions.
- Algorithms: Needleman-Wunsch (global, full-length alignment) and Smith-Waterman (local, best-matching substring).
- Both use dynamic programming — SeqAlign visualizes the DP matrix and traceback path.
- Foundational to bioinformatics: read mapping, comparative genomics, variant calling all depend on fast sequence alignment.
- Connection to general dynamic programming: the edit distance / Levenshtein distance problem is the same algorithm applied to strings generally.

[Original](http://www.chrisfenton.com/seqalign/)
