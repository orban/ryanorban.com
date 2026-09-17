---
title: WebCamMesh — 3D Webcam Visualization
date: 2013-02-09
categories:
  - webgl
  - three-js
  - creative-coding
  - webcam
  - computer-vision
description: WebCamMesh uses WebGL and the browser's webcam API to create a real-time 3D mesh from the live video feed — mapping webcam pixel brightness to vertex displacement. An early example of combining browser camera access with WebGL for real-time visual effects.
params:
  source: pinboard
  sourceUrl: http://airtightinteractive.com/demos/js/webcammesh/
---

![WebCamMesh — 3D Webcam Visualization](/images/notes/webcammesh-webgl.png)

## Summary

Airtight Interactive built WebCamMesh to demonstrate combining the browser's getUserMedia webcam API with WebGL rendering via Three.js. The content field notes this was shared with a @stamen tag — Stamen Design, the data visualization studio, suggesting the visualization context.

The technique: access the webcam stream via `getUserMedia`, sample pixel brightness values from each frame, and map those brightness values to the Y-displacement of a grid of vertices in a 3D mesh. Bright pixels push vertices toward the camera, dark pixels pull them away — creating a real-time 3D relief map of the webcam image. The result is your face rendered as a rippling 3D landscape.

What made this notable in early 2013: `getUserMedia` had only been standardized in HTML5 recently, and combining it with WebGL was still experimental territory. The browser had become a platform for real-time computer vision and interactive graphics — capabilities that previously required native apps or Flash plugins. This fit the broader narrative of WebGL and HTML5 APIs expanding what was possible in the browser without plugins.

## Key points

- getUserMedia API: allows browser-based webcam access without plugins — standardized in 2012-2013, enabling a wave of browser-based camera experiments
- Pixel-to-vertex displacement technique: sample image brightness → drive mesh geometry → creates a real-time 3D relief map from the video stream
- Combines two emerging browser capabilities: WebGL (3D rendering) and getUserMedia (camera access) — neither was universally supported in 2013
- Airtight Interactive was part of the browser creative coding community along with Chrome Experiments, three.js, and similar groups
- Stamen Design was tagged — their work in data visualization and interactive cartography made real-time WebGL experiments relevant to them

[Original](http://airtightinteractive.com/demos/js/webcammesh/)
