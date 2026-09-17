---
title: "Genetic Boids: Evolutionary Flocking Simulation"
date: 2025-05-24
categories:
  - simulation
  - emergence
  - evolutionary-algorithms
  - boids
  - creative-coding
description: Genetic Boids combines Craig Reynolds' flocking algorithm with evolutionary mechanics — up to 800 entities exhibit alignment, separation, and cohesion, with lifespan and signal parameters that drive emergent population behavior.
params:
  source: pinboard
  sourceUrl: https://attentionmech.github.io/genetic-boids/
---

![Genetic Boids: Evolutionary Flocking Simulation](/images/notes/genetic-boids.png)

## Summary

[Genetic Boids](/notes/genetic-boids/) is an interactive simulation by @attentionmech that combines Craig Reynolds' classic boids flocking algorithm with evolutionary mechanics. The three core boid behaviors remain — alignment (orient toward neighbors' heading), separation (avoid crowding), and cohesion (attract toward group center) — but layer on top a lifespan system and signal mechanics that can drive emergent evolution over time.

The standard boids algorithm produces surprisingly organic-looking collective motion from simple local rules with no global coordination. [Genetic Boids](/notes/genetic-boids/) extends this with a "Signal" mechanic — probability, range, and force parameters that represent inter-entity communication, possibly modeling how information or behavioral traits propagate through the population. With lifespan limits, generations turn over and the population's aggregate behavior can shift.

This sits in the tradition of artificial life simulations — Conway's Game of Life, Tierra, Avida — where complex emergent behavior arises from minimal rule sets. The @attentionmech account produces these interactive creative coding experiments consistently; this is one of their more complete simulations with preset configurations (Calm, Chaotic, Swarm, Signals).

## Key points

- Boids algorithm: alignment, separation, cohesion — emergent flocking from local rules.
- Evolutionary layer: lifespan limits cause generational turnover; signals enable information propagation.
- Up to 800 entities simulated in real-time in browser.
- Preset configurations (Calm, Chaotic, Swarm, Signals) for exploring parameter space.
- Part of the artificial life / emergence tradition: complex behavior from simple rules.
- Creative coding experiment by @attentionmech — a series of interactive simulations.

[Original](https://attentionmech.github.io/genetic-boids/) → GitHub
