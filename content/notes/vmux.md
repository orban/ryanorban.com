---
title: "vmux: sandbox runtime for AI agents"
date: 2026-02-05
categories:
  - ai-agents
  - infrastructure
  - sandbox
  - developer-tools
  - cloudflare
description: vmux is a sandbox runtime for AI agents — preview URLs, log tailing, and tmux attach, running on Cloudflare CPU with Modal GPU backends. Gives agents a managed execution environment rather than direct host access.
params:
  source: pinboard
  sourceUrl: https://vmux.sdan.io/
---

![vmux: sandbox runtime for AI agents](/images/notes/vmux.png)

## Summary

[vmux](/notes/vmux/) is a hosted sandbox runtime purpose-built for AI agents. The pitch is concise: preview URLs, log tail, tmux attach, running on Cloudflare CPU with Modal GPU backends. Instead of giving agents direct access to a developer machine or a generic cloud VM, [vmux](/notes/vmux/) provides a managed execution environment with the primitives agents specifically need.

The preview URLs feature is notable — it lets agents serve and share web previews during development tasks without agents needing to configure networking themselves. Combined with log tailing and tmux attach for interactive sessions, it covers the main surfaces an agent interacts with when doing real development work.

Using Cloudflare for CPU workloads and Modal for GPU backends is an interesting infrastructure split: stateless compute at the edge for most agent tasks, with GPU capacity available for model inference or heavier computation when needed. This suggests [vmux](/notes/vmux/) is designed for AI agents that may need to run models locally as part of their work, not just make API calls.

## Key points

- Managed sandbox runtime for AI agents — preview URLs, log tailing, tmux attach.
- Cloudflare CPU for general compute, Modal GPU backends for heavier workloads.
- Preview URLs let agents serve web previews without manual networking configuration.
- Provides infrastructure isolation between agents and the host machine.
- Designed for agents doing real development work, not just API calls.

[Original](https://vmux.sdan.io/)
