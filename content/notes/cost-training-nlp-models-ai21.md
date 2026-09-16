---
title: "The Cost of Training NLP Models: A Concise Overview"
date: 2022-08-26
categories:
  - nlp
  - training-costs
  - scaling
  - machine-learning
  - economics
description: AI21 Labs' 2020 overview of the financial and compute cost of training large NLP models, tracing the exponential growth in training expenditure from BERT through GPT-3. An early quantitative lens on the economics of scale in language model development.
params:
  source: papers
  sourceUrl: https://arxiv.org/abs/2004.08900
---

## Summary

A short but influential overview paper from AI21 Labs (Or Sharir, Barak Peleg, Yoav Shoham, 2020) that quantifies the financial cost of training large NLP models. Written when GPT-3 was the newest frontier model, it documents the exponential growth in compute expenditure from early neural language models through BERT and into the era of hundred-billion-parameter models.

The core finding is that training costs have grown at a pace dramatically faster than Moore's Law. BERT-Large cost roughly $7,000 to train in 2018; GPT-3 cost an estimated $4–12 million in cloud compute in 2020. The paper breaks costs into hardware (GPU/TPU type and count), duration, and cloud rental rates, making the analysis reproducible and auditable. It also discusses the carbon footprint of training large models, situating compute costs within an environmental impact frame — anticipating the AI sustainability debates that intensified after Emma Strubell's energy cost analysis.

The paper is historically important as one of the first attempts to make model training costs legible and comparable. It provided the quantitative anchor for subsequent debates about who can afford to do frontier AI research, the concentration of AI capability in well-resourced organizations, and the tension between scientific openness and the cost barrier to reproduction. Read alongside the neural scaling laws work from Kaplan et al. and Hoffmann et al., it shows why compute efficiency (not just raw scale) became a central research priority.

## Key points

- BERT-Large ~$7K to train in 2018; GPT-3 ~$4–12M in 2020 — costs roughly doubled every 6 months during this period
- Cost breakdown is hardware × duration × cloud rate; the paper makes these inputs explicit for reproducibility
- Carbon footprint of NLP training is quantified alongside dollar cost — early entry in the AI sustainability discourse
- Key structural observation: only a handful of institutions can afford frontier model training, concentrating AI capability geographically and organizationally
- Context for neural scaling laws: understanding *why* compute efficiency research matters requires knowing how much scale costs

[Original paper](https://arxiv.org/abs/2004.08900)
