---
title: Training Language Models with Natural Language Feedback
date: 2022-11-24
categories:
  - RLHF
  - alignment
  - natural-language-feedback
  - fine-tuning
  - NLP
description: Proposes learning from natural language feedback on model outputs rather than simple comparison labels, using a generate-filter-finetune loop to train GPT-3 to human-level summarization with only 100 feedback samples. Natural language carries more alignment signal per human evaluation than pairwise comparisons.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/2204.14146v2.pdf
---

## Summary

This paper from NYU and collaborators tackles a core problem in RLHF: comparison feedback (thumbs up/down between two outputs) is informationally sparse. Each human evaluation conveys little about *why* one output is better. The authors propose using natural language feedback — full written critiques of model outputs — which packs far more signal per annotation.

The method runs in three steps: a language model is conditioned on the original input, its output, and a human critique to generate multiple candidate *refinements*. The best refinement is selected by similarity to the feedback. That refinement then trains the model via standard supervised fine-tuning. This avoids the complexity of a full reward model + RL from Human Feedback loop.

In synthetic experiments, only large models (~175B parameters) reliably incorporate feedback to improve outputs. But using just 100 real human critiques, the algorithm fine-tunes a GPT-3 model to near-human-level performance on summarization. The gap between how much information comparison vs. language feedback conveys has direct implications for how cheaply alignment can be achieved.

## Key points

- Natural language feedback packs more information per annotation than binary preference learning comparisons
- Only very large language models (~175B) can reliably follow verbal critiques to generate better refinements
- With just 100 human feedback samples, GPT-3 reaches human-level summarization quality
- The refinement-selection step (picking the highest-similarity-to-feedback candidate) is critical to quality
- This prefigures later work on [constitutional AI](/notes/constitutional-ai/) and self-critique loops in AI alignment

[Original paper](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/2204.14146v2.pdf)
