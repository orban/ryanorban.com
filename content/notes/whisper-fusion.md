---
title: "WhisperFusion: real-time voice conversations with AI"
date: 2024-01-29
categories:
  - voice-ai
  - whisper
  - speech-to-text
  - tts
  - llm
  - real-time
description: WhisperFusion is Collabora's pipeline for real-time voice conversations with AI — combining WhisperLive (real-time STT) with WhisperSpeech (TTS) and an LLM to create a fully local end-to-end spoken AI assistant.
params:
  source: pinboard
  sourceUrl: https://github.com/collabora/WhisperFusion
---

![WhisperFusion: real-time voice conversations with AI](/images/notes/whisper-fusion.png)

## Summary

WhisperFusion is an open-source pipeline from Collabora that combines three components into a real-time voice AI system: WhisperLive for streaming speech-to-text recognition, a local LLM for response generation, and WhisperSpeech for text-to-speech synthesis. The result is a fully local, end-to-end spoken conversation system — you speak, it transcribes in real time, sends the text to an LLM, and reads the response back using synthesized speech.

The architecture is three-stage, with each component running as a concurrent service. WhisperLive streams audio from the microphone and produces rolling transcriptions using OpenAI Whisper. The transcription is sent to an LLM (supports various backends including llama.cpp and Mixtral). The LLM response is streamed to WhisperSpeech which synthesizes audio. The goal is minimal latency at each stage so the conversation feels natural rather than turn-based.

WhisperFusion represents an early attempt at local spoken AI assistants — the stack that Siri, Alexa, and Google Assistant run in the cloud, reimplemented for local deployment. The 2024 timing predates the current wave of local voice assistant tooling, making it a pioneering effort in the space. Running entirely locally means no cloud dependency, no audio leaving your machine, and no API costs.

## Key points

- Three-stage pipeline: WhisperLive (streaming STT) + LLM + WhisperSpeech (TTS).
- Fully local — audio never leaves the machine, no cloud API costs.
- OpenAI Whisper-based transcription with real-time streaming.
- Supports llama.cpp, Mixtral, and other LLM backends.
- From Collabora, open-source on GitHub.
- Precursor to the current wave of local voice AI assistants.

[Original](https://github.com/collabora/WhisperFusion)
