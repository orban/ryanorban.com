---
title: "Learning World Model Learning: inverse dynamics"
date: 2026-02-06
categories:
  - robotics
  - world-models
  - inverse-dynamics
  - machine-learning
  - open-source
description: Inverse dynamics learning as part of a 'learning world model learning from scratch' series — teaches robots to infer what actions produced observed state transitions. A ground-up educational approach to the robotics data problem.
params:
  source: pinboard
  sourceUrl: https://github.com/pham-tuan-binh/learning-world-model-learning/tree/main/2.inverse-dynamics
---

![Learning World Model Learning: inverse dynamics](/images/notes/inverse-dynamics.png)

## Summary

Learning World Model Learning is an educational project by Pham Tuan Binh that builds up world model concepts from scratch. The inverse dynamics module (section 2) teaches the technique of inferring what actions caused an observed state transition — if you see the robot go from state A to state B, [inverse dynamics](/notes/inverse-dynamics/) gives you the action that produced it.

The project opens with a compelling cost analysis of the robotics data problem: scaling robotic training data to GPT-2 equivalence (~10B tokens) at human collection rates would take 10 years and $400,000 at minimum wage. World models are the proposed solution — learn a model of environment dynamics from limited real data, then generate synthetic experience. [Inverse dynamics](/notes/inverse-dynamics/) is a key component: you can mine existing video data for implicit action labels without teleoperation.

This addresses one of the fundamental bottlenecks in embodied AI: while LLMs benefit from internet-scale text, robots can't easily access equivalent diversity of experience. World models trained on passive video data (using [inverse dynamics](/notes/inverse-dynamics/) to infer actions) could close that gap substantially cheaper than physical data collection.

## Key points

- [Inverse dynamics](/notes/inverse-dynamics/): infer what actions caused observed state transitions — labels video data implicitly.
- Part of a from-scratch world model learning series tackling the robotics data problem.
- Robotics data gap: scaling to LLM-equivalent training data is 10x more expensive than text.
- World models + [inverse dynamics](/notes/inverse-dynamics/) enable training from passive video without teleoperation.
- Educational resource — builds intuition for embodied AI data efficiency techniques.

[Original](https://github.com/pham-tuan-binh/learning-world-model-learning/tree/main/2.inverse-dynamics)
