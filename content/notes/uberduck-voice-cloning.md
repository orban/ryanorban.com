---
title: "Uberduck: Voice Cloning and Text-to-Speech"
date: 2022-04-01
categories:
  - machine-learning
  - text-to-speech
  - voice-cloning
  - ai
  - audio
description: Uberduck is a text-to-speech and voice cloning platform that gained early viral traction through celebrity voice imitations and rap generation. Early consumer-facing example of generative audio before ElevenLabs dominated the space.
params:
  source: pinboard
  sourceUrl: https://uberduck.ai/
---

## Summary

Uberduck is a text-to-speech and voice cloning platform that became notable in 2021-2022 for its library of celebrity and character voices — allowing users to generate speech or rap lyrics in the style of famous voices. The platform combined neural TTS technology with a community-contributed voice model library and a web interface simple enough for non-ML users to access. This combination made it one of the first viral consumer products in generative audio.

The underlying technology draws on Tacotron 2 and WaveGlow/HiFi-GAN style architectures — neural networks that convert text to mel spectrograms (intermediate audio representation) and then mel spectrograms to waveforms. Voice cloning requires relatively few samples of a target voice (the platform's community approach meant users could contribute their own trained models). The quality in 2022 was good enough to be entertaining but not convincing for serious deepfake applications — a distinction that has since collapsed with models like ElevenLabs.

The rap generation feature is worth noting as an early example of combining language models (for lyric generation) with neural TTS (for delivery) — a compositional approach to creative audio generation. By 2022, this felt novel; by 2024, multi-step generative pipelines combining text, voice, and music models became standard. Uberduck represents the early consumer-facing edge of what was then primarily a research area. The platform later pivoted toward developer APIs and video generation tools as the competitive landscape intensified with ElevenLabs, Play.ht, and voice features in major AI products.

## Key points

- Neural TTS pipeline: text → mel spectrogram (Tacotron 2) → waveform (HiFi-GAN) — standard architecture for high-quality speech synthesis.
- Community voice model library enabled celebrity/character voices without Uberduck owning all training data.
- Early viral consumer product for voice cloning — before ElevenLabs professionalized the space.
- Rap generation: combined LM-based lyric generation with neural voice delivery — early compositional generative audio.
- Positioned as developer API as the market matured; competed with ElevenLabs, Play.ht, Resemble AI.
- Demonstrates the 2022 pattern: research-quality audio generation becoming accessible through web products.

[Original](https://uberduck.ai/)
