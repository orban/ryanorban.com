---
title: Beware of Unreliable Data in Model Evaluation
date: 2023-06-29
categories:
  - llm
  - evaluation
  - data-quality
  - prompt-engineering
  - ml-ops
description: Cleanlab's case study showing that noisy test data leads to suboptimal prompt selection for LLMs — you can choose the wrong prompt because your evaluation data contains labeling errors. A practical warning about data quality in LLM evaluation pipelines.
params:
  source: pinboard
  sourceUrl: https://cleanlab.ai/blog/prompt-selection/
---

![Beware of Unreliable Data in Model Evaluation](/images/notes/cleanlab-unreliable-data-llm-evaluation.png)

## Summary

Cleanlab published this case study using their own Flan-T5 prompt engineering work to demonstrate a subtle but important point: evaluation data that contains labeling errors causes you to select worse prompts than you'd choose with clean data. The finding is counterintuitive — you might think label noise in test data just adds variance, but it can systematically bias selection toward prompts that happen to do well on the noisy labels.

The concrete example: you're comparing five prompt templates for a classification task. You evaluate each on your test set and pick the one with highest accuracy. But if 10% of test labels are wrong, you'll often pick a prompt that correctly handles noisy labels rather than the prompt that best handles clean, correct labels. The winning prompt may have learned to predict the noisy pattern rather than the true pattern. This is a form of overfitting to noise in the evaluation set.

Cleanlab's solution is confident learning — a technique for identifying likely mislabeled examples in training and test sets by looking at agreement between model confidence scores and labels. By cleaning the test set before running prompt evaluation, you get more reliable comparisons between prompts. This is broadly applicable: any LLM evaluation workflow that uses human-annotated test data is susceptible to this problem. The post is a practical warning for anyone running prompt selection experiments or fine-tuning comparisons.

## Key points

- Label noise in evaluation data systematically biases prompt engineering selection — not just adds noise.
- Prompts that "win" on noisy test sets may be learning the noise pattern, not the true task.
- Cleanlab's confident learning detects mislabeled test examples via model confidence vs label disagreement.
- Clean your test set before evaluating — noisy test data is at least as problematic as noisy training data.
- Applies broadly: any LLM evaluation with human-annotated data is at risk.
- Flan-T5 case study: prompt selection outcome changed after test set cleaning.

[Original](https://cleanlab.ai/blog/prompt-selection/)
