---
title: "Landmark Attention: Random-Access Infinite Context"
date: 2023-05-28
categories:
  - research
  - llm
  - attention
  - context-window
  - paper
description: Landmark Attention paper extending LLaMA 7B to 32k token context by using landmark tokens to represent blocks of input, enabling attention-based retrieval of relevant blocks rather than attending over all tokens. Achieves near-GPT-4 context length through architectural change rather than longer pretraining.
params:
  source: pinboard
  sourceUrl: https://arxiv.org/abs/2305.16300
---

![Landmark Attention: Random-Access Infinite Context](/images/notes/landmark-attention-infinite-context.png)

## Summary

This paper from 2023 presents Landmark Attention — a technique for extending transformer context length without the quadratic memory cost of full attention. The approach: divide the input into fixed-size blocks and add a special landmark token to each block. The model trains its attention mechanism to use landmark tokens as proxies for their blocks, allowing it to identify and retrieve relevant blocks without attending over all tokens.

The mechanism closely resembles how RAG works at the document level, but implemented entirely within the attention mechanism. Rather than a separate retrieval step, the model learns to use landmark tokens as a compressed representation of each block, then performs selective attention over blocks rather than individual tokens. This preserves the random-access flexibility of attention (any block can be retrieved) while scaling to arbitrary context lengths.

The practical result: LLaMA 7B fine-tuned with Landmark Attention achieves comparable performance to Transformer-XL while retrieving significantly fewer tokens per step, and can handle context lengths up to 32k tokens — matching GPT-4's context window at the time of publication. This was notable because GPT-4's context length required a much larger model; Landmark Attention achieved similar effective context in a 7B model through architectural efficiency.

## Key points

- Landmark tokens represent each block of input; model learns to use them for block selection in attention.
- Preserves random-access flexibility: any block can be retrieved, unlike recurrent memory approaches.
- Linear memory cost vs. quadratic for full attention over the full context.
- Fine-tuned LLaMA 7B to 32k token context — matches GPT-4 context at the time with a 7B model.
- Part of the 2023 wave of context extension research before native long context became the standard solution.

[Original](https://arxiv.org/abs/2305.16300)
