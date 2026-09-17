---
title: "Internet of Agents: Browser Agent Swarms via MultiOn"
date: 2023-12-12
categories:
  - ai-agents
  - multion
  - browser-automation
  - multi-agent
  - open-source
description: Internet of Agents is an open-source framework for building swarms of internet-browsing AI agents using MultiOn, enabling autonomous web tasks at scale. An early demonstration of multi-agent browser automation coordinated through a single API.
params:
  source: pinboard
  sourceUrl: https://github.com/Div99/InternetOfAgents/tree/main
---

![Internet of Agents: Browser Agent Swarms via MultiOn](/images/notes/internet-of-agents.png)

## Summary

[Internet of Agents](/notes/internet-of-agents/) is an open-source framework built on MultiOn that enables coordinating swarms of internet-browsing AI agents for web automation tasks. MultiOn provides a browser automation API where you describe a web task in natural language and an agent executes it — navigating pages, filling forms, extracting data, clicking buttons. [Internet of Agents](/notes/internet-of-agents/) layers a multi-agent coordination framework on top, dispatching multiple agents in parallel to different URLs or tasks.

The architecture follows the [agent swarm](/notes/agent-swarm/) pattern: a coordinator agent decomposes a high-level goal (research competitors, collect product data across sites, monitor multiple pages) into subtasks, dispatches browser agents to execute each subtask, and aggregates the results. The browser agents are autonomous — each one browses the web independently to complete its assigned task.

This was an early (December 2023) exploration of coordinated browser agent swarms, predating the Claude Computer Use, OpenAI Operator, and similar products that made browser automation more mainstream. The combination of LLM reasoning + browser control was just becoming reliable enough to build on in late 2023, and MultiOn was one of the first APIs to make browser agents accessible without building a custom automation stack.

## Key points

- [Agent swarm](/notes/agent-swarm/) pattern for browser automation: coordinator + multiple MultiOn browser agents in parallel.
- MultiOn API: describe a web task in natural language, agent executes it autonomously.
- Use cases: competitive research, product data collection, multi-site monitoring, form automation at scale.
- December 2023: early multi-agent browser automation before Computer Use and OpenAI Operator.
- Open-source — demonstrates the coordination layer on top of an existing browser automation API.

[Original](https://github.com/Div99/InternetOfAgents) → GitHub
