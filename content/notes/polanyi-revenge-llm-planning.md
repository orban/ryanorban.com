---
title: "Avenging Polanyi's Revenge: LLM Approximate Omniscience in Planning"
date: 2023-08-03
categories:
  - llm
  - planning
  - research
  - polanyi
  - tacit-knowledge
description: A talk titled 'Avenging Polanyi's Revenge' arguing that LLMs' approximate omniscience changes planning — they've absorbed tacit knowledge that previously required human experts, enabling a different category of automated planning than rule-based systems allowed.
params:
  source: pinboard
  sourceUrl: https://m.youtube.com/watch?v=BmyB-4S9QuY&feature=youtu.be
---

![Avenging Polanyi's Revenge: LLM Approximate Omniscience in Planning](/images/notes/polanyi-revenge-llm-planning.png)

## Summary

This talk (from a research presentation) invokes Michael Polanyi's concept of tacit knowledge — we know more than we can tell — and his critique that knowledge which can't be articulated can't be automated. Polanyi's Revenge is the observation that attempts to automate expert tasks (in the 1980s AI and expert systems era) failed because experts couldn't fully articulate their knowledge, so rule-based systems couldn't capture it.

The avenging claim: LLMs may have sidestepped this problem. By training on vast amounts of human-generated text, LLMs have absorbed tacit knowledge in compressed form without requiring experts to articulate it explicitly. A LLM that has read millions of pages of engineering documents, project reports, and technical discussions has absorbed contextual judgment that would be impossible to encode as rules.

The "approximate omniscience" framing describes LLMs' distinctive epistemic character: they have broad, shallow knowledge across almost everything, which makes them useful for planning (where knowing roughly how things work across many domains matters more than deep expertise in one). This is different from traditional planning systems, which required complete domain models.

The practical implication: LLM-based planners can handle open-world tasks that defeated classical planners precisely because classical planners couldn't handle what they hadn't been explicitly taught, while LLMs can reason by analogy to related situations they've encountered in training.

## Key points

- Polanyi's Revenge: 1980s expert systems failed because tacit knowledge couldn't be articulated into rules.
- LLMs may have sidestepped this by absorbing tacit knowledge from text without requiring explicit articulation.
- "Approximate omniscience": broad shallow knowledge across many domains enables cross-domain planning.
- Classical planners need complete domain models; LLM planners can reason by analogy from training.
- Raises a new version of the same question: what happens when LLM training data doesn't cover a domain?

[Original](https://m.youtube.com/watch?v=BmyB-4S9QuY&feature=youtu.be)
