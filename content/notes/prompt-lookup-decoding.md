---
title: "Prompt Lookup Decoding: Speculative Decoding without a Draft Model"
date: 2023-12-24
categories:
  - llm
  - inference
  - speculative-decoding
  - performance
  - research
description: Prompt lookup decoding replaces the draft model in speculative decoding with simple n-gram string matching against the prompt itself — achieving 2.4x speedup on summarization and QA with zero quality loss. Works whenever output heavily references the input, which is most practical LLM tasks.
params:
  source: pinboard
  sourceUrl: https://github.com/apoorvumang/prompt-lookup-decoding
---

![Prompt Lookup Decoding: Speculative Decoding without a Draft Model](/images/notes/prompt-lookup-decoding.png)

## Summary

Speculative decoding speeds up LLM inference by using a small, cheap "draft" model to propose candidate tokens, then having the full model verify them in parallel. The bottleneck is that you need a high-quality draft model that's compatible with your target model. [Prompt lookup decoding](/notes/prompt-lookup-decoding/) replaces the draft model entirely with a lookup table: when the model is about to generate a token, search the input prompt for sequences that match the recent context, and propose the continuation from the prompt as draft candidates.

The key insight is that input-grounded tasks — summarization, document-based QA, editing — have high n-gram overlap between input and output. If you're summarizing a document that says "the committee voted 7-3 to approve", the summary is very likely to contain voted 7-3. By finding that n-gram in the prompt and proposing the following tokens as drafts, you skip the draft model entirely and get essentially free speculation using string matching.

The results on CNN/DailyMail summarization and context-based QA show ~2.4x speedup with no quality degradation — the verification step in speculative decoding rejects incorrect candidates, so accuracy is preserved by construction. The method works with any decoder model, requires no training or additional parameters, and is compatible with both greedy and sampling decoding. It's a compelling demonstration that architectural improvements to inference don't always require complex machinery.

## Key points

- Replaces the draft model in speculative decoding with n-gram string matching against the input prompt.
- Exploits high n-gram overlap between input and output in summarization, QA, and document editing tasks.
- ~2.4x speedup on CNN/DailyMail and context-based QA — no quality degradation.
- Works with any decoder model, no training required, no architectural changes.
- Quality preserved by construction: the full model verifies and rejects incorrect draft candidates.
- Simple but effective: shows that inference speedups don't always require specialized draft models.

[Original](https://github.com/apoorvumang/prompt-lookup-decoding) → GitHub
