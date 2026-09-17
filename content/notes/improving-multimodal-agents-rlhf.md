---
title: Improving Multimodal Interactive Agents with RLHF
date: 2022-11-22
categories:
  - rlhf
  - multimodal
  - embodied-agents
  - reinforcement-learning
  - research
description: The Interactive Agents Team at DeepMind (arXiv:2211.11602, 2022) applies RLHF to agents that must understand language instructions and act in visual environments, using human preference feedback to train a reward model for PPO-based RL. The result demonstrates that RLHF substantially improves instruction-following in embodied multimodal settings beyond what supervised learning alone achieves.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/2211.11602.pdf
---

## Summary

DeepMind's Interactive Agents Team (arXiv:2211.11602, 2022) extends RLHF (reinforcement learning from human feedback) beyond language models to agents operating in visual environments. The agents must both understand natural language instructions and take actions in a 3D environment — a harder setting than pure language generation because the action space is grounded in perception and the consequences of actions play out over time. Applying RLHF here required adapting the preference collection and reward modeling pipeline to handle the multimodal, sequential nature of embodied agent behavior.

Human raters watch videos of agent trajectories and provide preference judgments: given two agents attempting the same instruction, which did better? These preferences train a reward model that scores trajectories. The reward model is then used to fine-tune the agent with PPO (Proximal Policy Optimization). The setup mirrors the InstructGPT and Sparrow approach but operates over sequences of environment observations and actions rather than text tokens.

The paper's main finding is that RLHF substantially improves instruction-following compared to supervised learning baselines. Agents trained purely on behavioral cloning (imitating expert demonstrations) learn to perform the demonstrated actions but struggle to generalize to novel instructions or environments. RLHF-trained agents show better instruction following and adapt more flexibly, because the human preference signal captures what following the instruction actually means rather than just mimicking surface behaviors. This result positioned RLHF as broadly applicable to grounded, embodied settings — not just language generation — and connected to concurrent work on embodied AI and instruction-following robotics.

## Key points

- Applies RLHF to multimodal embodied agents: language input, visual observation, environment actions
- Human raters compare trajectory videos to generate preference data; these train a reward model for PPO
- RLHF substantially outperforms behavioral cloning (supervised learning on demonstrations) for instruction-following
- Extends DeepMind's Sparrow RLHF work from dialogue to grounded visual environments
- Early evidence that RLHF generalizes beyond text generation to complex multimodal sequential decision-making

[Source](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/2211.11602.pdf)
 → AI agent
