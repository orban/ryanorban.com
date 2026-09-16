---
title: Building a Virtual Machine Inside ChatGPT
date: 2022-12-04
categories:
  - chatgpt
  - creative-prompting
  - emergent-behavior
  - experiments
  - roleplay
description: Jonas Degrave's experiment prompting ChatGPT to roleplay as a Linux virtual machine — executing shell commands, maintaining state, and producing plausible output. One of the most striking early demonstrations of ChatGPT's emergent simulation capabilities.
params:
  source: pinboard
  sourceUrl: https://www.engraved.blog/building-a-virtual-machine-inside/
---

## Summary

Jonas Degrave's viral December 2022 blog post demonstrates prompting ChatGPT to roleplay as a Linux virtual machine, executing shell commands and producing plausible output. The setup is a system prompt establishing ChatGPT as a terminal, then a conversation where commands like `ls`, `pwd`, `cat`, `python3`, and `gcc` are "executed" and ChatGPT responds with realistic-looking terminal output. The machine maintains state across the conversation — creating files, editing them, and retrieving them later.

The result is striking because ChatGPT doesn't actually execute code. It simulates the outputs from training on massive amounts of terminal session data and code. `python3 -c "print(2+2)"` returns `4`; a simple C program compiles and runs. The simulation breaks for complex computations (it hallucinates outputs) but the illusion holds for typical interactive terminal use. The experiment revealed something important about what LLMs have implicitly learned: the statistical patterns of shell interactions are embedded in the weights.

This experiment became one of the most-cited early demonstrations of emergent behavior in ChatGPT. It contributed to the discourse around what capabilities language models have "really" acquired versus memorized versus can hallucinate plausibly. The deeper lesson: LLMs can simulate any system for which they've seen enough interaction transcripts — the simulation quality depends on how much training data exists for that system's pattern of input→output. The same principle applies to code interpretation, math computation, and other pseudo-tool uses that later became actual tool use in function calling.

## Key points

- ChatGPT prompted as a Linux VM: executes shell commands, maintains file state, produces plausible output.
- No actual code execution — pure statistical simulation from training on terminal session data.
- Simulation is convincing for typical commands; breaks on computationally intensive or novel operations.
- Reveals that LLMs have implicitly learned input→output patterns for any heavily documented system.
- One of the first major demonstrations of emergent behavior that went viral post-ChatGPT launch.
- Conceptual precursor to actual tool use via function calling — shows why simulated tool use is unreliable.

[Original](https://www.engraved.blog/building-a-virtual-machine-inside/)
