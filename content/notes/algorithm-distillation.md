---
title: In-Context Reinforcement Learning with Algorithm Distillation
date: 2022-10-27
categories:
  - reinforcement-learning
  - in-context-learning
  - meta-learning
  - transformers
  - deepmind
description: Algorithm Distillation trains a causal transformer on sequences of RL learning histories so the model can improve its policy entirely in-context without gradient updates. A key step toward meta-learning agents that get better at RL through experience rather than parameter updates.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/IN-CONTEXT REINFORCEMENT LEARNING WITH ALGORITHM DISTILLATION.pdf
---

## Summary

Algorithm Distillation (AD), from DeepMind (Laskin et al., 2022), is a method for distilling entire reinforcement learning algorithms into a neural network by training it on sequences of RL learning histories. The core idea: if you expose a causal transformer to many episodes of an RL agent improving at a task, the transformer learns to predict the improving agent's behavior — and this learned prediction generalizes to new tasks without any gradient updates.

This is a form of meta-learning or in-context learning applied to RL. Traditional meta-RL (like MAML or RL²) distills the learned policy but not the learning algorithm itself. AD goes further: it distills the *dynamic process* of improvement. The training dataset consists of full learning histories — sequences of (observation, action, reward) tuples across many episodes — and the transformer is trained autoregressively to predict actions given this cross-episode context.

The implications are significant for AI agents. An AD-trained model can reinforce-learn in-context: given a few episodes of interacting with a new environment, it improves without updating weights. This is analogous to how few-shot prompting allows GPT-style models to "learn" tasks in context. AD extends this to the RL regime, where tasks involve sequential decisions rather than single-turn outputs. The paper shows this works in sparse-reward environments and with pixel-based observations — non-trivial challenges.

## Key points

- [Algorithm Distillation](/notes/algorithm-distillation/) differs from behavioral cloning of expert policies — it distills the *learning dynamic*, not just the end state, enabling continued improvement in context
- The trained model is more data-efficient than the source RL algorithm that generated the training data — the transformer extracts a better inductive bias from the learning histories
- Works across combinatorial task structure and sparse rewards, suggesting the in-context RL mechanism is robust to hard exploration problems
- Related to Decision Transformer and trajectory optimization but focuses on the learning process rather than optimal behavior
- Points toward foundation models for RL: a single model that can adapt to any RL task through context, analogous to GPT's few-shot capability for supervised tasks

[Algorithm Distillation Paper (PDF)](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/IN-CONTEXT%20REINFORCEMENT%20LEARNING%20WITH%20ALGORITHM%20DISTILLATION.pdf) → AI agent
