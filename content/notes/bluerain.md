---
title: Bluerain
date: 2024-12-14
categories:
  - visualization
  - bluesky
  - generative-art
  - real-time
  - creative-coding
description: Bluerain visualizes the Bluesky firehose as Matrix-style falling text rain — each character stream is a live post flowing through the AT Protocol. A beautiful way to sense the scale and flow of social network activity.
params:
  source: pinboard
  sourceUrl: https://simone.computer/bluerain/
---

![Bluerain](/images/notes/bluerain.png)

## Summary

[Bluerain](/notes/bluerain/) is a visual experiment by Simone Computer that renders the live Bluesky firehose as a Matrix-style digital rain. Instead of green characters falling through a CRT screen, you're watching real posts from the AT Protocol firehose rendered as cascading text. Each column of characters represents live content flowing through the network in real time.

The Bluesky firehose is the unfiltered stream of all public events on the AT Protocol network — posts, reposts, likes, follows, profile updates — available as a WebSocket stream. It's one of the unique affordances of AT Protocol's open architecture compared to closed platforms: you can access the full event stream programmatically without special permission. [Bluerain](/notes/bluerain/) uses this to create a generative visualization that's both aesthetically compelling and informative about network activity.

The piece sits in a tradition of social network data visualizations that make the scale of real-time human communication viscerally perceivable. Related to projects like Firehose.social, other AT Protocol tooling, and the creative coding aesthetic that treats live data as material. Made by Simone Computer (simone.computer), who makes other web-based generative and interactive work.

## Key points

- Live Bluesky firehose rendered as Matrix-style falling text rain.
- Uses AT Protocol's open WebSocket event stream — a unique affordance of the decentralized architecture.
- Real-time: you're seeing actual posts as they happen.
- Generative visualization that makes network scale physically perceivable.
- From Simone Computer — related to the broader creative coding data visualization tradition.

[Original](https://simone.computer/bluerain/)
