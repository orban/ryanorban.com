---
title: Kiln Fine-Tuning LLM Models Guide
date: 2024-12-14
categories:
  - fine-tuning
  - llm
  - machine-learning
  - synthetic-data
  - ai-tools
description: "Kiln's practical fine-tuning guide walks through generating synthetic training data (the 'Ladder' strategy: 10 manual → 30 LLM → 1000 synthetic) and running training jobs on OpenAI, Fireworks, and Unsloth. Emphasizes data quality over cost during generation."
params:
  source: pinboard
  sourceUrl: https://github.com/Kiln-AI/Kiln/blob/main/guides/Fine%20Tuning%20LLM%20Models%20Guide.md
---

![Kiln Fine-Tuning LLM Models Guide](/images/notes/kiln-fine-tuning-guide.png)

## Summary

Kiln AI is a platform for building fine-tuned language models, and this guide documents their practical workflow. The core process has six steps: define the task specification, generate synthetic training data, select models for fine-tuning, dispatch training jobs, deploy the fine-tuned versions, and optionally run training locally. The guide covers training on OpenAI (GPT-4o, GPT-4o-mini), Fireworks (Llama, Mixtral), and Unsloth for open-source local training.

The Ladder data strategy is the most useful concept: start with ~10 manually curated examples, use those to generate ~30 LLM-assisted examples, then scale to ~1000 synthetic examples for actual training. The recommendation is to prioritize quality during data generation — use expensive models, detailed prompts, and token-heavy techniques — because the fine-tuned model can never exceed the quality of its training data. The guide explicitly warns against cutting corners at the data generation stage.

The output format for training data follows the Hugging Face chat template in JSONL, compatible with Axolotl and other training frameworks. The guide covers reserving test/validation splits for evaluation and iteration cycles for hyperparameter tuning and targeted quality fixes. Related to the broader LLM fine-tuning ecosystem and synthetic data generation as a training data strategy.

## Key points

- "Ladder" data strategy: 10 manual → 30 LLM-generated → 1000 synthetic examples.
- Prioritize quality over cost at data generation — fine-tune output quality is capped by training data.
- Supports OpenAI, Fireworks, and Unsloth (local) as training backends.
- Hugging Face JSONL chat format; Axolotl-compatible.
- Fine-tuning workflow ends with iterative hyperparameter tuning and targeted bug fixes.

[Original](https://github.com/Kiln-AI/Kiln/blob/main/guides/Fine%20Tuning%20LLM%20Models%20Guide.md) → GitHub
