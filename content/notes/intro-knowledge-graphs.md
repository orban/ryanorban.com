---
title: An Introduction to Knowledge Graphs
date: 2021-05-22
categories:
  - knowledge-graphs
  - ai
  - nlp
  - semantic-web
  - data-science
description: Stanford AI Lab's introduction to knowledge graphs — what they are, how they're constructed, and where they're used. A solid conceptual overview covering entity linking, relation extraction, and the gap between structured and unstructured knowledge.
params:
  source: pinboard
  sourceUrl: http://ai.stanford.edu/blog/introduction-to-knowledge-graphs/
---

## Summary

This Stanford AI Lab blog post introduces knowledge graphs — structured representations of real-world entities and their relationships — covering both the conceptual foundations and the practical challenges of building and maintaining them. A knowledge graph stores facts as triples: (entity, relation, entity), e.g., (Barack Obama, bornIn, Hawaii). The structure enables reasoning, question answering, and semantic search that plain text retrieval can't match.

The post covers the major components of a knowledge graph pipeline: named entity recognition (identifying entities in text), entity linking (mapping mentions to canonical entries in the graph), and relation extraction (inferring relationships from text). It also addresses the ongoing challenge of knowledge graph completion — using embedding-based methods (like TransE, RotatE) to predict missing facts the graph doesn't explicitly contain.

From a 2026 vantage point, this post represents the pre-LLM era of knowledge graph research. The assumption was that structured knowledge graphs were a necessary complement to language models because LLMs couldn't reliably recall facts. That assumption has been partially undermined — LLMs can retrieve many facts from their parameters — but structured graphs remain valuable for freshness (up-to-date information), traceability (knowing where a fact came from), and precision (no hallucination).

## Key points

- Knowledge graphs store facts as triples: (entity, relation, entity) — enables structured reasoning over relationships.
- Construction pipeline: named entity recognition → entity linking → relation extraction from text.
- Knowledge graph completion: embedding methods predict missing facts (TransE, RotatE models).
- Used in Google Knowledge Graph, Wikidata, Freebase, and enterprise data integration.
- Complements LLMs: graphs provide freshness, traceability, and zero-hallucination retrieval that parametric memory can't guarantee.

[Original](http://ai.stanford.edu/blog/introduction-to-knowledge-graphs/)
