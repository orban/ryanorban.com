---
title: "Qwen3-TTS-12Hz-1.7B-CustomVoice: open custom voice TTS"
date: 2026-01-26
categories:
  - tts
  - voice
  - qwen
  - hugging-face
  - open-source
  - custom-voice
description: Qwen3-TTS-12Hz-1.7B-CustomVoice is Alibaba's compact open TTS model with custom voice cloning capability — 1.7B parameters, 12Hz token rate, available on Hugging Face. Part of the Qwen3 model family.
params:
  source: pinboard
  sourceUrl: https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice
---

![Qwen3-TTS-12Hz-1.7B-CustomVoice: open custom voice TTS](/images/notes/qwen-tts.png)

## Summary

Qwen3-TTS-12Hz-1.7B-CustomVoice is Alibaba's text-to-speech model released through Qwen (their open model family) on Hugging Face. The model is 1.7B parameters with a 12Hz token generation rate, and adds custom voice cloning to the Qwen3 TTS line. Alibaba frames the Qwen series as part of their effort to "advance and democratize artificial intelligence through open source."

The custom voice capability is the headline feature — users can clone a voice and synthesize speech in that voice without fine-tuning. Combined with the relatively small 1.7B parameter footprint, this is oriented at local deployment and integration into applications rather than requiring API calls to hosted services.

This sits in the same space as ElevenLabs and Cartesia on the custom voice side, but as an open-weight model you can run locally. For developers building voice interfaces into AI applications, open-weight TTS with custom voice is a meaningful cost and privacy improvement over hosted solutions.

## Key points

- 1.7B parameter TTS model with custom voice cloning — no fine-tuning required.
- 12Hz token generation rate; available as open weights on Hugging Face.
- Part of Alibaba's Qwen3 model family; open-source commitment from Alibaba's AI division.
- Local deployment option vs. hosted TTS services like ElevenLabs.
- Custom voice without API dependency — relevant for privacy-sensitive or cost-sensitive voice applications.

[Original](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice)
