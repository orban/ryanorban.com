---
title: "Generate Rather Than Retrieve: Large Language Models Are Strong Context Generators"
date: 2023-02-22
categories:
  - llm
  - rag
  - retrieval
  - knowledge-intensive-nlp
  - research
description: Yu et al. (2022) show that prompting an LLM to generate its own background context before answering a question (GenRead) outperforms retrieval-based approaches on several knowledge-intensive NLP benchmarks. The result challenges the assumption that retrieval is necessary for grounding LLM outputs.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/GENERATE RATHER THAN RETRIEVE- LARGE LANGUAGE MODELS ARE STRONG CONTEXT GENERATORS.pdf
---

## Summary

Wenhao Yu, Dan Iter, Shuohang Wang, Yichong Xu, Mingxuan Ju, Soho Guo, Taoxin Hu, Ruohong Zhang, Shuai Lu, Ning Qian, and Pengcheng He from Microsoft Research propose GenRead — a counterintuitive alternative to retrieval-augmented generation that uses the LLM itself to generate the background context a question requires, rather than retrieving it from an external corpus.

The standard assumption in knowledge-intensive NLP is that a retrieval step (like DPR in RAG) is necessary to provide the model with accurate, up-to-date factual grounding. GenRead challenges this: given a question, prompt the model to generate a few-sentence contextual document about the topic first, then answer using that generated context. The generated context is often more semantically relevant to the specific question than the top-k retrieved passages, because the model generates exactly what it needs rather than hoping the retrieval system surfaces the right document.

On three question-answering benchmarks — Natural Questions, TriviaQA, and WebQuestions — GenRead outperforms the RAG baseline and matches or beats DPR-based fusion-in-decoder models. The results are surprising because the generated context is not drawn from any external knowledge store and cannot be verified for accuracy, yet it's more useful for answer generation than retrieved Wikipedia passages. The authors hypothesize this is because retrieval optimizes for term overlap while generation optimizes for relevance to the question's underlying information need.

This paper sits in productive tension with the dominant RAG paradigm: it's not arguing retrieval is useless, but that LLMs have more internalized knowledge than RAG-centric pipelines credit. The result influenced later work on self-RAG, chain-of-thought prompting, and the use of scratchpads for reasoning.

## Key points

- GenRead: prompt an LLM to generate a contextual document for a question before answering — no retrieval step, no external index.
- Generated context outperforms retrieved Wikipedia passages on Natural Questions, TriviaQA, and WebQuestions.
- Generated context is more semantically relevant than retrieval because it's tailored to the question's information need, not term overlap.
- Challenges the RAG assumption: LLMs already contain rich knowledge that retrieval can fail to unlock.
- Results apply to GPT-3 (175B parameters); smaller models show less benefit since they have less internalized knowledge.
- Influenced self-RAG, iterative refinement, and prompting methods that use the model's own outputs as intermediate reasoning.

[Original PDF](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/GENERATE%20RATHER%20THAN%20RETRIEVE-%20LARGE%20LANGUAGE%20MODELS%20ARE%20STRONG%20CONTEXT%20GENERATORS.pdf)
