---
title: GPT-3 Long Instruction Following (Riley Goodside)
date: 2022-08-12
categories:
  - gpt-3
  - prompt-engineering
  - llm
  - demonstrations
  - riley-goodside
description: Riley Goodside demonstrates GPT-3 following a nearly 2,000-character instruction prompt precisely. An early illustration that LLMs can be reliable instruction followers with detailed context, countering the intuition that prompts should be kept short.
params:
  source: pinboard
  sourceUrl: https://twitter.com/goodside/status/1557524546412052482/photo/1
---

![GPT-3 Long Instruction Following (Riley Goodside)](/images/notes/gpt3-long-instructions.png)

## Summary

This post by Riley Goodside demonstrates GPT-3's ability to follow extremely long, complex instructions — a nearly 2,000 character prompt where every word is followed. In 2022, this was a striking demonstration because the common perception was that GPT-3 struggled with long contexts and nuanced instructions. Showing it faithfully execute multi-sentence, multi-constraint prompts was empirically meaningful.

Riley Goodside was one of the most influential early prompt engineering practitioners, working at Scale AI and sharing practical techniques publicly. His Twitter posts were a primary venue for the emerging discipline of prompt engineering as applied art — concrete demonstrations of what was and wasn't possible with large language models.

This demonstration belongs to a genre of "GPT-3 capabilities" posts common in 2022: sharing surprising behaviors that helped the community calibrate what these models could actually do. It directly informs prompt engineering practice: if GPT-3 can faithfully follow a 2,000 character instruction, then precise, detailed prompts are worth writing. This countered the intuition that prompts needed to be short and simple.

## Key points

- GPT-3 follows a ~2,000 character instruction prompt faithfully — every specified constraint honored.
- By Riley Goodside (Scale AI), a key early prompt engineering practitioner.
- Countered the keep prompts short intuition — detailed, long prompts were viable and effective.
- Part of a 2022 genre of capability demonstrations that calibrated community understanding of LLM behavior.
- Connects to chain-of-thought prompting research: giving models more specification improves behavior.
- Directly practical: if the model follows long instructions, write long instructions.

[Original](https://twitter.com/goodside/status/1557524546412052482/photo/1)
