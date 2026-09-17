---
title: Language Models as Models of the Visual World
date: 2022-10-04
categories:
  - machine-learning
  - vision-language
  - research
  - multimodal
  - soft-prompts
description: Research showing language models can use linear projections of image representations as soft prompts for vision-language tasks — without tuning the LM or image encoder. An early signal for the efficiency of frozen model feature reuse in multimodal architectures.
params:
  source: pinboard
  sourceUrl: https://twitter.com/jack_merullo_/status/1577051483019030528
---

## Summary

Jack Merullo's research paper shows that language models contain surprisingly strong representations of the visual world even without explicit image training. The key finding: you can take a frozen image encoder (like CLIP's visual encoder), project its output to the LM's embedding dimension with a simple linear layer, and use the resulting vectors as soft prompts for vision-language tasks — without fine-tuning either the LM or the image encoder.

This is a remarkable result because it suggests that LLM embeddings and visual encoder embeddings share structure that a linear projection can bridge. If the models were encoding fundamentally different representations, a linear transform wouldn't suffice — you'd need a more complex adapter. The success of the linear projection implies alignment in representational geometry.

The practical implication: multimodal capability can be added to LLMs more efficiently than expected. This foreshadowed work like LLaVA (which uses a linear projection to connect CLIP and LLaMA) and BLIP-2's Q-Former — approaches that achieved strong multimodal performance with minimal additional training. The full fine-tuning of GPT-4V and similar models is the heavyweight option; this work suggested lightweight bridging was possible.

## Key points

- LLMs have latent visual world representations even without image training.
- Linear projection of image encoder outputs as soft prompts bridges modalities without fine-tuning.
- Alignment in representational geometry between visual and language encoders enables this.
- Precursor to LLaVA, BLIP-2, and lightweight multimodal adapter approaches.
- No fine-tuning of LM or image encoder required — efficiency implication for multimodal models.
- Published by Jack Merullo et al., October 2022.

[Original](https://twitter.com/jack_merullo_/status/1577051483019030528)
