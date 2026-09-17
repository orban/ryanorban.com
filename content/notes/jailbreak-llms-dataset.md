---
title: "jailbreak_llms: CCS'24 Jailbreak Prompt Dataset"
date: 2024-06-11
categories:
  - ai-safety
  - security
  - llm
  - jailbreak
  - dataset
  - research
description: A dataset of 15,140 ChatGPT prompts including 1,405 jailbreak prompts collected from Reddit, Discord, and open-source datasets — published at CCS 2024. The most comprehensive public collection of real-world jailbreak attempts against LLMs.
params:
  source: pinboard
  sourceUrl: https://github.com/verazuo/jailbreak_llms
---

![jailbreak_llms: CCS'24 Jailbreak Prompt Dataset](/images/notes/jailbreak-llms-dataset.png)

## Summary

This GitHub repository from verazuo provides a dataset of 15,140 ChatGPT prompts, including 1,405 jailbreak prompts collected from Reddit, Discord, websites, and open-source datasets. Published at CCS 2024 (ACM Conference on Computer and Communications Security), this is the most comprehensive public collection of real-world jailbreak attempts against large language models.

The jailbreak prompt collection is particularly valuable for safety research because it represents actual adversarial prompts that were shared and circulated in communities explicitly trying to bypass ChatGPT's safety measures — not synthetically generated test cases, but real attempts that real users found effective or promising. The taxonomy covers role-playing exploits (DAN and variants), hypothetical framing ("imagine you're an AI without restrictions"), privilege escalation, encoding tricks, and multi-turn escalation strategies.

For AI safety researchers and teams deploying LLM applications, this dataset serves several purposes: training safety classifiers to recognize jailbreak patterns, evaluating new models against known attack vectors, and understanding the distribution of techniques that adversarial users actually employ. It complements the automated tools (Garak, PyRIT, Promptfoo) with ground-truth data about what jailbreaks actually looked like in the wild up to the collection date.

## Key points

- 15,140 ChatGPT prompts; 1,405 confirmed jailbreak prompts.
- Sourced from Reddit, Discord, and existing open-source datasets — real-world adversarial traffic.
- Published at CCS 2024 — peer-reviewed academic context.
- Categories: role-playing (DAN), hypothetical framing, encoding tricks, privilege escalation, multi-turn.
- Useful for training safety classifiers and evaluating model vulnerability to known attacks.
- Complements automated red-teaming tools with ground-truth human-generated adversarial prompts.

[Original](https://github.com/verazuo/jailbreak_llms) → GitHub
