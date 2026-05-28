---
title: "Gorilla CLI: LLMs for Your CLI"
date: 2023-06-29
categories:
  - llm
  - cli
  - developer-tools
  - open-source
  - function-calling
description: Gorilla CLI is an LLM-powered tool that converts natural language commands into correct shell commands — type what you want to do, get the right command. Built by the team behind the Gorilla LLM model for API function calling.
params:
  source: pinboard
  sourceUrl: https://github.com/gorilla-llm/gorilla-cli
---

![Gorilla CLI: LLMs for Your CLI](/images/notes/gorilla-cli-llm.png)

## Summary

Gorilla CLI from the Gorilla LLM team at UC Berkeley turns natural language into correct shell commands. Instead of remembering exact flags and syntax, you type what you want to do and Gorilla CLI generates the command. `gorilla list all files modified in the last 24 hours` → `find . -mtime -1 -type f`. The tool executes only after user confirmation, not automatically.

The project connects to the Gorilla LLM research project — a model specifically fine-tuned on API documentation (including CLI tools, REST APIs, and Python libraries) to generate accurate function calls. The research finding was that fine-tuning on API docs dramatically reduced hallucinated API calls — standard LLMs frequently generate plausible-looking but non-existent function signatures; Gorilla was trained to be accurate. The CLI tool applies this capability to shell commands.

The CLI-as-interface-for-LLMs category had several entries in 2023: Gorilla CLI, GitHub Copilot CLI (`gh copilot suggest`), Amazon CodeWhisperer's CLI integration, and various terminal AI tools. All address the same friction: developers forget CLI syntax constantly (especially for tools used occasionally), and LLMs have absorbed vast amounts of CLI documentation. The bottleneck is reliability — the cost of a wrong suggestion is executing a damaging command. Gorilla's confirmation step and accuracy focus address this.

## Key points

- Natural language → shell command with confirmation before execution — never auto-runs.
- From the Gorilla LLM research project: fine-tuned on API/CLI documentation for accuracy over general LLMs.
- Gorilla LLM key finding: fine-tuning on API docs reduces hallucinated function signatures significantly.
- Use case: shell commands you use rarely enough to forget syntax — `ffmpeg`, `find`, `tar`, `curl` with complex flags.
- Competes with GitHub Copilot CLI, Warp AI, and other terminal AI tools.
- Open-source — runs locally without sending commands to a cloud service.

[Original](https://github.com/gorilla-llm/gorilla-cli)
 → REST API, GitHub
