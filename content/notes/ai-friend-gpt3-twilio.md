---
title: How to Call an AI Friend Using GPT-3 with Twilio Voice
date: 2022-12-06
categories:
  - gpt-3
  - twilio
  - voice
  - tutorial
  - conversational-ai
description: A tutorial for building a callable AI 'friend' using GPT-3, Twilio Voice, and Twilio Functions — demonstrating the phone-based AI assistant pattern before it became common. The call-able AI interface predates consumer voice assistants built on LLMs.
params:
  source: pinboard
  sourceUrl: https://www.scien.cx/2022/07/18/how-to-call-an-ai-friend-using-gpt-3-with-twilio-voice-and-functions/
---

## Summary

This tutorial (from July 2022, bookmarked in December) walks through building an AI friend you can actually call on the phone using GPT-3, Twilio Voice, and Twilio Functions. When you call the number, Twilio's speech-to-text converts your speech to text, passes it to GPT-3 via the OpenAI API, gets a text response, and uses text-to-speech to speak it back. The entire pipeline runs in Twilio Functions (serverless), so there's no infrastructure to manage.

The pattern here is the same as the Contigo hackathon project: phone as the interface, Twilio as the telecom layer, LLM as the reasoning layer, and TTS/STT bridging audio to text. What distinguishes this tutorial is that it was published in July 2022 — five months before ChatGPT's launch — when building anything interactive with GPT-3 required significantly more effort. The `text-davinci-002` model in use at that time was capable but required careful prompt engineering for conversational behavior.

The AI friend framing is interesting: it predicts the companion AI category that would emerge with products like Character.AI, Replika, and later Claude's and GPT-4's conversational capabilities. Building it as a phone call rather than a chat interface makes it accessible to anyone with a phone — no app download, no account. This friction-reduction for AI access via telecommunications infrastructure became a recurring theme in AI product design.

## Key points

- Builds a callable AI "friend" using GPT-3 + Twilio Voice + Twilio Functions (serverless).
- Pipeline: phone call → speech-to-text → GPT-3 → text-to-speech → spoken response.
- Published July 2022 — predates ChatGPT; demonstrates the pattern 5 months early.
- No infrastructure needed: Twilio Functions handles the serverless execution.
- "AI friend" framing anticipates companion AI products (Replika, Character.AI).
- Phone interface removes friction: no app or account required from the caller.

[Original](https://www.scien.cx/2022/07/18/how-to-call-an-ai-friend-using-gpt-3-with-twilio-voice-and-functions/)
