---
title: "TART: Task-Aware Retrieval with Instructions"
date: 2022-11-18
categories:
  - retrieval
  - nlp
  - information-retrieval
  - instruction-following
  - research
description: TART (Task-Aware Retrieval with Instructions) introduces BERRI, a dataset of ~40 retrieval tasks annotated with human-written task instructions, and trains a multi-task retrieval system that adapts its behavior based on explicit instructions. TART outperforms much larger models on BEIR by understanding the user's intent rather than just matching query-document similarity.
params:
  source: papers
  sourceUrl: https://arxiv.org/abs/2211.09260
---

## Summary

Standard dense retrieval systems like DPR learn a single similarity function: embed query, embed document, rank by dot product. This works when "retrieve documents relevant to this query" is the whole specification. But real information retrieval tasks are more varied: sometimes you want documents that contradict the query (for fact-checking), sometimes you want fine-grained passages rather than whole documents, sometimes you want diverse results rather than near-duplicates. Akari Asai, Patrick Lewis, and collaborators at UW and Meta AI address this by making the task specification explicit.

TART (Task-Aware Retrieval with Instructions) trains a retrieval model on BERRI — a dataset of approximately 40 heterogeneous retrieval tasks, each annotated with a human-written instruction describing what kind of retrieval is wanted. The instruction is encoded alongside the query and used to condition the retrieval. Rather than asking "what document is similar to this query?, TART asks given this instruction about what I need, what document serves this task?" A model that can parse the instruction can generalize to retrieval tasks it wasn't explicitly trained on.

TART achieves state-of-the-art results on BEIR (the heterogeneous retrieval benchmark) and LOTTE, outperforming models significantly larger than itself. The key insight: zero-shot retrieval generalization requires understanding the retrieval intent, not just the query-document similarity. This is analogous to how instruction-tuned LLMs outperform base models on unseen tasks — the instruction carries information about the evaluation criterion that a task-agnostic model lacks. TART is a natural precursor to instruction-following embedding models like E5-instruct and INSTRUCTOR.

## Key points

- BERRI dataset: ~40 retrieval tasks with human-written instructions — the first large-scale instruction-annotated retrieval training collection
- TART encodes the task instruction alongside the query to condition retrieval — allows different similarity functions for different needs
- Outperforms much larger models on BEIR benchmark: instruction-following > scale for zero-shot retrieval generalization
- Addresses retrieval tasks that don't fit standard relevance: fact-checking (retrieve contradictions), diversity-seeking, granularity variation
- Precursor to instruction-tuned embedding models: INSTRUCTOR, E5-instruct, BGE-M3 all extend this direction
- Connects instruction tuning in LLMs with the dense retrieval literature — both benefit from explicit task specification

[Original](https://arxiv.org/abs/2211.09260)
