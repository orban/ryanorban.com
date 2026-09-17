---
title: "llm-reasoners: Advanced LLM Reasoning Algorithms"
date: 2023-08-02
categories:
  - llm
  - reasoning
  - research
  - python
  - planning
description: llm-reasoners is a library for advanced LLM reasoning algorithms — implementing Tree of Thoughts, RAP (Reasoning via Planning), and other structured reasoning approaches over standard chain-of-thought. Useful for research into how to get LLMs to reason more reliably on complex tasks.
params:
  source: pinboard
  sourceUrl: https://github.com/Ber666/llm-reasoners
---

![llm-reasoners: Advanced LLM Reasoning Algorithms](/images/notes/llm-reasoners-library.png)

## Summary

llm-reasoners is a research library implementing advanced LLM reasoning algorithms beyond standard chain-of-thought prompting. The library includes implementations of Tree of Thoughts (ToT), RAP (Reasoning via Planning), MCTS (Monte Carlo Tree Search) applied to language model reasoning, and other structured search approaches to LLM problem-solving.

The motivation: chain-of-thought prompting works well for many tasks but struggles with problems that require exploring multiple solution paths, backtracking, or making decisions that only look good several steps later. These are exactly the cases where search algorithms shine. Tree of Thoughts breaks the reasoning process into discrete thoughts that form a tree, allowing the model to explore branches and backtrack — more like how humans solve hard puzzles than the linear chain-of-thought process.

RAP specifically frames reasoning as a planning problem: the LLM acts as both a world model (predicting the consequences of reasoning steps) and an agent (selecting next steps). This allows applying classical planning algorithms (MCTS, A*) to LLM reasoning, structured search over the space of possible reasoning paths rather than greedy left-to-right generation.

The library was part of a 2023 research wave exploring structured reasoning in LLMs, which also included Self-Consistency, ReAct, and Reflexion — all trying to address the same underlying weakness of single-pass LLM reasoning.

## Key points

- Implements Tree of Thoughts, RAP, MCTS-based reasoning — structured alternatives to chain-of-thought.
- Tree of Thoughts: reasoning as a branching tree, enabling exploration and backtracking.
- RAP: LLM as world model + agent, applying classical planning to reasoning.
- Part of 2023's structured reasoning research wave alongside Reflexion, ReAct, Self-Consistency.
- Addresses chain-of-thought's limitation on problems requiring multi-path exploration.

[Original](https://github.com/Ber666/llm-reasoners) → GitHub, AI agent
