---
title: Modeling Vocabulary for Big Code Machine Learning
date: 2022-05-12
categories:
  - machine-learning
  - nlp
  - software-engineering
  - source-code
  - language-models
description: An empirical study of vocabulary modeling decisions for machine learning systems on source code, evaluated across 14,436 projects. It matters because the choices made when tokenizing and preprocessing code vocabularies have an outsized impact on neural language model accuracy, yet were poorly documented before this work.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/1904.01873v1.pdf
---

## Summary

Hlib Babii, Andrea Janes, and Romain Robbes tackle a largely overlooked problem in machine learning on source code: before training a neural language model on code, practitioners must make a series of vocabulary modeling decisions — how to split identifiers, whether to lowercase tokens, how to handle out-of-vocabulary terms — and these choices are rarely justified or even documented in published work. The paper provides the first systematic empirical treatment of these decisions.

Working with a corpus of 14,436 Java projects, the authors trained models on 10,106 of them while holding out the rest for evaluation. They measured the impact of each vocabulary decision on model quality using cross-entropy as the primary metric. Their key finding is that a small subset of decisions has decisive characteristics — choices that reliably produce well-trained models quickly — while the majority of decisions have smaller effects. This gives practitioners an actionable shortlist of what to get right first.

The broader significance is methodological: ML for software engineering had been accumulating a body of work without a shared vocabulary (no pun intended) around data preparation. This paper provides that foundation. It sits alongside work on code embeddings and code2vec as part of the infrastructure for treating code as a learnable artifact, and directly informs subsequent large language models for code like Codex and [StarCoder](/notes/starcoder/) that benefit from principled tokenization strategies.

## Key points

- Vocabulary modeling decisions (tokenization, casing, splitting) are frequently undocumented in big code ML literature — this paper catalogs and empirically ranks them.
- Large-scale study across 14,436 open-source Java projects; training set of 10,106 projects provides statistically robust comparisons.
- A small subset of decisions is decisive for neural language model accuracy; the rest matter less — focus effort on the high-impact choices.
- Identifier splitting (separating camelCase/snake_case into subtokens) is among the most impactful preprocessing choices for source code models.
- Results generalize guidance for training any model on source code, from code completion to bug detection to program synthesis.

[Original paper](file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/1904.01873v1.pdf)
