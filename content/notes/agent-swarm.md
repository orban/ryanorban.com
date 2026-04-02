---
title: "Agent Swarm: persistent multi-agent coding framework"
date: 2026-02-26
categories:
  - ai-agents
  - multi-agent
  - orchestration
  - docker
  - open-source
description: Agent Swarm is a lead/worker AI coding agent framework with persistent identity files, session memory extraction, and Docker isolation. Each agent accumulates expertise across sessions through SOUL.md, IDENTITY.md, TOOLS.md, CLAUDE.md.
params:
  source: pinboard
  sourceUrl: https://github.com/desplega-ai/agent-swarm
---

![Agent Swarm: persistent multi-agent coding framework](/images/notes/agent-swarm.png)

## Summary

[Agent Swarm](/notes/agent-swarm/) is a multi-agent framework where a lead agent delegates tasks to worker agents running in isolated Docker containers. The distinguishing feature is the persistent identity system: each agent maintains four evolving files — `SOUL.md`, `IDENTITY.md`, `TOOLS.md`, and `CLAUDE.md` — that persist across sessions and accumulate expertise over time. Agents aren't fresh instances each run; they carry forward what they've learned.

The memory layer is specifically designed to combat the failure mode of agents repeating mistakes. At the end of each session, a lightweight model extracts key learnings: mistakes made, patterns discovered, failed approaches, codebase-specific knowledge. This gets stored in a searchable database. On the next session, agents query that memory before making decisions, letting past experience inform current work.

Task ingestion works through Slack, GitHub, GitLab, and email — so existing team workflows can trigger agents directly. The lead agent breaks incoming tasks into subtasks, assigns them to workers, and tracks progress through a dashboard. Completed work generates PRs or closes issues; there's no need to babysit individual agent runs.

## Key points

- Lead/worker coordination: one lead agent delegates and tracks work across multiple Docker-isolated workers.
- Persistent identity files (`SOUL.md`, `IDENTITY.md`, `TOOLS.md`, `CLAUDE.md`) — agents accumulate expertise across sessions.
- Session memory extraction: lightweight model extracts lessons learned, mistakes, and patterns after each run.
- Task ingestion via Slack, GitHub, GitLab, and email — fits existing team workflows.
- Agents can modify their own startup scripts and environment knowledge — self-improvement loop.

[Original](https://github.com/desplega-ai/agent-swarm)
