---
title: "PEER: A Collaborative Language Model"
date: 2022-08-26
categories:
  - nlp
  - language-models
  - collaborative-writing
  - research
  - meta-ai
description: PEER is a language model trained to collaboratively write text with humans — drafting, suggesting edits, following instructions, and explaining its changes. An early formalization of human-AI collaborative writing that anticipates modern writing assistant workflows.
params:
  source: pinboard
  sourceUrl: https://arxiv.org/abs/2208.11663
---

![PEER: A Collaborative Language Model](/images/notes/peer-collaborative-language-model.png)

## Summary

PEER (Plan, Edit, Explain, Repeat) is a language model from Meta AI (Timo Schick et al.) trained to incrementally write text and collaborate with humans in a structured way. Unlike standard language models that generate text in one pass, PEER was trained on a four-step cycle: Plan (outline what to write), Edit (modify existing text), Explain (describe what was changed and why), Repeat (iterate). This made the model legible — it could articulate its edits rather than just producing them.

The training data came from Wikipedia edit histories, which provide a natural record of incremental collaborative writing: initial drafts, subsequent edits, and edit summaries that explain the changes. This gave PEER a corpus of human-human collaborative writing to learn from, with explicit edit traces. The model could then generalize: given a draft and an instruction, produce an edited version with an explanation of what changed and why.

PEER is an early example of the "chain of thought" and "tool use" patterns before they were formalized — the model reasons about its edits rather than just making them. The work anticipates collaborative writing tools like Notion AI, Cursor, and modern code review assistants that don't just produce output but explain their reasoning. The explicit plan-edit-explain loop also foreshadows AI agent architectures that use scratchpads and reasoning traces before acting.

## Key points

- PEER models collaborative writing as Plan → Edit → Explain → Repeat cycles, producing legible edits.
- Trained on Wikipedia edit histories — natural corpus of incremental, explained collaborative revision.
- Can draft, add suggestions, follow instructions, perform edits, self-correct, and explain reasoning.
- Early instance of reasoning-before-acting pattern that later formalized as chain of thought and scratchpad prompting.
- From Meta AI (Timo Schick); published August 2022.
- Anticipates modern writing assistants (Notion AI, Cursor) and AI agent architectures that explain their actions.

[Original](https://arxiv.org/abs/2208.11663)
