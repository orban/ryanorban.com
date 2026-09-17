---
title: How to Play with the GPT-3 Language Model
date: 2022-08-07
categories:
  - gpt-3
  - llm
  - tutorial
  - openai
  - simon-willison
description: Simon Willison's practical guide to getting started with GPT-3 — written in June 2022 when most developers still hadn't touched it. One of the clearest early explainers on the OpenAI API and what the model could actually do.
params:
  source: pinboard
  sourceUrl: https://simonwillison.net/2022/Jun/5/play-with-gpt3/
---

## Summary

Simon Willison wrote this tutorial in June 2022 as a practical on-ramp for developers who had heard about GPT-3 but hadn't actually used it. At the time, GPT-3 was available via OpenAI's API but behind a waitlist, and the mental model most developers had of it was either inflated (AGI) or wrong (autocomplete). Willison's framing was deliberately demystifying: this is a text-in, text-out API, and here's how you get access and start experimenting.

The guide covers the OpenAI Playground as the fastest way to explore without writing code, explains the different model variants (text-davinci, text-curie, text-ada), and walks through prompt construction. The key insight Willison emphasizes is that GPT-3 is a completion engine: it continues whatever you give it, so the prompt is everything. Getting good results means learning to write prompts that set up the completion you want — what became known as prompt engineering.

By August 2022 when this was bookmarked, GPT-3 access was becoming more open, but the practitioner community was still small. Willison was one of the earliest developers doing serious public exploration, and his blog became a primary source for the community figuring out what the model could do. This post is an artifact of that early period when simply knowing how to call the API was rare.

## Key points

- GPT-3 is a completion engine — the prompt structure determines output quality
- OpenAI Playground removes friction for initial exploration; API access for production use
- Model variants had different capability/cost tradeoffs: davinci (best), curie, babbage, ada
- Prompt engineering emerges here as the core SKILL: setting up context so completions are useful
- Published by Simon Willison, whose blog became a key reference for early LLM practitioners
- June 2022 — before ChatGPT, when most developers had not directly interacted with a large language model

[Original](https://simonwillison.net/2022/Jun/5/play-with-gpt3/)
