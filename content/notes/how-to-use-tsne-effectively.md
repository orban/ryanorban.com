---
title: How to Use t-SNE Effectively
date: 2016-12-14
categories:
  - machine-learning
  - visualization
  - dimensionality-reduction
  - tsne
  - data-science
description: Martin Wattenberg, Fernanda Viégas, and Ian Johnson's interactive Distill article on how t-SNE maps actually work — and how to avoid misreading them. Essential reading before trusting any t-SNE plot.
params:
  source: pinboard
  sourceUrl: http://distill.pub/2016/misread-tsne/
---

![How to Use t-SNE Effectively](/images/notes/how-to-use-tsne-effectively.png)

## Summary

t-SNE (t-distributed Stochastic Neighbor Embedding) is one of the most widely-used tools in data science for dimensionality reduction and visualizing high-dimensional data in 2D or 3D. This interactive Distill article by Martin Wattenberg, Fernanda Viégas, and Ian Johnson uses live visualizations to show how t-SNE maps can be deeply misleading when hyperparameters are misunderstood or output is interpreted naively.

The central insight: t-SNE's output is sensitive to the `perplexity` parameter in non-obvious ways. Perplexity controls the effective number of neighbors the algorithm considers for each point — low perplexity captures tight local structure; high perplexity sees more global patterns. The same dataset visualized with perplexities of 5 vs. 50 vs. 200 can look completely different. The article shows that cluster sizes, distances between clusters, and the overall "shape" of a t-SNE plot are unreliable — you can't conclude that two clusters are more similar just because they appear closer together.

The article was published on Distill, an interactive machine learning journal that pioneered combining explanations with live, manipulable diagrams. This format proved particularly suited to demonstrating t-SNE pitfalls, since you can adjust parameters in real time and watch how the map changes. By 2021, UMAP had largely displaced t-SNE for practical work because it's faster, more deterministic, and better preserves global structure — but the interpretive pitfalls Wattenberg et al. identified apply to dimensionality reduction visualizations broadly.

## Key points

- t-SNE's `perplexity` hyperparameter fundamentally changes the map's topology — different settings produce qualitatively different visualizations of the same data.
- Distances between clusters in a t-SNE plot are meaningless: two nearby clusters may not be more similar than two far-apart ones.
- Cluster sizes are artificial — t-SNE expands small, dense clusters and compresses large, spread-out ones.
- Running t-SNE multiple times (it's stochastic) can produce different layouts; stable structure across runs is more trustworthy than any single run.
- Distill was the first publication to make interactive, notebook-style ML explainers first-class journal content — this article was an early demonstration of that format's power.

[Original](http://distill.pub/2016/misread-tsne/)
