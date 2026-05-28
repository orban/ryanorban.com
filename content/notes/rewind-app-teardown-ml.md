---
title: Tearing Down the Rewind App
date: 2023-01-20
categories:
  - ml
  - macos
  - reverse-engineering
  - ocr
  - privacy
description: Kevin Chen's technical teardown of the Rewind app — which records your entire screen continuously while claiming not to tax system resources. The teardown reveals clever use of on-device Apple ML frameworks, differential compression, and local OCR to make this technically feasible.
params:
  source: pinboard
  sourceUrl: https://kevinchen.co/blog/rewind-ai-app-teardown/
---

![Tearing Down the Rewind App](/images/notes/rewind-app-teardown-ml.png)

## Summary

Kevin Chen's technical teardown of Rewind (rewind.ai) answers the question posed in the app's marketing: how does an app that records your entire screen continuously manage to not noticeably impact system performance? The answer involves several clever technical choices that exploit Apple Silicon capabilities and macOS APIs unavailable on other platforms.

The core technique: Rewind uses the Screen Recording API to capture screen contents as pixel buffers, then applies Apple's VideoToolbox hardware H.264/HEVC encoder — the same encoder used for FaceTime — to compress screen content. The neural engine on Apple Silicon handles this acceleration natively, which is why the app claims minimal CPU overhead. Differential encoding further reduces the data: only changed regions are re-encoded each frame, and static UI elements compress extremely efficiently.

For search and retrieval, Rewind applies on-device OCR via Vision framework to extract text from screen recordings, then indexes it locally. The LLM component (for question-answering over your history) runs inference locally as well, avoiding the privacy implications of sending screen content to a cloud service. The teardown is a good case study in how Apple Silicon's heterogeneous compute (CPU, GPU, Neural Engine, VideoToolbox) enables ML-powered applications that would be impractical on Intel hardware.

## Key points

- Rewind uses hardware H.264/HEVC encoding via VideoToolbox — Neural Engine acceleration, not CPU
- Differential encoding: only changed screen regions re-encoded per frame, dramatically reducing load
- On-device OCR via Vision framework indexes screen text locally — no cloud transmission
- Apple Silicon's heterogeneous compute makes this feasible; would be impractical on Intel macOS
- Teardown method: Hopper Disassembler + LLDB + Frida for dynamic tracing of private APIs

[Original](https://kevinchen.co/blog/rewind-ai-app-teardown/)
