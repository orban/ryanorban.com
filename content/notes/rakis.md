---
title: "Rakis Stability Test 1: Results from a Month of Running an AI Network"
date: 2024-07-19
categories:
  - decentralized-ai
  - p2p
  - browser-ai
  - inference
  - distributed-systems
description: "Rakis ran Stability Test 1: a month-long production test of a fully in-browser peer-to-peer AI inference network. 10 million tokens across ~2,000 nodes with embedding-based consensus for verification — early evidence that browser-native decentralized AI inference is viable."
params:
  source: pinboard
  sourceUrl: https://olickel.com/rakis-st1
---

![Rakis Stability Test 1: Results from a Month of Running an AI Network](/images/notes/rakis.png)

## Summary

[Rakis](/notes/rakis/) is a peer-to-peer AI inference network that runs entirely in web browsers — no central servers, distributed via Vercel, Hugging Face, or self-hosted. Stability Test 1 (ST1) was a month-long production test of the system. The results: 10 million tokens processed, 2,000+ nodes participating, and 25%+ of visitors submitting inference requests.

The architectural bet here is significant: WebGPU and WebAssembly have made in-browser ML inference practical, and WebRTC-based P2P networking means you can build a distributed compute network without any infrastructure. [Rakis](/notes/rakis/) combines these — your browser becomes both a node in the inference network and a client consuming inferences from other nodes. The consensus mechanism uses embedding-based clustering to verify that different nodes produced consistent outputs for the same prompt.

The consensus results are interesting: 27.7% of quorums achieved 100% agreement, which improved to 85.8% when corrected for network transmission delays. The main challenge was network partitioning — nodes couldn't always see identical inference data. Despite that, the system maintained stable throughput through the month. At the time of saving (2024), this was early-stage research; it's a useful data point on where browser-based decentralized AI was in mid-2024.

## Key points

- First completely in-browser P2P AI inference network — no central servers.
- ~2,000 nodes, 10M tokens, 1,000+ AI workers in Stability Test 1.
- 25%+ of visitors submitted inference requests; 15%+ ran AI models in their browsers.
- Embedding-based consensus for verifying inference consistency across nodes.
- 85.8% quorum agreement when corrected for transmission delays.
- Network partitioning emerged as the primary architectural challenge.
- Validates premise: WebGPU + WebAssembly + WebRTC can sustain distributed inference.

[Original](https://olickel.com/rakis-st1)
