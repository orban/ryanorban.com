---
title: Collada Animation Viewer
date: 2013-02-12
categories:
  - three-js
  - collada
  - 3d
  - webgl
  - animation
description: A Three.js-based COLLADA animation viewer running in the browser — demonstrating that complex rigged 3D models exported from tools like Blender or Maya could be rendered and animated in WebGL via Three.js.
params:
  source: pinboard
  sourceUrl: http://n.ethz.ch/~crobi/threejs-collada/view.html
---

## Summary

This ETH Zurich experiment demonstrated loading and animating COLLADA (`.dae`) files in the browser using Three.js. COLLADA is an XML-based 3D asset interchange format developed by Sony, widely supported by 3D modeling tools like Blender, Maya, and 3ds Max — making it a bridge between professional 3D content creation and web rendering.

The significance: in 2013, getting a rigged, animated 3D character from a modeling tool into the browser required a working pipeline — export to COLLADA, load via Three.js's `ColladaLoader`, parse the skeletal animation rig and keyframe data, and drive the animation via requestAnimationFrame. This demo showed that pipeline working end-to-end.

Bookmarked alongside the Three.js getting-started tutorial and [CSS 3D Clouds](/notes/css-3d-clouds/), this reflects a period of rapid exploration of browser 3D capabilities. The set of bookmarks suggests interest in what was possible in the browser for interactive 3D, whether for data visualization, creative projects, or games.

## Key points

- COLLADA (`.dae`): the standard interchange format for 3D assets between tools — Blender, Maya, Cinema 4D all export it
- Three.js `ColladaLoader` parses the COLLADA XML structure, extracts geometry, materials, and skeletal animation data
- Skeletal animation in 3D: bones define a rig; vertex weights determine how geometry deforms when bones move — the foundation of character animation
- The WebGL pipeline in 2013: asset creation in professional tools → COLLADA export → Three.js loading → browser rendering — all viable but requiring significant engineering
- glTF (GL Transmission Format) has largely replaced COLLADA for web 3D — designed specifically for efficient real-time delivery, more compact and faster to parse

[Original](http://n.ethz.ch/~crobi/threejs-collada/view.html)
