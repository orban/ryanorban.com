---
title: Getting Started with Three.js
date: 2013-02-12
categories:
  - three-js
  - webgl
  - 3d
  - javascript
  - creative-coding
description: Paul Lewis's introductory Three.js tutorial on Aerotwist — setting up a renderer, camera, and scene to build browser-based 3D graphics. The canonical 2013 entry point for WebGL development via the Three.js abstraction layer.
params:
  source: pinboard
  sourceUrl: http://www.aerotwist.com/tutorials/getting-started-with-three-js/
---

## Summary

Paul Lewis (Aerotwist) published this tutorial as one of the most widely shared introductions to Three.js — the JavaScript library that abstracts WebGL into a usable API for 3D graphics in the browser. The saved content shows the foundational boilerplate: setting up scene dimensions, camera attributes, creating a `WebGLRenderer`, `PerspectiveCamera`, and `Scene`, positioning the camera back from origin, and attaching the renderer's DOM element to the page.

```javascript
var renderer = new THREE.WebGLRenderer();
var camera = new THREE.PerspectiveCamera(VIEW_ANGLE, ASPECT, NEAR, FAR);
var scene = new THREE.Scene();
camera.position.z = 300;
renderer.setSize(WIDTH, HEIGHT);
```

This boilerplate encapsulates what makes Three.js valuable: raw WebGL requires hundreds of lines of GLSL shader code and API setup for a basic scene. Three.js reduces that to a dozen lines of familiar JavaScript. In 2013, WebGL had just achieved broad browser support (Chrome, Firefox, Safari), and Three.js was the dominant library for exploiting it.

The tutorial would go on from this setup to add geometric objects (spheres, cubes), materials (Phong, Lambert, MeshBasic), lighting (point lights, directional lights, ambient), and animations via `requestAnimationFrame`.

## Key points

- Three.js abstracts WebGL's low-level GLSL/buffer/state-machine API into JavaScript objects — the scene graph model (scene → mesh → geometry + material) is far more ergonomic
- `PerspectiveCamera(fov, aspect, near, far)`: field of view in degrees, aspect ratio, near/far clipping plane — the four parameters of a frustum
- WebGL had just achieved broad browser support in 2012-2013: Chrome, Firefox, Safari all supported it; IE did not yet
- Paul Lewis (Aerotwist) was an influential figure in browser performance and creative web development — his tutorials set standards for clarity
- Three.js created by Mr.doob (Ricardo Cabello) — still the dominant browser 3D library, though Babylon.js and native WebGPU are notable alternatives

[Original](http://www.aerotwist.com/tutorials/getting-started-with-three-js/)
