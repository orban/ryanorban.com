---
title: Digital Sound Processing Tutorial for the Braindead
date: 2013-12-24
categories:
  - dsp
  - audio
  - signal-processing
  - tutorial
  - filters
description: Olli Niemitalo's 1998 beginner DSP tutorial covering filters, FFT, interpolation, and audio synthesis techniques. Honest about its approximations but remains a clear, practical entry point into audio signal processing.
params:
  source: pinboard
  sourceUrl: http://yehar.com/blog/?p=121
---

## Summary

Written by Olli Niemitalo in 1998, this tutorial introduces audio digital signal processing (DSP) for enthusiasts who want practical understanding without requiring a formal signals background. It's refreshingly honest — "it is not entirely accurate in places but may serve as a nice tutorial" — and focuses on intuition and implementation over mathematical rigor.

The tutorial covers the foundational DSP stack: sampled sound and the Nyquist frequency, sine wave decomposition and complex number representation, and the basics of filter design. On the filter side, it explains FIR filters (finite impulse response, stable but computationally expensive) and IIR filters (infinite impulse response, efficient but potentially unstable), plus the pole-zero plot design methodology for IIR filters.

The more advanced sections cover FFT-based filtering with the overlap-add method, interpolation techniques (linear, Hermite interpolation, sinc), frequency shifting via amplitude modulation, and practical effects like the flanger. The musical context (harmonics, chromatic scale, wavetable synthesis) grounds the math in audible results.

## Key points

- Covers FIR filters vs IIR filters: FIR is always stable, IIR is efficient but requires careful design to avoid instability.
- Pole-zero design for IIR filters — place poles near the unit circle to create resonances, zeros to create notches.
- FFT-based filtering with overlap-add: efficient for long FIR filters (convolution in frequency domain).
- Interpolation: linear → cheap but audible artifacts; Hermite interpolation → better for audio; sinc → ideal but expensive.
- Applications: flanger effect, wavetable synthesis, frequency shifting, allpass/bandpass/notch filters.
- Nyquist theorem: must sample at 2× the highest frequency to avoid aliasing — the foundational constraint of all digital audio.

[Original](http://yehar.com/blog/?p=121)
