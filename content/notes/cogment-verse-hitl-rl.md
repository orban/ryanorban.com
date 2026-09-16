---
title: "Cogment Verse: Human-in-the-Loop Reinforcement Learning"
date: 2022-01-22
categories:
  - reinforcement-learning
  - human-in-the-loop
  - ai
  - multi-agent
  - research
  - open-source
description: Cogment Verse is an SDK for training and validating AI agents in human-in-the-loop learning (HITL) and multi-agent reinforcement learning environments. Provides a web UI for human participation in training alongside standard RL algorithms like A2C and PPO.
params:
  source: pinboard
  sourceUrl: https://github.com/cogment/cogment-verse
---

## Summary

Cogment Verse is an open-source SDK built on the [Cogment](/notes/cogment/) platform for training reinforcement learning agents in environments that include human participants. It addresses a specific research challenge: when you want to combine human expertise with automated learning — either to bootstrap agent training from human demonstrations or to study how agents and humans learn together.

The framework supports environments compatible with OpenAI Gym specifications, which means existing RL environments plug in without major changes. Key algorithms included are A2C, PPO, and behavioral cloning from human demonstrations. The web-based interface for interactive gameplay is the distinctive piece — humans can directly participate in training sessions, providing the human-in-the-loop part of HITL learning.

Multi-agent reinforcement learning (MARL) support via PettingZoo and Overcooked-AI integration makes it relevant for research on agent coordination and human-AI teaming. Isaac Gym integration addresses physics simulation for robotics research. Cogment Verse has been used in published work on warm-start learning and curriculum design — it's research-grade, not just a toy framework.

## Key points

- Human-in-the-loop learning (HITL): humans participate in training sessions via web UI, providing demonstrations or real-time feedback.
- Supports OpenAI Gym-compatible environments plus PettingZoo (MARL) and Isaac Gym (physics/robotics).
- Built-in algorithms: A2C, PPO, behavioral cloning from demonstrations.
- Multi-agent reinforcement learning (MARL) use case: studying agent coordination and human-AI teaming.
- Research-grade: has been cited in published work on warm-start learning and curriculum learning for RL.

[Original](https://github.com/cogment/cogment-verse) → GitHub, AI agent
