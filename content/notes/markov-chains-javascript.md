---
title: "Markov Chains: The Sad Case of Mr. Markov and What's His Face"
date: 2013-01-23
categories:
  - markov-chains
  - javascript
  - probabilistic-computing
  - text-generation
  - algorithms
description: A practical JavaScript tutorial on Markov chains for text generation — building a next-word predictor from a corpus. A good introductory implementation of a probabilistic sequence model that predates the LLM era by a decade.
params:
  source: pinboard
  sourceUrl: http://blog.javascriptroom.com/2013/01/21/markov-chains/
---

## Summary

This JavaScript tutorial on Markov chains demonstrates building a simple text generator by analyzing an existing corpus. A Markov chain is a probabilistic model where the probability of the next state depends only on the current state — in text generation, this means the probability of the next word depends only on the current word (or in higher-order chains, the last n words). The result is text that locally resembles the training corpus but lacks long-range coherence.

The implementation is straightforward: parse a text source into word pairs (or n-grams), build a lookup table mapping each word to a weighted list of words that follow it, then generate text by random walks through the table. The sad case framing refers to how the generated text can be superficially plausible at the sentence level but fall apart when read as a paragraph — a property that's both the limitation of the model and the source of the comedy in generated output.

Markov chain-based text generators were a popular JavaScript project in the early 2010s because they produced amusing output from interesting corpora — Twitter feeds, novels, political speeches. The technique predates modern language models by decades (Andrei Markov developed the theory in 1906), but it demonstrates the core idea that underlies much of natural language processing: sequential token prediction as a probabilistic process. The difference between a Markov chain and a transformer is essentially the depth of the conditional dependency.

## Key points

- Markov chain text generation: next-word probability conditioned on current word (or last n words in higher-order chains)
- Implementation: build a transition probability table from corpus, do random walks to generate text
- N-gram order trades off: higher order → more coherent locally, less diverse; first-order → more random, sometimes funnier
- The model's failure mode (local coherence, global incoherence) is the same failure mode of early n-gram language models
- Historical continuity: transformers and LLMs are doing the same fundamental task (next token prediction) with much richer conditional dependencies

[Original](http://blog.javascriptroom.com/2013/01/21/markov-chains/)
