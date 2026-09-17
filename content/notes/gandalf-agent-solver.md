---
title: "ai-llm-agent-solver: Autonomous Gandalf Challenge Solver"
date: 2024-07-28
categories:
  - ai-agents
  - prompt-injection
  - security
  - python
  - llm
description: An LLM-powered agent that autonomously solves the Gandalf AI challenge — a prompt injection security game where you try to extract a secret password from a guarded AI. Uses OpenAI API and agent-based reasoning.
params:
  source: pinboard
  sourceUrl: https://github.com/SabrinaRamonov/ai-llm-agent-solver
---

![ai-llm-agent-solver: Autonomous Gandalf Challenge Solver](/images/notes/gandalf-agent-solver.png)

## Summary

This repository by Sabrina Ramonov implements an LLM-powered AI agent that autonomously solves the Gandalf AI challenge — a popular prompt injection game where players try to extract a secret password from an AI model that's been instructed to keep it secret. The agent uses OpenAI's API to reason about and execute multi-turn attacks automatically.

The Gandalf challenge (by Lakera) is a canonical AI security demonstration. Each level is progressively harder to break, using different guardrails, system prompt protections, and instruction hierarchies. Solving it autonomously — rather than manually — demonstrates the viability of automated prompt injection attacks, which is the core safety concern: if an agent can be automated to attack other AI systems, the attack surface expands dramatically.

The implementation is interesting from a red teaming perspective. Manual prompt injection requires creativity and iteration; an automated agent can explore the attack space more systematically. This connects to broader work on adversarial AI, LLM security, and the question of how AI systems can be made more robust against automated adversaries.

## Key points

- Autonomous AI agent that solves the Gandalf AI challenge — a prompt injection security game.
- The Gandalf challenge (by Lakera) tests progressively harder instruction-following guardrails.
- Uses OpenAI API + agent-based reasoning for automated multi-turn attacks.
- Demonstrates the feasibility of automating prompt injection attacks.
- Python + Poetry for dependency management.
- Connects to red teaming, adversarial AI, and LLM security research.

[Original](https://github.com/SabrinaRamonov/ai-llm-agent-solver) → GitHub
