---
title: A Generalist Agent
date: 2022-05-13
categories:
  - generalist-agent
  - multi-task
  - reinforcement-learning
  - multi-modal
  - deepmind
description: Presents Gato, a single transformer that acts as a multi-modal, multi-task, multi-embodiment generalist policy across 600+ tasks including Atari, robotic manipulation, image captioning, and dialogue using identical weights. Demonstrates that scaling language model principles to non-text domains produces surprisingly capable generalist behavior.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/Generalist Agent.pdf
---

## Summary

This DeepMind paper by Scott Reed, Konrad Zolna, Emilio Parisotto, and 17 co-authors including Nando de Freitas presents Gato, a single transformer model that operates as a generalist policy across over 600 diverse tasks. Gato uses a unified tokenization scheme to represent text, images, discrete actions, and continuous control signals (robot joint torques) as a flat sequence, then applies a standard autoregressive decoder to predict the next token. The same network weights handle Atari gameplay, real robotic arm manipulation, image captioning, question answering, and dialogue — selecting output type based on context.

The central claim is that multi-task learning at scale, using the same architectural recipe that drives progress in large language models, generalizes beyond text. Gato is trained on a massive dataset of demonstrations spanning digital and physical domains, with tasks serialized into sequences through domain-specific tokenizers. For continuous control, actions are discretized into bins; for vision, image patches are embedded; for text, standard subword tokens are used. The unified sequence is processed by a single transformer with 1.2B parameters.

Gato does not achieve state-of-the-art on any individual task — it explicitly trades per-task performance for breadth. But it demonstrates that a single model can be competent across qualitatively different domains, providing empirical grounding for foundation model thinking applied to embodied AI and robotics. The paper sparked significant discussion about the scaling hypothesis in reinforcement learning and whether sufficiently large generalist models might surpass specialists, a debate that continues in subsequent work on multi-task RL and world models.

## Key Points

- Gato uses a single 1.2B parameter transformer for 600+ tasks across text, vision, and robotic control
- Unified tokenization: continuous actions discretized, images patched, text subword-tokenized — all flattened into one sequence
- Same weights handle Atari, robotic arm stacking, image captioning, and chat — output type selected from context
- Competent but not state-of-the-art on individual tasks; trades depth for breadth
- Extends large language model scaling intuitions to multi-modal and embodied AI settings

[Original](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/Generalist%20Agent.pdf) → AI agent
