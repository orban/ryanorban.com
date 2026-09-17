---
title: The Bitter Lesson
date: 2022-03-10
categories:
  - machine-learning
  - research
  - ai-history
  - scaling
  - philosophy
description: Rich Sutton's 2019 essay arguing that the dominant lesson from 70 years of AI research is that general methods leveraging computation always win over human-engineered knowledge — a humbling argument against clever domain-specific tricks. One of the most cited and debated essays in ML.
params:
  source: pinboard
  sourceUrl: http://www.incompleteideas.net/IncIdeas/BitterLesson.html
---

## Summary

Rich Sutton's short 2019 essay, published on his personal site, makes a pointed argument about what the history of artificial intelligence actually teaches us. The [bitter lesson](/notes/bitter-lesson/) is this: every time AI researchers have tried to build knowledge and structure into systems — clever representations, hand-crafted features, domain-specific architectures — they have eventually been beaten by general methods that instead leverage more computation.

Sutton traces this through major AI milestones: chess engines won not by encoding chess knowledge but by search; speech recognition improved through scaling data and models, not through linguistic representations; computer vision broke open with deep learning and scale, not through hand-crafted feature extractors; Go was conquered by Monte Carlo tree search and learned value functions, not by Go-specific heuristics. Each time, the lesson was that researchers who built general methods that scale won, while those who built in human knowledge had temporary wins that eventually reversed.

The essay is deliberately provocative. It implies that most of what AI researchers actually do — crafting architectures, designing objective functions, encoding domain knowledge — is fighting the wrong battle. The two general methods that scale are search and learning, and research energy should flow toward making those better rather than making systems smarter through human cleverness.

The "bitter" in "bitter lesson" is directed at researchers: it is bitter because it tells us our specialized knowledge is mostly counterproductive in the long run, and that raw computation plus simple methods eventually wins. This sits in direct tension with the intuition that understanding the domain should help. It is a key intellectual backdrop to the success of large language models and the scaling hypothesis.

## Key points

- General methods + computation beat domain-specific knowledge, repeatedly, across all major AI domains.
- The two scalable primitives are search and learning — both became enormously more powerful as compute grew.
- chess, speech recognition, computer vision, Go: each domain had the same arc — specialized knowledge temporarily ahead, then beaten by scale.
- The lesson is bitter because it humbles researchers: clever domain-specific tricks are usually a dead end.
- Directly relevant to the success of large language models — pretrained transformers trained on raw data beat task-specific systems at nearly everything.
- Counterpoint: systems thinking argues some inductive biases are genuinely useful — the debate is about which ones.

[Original](http://www.incompleteideas.net/IncIdeas/BitterLesson.html)
