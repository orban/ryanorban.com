---
title: "PEER: A Collaborative Language Model"
date: 2022-08-26
categories:
  - collaborative-writing
  - language-models
  - editing
  - meta-ai
description: PEER is a language model trained to simulate the full collaborative writing workflow — drafting, suggesting edits, explaining changes, and integrating feedback — by learning from Wikipedia edit histories. It achieves strong performance on editing and revision tasks without task-specific training.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/2208.11663.pdf
---

## Summary

PEER (Plan, Edit, Explain, Repeat) is a language model from Meta AI trained to model the entire iterative writing process rather than just produce text. It learns four interconnected skills: drafting content, proposing edits, explaining the rationale behind changes, and integrating feedback into revised drafts. The training signal comes from Wikipedia edit histories — a large, naturally occurring dataset of real human collaborative writing with traceable revision chains.

The design philosophy behind PEER is that writing is inherently iterative and collaborative, but most language models are trained to produce single outputs from single prompts. By modeling the full revision loop, PEER captures the reasoning behind changes — not just what was changed, but why. This makes it more useful as a genuine writing collaborator rather than a one-shot text generator.

PEER achieves strong performance on editing, revision, and critique tasks without fine-tuning on task-specific datasets. This is notable because it suggests that learning from the structure of Wikipedia edits transfers broadly to writing assistance tasks. The approach points toward a paradigm where collaborative writing assistants are trained on naturally occurring collaborative data rather than purpose-built instruction datasets.

## Key points

- PEER models four skills: plan, edit, explain changes, and repeat — simulating the full collaborative writing loop
- Trained on Wikipedia edit histories as naturally occurring collaborative writing data
- Explains the rationale behind edits, not just what changed — enabling more transparent writing assistance
- Strong performance on editing and revision benchmarks without task-specific fine-tuning
- From Meta AI; points toward training language models on naturally iterative human processes

[Original](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/2208.11663.pdf)
