---
title: "ABX: Blind Audio Comparison Testing"
date: 2022-03-31
categories:
  - audio
  - testing
  - psychoacoustics
  - tools
  - open-source
description: ABX by jaakkopasanen is an open-source tool for conducting blind A/B/X audio comparison tests — the gold standard for objectively evaluating whether two audio signals are perceptibly different. Used for testing headphone EQ curves, codecs, and audio processing.
params:
  source: pinboard
  sourceUrl: https://github.com/jaakkopasanen/ABX
---

## Summary

ABX testing is the gold standard methodology for determining whether two audio signals are perceptibly different — and this tool by Jaakko Pasanen (the creator of AutoEQ) implements it as a free, open-source application. The test structure: listener hears sample A, sample B, and an unknown sample X (which is secretly either A or B); the listener must identify whether X matches A or B. Without being able to consciously remember and compare, many perceived "obvious" differences in audio quality disappear — the test cuts through expectation bias and placebo effects.

The ABX test's statistical power comes from repetition. A single X identification could be luck; 10-16 trials produce statistically meaningful results. If a listener can consistently identify X at better-than-chance rates (p < 0.05), the audible difference is real. If not, the signals are perceptibly equivalent under blind conditions, regardless of what measurements show. This is why ABX testing regularly demonstrates that expensive audio equipment, high-bitrate codecs, and elaborate signal processing are inaudible under controlled conditions — a deeply uncomfortable result for audiophile culture.

Jaakko Pasanen is known in the headphone community for AutoEQ, a project that provides pre-computed EQ filters derived from headphone measurements to correct frequency response deviations. ABX testing is the natural companion tool: after applying an EQ curve, you'd use ABX to verify whether the EQ actually changed the perceptible sound quality, or whether it's a placebo. The tool also serves codec testing (can you hear MP3 at 320kbps vs. FLAC?), DAC comparison, and any other situation where you need a rigorous double-blind assessment.

## Key points

- ABX testing: blind A/B/X comparison — identify whether unknown X matches A or B, repeated to achieve statistical significance.
- Eliminates expectation bias: without knowing which is which, many "obvious" audio differences become undetectable.
- Statistical framework: 10-16 trials minimum for p < 0.05 confidence — short tests don't produce reliable results.
- By Jaakko Pasanen, author of AutoEQ — the headphone measurement and EQ correction project.
- Practical uses: codec comparison (MP3 vs. FLAC), EQ effectiveness verification, DAC/amplifier evaluation.
- An open-source implementation of the Foobar2000 ABX Comparator concept, platform-independent.

[Original](https://github.com/jaakkopasanen/ABX)
 → GitHub
