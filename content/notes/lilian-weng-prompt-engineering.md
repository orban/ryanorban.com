---
title: "Prompt Engineering: Lilian Weng's Comprehensive Survey"
date: 2023-03-20
categories:
  - prompt-engineering
  - llm
  - chain-of-thought
  - few-shot
  - research
description: Lilian Weng's canonical reference on prompt engineering techniques — zero-shot, few-shot, chain-of-thought, self-consistency, tree-of-thoughts, and more — grounded in research papers. Still the most comprehensive single-author survey of the space.
params:
  source: pinboard
  sourceUrl: https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/
---

![Prompt Engineering: Lilian Weng's Comprehensive Survey](/images/notes/lilian-weng-prompt-engineering.png)

## Summary

Lilian Weng (research lead at OpenAI) published what became the canonical reference on prompt engineering techniques. The post surveys the full landscape: basic techniques (zero-shot prompting, few-shot prompting), reasoning techniques (chain-of-thought prompting, self-consistency, least-to-most prompting), advanced architectures ([tree-of-thoughts](/notes/tree-of-thoughts/), ReAct, Reflexion), and instruction alignment approaches. Each technique is grounded in citations to the underlying papers.

The timing was significant — published March 2023, right when GPT-4 launched and prompt engineering was becoming a mainstream practice. The post provided structure to a field that had been accumulating ad-hoc techniques without a common vocabulary. Weng's synthesis made it clear that prompting wasn't just phrasing things nicely but a set of principled techniques with measurable effects on model performance.

Chain-of-thought prompting — asking models to reason step-by-step before answering — was the highest-impact technique, showing that reasoning quality scales with prompt structure in a way that few-shot examples alone don't achieve. Self-consistency (sample multiple reasoning paths, take the majority vote) further improved reliability. These techniques laid the foundation for the agent reasoning patterns that LangChain, LlamaIndex, and similar frameworks later encoded.

## Key points

- Surveys zero-shot, few-shot, chain-of-thought, self-consistency, [tree-of-thoughts](/notes/tree-of-thoughts/), ReAct, Reflexion.
- Chain-of-thought prompting: asking for step-by-step reasoning dramatically improves complex task performance.
- Self-consistency: sample multiple reasoning chains and take majority vote — more reliable than greedy decoding.
- Written by Lilian Weng (OpenAI) — provides research citations and rigorous framing over the space.
- Still the most comprehensive single-author survey; updated periodically as new techniques emerge.

[Original](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/) → AI agent, GitHub
