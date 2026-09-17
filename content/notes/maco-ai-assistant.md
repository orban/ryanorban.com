---
title: "macOSpilot: Voice + Vision AI Assistant for macOS"
date: 2023-12-13
categories:
  - macos
  - ai-assistant
  - voice
  - vision
  - open-source
description: macOSpilot is an open-source macOS AI assistant that combines voice input and screen vision to answer questions about any application in context — it sees what you're looking at and hears your question, then responds in audio. An early demonstration of multimodal desktop AI assistance.
params:
  source: pinboard
  sourceUrl: https://github.com/elfvingralf/macOSpilot-ai-assistant
---

![macOSpilot: Voice + Vision AI Assistant for macOS](/images/notes/maco-ai-assistant.png)

## Summary

macOSpilot is an open-source macOS AI assistant that combines voice recognition, screen capture, and text-to-speech to create a context-aware assistant for any application. The interaction pattern: press a hotkey, ask a question about whatever is on your screen, and get an audio response. The assistant sees your screen (via screenshot), hears your question (via Whisper transcription), sends both to an LLM, and speaks the response.

This is the multimodal desktop assistant pattern that emerged in late 2023 as GPT-4 Vision became available. Before vision-capable LLMs, desktop assistants were limited to text input — they couldn't see context. With vision, the assistant can answer what does this error mean? by reading the terminal, how do I use this dialog? by seeing the interface, or summarize what's on my screen without you having to describe it.

macOSpilot is a simple proof-of-concept implementation, but it points toward the category of tools that became products: Copilot+ PC features, macOS AI features in later versions, and various productivity tools using screen context + LLM. The open-source nature means developers can extend it, and the January 2023 release context makes it an early exploration of the multimodal desktop AI space.

## Key points

- Voice + screen vision + text-to-speech: question about anything on screen, answered aloud.
- Stack: Whisper for voice transcription, GPT-4 Vision for screen understanding, TTS for output.
- Works across any application — context comes from the screenshot, not application-specific integrations.
- Early (Dec 2023) open-source demonstration of multimodal desktop AI assistance.
- Points toward products like Copilot+ PC features and macOS AI — the capability pattern was clear.

[Original](https://github.com/elfvingralf/macOSpilot-ai-assistant) → GitHub
