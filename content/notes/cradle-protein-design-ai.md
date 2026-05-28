---
title: "Cradle: AI Platform for Protein Engineering"
date: 2022-12-29
categories:
  - biotech
  - protein-design
  - ai
  - drug-discovery
  - generative-ai
description: Cradle is an AI platform for protein engineering and design — uses generative models to suggest protein sequence modifications that improve properties like stability, expression, and activity. Targets the biotech workflow where engineers iteratively improve proteins through wet lab cycles.
params:
  source: pinboard
  sourceUrl: https://cradle.bio/
---

## Summary

Cradle is a protein engineering platform that uses generative AI to suggest protein sequence modifications, accelerating the design-build-test cycle in biotech and drug discovery. The core problem: engineering a protein to have desired properties (better stability, higher expression yield, stronger binding affinity) traditionally requires many rounds of mutation-and-test in the wet lab. Cradle uses ML models to propose which mutations are most likely to improve the target property, reducing the number of experimental cycles required.

The underlying approach draws on protein language models — similar to large language models but trained on protein sequences rather than text. ESMFold, AlphaFold, and the protein language model ESM-2 demonstrated that transformer architectures can learn the evolutionary grammar of proteins well enough to generate plausible sequences and predict structure. Cradle applies this in a closed-loop system where model predictions guide lab experiments and lab results improve the model.

Cradle launched in late 2022, at the moment when the protein ML field was still processing the implications of AlphaFold 2 (2021) and figuring out how to move from structure prediction to functional design. The company targets biotech engineers and researchers who understand protein biology but need better computational tools for the design step. This puts it alongside tools like Evolvere and ProteinMPNN in the AI-assisted protein engineering space.

## Key points

- Suggests protein sequence mutations that improve stability, expression, or binding — reducing wet lab cycles.
- Based on protein language models similar to LLMs but trained on evolutionary sequence data.
- Builds on AlphaFold / ESM-2 wave of protein ML; moves from structure prediction to design.
- Targets biotech engineers as users — closed-loop: model suggests → lab tests → model improves.
- Competes with ProteinMPNN, RFDiffusion, and specialized platforms for protein design.

[Original](https://cradle.bio/)
