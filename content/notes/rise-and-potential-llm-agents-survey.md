---
title: "The Rise and Potential of LLM-Based Agents: A Survey"
date: 2023-09-20
categories:
  - ai-agents
  - llm
  - survey
  - research
  - paper
description: An 86-page survey paper by Zhiheng Xi et al. comprehensively mapping the architecture, capabilities, and applications of LLM-based agents — establishing the planning/memory/tool-use framework that became the standard way to think about agent components. The field's foundational survey document.
params:
  source: pinboard
  sourceUrl: https://arxiv.org/abs/2309.07864
---

![The Rise and Potential of LLM-Based Agents: A Survey](/images/notes/rise-and-potential-llm-agents-survey.png)

## Summary

This 86-page survey by Zhiheng Xi, Wenxiang Chen, Xin Guo et al. is the most comprehensive early review of LLM-based AI agent research, written at the pivotal moment when the field was rapidly expanding but lacked a unifying framework. Published September 2023, it synthesizes the previous two years of research into a coherent architecture — establishing the tripartite framework of **brain** (the LLM itself), **perception** (multi-modal inputs), and **action** (tool use, code execution, physical world interaction).

The framework for agent components the survey introduces became standard: **planning** (task decomposition into subtasks, chain-of-thought, ReAct, reflection loops); **memory** (sensory/buffer memory in context vs. long-term storage in vector databases vs. parametric memory in model weights); **tool use** (calling APIs, executing code, web search); and **action** (output in text, code, or physical actuators). Nearly all subsequent agent frameworks — LangChain, AutoGPT, LlamaIndex agents — can be understood through this lens.

The applications section surveys agents in domains: social simulation, software development, scientific discovery, embodied agents. The limitations section is still relevant: LLM reasoning brittleness, lack of long-term memory, difficulty with sequential planning, and multi-agent coordination failures.

## Key points

- Establishes brain/perception/action architecture for LLM agents — now the standard framework.
- Agent components: planning (decomposition, reflection), memory (context/vector/parametric), tools, action.
- chain-of-thought, ReAct, and tree-of-thought covered as planning primitives.
- Memory taxonomy: sensory (in-context) vs. long-term (vector database) vs. parametric (in weights).
- Covers applications: social simulation, software engineering, science, embodied AI.
- September 2023: foundational survey written at the start of the agent era, widely cited since.

[Original](https://arxiv.org/abs/2309.07864)
