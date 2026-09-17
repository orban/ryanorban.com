---
title: "GPS: How the Global Positioning System Works"
date: 2022-01-18
categories:
  - gps
  - navigation
  - physics
  - interactive
  - education
  - signal-processing
description: Bartosz Ciechanowski's interactive explainer on how GPS works — from trilateration fundamentals through satellite orbital design, pseudorandom codes, and relativistic clock corrections. One of the best pieces of technical writing on the web.
params:
  source: pinboard
  sourceUrl: https://ciechanow.ski/gps/
---

![GPS: How the Global Positioning System Works](/images/notes/gps-interactive-explainer.png)

## Summary

Bartosz Ciechanowski's GPS explainer is one of the best pieces of technical writing on the web — a long-form interactive article that builds understanding of GPS from first principles through the kind of progressive conceptual development that textbooks rarely achieve. Each concept is introduced with an interactive visualization before the math, which inverts the usual order and works far better for building intuition.

The article starts with trilateration — how intersecting spheres of known radius around known points locate a position in 3D space. Then it shows why time-of-flight measurement (radio signals traveling at the speed of light) provides the distance measurements, and why receiver clocks don't need perfect synchronization (the system solves for position AND clock bias simultaneously using a fourth satellite). The orbital design section explains why 30 satellites in six inclined orbits achieves global coverage better than geostationary satellites. The signal encoding section covers pseudorandom codes that let receivers identify individual satellites and decode navigation data through noise.

The piece doesn't stop at the basics: it addresses relativistic time dilation (GPS satellites are traveling fast and are in weaker gravity than Earth surface — both effects shift clocks measurably, and uncorrected GPS would drift by kilometers per day). This is the kind of depth that makes the article both technically complete and genuinely surprising to read.

## Key points

- Trilateration: intersecting spheres of time-of-flight distance measurements from satellites at known orbital positions.
- Receiver clocks need no synchronization: four satellites solve for x, y, z AND clock bias simultaneously.
- Orbital design: 30 satellites in 6 inclined orbits — achieves global coverage without geostationary altitude (which creates delays).
- Pseudorandom codes: each satellite broadcasts a unique code, letting receivers identify sources and decode signal through noise.
- Special relativity + general relativity: satellite clocks run fast (less gravity) and slow (high velocity) — uncorrected error would reach km/day.
- One of Bartosz Ciechanowski's explainer series — consistently among the best interactive educational content online.

[Original](https://ciechanow.ski/gps/)
