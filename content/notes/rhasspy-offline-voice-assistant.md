---
title: Rhasspy — Offline Private Voice Assistant
date: 2022-11-22
categories:
  - voice-assistant
  - privacy
  - offline
  - self-hosted
  - nlp
  - iot
description: Rhasspy is a fully offline, privacy-first voice assistant framework supporting many human languages — no cloud required. Designed for Home Assistant integration and runs entirely on local hardware like a Raspberry Pi.
params:
  source: pinboard
  sourceUrl: https://github.com/rhasspy/rhasspy
---

## Summary

Rhasspy is an open-source, fully offline voice assistant framework designed for Home Assistant and IoT integrations. Where Alexa, Google Assistant, and Siri all send audio to cloud servers for processing, Rhasspy runs the entire stack — wake word detection, speech-to-text, intent recognition, and text-to-speech — on local hardware. It supports many human languages beyond English, including several underrepresented ones.

The architecture is modular: you choose which component to use for each stage of the pipeline. Wake word detection can use Porcupine, Snowboy, or a simpler phoneme-based detector. Speech-to-text can use Mozilla DeepSpeech, Kaldi, Vosk, or PocketSphinx. Intent recognition can be rule-based or use Flair for more flexible matching. This modularity means you can trade accuracy for resource requirements — important when running on a Raspberry Pi with limited compute.

The primary audience is privacy-conscious home automation users who want voice control without sending every spoken word to Amazon or Google. Home Assistant integration is first-class, with MQTT and Home Assistant event bus both supported. The project is now archived (development moved to Wyoming protocol and the Home Assistant voice satellite approach), but it was an important reference implementation for local voice pipelines during its active period.

## Key points

- Fully offline voice assistant — wake word, STT, intent recognition, TTS all run locally.
- Modular pipeline: swap out components per stage, optimizing for accuracy vs. resource usage.
- Multilingual — supports many languages, including less common ones underserved by commercial assistants.
- Home Assistant integration via MQTT or event bus — designed specifically for home automation.
- Privacy by design: no audio leaves the device.
- Now archived; succeeded by Wyoming protocol and Home Assistant's voice satellite project.

[Original](https://github.com/rhasspy/rhasspy) → GitHub
