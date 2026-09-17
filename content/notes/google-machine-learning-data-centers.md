---
title: Google Turns to Machine Learning to Build a Better Data Centre
date: 2014-05-28
categories:
  - machine-learning
  - google
  - data-centers
  - infrastructure
  - neural-networks
description: A 2014 report on Google applying machine learning to optimize data center cooling — one of the first public disclosures that Google was using neural networks to automate infrastructure decisions. DeepMind later published the full methodology in 2016.
params:
  source: pinboard
  sourceUrl: http://www.zdnet.com/google-turns-to-machine-learning-to-build-a-better-datacentre-7000029930/
---

## Summary

This 2014 ZDNet report covers Google's early use of machine learning to optimize data center operations — specifically cooling system efficiency. The disclosure was notable at the time because it was one of the first public acknowledgments that Google was using neural networks to automate infrastructure decisions that had previously required expert human operators.

The problem is a natural fit for reinforcement learning and regression: a data center has dozens of sensors (temperatures, power draws, equipment states), and the goal is to minimize energy consumption while keeping equipment within safe temperature ranges. The state space is too large for hand-tuned rules, but supervised learning on historical operator decisions can learn good policies.

DeepMind later published the full methodology in 2016, revealing they'd achieved 15-40% reductions in cooling energy by training deep neural networks on sensor data. The 2014 article captures the moment before that disclosure — Google was applying the same approaches from image recognition and search ranking to physical infrastructure. It was an early signal that ML would eventually penetrate every part of large-scale systems, not just user-facing products.

## Key points

- Data center cooling optimization is a high-dimensional control problem: hundreds of sensors, non-linear dynamics, delayed feedback — a natural fit for machine learning.
- Google was using neural networks internally for infrastructure optimization at least two years before DeepMind published results in 2016.
- Energy efficiency gains from ML control (15-40% in later disclosures) translate to hundreds of millions in operating cost savings at Google's scale.
- Signals the broader pattern: ML moving from consumer-facing applications (search, ads, images) into operational and infrastructure systems.
- Precursor to DeepMind for Google-scale applications: the same techniques for game-playing and protein folding also optimize cooling towers.

[Original](http://www.zdnet.com/google-turns-to-machine-learning-to-build-a-better-datacentre-7000029930/)
