---
title: Dat Project — Open Data Infrastructure
date: 2014-08-20
categories:
  - open-data
  - data-infrastructure
  - open-source
  - collaboration
description: Wired profile of Max Ogden and the Dat Project — a decentralized, versioned data sharing protocol designed to make scientific and public datasets as easy to share and update as code on GitHub. An ambitious vision for open data infrastructure that was ahead of its time.
params:
  source: pinboard
  sourceUrl: http://www.wired.com/2014/08/dat/
---

## Summary

Max Ogden's Dat Project was profiled in Wired in August 2014 as a vision for what open data infrastructure could look like if designed from the ground up. Dat was conceived as a "Git for data" — a decentralized, versioned, streaming protocol for sharing and updating large datasets that are too big or too mutable for GitHub to handle well.

The problem Dat addressed: scientific datasets and public datasets change over time, but there was no good way to version and distribute those changes. A CSV file on a government website gets updated without versioning; anyone who downloaded yesterday's version doesn't know it changed. Git solves this for code but was never designed for binary blobs, large files, or streaming updates. Dat would handle datasets the way BitTorrent handles files — decentralized, peer-to-peer — but with version history and the ability to subscribe to updates.

Max Ogden was working at the intersection of open data, [Node.js](/notes/nodejs/) (he was a core contributor), and civic tech. The Dat Project was funded by a Knight Foundation grant and positioned as infrastructure for open government data and scientific reproducibility. It later influenced thinking around IPFS and decentralized data sharing.

## Key points

- Dat Project: decentralized, versioned data sharing protocol — "Git for data" with streaming and BitTorrent-style distribution.
- Problem: large datasets change without versioning — no way to track or subscribe to updates.
- Built on [Node.js](/notes/nodejs/) by Max Ogden, funded by Knight Foundation.
- Target use cases: scientific datasets, government open data, reproducible research.
- Dat's data structures (hypercore, hyperdrive) later influenced IPFS and Hypercore Protocol.
- Ahead of its time in 2014 — the decentralized data vision has been partially realized through Hugging Face Datasets and DVC.

[Original](http://www.wired.com/2014/08/dat/)
