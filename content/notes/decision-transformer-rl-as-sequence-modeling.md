---
title: "Decision Transformer: Reinforcement Learning via Sequence Modeling"
date: 2022-04-12
categories:
  - reinforcement-learning
  - transformers
  - sequence-modeling
  - offline-rl
  - gpt
  - decision-making
description: Decision Transformer recasts offline reinforcement learning as a conditional sequence modeling problem, using a causally masked Transformer to generate actions conditioned on desired return, past states, and actions. It matches or exceeds model-free offline RL baselines on Atari, OpenAI Gym, and Key-to-Door without any value function or policy gradient computation.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/2106.01345.pdf
---

## Summary

Decision Transformer is a reframing of offline reinforcement learning as a sequence modeling problem, allowing the full machinery of large Transformer models — and the advances in language modeling behind GPT — to be applied to decision-making tasks without any explicit value function or policy gradient. The key insight is that if you condition an autoregressive model on a desired future return (reward), along with the history of states and actions, it can learn to produce action sequences that achieve that return.

The architecture feeds three interleaved token streams into a GPT-style causal Transformer: return-to-go tokens, state tokens, and action tokens. Each has its own learned linear embedding, and they share a positional encoding based on timestep (not absolute sequence position). At inference time, the desired return is set high, and the model autoregressively samples actions. Unlike Q-learning or actor-critic methods, there's no Bellman backup, no temporal difference error, and no reward discounting — the entire RL problem is reduced to supervised next-token prediction on offline trajectory data.

Evaluated on Atari games, OpenAI Gym MuJoCo locomotion tasks, and the Key-to-Door sparse reward task, Decision Transformer matches or exceeds CQL, IQL, and other state-of-the-art offline RL baselines. The result is important because it suggests that the inductive biases embedded in the Transformer — attention over long context, scalability, and representational power — are sufficient for credit assignment across long horizons, which was thought to require specialized RL algorithms.

## Key points

- Return-to-go conditioning: the model is given the sum of future rewards it should achieve, not a reward signal to optimize
- No value function, no Bellman equation; training is pure supervised imitation on offline trajectory datasets
- Uses GPT-2 architecture with separate token types for returns, states, and actions
- On Atari, outperforms CQL on most games despite requiring no environment interaction
- Opens a research direction: transformers for RL as a viable alternative to classical RL formulations

[Original](file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/2106.01345.pdf)
