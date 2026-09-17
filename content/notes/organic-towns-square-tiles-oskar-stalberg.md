---
title: Organic Towns from Square Tiles — Oskar Stålberg at IndieCade 2019
date: 2020-07-25
categories:
  - procedural-generation
  - algorithms
  - game-development
  - creativity
  - wave-function-collapse
description: Oskar Stålberg's IndieCade 2019 talk on generating organic-looking towns from square tiles using a constraint-propagation algorithm. A beautiful demonstration of how simple local rules produce complex emergent structure.
params:
  source: pinboard
  sourceUrl: https://www.youtube.com/watch?v=1hqt8JkYRdI
---

## Summary

Oskar Stålberg is a game developer known for Wave Function Collapse (WFC)-inspired procedural generation. This IndieCade talk explains how he generates organic-looking towns, roads, and landscapes from square tiles using a constraint propagation algorithm. The result looks like hand-designed medieval maps despite being entirely algorithmically generated.

The key insight: tile placement is constrained by what tiles can legally neighbor each other (e.g., a road tile must connect to other road tiles at the edges). Constraint propagation — resolving which tiles are possible in each cell based on neighbors, then collapsing the least-constrained cell — produces emergent structure that feels organic because the constraints encode local design rules. Low entropy propagates: placing one tile restricts neighbors, which restricts their neighbors, creating coherent regions from local decisions.

The technique is a variant of the Wave Function Collapse algorithm (Mxgmn, 2016), which Stålberg has evolved for his game projects including Bad North and Townscaper. Townscaper is the direct output of this research: a toy where clicking anywhere generates coherent coastal buildings, bridges, and arches through constraint-propagation tile rules. The aesthetic achievement — clearly algorithmic, but feeling designed — is a useful case study for anyone interested in emergent complexity from simple rule systems.

## Key points

- Wave Function Collapse-style constraint propagation: local tile compatibility rules produce globally coherent structure.
- Process: place tiles by resolving the lowest-entropy cell first, propagating constraints outward.
- Emergent complexity: organic-looking layouts from simple local rules — no global planner required.
- Townscaper is the product of this research — the playable demo of this technique.
- Useful model for thinking about emergent complexity and self-organization beyond games.
- By Oskar Stålberg — also contributed to the WFC algorithm ecosystem; Bad North used earlier version.

[Original](https://www.youtube.com/watch?v=1hqt8JkYRdI)
