---
title: Ranking YC Companies with a Neural Net
date: 2022-04-05
categories:
  - machine-learning
  - startups
  - y-combinator
  - nlp
  - data-science
description: Eric Jang trains a neural net to rank Y Combinator companies by prestige/success using only their names and descriptions — an experiment in whether language models encode meaningful startup quality signals. The results are surprisingly coherent.
params:
  source: pinboard
  sourceUrl: https://evjang.com/2022/04/02/yc-rank.html
---

## Summary

Eric Jang (ML researcher, former Google Brain/Robotics) built a system to rank Y Combinator companies using a neural network trained on nothing but company names and descriptions. The experiment is a probe: do language model embeddings encode meaningful signals about startup success, or is "quality" undetectable from text alone? The results are surprisingly coherent — the rankings correlate with the companies most practitioners would intuitively recognize as successful, suggesting that text about companies carries real quality signal.

The methodology uses sentence embeddings from a pretrained language model to represent each company, then trains a simple ranking model using human-annotated pairwise preferences (which of these two companies is more successful/prestigious?). This is a pairwise ranking approach — the model learns a preference function, not absolute scores. The annotation comes from practitioners who can assess company quality from context. Once trained, the model ranks the full set of YC companies without needing further human input.

What's interesting isn't the application (ranking startup companies) but the meta-observation: the quality signals that make a company recognizably successful are partly encoded in how it's described. Company descriptions that are specific, technically credible, and solve concrete problems rank higher than vague, buzzword-heavy ones. Eric Jang notes that this mirrors how humans actually evaluate startups in screening — descriptions matter beyond just information delivery, they're proxies for founder quality and market understanding. This connects to the broader question of what language model representations actually encode.

## Key points

- Language model embeddings encode quality signals about companies — success is partially visible in text descriptions.
- Pairwise ranking approach: train on human-annotated preferences (A vs. B), then generalize to full ranking.
- Results correlate with practitioner intuitions about YC company success — the model learns a coherent quality function.
- By Eric Jang (robotics/ML researcher); a personal project demonstrating LM representation capabilities.
- Connects to RLHF (Reinforcement Learning from Human Feedback) — similar pairwise preference learning mechanism.
- Meta-point: good startup descriptions are proxies for founder quality, just as good code is a proxy for engineering quality.

[Original](https://evjang.com/2022/04/02/yc-rank.html)
