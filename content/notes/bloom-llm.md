---
title: "BLOOM: Open Multilingual Large Language Model"
date: 2022-07-17
categories:
  - llm
  - open-source
  - multilingual
  - bigscience
  - hugging-face
description: BLOOM is the first open, multilingual large language model trained transparently by a global coalition of AI researchers — 176B parameters, 46 languages, trained on the Jean Zay supercomputer in France. A direct counterpoint to GPT-3's closed access.
params:
  source: pinboard
  sourceUrl: https://bigscience.huggingface.co/blog/bloom
---

![BLOOM: Open Multilingual Large Language Model](/images/notes/bloom-llm.png)

## Summary

BLOOM (BigScience Large Open-science Open-access Multilingual Language Model) is the first major large language model trained in complete transparency by a global coalition of AI researchers under the BigScience project, organized by Hugging Face. The model has 176 billion parameters — comparable to GPT-3 — and was trained for 11 weeks on the Jean Zay supercomputer in France, one of Europe's largest publicly-funded computing clusters.

The scope is deliberately multilingual: BLOOM can generate text in 46 natural languages and dialects plus 13 programming languages. This was a direct response to the English-centricity of most large models. The training corpus was curated to be consistent with the team's values around language diversity and responsible AI, and came with a Responsible AI License (RAIL) and Ethical Charter — an attempt to govern downstream use contractually rather than just through API terms of service.

The BigScience project involved over 1,000 researchers from 60+ countries, coordinating asynchronously to make decisions about training data, architecture, and release. The governance model is as notable as the technical model: this was science-as-collective-process rather than a lab releasing a product. By releasing the weights openly, BLOOM enabled any researcher to inspect, fine-tune, or study the model — a sharp contrast to GPT-3, which was only accessible via OpenAI's API.

## Key points

- 176B parameter model — competitive with GPT-3 in scale, open in weights
- Trained 11 weeks on Jean Zay supercomputer; compute provided by French national research infrastructure
- 46 natural languages + 13 programming languages — strongest multilingual LLM at its launch
- Released under Responsible AI License (RAIL) — restricts harmful downstream use
- BigScience coalition: 1,000+ researchers, 60+ countries, organized by Hugging Face
- Key significance: proved that open, democratic AI training at frontier scale was possible

[Original](https://bigscience.huggingface.co/blog/bloom)
