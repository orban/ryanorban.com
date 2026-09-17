---
title: "AI Adversarial Attacks: Automated Jailbreaks via Text Suffixes"
date: 2023-08-02
categories:
  - ai-safety
  - adversarial
  - jailbreak
  - research
  - security
description: Ars Technica covers the Universal Adversarial Attacks paper from CMU/Center for AI Safety — automated adversarial suffixes appended to prompts reliably bypass safety training on GPT-4, Claude, and open-source models. The attacks are transferable and potentially unstoppable with current alignment techniques.
params:
  source: pinboard
  sourceUrl: https://arstechnica.com/ai/2023/08/researchers-figure-out-how-to-make-ai-misbehave-serve-up-prohibited-content/
---

![AI Adversarial Attacks: Automated Jailbreaks via Text Suffixes](/images/notes/ai-adversarial-attacks-jailbreak.png)

## Summary

Ars Technica covered the "Universal and Transferable Adversarial Attacks on Aligned Language Models" paper from Andy Zou et al. at CMU and the Center for AI Safety. The core finding: researchers developed an automated method to generate adversarial suffixes — seemingly meaningless strings of text appended to prompts — that reliably bypass the safety training of aligned LLMs including GPT-4, Claude, and open-source models like LLaMA.

The attack is "universal" in that a single suffix can cause jailbreaks across many different harmful request types, and "transferable" in that suffixes optimized on open-source models (which researchers have access to) often work on closed models like GPT-4. The generation method uses gradient-based optimization on open-source models — you search for a suffix that maximizes the probability of the model beginning a harmful response. The resulting suffixes often look like random character strings but exploit low-level patterns in the model's token representations.

The paper created alarm in the AI safety community because it suggested that RLHF-based safety training might be fragile — a surface-level capability to refuse certain requests rather than a deep alignment of the model's values. If suffixes can bypass refusals, the question becomes whether more training just means more suffixes are needed to bypass it, or whether the approach is fundamentally limited.

Anthropic, OpenAI, and Google DeepMind all acknowledged the research and began work on defenses, though the paper's authors noted that current methods may be fundamentally unstoppable.

## Key points

- Adversarial suffixes (optimized text strings) reliably bypass safety training on GPT-4, Claude, LLaMA.
- Attack is universal (works across many request types) and transferable (open-source optimized → closed model).
- Gradient-based optimization on open-source models generates suffixes that transfer to proprietary ones.
- Suggests RLHF-based alignment may be fragile — refusals are surface behaviors, not deep values.
- From CMU / Center for AI Safety — major paper in AI safety and red teaming research.

[Original](https://arstechnica.com/ai/2023/08/researchers-figure-out-how-to-make-ai-misbehave-serve-up-prohibited-content/)
