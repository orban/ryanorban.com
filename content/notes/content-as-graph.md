---
title: Displaying Content as a Graph
date: 2024-01-01
categories:
  - information-architecture
  - knowledge-graph
  - web-design
  - ux
  - hypertext
description: An exploration of displaying web content as a graph rather than a hierarchy — examining the advantages of non-linear navigation, the pitfalls of disorienting users, and case studies of sites that have tried it. Advocates for graph structures where meaningful relationships exist between content nodes.
params:
  source: pinboard
  sourceUrl: https://thisisimportant.net/posts/content-as-a-graph/
---

![Displaying Content as a Graph](/images/notes/content-as-graph.png)

## Summary

Most web content is organized as a strict hierarchy: site → section → article. This maps cleanly to URLs and menus but imposes a tree structure on information that often has richer relationships. This piece explores what web content navigation would look like if it surfaced those relationships as a knowledge graph rather than a directory tree.

The argument for graph-based content is that human knowledge doesn't naturally fit hierarchies. A concept appears across multiple articles, articles reference each other laterally, and the same content can be legitimately "in" multiple categories simultaneously. Roam Research, Obsidian, and Wikipedia all demonstrate that graph-based navigation adds discovery value that pure hierarchy loses — you find things you weren't looking for by following connections.

The pitfalls are real: graph navigation can disorient users who expect spatial consistency (breadcrumbs, back buttons, known hierarchy). The node-link diagram visual that graph databases use for schemas becomes confusing at web scale. The article presumably examines case studies of attempts to surface graph structure in web UIs and analyzes which worked. The conclusion likely argues for selective use — graph relationships make sense where genuine conceptual connections exist, not as a universal replacement for hierarchy.

## Key points

- Tree hierarchy is a default web convention, not a fundamental requirement of content navigation.
- Graph structures surface lateral relationships that hierarchies bury — improves discovery.
- Tools like Obsidian, Roam Research, and Wikipedia demonstrate graph navigation value at scale.
- Key pitfall: disorientation — users lose spatial context when expected hierarchy is absent.
- Graph navigation works best where genuine multi-directional relationships exist in the content.
- Tension between information architecture for findability vs. exploration.

[Original](https://thisisimportant.net/posts/content-as-a-graph/)
