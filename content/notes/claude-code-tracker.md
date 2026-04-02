---
title: "Claude Code Performance Tracker: daily SWE-Bench monitoring"
date: 2026-01-29
categories:
  - claude-code
  - benchmarks
  - swe-bench
  - monitoring
  - developer-tools
description: MarginLab's Claude Code Performance Tracker monitors daily SWE-Bench-Pro scores with statistical significance testing to detect degradation. Answers whether Claude Code's coding performance is consistent over time.
params:
  source: pinboard
  sourceUrl: https://marginlab.ai/trackers/claude-code/
---

![Claude Code Performance Tracker: daily SWE-Bench monitoring](/images/notes/claude-code-tracker.png)

## Summary

MarginLab's Claude Code Performance Tracker monitors Claude Code's daily performance on SWE-Bench-Pro — a harder variant of the standard SWE-Bench coding benchmark. The tool applies statistical significance testing to distinguish real performance changes from noise, addressing the concern that LLM performance can degrade silently between model updates.

SWE-Bench and its variants have become the de facto benchmark for AI coding agent capability: the task is resolving real GitHub issues from open-source projects, graded by whether the test suite passes. SWE-Bench-Pro is harder, with issues requiring more complex multi-file changes. Daily tracking catches the regressions that wouldn't show up in point-in-time evaluations.

The tracker matters for teams that rely on Claude Code for production work. If performance degrades significantly (which can happen when Anthropic updates underlying models or routing), knowing about it quickly allows teams to adjust their workflows or escalate. Statistical significance testing prevents false alarms from daily variance.

## Key points

- Tracks Claude Code's daily SWE-Bench-Pro scores — harder than standard SWE-Bench.
- Statistical significance testing distinguishes real degradation from day-to-day variance.
- Addresses the silent degradation risk when underlying Anthropic models are updated.
- Useful for teams with Claude Code dependencies who need performance SLO visibility.
- From MarginLab, focused on AI coding agent reliability monitoring.

[Original](https://marginlab.ai/trackers/claude-code/)
