---
title: "Prompt Programming for Large Language Models: Beyond the Few-Shot Paradigm"
date: 2022-07-26
categories:
  - prompt-engineering
  - llm
  - few-shot
  - research
  - nlp
description: Reynolds and McDonell (2021) argue that prompting large language models is better understood as programming than as few-shot learning — the few examples in a prompt aren't training data but rather code that specifies the desired computation. This reframing opens up principled prompt design strategies that beat naive templating.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/Prompt Programming for Large Language Models- Beyond the Few-Shot Paradigm.pdf
---

## Summary

Laria Reynolds and Kyle McDonell (independent researchers) reframe prompting as a form of programming rather than few-shot learning. The conventional view in 2021 held that the examples you include in a prompt are there to teach the model the task via demonstration — analogous to few-shot in-context learning. Reynolds and McDonell argue this is wrong, or at least incomplete: the examples are better understood as *code* that specifies a desired computation by instantiating the task's structure, with the LLM acting as an interpreter.

This programming metaphor yields several practical design principles. Zero-shot prompts work when the task is unambiguous to the model's prior distribution; few-shot examples are needed when you need to constrain the *format* or *scope* of the output, not when you need to teach the task from scratch. The paper introduces the idea of **indirect prompts** — eliciting reasoning by asking the model to reason from a character's perspective (as an expert in X, explain...) — and **meta-prompts** — using the model itself to generate or critique prompts. Both techniques exploit the fact that the model has internalized vast amounts of implicit procedural knowledge from pre-training.

The paper also introduces the **vanishing text illusion**: a technique where you ask the model to describe what would appear in a document you haven't written yet, then use that output as a starting point. This documents a key property of LLMs: they can generate text that's consistent with hypothetical contexts. Reynolds and McDonell's framing was early and influential; many ideas here — indirect prompting, meta-prompting, zero-shot chain-of-thought — became standard practice and later appeared in more formal research.

## Key points

- Reframes prompt engineering as **prompt programming**: prompts specify computations; the LLM is an interpreter, not a learner.
- Few-shot examples aren't for teaching tasks but for constraining format and disambiguating scope within the model's prior.
- **Indirect prompts**: elicit knowledge by having the model adopt an expert perspective rather than directly stating the task.
- **Meta-prompts**: use the model to generate, evaluate, or refine its own prompts — an early formulation of self-refinement.
- Vanishing text illusion: models can generate content consistent with hypothetical documents they haven't been shown.
- Anticipates chain-of-thought prompting, zero-shot CoT, and role-based prompting that later formal papers formalized.

[Original PDF](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/Prompt%20Programming%20for%20Large%20Language%20Models-%20Beyond%20the%20Few-Shot%20Paradigm.pdf)
