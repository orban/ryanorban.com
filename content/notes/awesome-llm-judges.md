---
title: "Awesome LLM Judges: curated research on LLM evaluation systems"
date: 2025-02-10
categories:
  - llm
  - evaluation
  - llm-as-judge
  - research
  - resources
description: Curated collection of research on LLM-as-a-judge evaluation systems — covering ensemble methods, fine-tuned judge models, hallucination detection, generative reward models, and safety moderation. Maintained by Haize Labs alongside their Verdict library.
params:
  source: pinboard
  sourceUrl: https://github.com/haizelabs/Awesome-LLM-Judges
---

![Awesome LLM Judges: curated research on LLM evaluation systems](/images/notes/awesome-llm-judges.png)

## Summary

[Awesome LLM Judges](/notes/awesome-llm-judges/) is a curated GitHub repository from Haize Labs collecting research on using LLMs as automated evaluators. It maps the field from foundational approaches through specialized techniques, covering both the promise and the problems.

The collection is organized into substantive categories: starter papers on foundational LLM-as-a-judge approaches, ensemble methods including debate-based evaluation, fine-tuned judge models like Prometheus and JudgeLM specialized for evaluation tasks, hallucination detection tools, generative reward models that produce critique alongside scores, and safety applications for content moderation and oversight.

The dual focus is notable: it covers both building better evaluation systems and assessing the quality of those systems (bias, inconsistency, evaluator failure modes). Resources like JudgeBench address the meta-problem: once you're using LLMs to evaluate LLMs, how do you evaluate the evaluator? The repository connects directly to Verdict, Haize Labs' practical library for scaling judge-time compute.

## Key points

- Categories: starter papers, ensemble/debate methods, fine-tuned judges, hallucination detection, generative reward models, safety/oversight.
- Notable resources: Prometheus 2, JudgeLM, JudgeBench for evaluating evaluators.
- Addresses both building evaluation systems and their failure modes (bias, inconsistency).
- Maintained by Haize Labs alongside their Verdict library.
- Covers the meta-problem: who evaluates the LLM-as-a-judge?

[Original](https://github.com/haizelabs/Awesome-LLM-Judges)
