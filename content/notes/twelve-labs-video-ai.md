---
title: Twelve Labs — Video Understanding API
date: 2022-11-25
categories:
  - video-ai
  - multimodal
  - search
  - api
  - computer-vision
description: Twelve Labs provides a video understanding API that lets developers search, retrieve, and understand video content semantically — as if the model could actually watch and comprehend it. Fills the gap between text search and the dense information in video.
params:
  source: pinboard
  sourceUrl: https://twelvelabs.io/
---

## Summary

Twelve Labs builds video understanding infrastructure — models that can see, listen to, and comprehend video the way humans do, exposed via an API for developers. The core capability is semantic video search: rather than searching by transcript keywords or metadata tags, you can query a video library with natural language and retrieve relevant clips. "Find all moments where someone demonstrates how to reset the router" would work across a corpus of support videos.

The product sits at the intersection of several hard problems. Video is information-dense in a way that makes it expensive to process — you have visual frames, audio, speech, and often on-screen text, all carrying signal. Multimodal understanding that fuses these modalities rather than processing them independently is technically difficult and, as of 2022, not widely available as an API. Twelve Labs' models (including Marengo for search and Pegasus for generation) aim to do this fusion well.

The use cases the company targets: media and entertainment (searching rushes footage), e-learning (finding relevant moments in lecture recordings), security (video surveillance search), and user-generated content moderation. The developer pitch is API-first: index a video, run queries against it, get timestamps and segments back. As video generation has accelerated with Sora and similar models, the inverse problem — understanding and organizing video — has become a matching infrastructure need.

## Key points

- Semantic video search API: query video libraries with natural language, get relevant clips and timestamps.
- Multimodal understanding fusing visual, audio, and speech signals rather than treating them independently.
- Two model families: Marengo (search/retrieval) and Pegasus (video generation/understanding).
- Target verticals: media, e-learning, security, UGC moderation.
- Developer-friendly API: index → query → retrieve clips.
- Addresses the inverse of video generation — as video creation scales, video understanding becomes critical infrastructure.

[Original](https://twelvelabs.io/)
