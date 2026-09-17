---
title: "TokenCost: LLM API Cost Calculator"
date: 2023-12-27
categories:
  - llm
  - cost-management
  - developer-tools
  - ai-agents
  - python
description: TokenCost is a Python library from AgentOps that counts tokens and calculates USD costs for 400+ LLM models before making API calls. Keeps a live-updated pricing database so your cost estimates don't go stale when providers update pricing.
params:
  source: pinboard
  sourceUrl: https://github.com/AgentOps-AI/tokencost
---

![TokenCost: LLM API Cost Calculator](/images/notes/tokencost-llm-cost-calculator.png)

## Summary

TokenCost is a Python library from AgentOps for calculating the USD cost of LLM API usage. The core problem it solves: LLM providers frequently update pricing, add models, and change tokenization behavior — keeping accurate cost estimates in application code is a maintenance burden. TokenCost handles this centrally with a database of pricing for 400+ models across major providers (OpenAI, Anthropic, Google, Mistral, etc.) that stays updated as pricing changes.

The library does two things: token counting before a request is made (so you can estimate cost before incurring it), and cost calculation after (given prompt and completion token counts). Token counting uses Tiktoken for OpenAI models and the Anthropic beta token counting API for Claude 3+ models — the right tokenizer for the right model family. The calculation functions are simple: `calculate_prompt_cost()` and `calculate_completion_cost()`, both returning USD amounts.

For AI agent applications — where a single user interaction might chain dozens of LLM calls across multiple models — cost visibility is genuinely important. Without it, it's easy to build a workflow that costs $0.02 in testing but $2.00 in production because the actual path length differs. TokenCost gives you cost instrumentation that can be added to any prompt function call without restructuring existing code.

## Key points

- Database of 400+ LLM models with pricing that stays updated as providers change rates.
- Token counting via Tiktoken (OpenAI) and Anthropic beta API (Claude) — uses the right tokenizer.
- `calculate_prompt_cost()` and `calculate_completion_cost()` — simple function interface.
- Client-side counting: estimate costs before making API calls, not just after.
- Designed for AI agent workflows where multi-step LLM chains accumulate unpredictable costs.
- From AgentOps — fits into a broader agent observability toolkit.

[Original](https://github.com/AgentOps-AI/tokencost) → GitHub
