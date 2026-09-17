---
title: LLMs Confabulate, Not Hallucinate
date: 2023-10-06
categories:
  - llm
  - hallucination
  - terminology
  - cognitive-science
  - ai-safety
description: A terminological argument that LLMs "confabulate" rather than "hallucinate" — the distinction matters because confabulation (confidently filling gaps with plausible-sounding fabrication) implies a specific mechanism, while hallucination implies randomness. Getting the mechanism right leads to better mitigations.
params:
  source: pinboard
  sourceUrl: https://www.beren.io/2023-03-19-LLMs-confabulate-not-hallucinate/
---

![LLMs Confabulate, Not Hallucinate](/images/notes/llms-confabulate-not-hallucinate.png)

## Summary

Beren Millidge argues in this post that the common term "hallucination" mischaracterizes what LLMs do when they generate false information, and that "confabulation" is the technically correct term. The distinction isn't just terminological — it points to different underlying mechanisms and different mitigation strategies.

Hallucination in the neurological/psychological sense refers to perception without external stimulus — seeing or hearing things that aren't there. It implies randomness or noise. Confabulation, by contrast, is a well-documented neurological phenomenon where the brain generates confident, plausible-sounding explanations to fill gaps in knowledge or memory, without being aware it's doing so. Brain-damaged patients with certain types of amnesia will confidently describe events they have no memory of — not because they're lying, but because the confabulatory mechanism fills gaps automatically.

LLMs do the same thing: when asked about something outside their training distribution or knowledge, they generate text that is locally coherent and plausible-sounding but factually wrong. The mechanism isn't random noise — it's systematic gap-filling using learned patterns. This matters for mitigations: if it were hallucination (noise), you'd focus on reducing randomness. Since it's confabulation (systematic plausible gap-filling), you focus on grounding (RAG, citations) and uncertainty calibration (teaching models to say I don't know rather than filling the gap).

## Key points

- "Hallucination" implies randomness; "confabulation" implies systematic plausible gap-filling — LLMs do the latter.
- Confabulation is a documented neurological phenomenon: confident fabrication to fill knowledge gaps.
- The mechanism matters for mitigation: confabulation → grounding and uncertainty calibration, not noise reduction.
- RAG addresses confabulation by providing grounding context; the model fills gaps from retrieved facts instead.
- Getting terminology right guides better research and product design choices.
- Written by Beren Millidge, a neuroscience/ML researcher with background in predictive coding.

[Original](https://www.beren.io/2023-03-19-LLMs-confabulate-not-hallucinate/)
