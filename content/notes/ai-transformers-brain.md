---
title: How AI Transformers Mimic Parts of the Brain (Quanta Magazine)
date: 2022-09-13
categories:
  - transformers
  - neuroscience
  - machine-learning
  - cognitive-science
  - attention
description: Quanta Magazine's September 2022 piece on emerging research showing that transformer attention patterns converge with how the brain processes language and vision — a surprising empirical finding with implications for both AI interpretability and computational neuroscience.
params:
  source: pinboard
  sourceUrl: https://www.quantamagazine.org/how-ai-transformers-mimic-parts-of-the-brain-20220912/
---

## Summary

This Quanta Magazine article covers research finding structural parallels between transformer models and brain activity during language and vision tasks. Neuroscientists found that attention patterns in transformer models correlate with neural activity in regions like Broca's area and the fusiform face area — not by design, but as an emergent consequence of training on human-generated data. The convergence suggests that transformers may be discovering processing strategies that brains also evolved toward.

The research draws on representational similarity analysis — comparing the geometry of representations in transformer layers to those measured in brain imaging studies (fMRI and MEG). Middle layers of large language models tend to align most closely with language-related brain regions; early and late layers align less well. This layer-wise mapping suggests the transformer architecture's inductive biases somehow push toward biologically plausible representations, despite being trained purely on prediction loss.

The implications cut both ways. For AI interpretability, brain analogies provide a grounding for intuitions about what different layers do. For computational neuroscience, transformers become a tractable model system — you can probe the "brain" in arbitrary ways that aren't possible with biological subjects. This convergence is part of broader neuro-AI research connecting deep learning architectures to primate visual systems (the ventral stream — V1, V2, V4, IT cortex — has been mapped to CNN layers since AlexNet).

## Key points

- Transformer attention patterns show empirical alignment with neural activity in language and vision brain regions.
- Discovered via representational similarity analysis comparing transformer layer representations to fMRI/MEG data.
- Middle transformer layers align best with language areas like Broca's area; a non-obvious structural correspondence.
- Dual implication: AI interpretability gains biological grounding; neuroscience gets a tractable model system.
- Part of a broader neuro-AI program connecting deep learning to primate visual cortex (ventral stream, IT cortex).
- The convergence is emergent — not designed in — suggesting transformers discover biologically favored representations.

[Original](https://www.quantamagazine.org/how-ai-transformers-mimic-parts-of-the-brain-20220912/)
