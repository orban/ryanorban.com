---
title: "PromptSource: An Integrated Development Environment and Repository for Natural Language Prompts"
date: 2022-07-04
categories:
  - prompting
  - nlp
  - datasets
  - prompt-engineering
  - bigscience
  - multitask-learning
  - tools
description: PromptSource is an IDE and community repository for creating, sharing, and iterating on natural language prompts that map dataset examples to input-output pairs for language model training and evaluation. With over 2,000 prompts for ~170 datasets, it provided the infrastructure behind the T0 family of models and multitask prompted training research.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/2202.01279 1.pdf
---

## Summary

PromptSource, developed by the BigScience workshop and released by teams at Brown University, Hugging Face, and collaborators worldwide, is a practical system for the emerging practice of prompt engineering at research scale. A prompt in this context is a function that maps a structured dataset example (a question-answer pair, a premise-hypothesis, a sentence) into a natural language input and expected output, making it usable for training or evaluating language models in a zero-shot or few-shot setting.

The system has three components. First, a Jinja-based templating language that lets authors write prompts as code, referencing dataset fields by name and applying transformations. This makes prompts reproducible and tied to specific dataset schemas rather than written ad hoc. Second, an interactive interface that renders prompt outputs on live dataset examples, so authors can immediately see whether a prompt produces sensible inputs before committing it. Third, a community-driven contribution model with shared guidelines and a GitHub-hosted prompt collection that grew to over 2,000 prompts for roughly 170 datasets.

PromptSource was the direct infrastructure behind T0 (T-Zero), the multitask prompted model from the BigScience group that demonstrated surprisingly strong zero-shot generalization by training on a diverse set of prompted datasets. It also influenced FLAN and other instruction-tuning efforts that followed. In retrospect, PromptSource sits at the beginning of a wave — it treated prompt design as a first-class engineering problem requiring tooling and collaboration rather than ad hoc text manipulation, which is now standard thinking in the field.

## Key points

- Prompts are Jinja templates tied to specific dataset schemas, not free-form text strings — this makes them versioned, testable, and reproducible
- The interactive interface shows prompt outputs on real examples during authoring, dramatically reducing iteration time
- Community guidelines cover edge cases: how to handle multi-answer formats, label naming, prompt diversity requirements
- Directly enabled T0, which showed that multitask prompted training on diverse tasks transfers to unseen tasks without fine-tuning
- Over 2,000 prompts contributed; many are available on HuggingFace datasets and the `promptsource` library

[Original](file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/2202.01279 1.pdf)
