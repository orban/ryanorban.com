---
title: ROOTS Search Tool — BigScience
date: 2022-10-29
categories:
  - machine-learning
  - datasets
  - nlp
  - open-source
  - hugging-face
  - language-models
description: A Hugging Face Space for searching ROOTS — the massive multilingual dataset used to train BLOOM, the BigScience open LLM. Lets researchers trace which training documents a model might have learned from.
params:
  source: pinboard
  sourceUrl: https://huggingface.co/spaces/bigscience-data/roots-search
---

## Summary

The ROOTS search tool is a Hugging Face Spaces app by the BigScience data team that lets users search through the ROOTS corpus — the massive multilingual dataset used to train BLOOM, the 176-billion parameter open-source language model developed by the BigScience research workshop. ROOTS contains ~1.6TB of text across 59 languages, assembled from web crawls, books, code repositories, and other sources.

The search tool serves two purposes. First, data transparency: researchers and affected parties can determine whether their content was included in BLOOM's training data, which has implications for copyright, consent, and data governance. Second, model analysis: understanding what training data a model saw is relevant to interpreting its behavior — tendencies, biases, and capabilities often trace back to specific data sources.

BigScience was an important experiment in open, collaborative AI research: ~1,000 researchers from 60+ countries coordinated on a shared goal of training a large open language model with explicit attention to ethical considerations, dataset documentation, and model cards. BLOOM was trained on the Jean Zay supercomputer in France, funded by French research institutions. The data documentation practices BigScience developed influenced later work on dataset curation transparency, including the Data Governance recommendations that preceded Responsible AI frameworks.

## Key points

- Search interface for ROOTS corpus — the training data behind BLOOM, the open LLM.
- Supports data transparency: find whether specific content was in the training set.
- ROOTS: ~1.6TB, 59 languages, from web crawl, books, code, and other sources.
- BigScience was a collaborative effort of ~1,000 researchers building an open LLM.
- BLOOM (176B parameters) trained on Jean Zay supercomputer with explicit ethics focus.
- Precursor to modern dataset documentation and data governance practices in ML.

[Original](https://huggingface.co/spaces/bigscience-data/roots-search)
