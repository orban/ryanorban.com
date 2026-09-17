---
title: "PAL: Program-aided Language Models"
date: 2022-11-23
categories:
  - code-generation
  - reasoning
  - chain-of-thought
  - language-models
description: PAL prompts LLMs to generate Python programs as intermediate reasoning steps, then delegates actual computation to an interpreter, outperforming chain-of-thought on math and symbolic tasks. It neatly separates what LLMs are good at (translating problems to code) from what they're bad at (arithmetic).
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/2211.10435.pdf
---

## Summary

Luyu Gao, Aman Madaan, Shuyan Zhou, Uri Alon, Pengfei Liu, Yiming Yang, Jamie Callan, and Graham Neubig introduce PAL (Program-Aided Language Models), a prompting technique that instructs LLMs to decompose reasoning problems into Python programs rather than natural language chains. The programs are then executed by a real Python interpreter, with the interpreter's output used as the final answer. This cleanly sidesteps the well-documented weakness of language models on arithmetic and symbolic reasoning.

The key insight is a labor division: LLMs are strong at translating problem descriptions into structured code (they've seen millions of programming examples) but weak at executing multi-step arithmetic in their own forward pass. By outsourcing execution to a deterministic tool, PAL achieves accuracy that chain-of-thought prompting can't match on tasks where computation correctness matters. On GSM8K math word problems, MATH, and symbolic reasoning benchmarks, PAL substantially outperforms CoT with the same underlying model.

PAL prefigures the broader tool use paradigm that became standard in AI agents — the idea that language models should orchestrate external tools rather than attempt all computation natively. It connects directly to later work on ReAct, [Toolformer](/notes/toolformer/), code interpreter, and the entire trajectory of agentic LLMs that reason by writing and executing code. The paper is also notable for its clean evaluation methodology, which isolates the effect of program-aided reasoning from model size effects.

## Key points

- PAL generates Python programs as reasoning intermediates, then executes them with a real interpreter — separating language understanding from numerical computation.
- Outperforms chain-of-thought on GSM8K, MATH, and symbolic reasoning benchmarks while using the same base LLM.
- Addresses the core LLM arithmetic weakness: models hallucinate intermediate calculations; code doesn't.
- Early demonstration of the tool use paradigm — LLMs as orchestrators of external computation rather than self-contained reasoners.
- Directly influenced code interpreter, ReAct, [Toolformer](/notes/toolformer/), and the agentic LLM ecosystem where code execution is standard.

[Original](file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/2211.10435.pdf)
