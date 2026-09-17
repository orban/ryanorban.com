---
title: Building Safer Dialogue Agents (DeepMind / Sparrow)
date: 2022-09-23
categories:
  - ai-safety
  - dialogue-systems
  - deepmind
  - rlhf
  - alignment
description: DeepMind's blog post on Sparrow — a dialogue agent trained with reinforcement learning from human feedback and rules to be helpful, harmless, and honest. An early published account of RLHF-based safety fine-tuning for conversational AI.
params:
  source: pinboard
  sourceUrl: https://www.deepmind.com/blog/building-safer-dialogue-agents
---

## Summary

DeepMind's post describes Sparrow, their research dialogue agent designed to be safe, helpful, and accurate. Published in September 2022, it's one of the first detailed public accounts of using RLHF (reinforcement learning from human feedback) combined with explicit rules to train conversational AI that avoids harmful outputs.

Sparrow extends RLHF — the approach OpenAI used for InstructGPT — with a rule-based component. Human raters evaluate responses not just for quality but specifically for rule violations (don't give harmful advice, don't make unsubstantiated claims, don't pretend to be human). This two-track training (preference-based + rule-based) was DeepMind's attempt to make safety properties more explicit and auditable than pure preference learning.

The model also includes a search mechanism: it can query Google Search to ground claims rather than relying on memorized training data. This was an early integration of retrieval-augmented generation into a safety-conscious dialogue agent — the intuition being that factual grounding reduces confident hallucination.

Sparrow is historically significant as a contemporary of ChatGPT and Claude that took a more rules-explicit approach to alignment. The tension between rules and preferences remains active in safety research.

## Key points

- Sparrow by DeepMind: dialogue agent trained with RLHF + explicit safety rules.
- Two-track training: preference learning for quality + rule violations as negative signal.
- Rule violations include: harmful advice, unsubstantiated claims, pretending to be human.
- Includes Google Search grounding to reduce hallucination on factual questions.
- Contemporary of InstructGPT and early Claude — represents the rules-explicit safety approach.
- Published September 2022, before ChatGPT made these techniques public-facing.

[Original](https://www.deepmind.com/blog/building-safer-dialogue-agents) → AI agent
