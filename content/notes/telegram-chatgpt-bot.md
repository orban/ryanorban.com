---
title: Telegram ChatGPT Concierge Bot
date: 2023-04-10
categories:
  - chatbot
  - telegram
  - openai
  - voice
  - developer-tools
description: A Telegram bot that wraps ChatGPT with voice input/output — send it a voice message or text and get ChatGPT responses back in the same format. An early template for LLM-powered messaging bots before they became a commodity.
params:
  source: pinboard
  sourceUrl: https://github.com/RafalWilinski/telegram-chatgpt-concierge-bot
---

## Summary

telegram-chatgpt-concierge-bot is a TypeScript bot that connects Telegram to OpenAI's ChatGPT API, supporting both text and voice interactions. Send a text message and get a ChatGPT response; send a voice message and Whisper transcribes it before passing it to ChatGPT, with the option to receive responses as text or synthesized voice. The concierge framing captures the intent: a personal AI assistant accessible from wherever you use Telegram.

The implementation handles conversation history — the bot maintains context across messages so you can have multi-turn conversations rather than isolated one-shot queries. It uses Redis for session storage, which lets conversation state persist across bot restarts. The TypeScript codebase with Node.js runtime is a relatively accessible starting point for developers who want to build on top of it.

In early 2023, this kind of bot was a common pattern for giving non-technical users access to LLM capabilities — Telegram and WhatsApp were already the daily communication apps for millions of people, so wrapping ChatGPT in a familiar messaging interface lowered the adoption barrier. The pattern was quickly commoditized (dozens of similar bots emerged), but the implementation choices here — voice round-trip with Whisper, conversation memory, clean TypeScript code — made it a useful starting template. Related to later tools like LangChain Telegram integrations and commercial offerings from Chatbase and similar services.

## Key points

- Telegram bot wrapping ChatGPT with voice input (Whisper STT) and voice output option.
- Conversation history via Redis — multi-turn dialogue preserved across messages.
- TypeScript/Node.js implementation — clean starting point for customization.
- Early 2023 template for messaging-app LLM interfaces before the pattern was commoditized.
- Demonstrates the mobile-first LLM access pattern: familiar messaging UI, no new app needed.
- Voice round-trip: voice → Whisper → ChatGPT → TTS — fully accessible without typing.

[Original](https://github.com/RafalWilinski/telegram-chatgpt-concierge-bot) → GitHub
