---
title: Map of Reddit
date: 2022-05-15
categories:
  - reddit
  - visualization
  - community
  - graph
  - data-viz
description: Andrei Kashcha's interactive force-directed graph visualizing Reddit's subreddit communities as a navigable map — clusters emerge from cross-posting and subscriber overlap patterns. A striking example of community structure made visible through graph layout.
params:
  source: pinboard
  sourceUrl: https://anvaka.github.io/map-of-reddit/
---

![Map of Reddit](/images/notes/map-of-reddit.png)

## Summary

[Map of Reddit](/notes/map-of-reddit/) by Andrei Kashcha (anvaka) is an interactive force-directed graph visualization of Reddit's community structure. Subreddits are nodes; edges represent user overlap (people who post in both subreddits). The graph layout algorithm clusters related communities together, producing visible neighborhoods: gaming subreddits cluster, crypto subreddits cluster, progressive politics and conservative politics sit on opposite sides of the graph. The emergent geography makes Reddit's community structure legible in a way that browsing subreddits sequentially never does.

The technical approach uses UMAP or t-SNE-style dimensionality reduction (or force-directed layout directly) applied to the subreddit co-subscription matrix. The result is a zoomable, navigable map where you can see which communities are tightly coupled (frequent cross-posting between programming subreddits) versus loosely connected (sci-fi books and political commentary barely overlap).

This kind of community graph visualization is a recurring pattern in social network analysis — applied to Twitter follow graphs, GitHub contribution networks, and academic citation networks. The Reddit version is particularly striking because the communities are named, so the geographic metaphor resonates: you can literally point to where crypto lives or where the fitness community is relative to everything else.

## Key points

- [Map of Reddit](/notes/map-of-reddit/): force-directed layout of subreddits weighted by user overlap — community structure as geography
- Clusters emerge from behavior, not taxonomy — programming subreddits cluster without being told they're related
- Related work: Twitter community map (similar approach for Twitter), GitHub contribution graphs
- Built by Andrei Kashcha (anvaka), who also built ngraph and other graph visualization tools
- Interesting for community analysis: measuring which communities are bridges vs. isolated, which are growing clusters
- The visualization makes filter bubbles legible — you can see how far apart different political communities sit

[Original](https://anvaka.github.io/map-of-reddit/)
