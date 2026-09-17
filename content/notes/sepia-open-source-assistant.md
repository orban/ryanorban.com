---
title: "SEPIA: Open-Source Voice Assistant"
date: 2022-03-09
categories:
  - voice-assistant
  - open-source
  - self-hosting
  - privacy
  - ai
description: SEPIA is an open-source, self-hosted voice assistant framework — a privacy-preserving alternative to Alexa, Google Assistant, and Siri. Runs entirely on your own server, with custom skill development support.
params:
  source: pinboard
  sourceUrl: https://github.com/SEPIA-Framework/sepia-docs
---

## Summary

SEPIA (Smart Experiences for Personal Intelligent Assistants) is an open-source voice assistant framework that runs entirely on self-hosted infrastructure. It's the self-hosting answer to Amazon Alexa, Google Assistant, and Apple Siri — your voice assistant, your server, your data.

The architecture is a client-server model: a server component handles natural language processing, SKILL execution, and API integrations; clients (web, Android, potentially custom hardware) handle voice input and audio output. SEPIA includes its own NLP pipeline, a skill system for adding custom capabilities, and a smart home integration layer that works with Home Assistant and other home automation platforms.

The privacy case is strong: commercial voice assistants send every utterance to cloud servers for processing. Even if the companies claim to protect this data, it's recorded, stored, and accessible to employees and potentially governments. A self-hosted voice assistant processes everything locally — no utterance ever leaves your network. This is especially relevant for sensitive home automation (locks, alarms) and for users in jurisdictions where cloud data is subject to government access.

The tradeoff vs. commercial assistants: SEPIA's NLP and skill ecosystem are less mature, voice recognition (if using on-device ASR) is less accurate, and setup requires technical knowledge. But as Whisper (OpenAI's open-source speech recognition) and local LLMs improved from 2022 onward, the capability gap narrowed significantly.

## Key points

- Self-hosted voice assistant — all processing on your own server, no data to third-party cloud.
- Privacy-first: voice commands never leave your network, unlike Alexa, Google Assistant, Siri.
- Home Assistant integration for home automation via voice — privacy-preserving smart home control.
- Custom skill development for extending capabilities.
- The capability gap with commercial assistants has been closing as Whisper and local LLMs improved.

[Original](https://github.com/SEPIA-Framework/sepia-docs) → GitHub
