---
title: "LLM Council: multi-model deliberation as a Claude Code plugin"
date: 2026-02-14
categories:
  - llm
  - claude-code
  - multi-model
  - reasoning
  - plugins
description: "LLM Council is a Claude Code plugin that runs a 3-phase multi-model deliberation on any query: parallel responses, cross-model ranking, chairman synthesis. Built by DAIR.AI on Fireworks AI inference."
params:
  source: pinboard
  sourceUrl: https://github.com/dair-ai/dair-academy-plugins/tree/main/plugins/llm-council
---

![LLM Council: multi-model deliberation as a Claude Code plugin](/images/notes/llm-council.png)

## Summary

[LLM Council](/notes/llm-council/) is a Claude Code plugin from DAIR.AI that implements Andrej Karpathy's LLM Council concept — running multiple LLMs in parallel to deliberate on a query, with cross-model ranking and synthesis. The plugin runs on Fireworks AI inference, making the parallel model calls practical in terms of cost and speed.

The three-phase process: Phase 1 runs all selected models independently in parallel (parallel responses). Phase 2 asks each model to review and rank the other models' anonymized responses (cross-model ranking). Phase 3 has a designated Chairman model synthesize the final answer using all responses and rankings (chairman synthesis). The anonymization in Phase 2 is important — it prevents models from deferring to known-authoritative sources and forces genuine quality assessment.

Available models are all open-weight running on Fireworks AI: GLM 5 (Z.AI, 744B MoE), DeepSeek V3.1, Kimi K2.5, Qwen3 235B, Llama 4 Maverick. The model mix covers the main families of current frontier open-weight models. The council approach is most valuable for complex questions where a single model may have blind spots — getting diverse perspectives and having them critique each other produces more thorough answers than any single model alone.

## Key points

- 3-phase multi-model deliberation: parallel responses → cross-model ranking (anonymized) → chairman synthesis.
- Available models: GLM 5, DeepSeek V3.1, Kimi K2.5, Qwen3 235B, Llama 4 Maverick.
- Runs on Fireworks AI for affordable parallel inference at scale.
- Implements Andrej Karpathy's LLM Council concept as a practical Claude Code plugin.
- Built by DAIR.AI.

[Original](https://github.com/dair-ai/dair-academy-plugins/tree/main/plugins/llm-council)
