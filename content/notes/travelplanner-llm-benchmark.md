---
title: "TravelPlanner: A Benchmark for Real-World Planning with Language Agents"
date: 2024-06-11
categories:
  - llm
  - benchmarking
  - research
  - planning
  - ai-agents
  - arxiv
description: TravelPlanner is a benchmark for evaluating LLM planning capabilities in complex real-world scenarios — GPT-4 scored 0.6% on the full benchmark, revealing that even the best LLMs struggle with multi-constraint sequential planning. A sobering check on agentic AI ambitions.
params:
  source: pinboard
  sourceUrl: https://arxiv.org/abs/2402.01622
---

![TravelPlanner: A Benchmark for Real-World Planning with Language Agents](/images/notes/travelplanner-llm-benchmark.png)

## Summary

TravelPlanner is a benchmark designed to test LLM planning capabilities in a realistic, constrained setting: creating detailed travel itineraries. The benchmark provides a rich environment with tools to query nearly 4 million data records (flights, hotels, restaurants, attractions) and 1,225 carefully designed planning tasks with specific constraints — budget limits, dietary restrictions, accommodation preferences, transportation requirements. Success requires satisfying all constraints, not just producing a plausible-sounding plan.

The results are striking and sobering: even GPT-4 achieves only 0.6% success rate on the full benchmark (all constraints must be satisfied). Models consistently fail to track multiple constraints simultaneously, pick the wrong tools to gather information, lose track of state across multi-step planning, and hallucinate data rather than querying the available tools. The benchmark is specifically designed to avoid the vibes-based evaluation problem — it has objective right answers, so you can't fool it with confident-sounding but incorrect plans.

This is a meaningful data point for claims about AI agent capability in 2024. The failure mode isn't that models can't describe travel planning — they can produce excellent-sounding itineraries. The failure is that they can't satisfy all the *specific, simultaneous constraints* of a real booking. This connects to fundamental questions about LLM planning: these models are trained to produce plausible text, not to do constraint satisfaction. TravelPlanner separates "generates a travel plan that sounds good from generates a travel plan that actually works."

## Key points

- 1,225 travel planning tasks with specific constraints (budget, dietary, accommodation preferences).
- Tools provide access to ~4M real data records; agents must query tools, not hallucinate answers.
- GPT-4: 0.6% full success rate. Performance collapses when multiple constraints must be satisfied simultaneously.
- Failure modes: constraint tracking, wrong tool selection, state management across steps, hallucinated data.
- Objective benchmark — no vibes-based scoring, constraints either satisfied or not.
- Key finding: LLMs can *describe* planning but can't reliably *do* planning in constrained settings.

[Original](https://arxiv.org/abs/2402.01622)
