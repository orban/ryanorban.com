---
title: "Jim Fan: Foundation Models for Embodied Agents"
date: 2023-03-13
categories:
  - ai-agents
  - embodied-ai
  - foundation-models
  - research
  - robotics
description: Jim Fan's talk on foundation models for embodied agents — covering how large pretrained models can be adapted for physical and simulated agents that act in the world. Previews the Voyager and MineDreamer research that followed from his NVIDIA lab.
params:
  source: pinboard
  sourceUrl: https://www.youtube.com/watch?v=17CeLwjwTVI
---

![Jim Fan: Foundation Models for Embodied Agents](/images/notes/jim-fan-foundation-models-embodied-agents.png)

## Summary

Jim Fan (senior research scientist at NVIDIA) gave this talk on applying foundation models to embodied AI — agents that perceive and act in physical or simulated environments rather than producing text. The central argument: the same scaling and pretraining paradigm that produced GPT-4 and DALL-E should be applied to agents that control robots, game characters, and simulated bodies.

The research agenda at Jim Fan's lab (NVIDIA's AI Research group) centered on what he calls foundation agents — models pretrained on diverse multi-task, multi-embodiment data that can be fine-tuned for specific physical tasks. This contrasts with narrow reinforcement learning approaches that train a separate policy per task. The foundation model framing brings transfer learning to embodied AI: a model that has learned to navigate, manipulate objects, and understand scenes can adapt to new tasks without training from scratch.

Jim Fan's subsequent work materialized as Voyager (an LLM-powered agent for Minecraft that discovers skills through self-play) and MineDreamer, both demonstrating that language model reasoning could drive embodied task completion in simulated environments. The talk sits at the intersection of the LLM scaling thesis and the robotics foundation model thesis that later produced RT-2, π0, and Physical Intelligence's work.

## Key points

- Argues for applying the foundation model pretraining paradigm to embodied agents — transfer learning over diverse multi-task data.
- Contrasts with narrow reinforcement learning: separate policies per task don't generalize; pretrained models do.
- Jim Fan's subsequent work: Voyager (LLM-driven Minecraft agent with SKILL discovery), MineDreamer.
- Connects LLM reasoning to physical/simulated action — language as the interface for embodied control.
- Related to RT-2, Physical Intelligence, and the broader robot foundation model research wave.

[Original](https://www.youtube.com/watch?v=17CeLwjwTVI) → AI agent
