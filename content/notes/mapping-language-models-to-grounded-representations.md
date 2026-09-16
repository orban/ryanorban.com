---
title: Mapping Language Models to Grounded Representations
date: 2022-11-02
categories:
  - nlp
  - language-models
  - grounding
  - semantics
description: An NLP paper from late 2022 on mapping language model representations to grounded meaning — likely examining whether and how LLM internal representations correspond to real-world referents or structured semantic formalisms. Addresses the 'grounding problem' at the heart of debates about whether LLMs understand language.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/mapping_language_models_to_gro.pdf
---

## Summary

This paper, saved in November 2022, addresses the symbol grounding problem as it applies to large language models. The core question: do the representations learned by LLMs through text-only training correspond to anything in the world, or are they purely distributional patterns without genuine semantic grounding? This was an active research thread in 2022 as GPT-3 and ChatGPT demonstrated surprising capabilities, sparking debate about what understanding means for language models.

The grounding problem is longstanding in linguistics and cognitive science. Distributional semantics models (word2vec, GloVe, and their neural descendants) learn word meaning from co-occurrence statistics, but philosophers and linguists like Luc Steels and Stevan Harnad have argued this gives symbols meaning only relative to other symbols — not to perceptual or physical reality. Multimodal models (CLIP, DALL-E, GPT-4V) partially address this by training on image-text pairs, but the question of whether even those models have grounded representations remains contested.

Work in this space from 2022 explored techniques for evaluating whether model representations align with formal semantic representations (like Abstract Meaning Representation), logical forms, or perceptual features. Papers by Patel & Pavlick and related work examined whether probing classifiers could extract structured meaning from LLM hidden states, finding partial success — models encode some semantic structure but with consistent gaps around negation, quantifiers, and physical world reasoning. This connects to Jacob Andreas's concurrent work on language models as agent models and the broader debate about whether next-token prediction is sufficient for meaning.

## Key points

- Addresses the symbol grounding problem for LLMs: do text-only models learn semantically grounded representations?
- 2022 framing predates multimodal training being standard — focuses on pure language model representations
- Probing approaches can extract structured semantic properties from LLM hidden states, but coverage is incomplete
- Distributional semantics gives models relational meaning; grounding requires connection to perceptual reality or formal semantics
- Connected to debates about LLM understanding vs. stochastic parrots — do the representations correspond to the world?
- Pairs with [Language Models as Agent Models](/notes/language-models-as-agent-models/) (Jacob Andreas) on what LLMs implicitly learn from text

[Source PDF](file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/mapping_language_models_to_gro.pdf)
 → AI agent
