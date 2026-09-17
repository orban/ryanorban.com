---
title: "Cinder: The Library for Professional-Quality Creative Coding in C++"
date: 2013-01-21
categories:
  - creative-coding
  - cpp
  - graphics
  - opengl
  - tools
description: Cinder is a C++ library for professional-quality creative coding — graphics, audio, video, computer vision, and OpenGL, all in one framework. The C++ equivalent of Processing, but faster and used for commercial-quality interactive installations.
params:
  source: pinboard
  sourceUrl: http://libcinder.org/
---

## Summary

Cinder is a C++ library developed by The Barbarian Group, a creative technology firm, for building high-performance interactive media applications. Where Processing is the entry-level tool for creative coding (Java-based, approachable, slow), Cinder is the production-quality alternative — it runs at native C++ speed, gives direct access to OpenGL, and has been used for major commercial installations, TV broadcast graphics, and large-scale projection mapping work.

The framework provides wrappers for common creative coding needs: 2D/3D graphics via OpenGL, audio analysis, video playback, image processing, computer vision via OpenCV, networking, and file I/O. The design philosophy is that it should feel like high-level scripting (minimal boilerplate, sensible defaults) while retaining the performance of native code. This made it attractive for work where Processing's Java overhead was a problem — real-time audio visualization, high-frame-rate interactive installations, or anything that needed to push a lot of pixels.

The creative coding community in 2013 was split between Processing (Java, accessible, pedagogically important), openFrameworks (C++, open-source, community-driven), and Cinder (C++, more opinionated, polished, commercially-backed). These three formed the de facto toolkit for the interactive art and generative design world before web technologies like Three.js and p5.js became capable enough to compete.

## Key points

- Cinder vs Processing: same domain (creative coding), different performance tier — Cinder is C++ with near-metal speed; Processing is Java with a simpler API
- Cinder vs openFrameworks: both C++, but Cinder is more opinionated and commercially polished; openFrameworks is more community-driven and permissive
- The Barbarian Group was a prominent creative technology agency; Cinder was their internal tool made public
- Used for: commercial installations, broadcast motion graphics, interactive art requiring real-time performance
- 2013 was the library's peak relevance; web graphics (via WebGL, Three.js, p5.js) later closed the performance gap for many use cases

[Original](http://libcinder.org/)
