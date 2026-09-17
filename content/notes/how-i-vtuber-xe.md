---
title: How I VTuber — Xe Iaso's Setup
date: 2022-01-14
categories:
  - streaming
  - vtubing
  - setup
  - creative
  - tech
description: Xe Iaso's technical walkthrough of their VTubing setup — the software, avatar rigging, face tracking, and streaming stack used to stream as a virtual character while keeping a developer's privacy. Practical guide at the intersection of live coding and virtual avatar streaming.
params:
  source: pinboard
  sourceUrl: https://christine.website/blog/vtubing-setup-2022-01-13
---

## Summary

Xe Iaso (Christine Dodrill) is a developer known for detailed technical blog posts and a distinctive writing style. This post from January 2022 documents their VTubing setup — the practice of streaming online as a virtual animated avatar (a VTuber, popularized by Japanese content creators like Hololive). The motivation for a developer blogger is often privacy: you can be present and expressive on camera without exposing your physical appearance.

The technical stack for VTubing involves several layers: face tracking software that reads webcam input and translates facial expressions to avatar bone movements, an avatar created in VRoid Studio or Live2D, a virtual camera that outputs the rendered avatar as a video feed that streaming software treats like a real webcam, and OBS or similar software to compose the full stream. VTube Studio is the common iOS/Android face tracking app that uses the phone's front-facing camera's depth sensor (originally ARKit on iPhone X+) for high-quality expression capture.

For developers who want to stream live coding, the VTuber approach solves the I don't want to be on camera problem without requiring a static facecam-free setup. Xe's blog post likely covers their specific software versions, configuration choices, and lessons from getting the pipeline to work reliably — the kind of practical detail that's hard to find in tutorial content aimed at gaming audiences.

## Key points

- VTubing = streaming as a virtual avatar; VTube Studio handles face tracking via phone camera
- Avatar rigging: VRoid Studio (3D) or Live2D (2D) for avatar creation; expression bones mapped to face tracking input
- Virtual camera output makes the rendered avatar appear as a standard webcam feed in OBS
- Privacy-preserving option for developers who want video presence without physical exposure
- Xe Iaso writes technically detailed blog posts aimed at developers — this is that style applied to a streaming setup

[Original](https://christine.website/blog/vtubing-setup-2022-01-13)
