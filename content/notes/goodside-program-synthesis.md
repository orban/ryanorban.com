---
title: GPT-3 Complete-Program Synthesis (Riley Goodside)
date: 2022-08-20
categories:
  - gpt-3
  - program-synthesis
  - prompt-engineering
  - riley-goodside
  - llm
description: Riley Goodside demonstrates complete-program synthesis using GPT-3 via the 'format trick' — combining instruction prompts with contextually informative templates to generate entire programs deterministically. An early exploration of LLMs for structured code generation beyond autocomplete.
params:
  source: pinboard
  sourceUrl: https://mobile.twitter.com/goodside/status/1559801520773898240
---

## Summary

Riley Goodside describes a "novel, powerful method of complete-program synthesis using GPT-3" that combines instruction prompts with what he calls "contextually informative templates — a generalization of the format trick" shown to him by Boris Power. The approach generates complete programs in a single call at temperature 0 (deterministic), not just code snippets.

The format trick refers to providing GPT-3 with a structured example that demonstrates the desired output format — not just instructions, but a template that shows the shape of a valid solution. This is few-shot prompting applied specifically to program synthesis: the model sees not just what to do, but what success looks like structurally. The deterministic temperature 0 setting treats GPT-3 as a reliable synthesis engine, not a creative generator.

This predates widespread AI-assisted coding via GitHub Copilot and ChatGPT, representing early practitioner exploration of whether LLMs could synthesize complete programs from high-level descriptions rather than just autocomplete existing code. Riley Goodside's public experiments at Scale AI were highly influential in calibrating the community's understanding of GPT-3 for code generation.

## Key points

- Complete-program synthesis from GPT-3 using instruction + template combination.
- The "format trick" (from Boris Power): show the model a template of the desired output structure.
- Temperature 0 (deterministic) generation — treating GPT-3 as a reliable synthesis tool.
- Generalization of few-shot prompting applied specifically to program synthesis.
- By Riley Goodside (Scale AI) — key early prompt engineering practitioner.
- Precursor to the GitHub Copilot and ChatGPT era of AI-assisted coding.

[Original](https://twitter.com/goodside/status/1559801520773898240) → GitHub
