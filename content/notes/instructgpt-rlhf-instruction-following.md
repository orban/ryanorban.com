---
title: Training Language Models to Follow Instructions with Human Feedback (InstructGPT)
date: 2022-07-30
categories:
  - rlhf
  - instruction-following
  - alignment
  - openai
  - fine-tuning
  - language-models
description: OpenAI's InstructGPT paper (2022) shows that a 1.3B model fine-tuned with RLHF on human preference data is preferred over raw GPT-3 at 175B — establishing that alignment via human feedback is more important than raw scale for following instructions. This is the foundational paper behind ChatGPT and the instruction-tuned era.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/Training_language_models_to_follow_instructions_with_human_feedback.pdf
---

## Summary

Long Ouyang, Jeff Wu, Xu Jiang, and colleagues at OpenAI introduce InstructGPT, the result of fine-tuning GPT-3 with Reinforcement Learning from Human Feedback (RLHF) to follow instructions. The headline result is startling: a 1.3B InstructGPT model is preferred by human evaluators over GPT-3 at 175B on the vast majority of prompts. Scale alone doesn't produce helpful behavior — the alignment procedure does.

The training pipeline has three stages. First, the base GPT-3 is fine-tuned on a dataset of human-written demonstrations of desired behavior (supervised fine-tuning, SFT). Second, a reward model is trained from human comparisons: labelers rank multiple model outputs from best to worst, and the reward model learns to predict these preference orderings. Third, the SFT model is further fine-tuned using Proximal Policy Optimization (PPO) to maximize the reward model's score, subject to a KL divergence penalty against the original model to prevent reward hacking. This three-step loop — demonstrate, compare, optimize — became the standard RLHF recipe.

The paper surfaces several important findings. InstructGPT produces fewer fabrications (hallucinations) and is less likely to generate toxic outputs than the base model. The fine-tuned model also improves on tasks not represented in the fine-tuning data, suggesting the RLHF procedure teaches something more general than just mimicking demonstrations. The authors are candid about the limitations: labeler preferences may not represent all users or cultures, and the reward model itself can be gameable — a model that optimizes the reward signal too hard drifts away from actual human preferences, a problem the KL penalty mitigates but doesn't solve.

## Key points

- The three-stage RLHF recipe — SFT on demonstrations, reward model trained from comparisons, PPO optimization with KL divergence penalty — became the template for all instruction-tuned models including ChatGPT.
- A 1.3B InstructGPT model is preferred over 175B GPT-3 on human evaluation — the clearest early demonstration that alignment matters more than scale for instruction following.
- Reduced hallucination and toxicity relative to the base model, though not eliminated — RLHF shifts behavior toward what labelers prefer, not objective accuracy.
- Introduces the concept of alignment tax: some RLHF fine-tuned models regress on certain academic NLP benchmarks, trading raw capability for helpfulness.
- Labeler agreement is imperfect — the reward model captures labeler preferences which may not generalize across cultures or user contexts.

[Original PDF](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/Training_language_models_to_follow_instructions_with_human_feedback.pdf)
