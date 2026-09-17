---
title: "Hex: press-and-hold voice transcription for macOS"
date: 2026-01-24
categories:
  - voice
  - transcription
  - mac-app
  - developer-tools
  - open-source
description: Hex is an open-source macOS press-and-hold voice transcription app — hold a hotkey, speak, release, and the text is pasted wherever you're typing. Uses Parakeet TDT v3 or WhisperKit for on-device transcription.
params:
  source: pinboard
  sourceUrl: https://github.com/kitlangton/Hex
---

![Hex: press-and-hold voice transcription for macOS](/images/notes/hex-voice.png)

## Summary

Hex is an open-source macOS app for global hotkey voice transcription. The workflow is minimal: hold a hotkey, speak, release, and the transcribed text is pasted wherever your cursor is. Two recording modes — press-and-hold for short dictations, double-tap-to-lock for longer ones. Available for Apple Silicon Macs via direct download or Homebrew.

The transcription backends are the interesting technical detail. Parakeet TDT v3 via FluidAudio is the default: fast, multilingual, and optimized for accuracy. WhisperKit is the alternative for developers who prefer Whisper-based on-device transcription. Both run locally — no API calls, no cloud dependency. The app uses Swift Composable Architecture (SCA) for state management, pointing to a thoughtfully structured codebase.

Hex fills a simple but genuinely useful gap in developer workflows. Dictating prose, comments, commit messages, or longer prompts to Claude Code is faster than typing when you know what you want to say. The on-device transcription means there's no latency penalty for short dictations and no concern about audio data leaving the machine.

## Key points

- Global hotkey voice transcription: hold to record, release to paste — works in any app.
- Parakeet TDT v3 (default) or WhisperKit for on-device transcription — no cloud.
- Two modes: press-and-hold for short clips, double-tap-to-lock for longer dictation.
- Open-source, Apple Silicon only, installable via Homebrew (`brew install --cask kitlangton-hex`).
- Built with Swift Composable Architecture.

[Original](https://github.com/kitlangton/Hex)
