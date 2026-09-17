---
title: "Pretrain, Prompt, Predict: NLP Survey"
date: 2022-07-27
categories:
  - nlp
  - prompt-learning
  - pretrained-models
  - survey
  - few-shot
description: A comprehensive survey of the Pretrain, Prompt, Predict paradigm in NLP — covering prompt engineering, answer engineering, and in-context learning as a unified framework. The academic backbone behind what practitioners call 'prompt engineering'.
params:
  source: pinboard
  sourceUrl: http://pretrain.nlpedia.ai/
---

## Summary

pretrain.nlpedia.ai is the companion website to a major academic survey paper on prompt-based learning in NLP, organized around what the authors call the [Pretrain, Prompt, Predict](/notes/pretrain-prompt-predict/) paradigm. The thesis: NLP went through two major paradigm shifts. First was the move from task-specific feature engineering to task-specific models trained on fixed datasets. Second — the current era — is using pretrained language models adapted through prompting rather than fine-tuning on labeled datasets. The survey maps this second shift comprehensively.

The framework covers prompt engineering at the academic level: discrete prompts (human-written text templates), continuous prompts (soft prompts that are learned vectors), and hybrid approaches. Answer engineering addresses how you extract a final answer from the model's generation — for classification, this means mapping generated tokens back to labels. Multi-prompt learning covers ensembling prompts, chain-of-thought, and augmentation strategies. The in-context learning section covers few-shot and zero-shot settings where no parameter updates occur.

By 2022, this survey served as the academic backbone for what practitioners were calling "prompt engineering." It formalized vocabulary and provided systematic analysis of what was mostly ad-hoc practitioner knowledge at the time. The curated paper lists per topic — classification, information extraction, QA, generation — make it a useful reference for understanding what's been done in each application area.

## Key points

- "Pretrain, Prompt, Predict": the third NLP paradigm after feature engineering → task-specific models → prompting
- Prompt engineering: discrete (text templates), continuous (soft prompts), hybrid approaches
- Answer engineering: mapping model generation back to task labels for classification
- In-context learning: zero-shot and few-shot adaptation without parameter updates
- Timeline of developments, GitHub paper lists, full survey PDF — comprehensive research resource
- Academic formalization of what practitioners were calling prompt engineering

[Original](http://pretrain.nlpedia.ai/)
