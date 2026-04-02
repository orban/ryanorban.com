---
title: Isomorphic Labs Drug Design Engine
date: 2026-02-10
categories:
  - drug-discovery
  - machine-learning
  - protein-structure
  - alphafold
  - isomorphic-labs
description: Isomorphic Labs' Drug Design Engine (IsoDDE) goes beyond AlphaFold 3 to predict binding affinity and identify cryptic drug pockets from amino acid sequences alone. The step from structure prediction to actual drug optimization.
params:
  source: pinboard
  sourceUrl: https://www.isomorphiclabs.com/articles/the-isomorphic-labs-drug-design-engine-unlocks-a-new-frontier
---

![Isomorphic Labs Drug Design Engine](/images/notes/isomorphic-labs-drug-design-engine.png)

## Summary

Isomorphic Labs released their Drug Design Engine (IsoDDE) in February 2026 — a unified computational system for drug discovery that extends beyond AlphaFold 3's structure prediction to cover the full workflow of drug design. AlphaFold 3 solved the structure prediction problem; IsoDDE addresses what you actually need to design drugs: binding affinity prediction, pocket identification, and antibody design.

The key advances over AlphaFold 3: IsoDDE more than doubles AF3's accuracy on challenging protein-ligand systems that differ significantly from training data, including complex phenomena like induced fits and cryptic pockets. It achieves 2.3x better performance on antibody-antigen interfaces. For binding affinity, it surpasses physics-based methods at much lower computational cost. And it can identify potential drug-binding sites using only the amino acid sequence as input — finding allosteric binding sites that wouldn't be visible from structure alone.

This matters because structure prediction, while revolutionary, was never the bottleneck in drug discovery. Knowing the structure of a protein doesn't directly tell you how tightly a drug candidate binds to it, or where to look for binding sites in an unexplored target. IsoDDE closes that gap by providing the predictive capabilities that connect structural knowledge to pharmaceutical development.

## Key points

- IsoDDE extends AlphaFold 3 from structure prediction to the full drug design workflow.
- More than doubles AF3's accuracy on out-of-distribution protein-ligand systems.
- Predicts binding affinity — how strongly molecules bind to targets — outperforming physics-based methods.
- Identifies drug-binding sites from amino acid sequence alone, including cryptic and allosteric pockets.
- 2.3x better performance than AF3 on antibody-antigen interfaces.
- Bridges the long-standing gap between computational prediction and practical pharmaceutical development.

[Original](https://www.isomorphiclabs.com/articles/the-isomorphic-labs-drug-design-engine-unlocks-a-new-frontier)
