---
title: ithy — Multi-LLM Research Aggregator
date: 2024-12-14
categories:
  - ai-tools
  - research
  - multi-llm
  - aggregation
  - search
description: ithy is an AI research platform that queries multiple LLMs simultaneously and synthesizes their responses into a single interactive article. The positioning is that combining ChatGPT, Gemini, and Claude produces better answers than any one alone.
params:
  source: pinboard
  sourceUrl: https://ithy.com/
---

![ithy — Multi-LLM Research Aggregator](/images/notes/ithy.png)

## Summary

[ithy](/notes/ithy/) is an AI research platform that queries multiple LLMs simultaneously — ChatGPT, Gemini, Claude, and others — and synthesizes their responses into a single unified article with charts, videos, and multimedia. It offers two modes: Fast Research (3x quicker) and Deep Research (more thorough). The core premise is that combining multiple model outputs produces more reliable answers than any single model alone, which maps to ensemble methods in classical machine learning.

The claim is backed by benchmark results, though the specifics depend on how "combined" output is defined. In practice, aggregating multiple LLM responses reduces the variance of individual model failures — if one model confidently gets a fact wrong, the others may correct it. This is most valuable for factual research queries where hallucination is the main risk, less so for reasoning tasks where one clear chain of thought is more reliable than a synthesis.

The output format — interactive articles rather than chat responses — is interesting from a UX perspective. It treats AI output as a document to be consumed, not a conversation to be continued. This aligns with how people actually use research tools. [ithy](/notes/ithy/) sits in the same space as Perplexity, You.com, and Consensus, competing on the AI-powered research positioning but with the multi-model aggregation as the differentiator.

## Key points

- Queries ChatGPT, Gemini, Claude, and others simultaneously, synthesizes into one article.
- Fast Research and Deep Research modes; multimedia output format.
- Multi-model aggregation reduces individual model hallucination risk.
- Competes with Perplexity and Consensus in the AI research tool space.
- The ensemble approach is well-established in ML but novel as a UX pattern for chat interfaces.

[Original](https://ithy.com/)
