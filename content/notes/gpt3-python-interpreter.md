---
title: GPT-3 + Python Interpreter (gpt.py)
date: 2022-09-13
categories:
  - gpt-3
  - llm
  - python
  - tool-use
  - replit
description: A 2022 Replit demo by Sergey Karayev showing GPT-3 armed with a Python interpreter — doing exact arithmetic, making API requests, and answering questions that pure text generation gets wrong. An early, concrete preview of what LLM tool use would look like.
params:
  source: pinboard
  sourceUrl: https://replit.com/@SergeyKarayev/gptpy
---

## Summary

This Replit demo by Sergey Karayev (with credit to Riley Goodside and Amjad Masad for the idea) demonstrated GPT-3 augmented with a live Python interpreter in September 2022. The setup: when GPT-3 generates Python code, it gets executed immediately, and the output is fed back into the context. This lets the model do things it can't do with pure text generation — exact arithmetic, API calls, file manipulation.

The significance at the time: GPT-3 was well-known to fail at basic math and to confabulate facts. Tool augmentation directly addressed both. By offloading computation to an interpreter, the model gets provably correct results for anything that can be computed. This was one of the clearest early demonstrations of what would become the core pattern behind ChatGPT plugins, Claude tool use, and modern AI agent architectures.

The demo predated ReAct, [Toolformer](/notes/toolformer/), and function calling as formalized concepts, but captured the same intuition: language models are good at planning and reasoning in natural language, while tools handle the things models get wrong. The combination is substantially more capable than either alone. Andrej Karpathy's later framing — LLMs as the reasoning engine with tools as the action layer — echoes what this demo showed informally.

## Key points

- GPT-3 + Python interpreter: model generates code, code runs, output feeds back into context.
- Enables exact arithmetic and live API calls — things GPT-3 alone gets wrong.
- Early (Sept 2022) demonstration of the tool use / function calling pattern that became standard.
- Built on Replit, making it immediately runnable by anyone with the link.
- Conceptually precedes ReAct, [Toolformer](/notes/toolformer/), and OpenAI function calling as formalized techniques.
- Direct ancestor of ChatGPT Code Interpreter and modern AI agent tool use.

[Original](https://replit.com/@SergeyKarayev/gptpy)
