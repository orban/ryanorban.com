---
title: Do Androids Grow Electric Plants?
date: 2022-01-29
categories:
  - generative-art
  - simulation
  - particle-systems
  - creative-coding
  - interactive
description: Alex's technical notes on SPACEFILLER's digital plant simulations — particle systems with repulsive forces, spring connections, friction, and Boids-inspired velocity matching that produce organic-looking lo-fi animated plants. A good introduction to particle simulation forces for creative coding.
params:
  source: pinboard
  sourceUrl: https://notes.spacefiller.space/living-wall/
---

## Summary

These notes by Alex (SPACEFILLER) document the technical implementation of algorithmically generated plant simulations — the engine behind a 2018 permanent installation called "Living Wall" and a series of generative posters. It's a clear, accessible explanation of how a small set of particle system forces combine to produce convincingly organic-looking plant forms.

The simulation runs at 60fps, with each frame's state derived from the previous one. Particles are the atoms of the system: position and velocity vectors that get updated each frame. The forces are the interesting part: repulsive forces keep particles from overlapping; spring forces connect particles and maintain desired separation distances (creating the structural skeleton of the plant); friction prevents unbounded acceleration; a flattening force smooths out zigzag patterns in chains; and velocity-matching behavior inspired by Craig Reynolds' Boids algorithm creates flocking-like coordination between nearby particles.

What's notable about this approach: complex, organic-looking behavior emerges from simple local rules applied to many particles. There's no top-down specification of "this is a branch shape" — the branch shape emerges from particles following forces. This is the emergent behavior paradigm in creative coding, and it's why particle systems remain a useful primitive for generative art decades after their introduction.

## Key points

- Six force types: repulsion, spring connections, friction, flattening, velocity-matching (Boids-inspired) — organic forms emerge from local rules.
- Craig Reynolds' Boids velocity-matching: nearby particles align velocities, producing flocking-like coordination without global coordination.
- Emergent behavior: plant shape not specified but emerges from particle interactions — the foundation of generative art with natural aesthetics.
- 60fps update loop; each frame fully determined by previous state — deterministic simulation, reproducible from any seed.
- Related: creative coding, generative art, particle systems, Processing, p5.js — common tools for this kind of simulation.

[Original](https://notes.spacefiller.space/living-wall/)
