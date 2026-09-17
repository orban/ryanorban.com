---
title: Prompt Injection Attacks Against GPT-3
date: 2022-12-26
categories:
  - security
  - prompt-injection
  - llm
  - ai-safety
  - gpt3
description: Simon Willison's September 2022 post naming and describing prompt injection attacks against GPT-3 — one of the first clear articulations of the attack class where malicious content in the environment overrides the developer's system prompt. The post that put the term 'prompt injection' into common use.
params:
  source: pinboard
  sourceUrl: https://simonwillison.net/2022/Sep/12/prompt-injection/
---

## Summary

This post by Simon Willison from September 2022 is one of the foundational pieces describing prompt injection attacks — the vulnerability class where user-supplied or environment-sourced text overrides or subverts the developer's intended instructions to an LLM. Willison's framing and the term prompt injection itself came largely from this post, which drew the analogy to SQL injection: just as user input can break out of its intended data context in a SQL query, text in an LLM's context can break out of its "data" role and act as instructions.

The attack pattern is straightforward but difficult to defend against: a developer writes a system prompt ("you are a helpful assistant that only answers questions about topic X"), a user inputs or causes the model to read text that says "ignore previous instructions and do Y instead," and the model complies. The model can't fundamentally distinguish between "instructions from the developer and text from the environment" — they're all just tokens.

Willison demonstrated this against early GPT-3-based applications and noted that the problem was structural: no amount of be careful about instructions in the system prompt fully prevents injection because the injected text can claim to be authorized or frame the original instructions as the malicious content. This became a critical security consideration as LLM applications moved from demos to production — agents reading web pages, processing emails, or executing tool calls are all surfaces for prompt injection. The attack class remains an active security research area in 2024-2025.

## Key points

- Named and defined prompt injection: adversarial text in the environment overriding developer instructions.
- SQL injection analogy: user input escaping its data role and acting as commands.
- Structural problem: models can't distinguish developer instructions from environmental text.
- Especially dangerous for AI agents reading external content (web pages, emails, documents).
- By Simon Willison — September 2022, one of the earliest and most-referenced descriptions.

[Original](https://simonwillison.net/2022/Sep/12/prompt-injection/)
