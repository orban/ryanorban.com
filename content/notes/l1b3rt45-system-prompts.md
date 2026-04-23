---
title: "L1B3RT45: AI System Prompts Collection"
date: 2024-09-25
categories:
  - llm
  - prompts
  - jailbreaking
  - research
  - transparency
  - ai-safety
description: L1B3RT45 is a GitHub repository collecting leaked and reverse-engineered system prompts from major AI assistants (Claude, ChatGPT, Mistral, Zamba2). With 18.5k stars, it documents the operational instructions guiding commercial AI models, useful for prompt engineering research and AI transparency.
params:
  source: pinboard
  sourceUrl: https://github.com/elder-plinius/L1B3RT45/blob/main/SYSTEMPROMPTS.mkd
---

![L1B3RT45: AI System Prompts Collection](/images/notes/l1b3rt45-system-prompts.png)

## Summary

L1B3RT45 (by elder-plinius) is a GitHub repository that collects leaked and reverse-engineered system prompts from major commercial AI assistants. The SYSTEMPROMPTS.mkd file documents the internal operational instructions for Mistral's Le Chat, OpenAI's ChatGPT (including O1, iOS, and Advanced Voice Mode variants), Anthropic's Claude (in Explanatory, Formal, and Concise modes), and Zyphra's Zamba2-7B.

The practical value of these prompts is understanding how commercial AI providers structure system-level instructions at scale. The prompts reveal which capabilities are enabled by default vs. restricted, how safety and content moderation rules are expressed in natural language instructions, how different operating modes are implemented (Claude's Explanatory mode vs. Concise mode, for example), and what tool capabilities are granted at the system level (web search, image generation, code execution).

With 18.5k GitHub stars, the repository has significant community interest. This reflects the broader prompt engineering community's interest in AI transparency — understanding the scaffolding beneath commercial AI services rather than treating models as black boxes. It's useful for researchers studying AI behavior, developers optimizing their own system prompts by example, and anyone interested in how major providers think about AI instruction design.

## Key points

- Collects system prompts from Claude, ChatGPT, Mistral Le Chat, and other commercial AI.
- Reveals: capability grants, safety rules, tool configurations, and behavioral modes.
- 18.5k stars — significant community interest in AI prompt transparency.
- Claude prompts show different modes: Explanatory, Formal, Concise — same model, different instructed behavior.
- Useful for prompt engineering research and understanding how commercial AI is constrained.
- Adjacent to AI safety research: how natural language instructions shape model behavior at the system level.

[Original](https://github.com/elder-plinius/L1B3RT45/blob/main/SYSTEMPROMPTS.mkd)
