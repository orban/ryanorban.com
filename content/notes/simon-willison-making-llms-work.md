---
title: Making Large Language Models Work For You
date: 2023-08-28
categories:
  - llm
  - prompt-engineering
  - practical-ai
  - wordpress
  - simon-willison
description: Simon Willison's WordCamp 2023 keynote on making LLMs work for you — a practical, grounded introduction covering what LLMs actually are, their real limitations, and the specific use cases where they're genuinely useful today. One of the better practitioner introductions from 2023.
params:
  source: pinboard
  sourceUrl: https://simonwillison.net/2023/Aug/27/wordcamp-llms/
---

![Making Large Language Models Work For You](/images/notes/simon-willison-making-llms-work.png)

## Summary

Simon Willison gave this keynote at WordCamp 2023 in National Harbor as a practical introduction to LLMs for a non-specialist developer audience. Willison is one of the most reliable voices on the practical applications of LLMs — he approaches them as a working developer building real tools, not as an AI researcher or a hype journalist, which gives his framing a useful ground-level quality.

The talk covers what LLMs actually are (next-token predictors trained on text corpora, not search engines, not databases, not reasoning systems in the logical sense), why they produce confident-sounding wrong answers (hallucination as a structural property of the prediction approach), and the practical use cases where they're genuinely useful today: writing assistance, code generation, explanation, summarization, and — Willison's favorite framing — as force multipliers for tasks where the output doesn't need to be perfect to be useful.

A theme throughout is epistemic hygiene: LLMs are tools with specific strengths and failure modes, and using them well requires understanding which is which. Willison has been particularly vocal about the hallucination problem and the risk of over-trusting model output. The WordCamp context (mostly WordPress developers) means the examples are concrete and practical rather than abstract — how these tools actually appear in development workflows.

## Key points

- LLMs are next-token predictors, not search engines or reasoning systems — understanding the mechanism explains the failures.
- Hallucination is structural: the model predicts what sounds right, not what is right.
- Most useful as "force multipliers" for tasks where imperfect output still helps — writing, code generation, explanation.
- Simon Willison's practitioner framing: treat with appropriate skepticism, verify outputs, don't over-rely.
- From WordCamp 2023; concrete developer-audience examples.

[Original](https://simonwillison.net/2023/Aug/27/wordcamp-llms/)
