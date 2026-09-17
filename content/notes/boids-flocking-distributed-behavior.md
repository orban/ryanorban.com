---
title: "Flocks, Herds, and Schools: A Distributed Behavioral Model"
date: 2012-09-16
categories:
  - simulation
  - emergent-behavior
  - computer-graphics
  - algorithms
  - complex-systems
description: Craig Reynolds's 1987 SIGGRAPH paper on Boids — the three-rule algorithm (separation, alignment, cohesion) that produces realistic flocking behavior from local agent interactions alone. One of the most cited demonstrations that complex group behavior emerges from simple rules, not central coordination.
params:
  source: pinboard
  sourceUrl: http://www.cs.toronto.edu/~dt/siggraph97-course/cwr87/
---

## Summary

Craig Reynolds's 1987 SIGGRAPH paper introduced Boids — a simulation of flocking behavior in birds (and schooling in fish, herding in mammals) that produces remarkably realistic group motion from just three simple rules applied to each agent individually:

1. **Separation**: steer to avoid crowding local flockmates
2. **Alignment**: steer toward the average heading of local flockmates
3. **Cohesion**: steer toward the average position of local flockmates

No central coordinator. No global state. Each Boid only knows about neighbors within a local radius, yet the emergent behavior — tight, wheeling flocks that split around obstacles and remerge — is indistinguishable from real bird flocks. This was a striking demonstration of emergent behavior and self-organization in complex systems.

The paper is a foundational text in artificial life and agent-based modeling. Its impact extends well beyond computer graphics: the Boids algorithm influenced swarm robotics, multi-agent systems, crowd simulation in video games and film (the wildebeest stampede in *The Lion King* used a Boids variant), and the broader scientific understanding of how collective intelligence arises in biology without central control. The ant colony optimization and particle swarm optimization algorithms in evolutionary computation draw on the same principles.

## Key points

- Boids algorithm: three local rules (separation, alignment, cohesion) → realistic global flocking behavior — no central control required
- Emergent behavior principle: complex group-level patterns arising from simple agent-level rules is a general phenomenon, not a simulation artifact
- Appeared at SIGGRAPH 1987 as a computer graphics contribution but became foundational for complex systems science
- Influenced swarm robotics, crowd simulation, multi-agent systems, and evolutionary computation (particle swarm optimization)
- Self-organization without central coordination: a model for understanding ant colonies, fish schools, markets, internet routing, and many other distributed systems

[Original](http://www.cs.toronto.edu/~dt/siggraph97-course/cwr87/)
 → AI agent
