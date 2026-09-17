---
title: slitscanner.js by Sha Hwang
date: 2013-01-17
categories:
  - creative-coding
  - javascript
  - video
  - visualization
  - tools
description: Sha Hwang's slitscanner bookmarklet applies slit-scan photography to YouTube and Vimeo videos in the browser — collapsing a spatial slice through time to produce streak-style images. A clever application of a classic experimental film technique to browser video.
params:
  source: pinboard
  sourceUrl: http://sketches.postarchitectural.com/slitscanner/
---

## Summary

Sha Hwang built a JavaScript bookmarklet that applies slit-scan photography to web videos. Slit-scanning is a technique from experimental photography and film: instead of capturing the entire frame at one moment, you capture a narrow strip (the slit) from each successive frame and stack them. The result collapses time into a spatial dimension — a moving object leaves a streak, a still background repeats uniformly, and the image becomes a visual record of motion over time rather than position at a moment.

The classic reference for slit-scanning is Douglas Trumbull's work on the stargate sequence in 2001: A Space Odyssey (1968) and the time-distortion effects in that film. In the digital era, slit-scan effects appeared in music videos, art installations, and as a technique for visualizing motion capture data. Hwang's contribution was making it trivially accessible: drag the bookmarklet to your browser, go to a YouTube or Vimeo video, click it, and watch the page transform.

Sha Hwang was part of the data visualization and creative coding community in San Francisco in the early 2010s — he worked with Stamen Design and was known for elegant, technically precise work. The slitscanner was a side project that demonstrated his fluency with canvas API manipulation, video scrubbing, and the kind of playful browser experimentation that defined that scene.

## Key points

- Slit-scan photography: a time-based imaging technique that replaces all space at one time with "one spatial slice across all time" — reveals motion as geometry
- Built as a bookmarklet: runs on any YouTube or Vimeo page, no installation — a one-click demo of the technique
- Canvas API: JavaScript's low-level drawing interface; the bookmarklet reads video pixels frame by frame and writes them as vertical strips onto a canvas
- Sha Hwang / Stamen Design: prominent in the 2010s SF data visualization scene; known for technically accomplished, aesthetically precise work
- The technique connects to experimental film, time-lapse photography, and the broader idea of using visualization to reveal temporal structure

[Original](http://sketches.postarchitectural.com/slitscanner/)
