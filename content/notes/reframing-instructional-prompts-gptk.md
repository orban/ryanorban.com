---
title: Reframing Instructional Prompts to GPTk's Language
date: 2026-04-29
categories:
  - prompt-engineering
  - llm
  - nlp
  - few-shot-learning
  - research
description: ACL 2022 Findings paper showing that manually reframing instructional prompts — decomposing tasks, itemizing steps, adding positive examples — yields 6–12% performance gains on GPT-2 and GPT-3. The key insight is that models respond better to concrete, step-by-step instructions than to long abstract descriptions.
params:
  source: papers
  sourceUrl: https://arxiv.org/abs/2109.07830
---

## Summary

This ACL 2022 paper by Swaroop Mishra, Daniel Khashabi, Chitta Baral, Yejin Choi, and Hannaneh Hajishirzi from Allen Institute for AI, University of Washington, and Arizona State University investigates what makes instructional prompts easier for language models to follow. The core claim: poorly phrased instructions fail not because the task is hard, but because the phrasing is ill-suited to how LLMs process text.

The paper introduces five prompt reframing techniques: task decomposition (breaking a complex task into simpler sub-steps), itemizing instructions as sequential steps, including positive examples, adding negative examples, and providing explanations. Across 12 NLP tasks in 6 categories, reframed prompts outperform original instructions by 12.5% on GPT-3 and 6.7% on GPT-2 in the few-shot learning setting. Crucially, reframed prompts also reduce the number of examples needed — making the approach especially valuable where in-context learning examples are expensive.

The study connects to the broader question of prompt sensitivity — small changes in prompt wording produce dramatically different outputs from the same model. While prompt engineering had been observed empirically, this paper provides systematic empirical grounding for *why* specific structural choices work. The finding that step-by-step decomposition helps anticipates chain-of-thought prompting, which was published later and showed similar structural intuitions.

## Key points

- Five reframing techniques: task decomposition, step itemization, positive examples, negative examples, explanation — each evaluated independently and combined.
- Zero-shot and few-shot learning both benefit, but the gains are larger in few-shot learning settings.
- Gains hold across model sizes (GPT-2 through GPT-3) — reframing is not a size-specific trick.
- Anticipates chain-of-thought prompting by showing that structured step-by-step decomposition helps models on complex tasks requiring multi-step reasoning.
- Published at ACL 2022 Findings; connects to the broader SUPER-NaturalInstructions line of work on instruction-following benchmarks.

[Original](https://arxiv.org/abs/2109.07830)
