---
title: "INDRA: Automated Biomedical Knowledge Assembly"
date: 2023-08-24
categories:
  - knowledge-graph
  - biomedical
  - nlp
  - systems-biology
  - research
description: INDRA (Integrated Network and Dynamical Reasoning Assembler) is an automated knowledge assembly system that reads biomedical literature and databases and produces causal graphs and dynamical models. A long-running academic system for automated scientific knowledge extraction.
params:
  source: pinboard
  sourceUrl: http://www.indra.bio/
---

![INDRA: Automated Biomedical Knowledge Assembly](/images/notes/indra-biomedical-knowledge.png)

## Summary

INDRA (Integrated Network and Dynamical Reasoning Assembler) is a system developed at Harvard Medical School for automatically assembling knowledge from biomedical literature and databases into causal graphs and dynamical models. It interfaces with NLP systems to extract statements from papers (e.g., protein A activates protein B) and databases like UniProt, PathwayCommons, and BioGRID, then assembles these into coherent network models.

The assembly process handles a fundamental challenge in biomedical AI: different sources use different terminology for the same biological entities and relationships. INDRA normalizes this through grounding — mapping entity mentions to standard identifiers — and assembly — merging statements from different sources about the same biological relationship, tracking evidence quality and source provenance. The result is a curated knowledge graph that represents what is known about biological mechanisms with explicit evidence links.

INDRA's output can be exported as networks for pathway analysis, as models for simulation (SBML, PySB), or as causal graphs for mechanistic reasoning. This positions it in the scientific knowledge graph space — automated extraction, assembly, and model construction from literature — that became more prominent with LLM-based literature reading tools. INDRA predates the LLM era but represents the same goal: making scientific knowledge machine-readable and actionable.

## Key points

- Reads biomedical literature and databases, assembles them into causal networks and dynamical models.
- Handles entity grounding (normalizing names to identifiers) and statement assembly (merging sources).
- Output: knowledge graphs, pathway analysis networks, and simulation-ready models (SBML, PySB).
- Developed at Harvard Medical School; long-running academic system (since ~2014).
- Pre-LLM automated scientific knowledge assembly — shares goals with modern literature reading agents.

[Original](http://www.indra.bio/)
 → AI agent
