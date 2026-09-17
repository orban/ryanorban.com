---
title: "LLM Visualization: Interactive 3D Transformer Walkthrough"
date: 2023-12-03
categories:
  - llm
  - education
  - visualization
  - transformer
  - explainability
description: An interactive 3D visualization of how LLMs work — walking through the transformer architecture token by token, layer by layer, with actual weight animations. The clearest visual explanation of attention, embeddings, and feedforward layers available.
params:
  source: pinboard
  sourceUrl: https://bbycroft.net/llm
---

![LLM Visualization: Interactive 3D Transformer Walkthrough](/images/notes/llm-visualization.png)

## Summary

[LLM Visualization](/notes/llm-visualization/) by Brendan Bycroft is an interactive, animated walkthrough of a transformer-based language model at the level of individual operations. It shows the attention mechanism, embeddings, positional encoding, layer normalization, and feedforward networks not as diagrams but as live computations on a real (small) model. You can step through token processing and see exactly what each layer does to the representation.

The key pedagogical achievement is making the attention mechanism concrete. "Attention computes a weighted sum of values" is a description; watching the attention weights animate for each head and seeing which tokens attend to which makes it visceral. For people who have read the Attention is All You Need paper but haven't seen the mechanics animate, this is the next-best thing to running the code yourself.

The implementation uses WebGL for 3D rendering, running a tiny GPT-2-like model in the browser. The model is small enough to be fully interactive while demonstrating all the key architectural components. For technical audiences, the source is available on GitHub, making it usable as a teaching tool for workshops or university courses on deep learning and NLP.

## Key points

- Interactive 3D animation of the full transformer forward pass — embeddings, attention, feedforward, layer norm.
- Attention heads animate to show which tokens attend to which — makes multi-head attention tangible.
- Runs a real small GPT-2-like model in the browser via WebGL.
- Step-by-step mode: pause at any layer to understand what that operation does.
- Better than static diagrams for building intuition about residual streams and information flow.
- By Brendan Bycroft — open source on GitHub.

[Original](https://bbycroft.net/llm)
