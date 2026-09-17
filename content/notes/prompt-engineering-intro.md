---
title: A Complete Introduction to Prompt Engineering
date: 2022-10-21
categories:
  - prompt-engineering
  - llm
  - tutorial
  - gpt
  - nlp
description: Mihail Eric's comprehensive introduction to prompt engineering for LLMs — covering few-shot prompting, chain-of-thought, instruction tuning, and evaluation. Published in late 2022 when prompt engineering was emerging as a recognized discipline.
params:
  source: pinboard
  sourceUrl: https://www.mihaileric.com/posts/a-complete-introduction-to-prompt-engineering/
---

## Summary

This guide by Mihail Eric is a systematic introduction to prompt engineering for large language models — written in late 2022 when the discipline was being named and documented. It covers the spectrum from basic prompting patterns to more sophisticated techniques that had recently been discovered: few-shot prompting (providing examples in the prompt), chain-of-thought prompting (asking the model to show its reasoning), instruction tuning (how fine-tuning on instructions changes model behavior), and evaluation strategies.

The timing matters: this was written after GPT-3 had been available for a couple of years, but before ChatGPT made LLMs mainstream and before GPT-4 raised the capability ceiling significantly. The techniques documented here were the frontier of practical LLM use. Chain-of-thought prompting in particular had only been formally described in a 2022 Google paper and was still being absorbed by practitioners.

Prompt engineering existed in an awkward disciplinary space in 2022: it was clearly important for getting useful outputs from LLMs, but it was also fragile (prompt sensitivity was high) and model-specific (techniques that worked on GPT-3 didn't necessarily transfer to other models). The question of whether it would remain important as models improved — or whether better models would make careful prompting unnecessary — was unresolved and remains so.

## Key points

- Systematic coverage of prompt engineering techniques: few-shot prompting, chain-of-thought, instruction following.
- Written at the moment prompt engineering was being named as a discipline — 2022 frontier techniques.
- Chain-of-thought prompting: eliciting step-by-step reasoning dramatically improves performance on complex tasks.
- Few-shot prompting: providing examples in-context shapes output format and task interpretation.
- Evaluation and iteration are as important as technique — knowing when a prompt works requires measurement.
- The field has moved fast since; later GPT-4, Claude, and Gemini shifted what works and why.

[Original](https://www.mihaileric.com/posts/a-complete-introduction-to-prompt-engineering/)
