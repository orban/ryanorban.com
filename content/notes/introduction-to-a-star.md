---
title: Introduction to A*
date: 2014-07-22
categories:
  - algorithms
  - pathfinding
  - graph-search
  - interactive
  - visualization
description: Amit Patel's interactive introduction to pathfinding algorithms, building from breadth-first search through Dijkstra's to A* — the standard reference for understanding the A* algorithm's design rationale. The interactive diagrams make the tradeoffs between algorithms immediately tangible.
params:
  source: pinboard
  sourceUrl: http://www.redblobgames.com/pathfinding/a-star/introduction.html
---

## Summary

Amit Patel's tutorial on Red Blob Games is the canonical visual introduction to the A* algorithm. It builds up from simpler algorithms — starting with breadth-first search, then Dijkstra's algorithm, then greedy best-first search — before introducing A* as the synthesis that gets the best of both. This layered approach makes the design rationale clear: each step adds a capability the previous algorithm lacked.

Breadth-first search explores uniformly in all directions, guaranteeing shortest path in an unweighted graph but wasting effort on irrelevant areas. Dijkstra's algorithm adds edge weights — it finds the lowest-cost path in a weighted graph but still explores without directional guidance. Greedy best-first search uses a heuristic to aim toward the goal, which is fast but not always optimal. A* combines Dijkstra's cost-from-start with a heuristic for estimated cost-to-goal: f(n) = g(n) + h(n). This makes it both optimal (when the heuristic is admissible) and efficient (it avoids exploring irrelevant regions).

The interactive diagrams let you change the map, place walls, and watch each algorithm explore in real time — making the tradeoffs visceral rather than abstract. The page has become the standard reference for anyone implementing pathfinding for game development or robotics.

## Key points

- A* = Dijkstra's algorithm + heuristic function — the heuristic guides exploration toward the goal without sacrificing optimality.
- An admissible heuristic never overestimates actual cost, guaranteeing optimal paths. Euclidean distance and Manhattan distance are common choices.
- Priority queue implementation is critical for performance — the open set needs efficient minimum extraction.
- The heuristic weight tradeoff: a more aggressive heuristic (weighted A*) finds paths faster but may sacrifice optimality.
- Applies directly to game AI, robot motion planning, navigation meshes, and GPS routing — any domain with traversal costs on a graph.

[Original](http://www.redblobgames.com/pathfinding/a-star/introduction.html)
