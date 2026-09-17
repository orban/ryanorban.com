---
title: High Dimensional Undirected Graphical Models
date: 2012-09-18
categories:
  - statistics
  - graphical-models
  - machine-learning
  - high-dimensional
  - larry-wasserman
description: Larry Wasserman's 'Normal Deviate' blog post on high-dimensional undirected graphical models — a rigorous but accessible treatment of the statistical theory for learning sparse graphs from data when the number of variables exceeds the sample size. Core to modern genomics and causal inference.
params:
  source: pinboard
  sourceUrl: https://normaldeviate.wordpress.com/2012/09/17/high-dimensional-undirected-graphical-models/
---

![High Dimensional Undirected Graphical Models](/images/notes/high-dimensional-graphical-models.png)

## Summary

Larry Wasserman's Normal Deviate blog was one of the best statistics blogs of the era — a Carnegie Mellon University professor who could write accessibly about hard statistical theory without dumbing it down. This post addressed undirected graphical models (also called Markov random fields or Markov networks) in the high-dimensional regime where the number of variables $p$ is much larger than the sample size $n$ — the $p >> n$ problem that dominated applied statistics in the 2010s.

The classical graphical model problem: given data on $p$ variables, learn the conditional independence structure — which variables are directly connected, which are independent once you condition on everything else. In the classical low-dimensional regime ($n >> p$), this is tractable via likelihood-based methods. In the high-dimensional regime that arises naturally in genomics (thousands of genes, hundreds of samples), neuroimaging (thousands of voxels, dozens of subjects), and social network analysis, classical methods fail.

The solution Wasserman covers is the graphical lasso (glasso) — adding an $L_1$ penalty to the log-likelihood of a Gaussian graphical model that sparsifies the estimated precision matrix (inverse covariance). The sparsity pattern of the precision matrix directly encodes the conditional independence structure of the graph. Robert Tibshirani's LASSO applied to graph estimation. The result is a computationally tractable method for recovering a sparse graph from high-dimensional data, with provable guarantees when the true graph is sparse and samples are sufficient.

## Key points

- Undirected graphical model: encodes conditional independence via edges — two nodes not connected are independent given all others
- High-dimensional challenge: $p >> n$ makes classical MLE ill-posed — the covariance matrix isn't even invertible
- Graphical lasso (glasso): $L_1$-penalized log-likelihood estimation of the precision matrix — sparsity in precision matrix = sparse graph
- Applications: gene regulatory network inference from expression data, fMRI functional connectivity, undirected Boltzmann machines
- Normal Deviate blog (Larry Wasserman): high signal-to-noise statistics writing for practitioners who can handle math

[Original](https://normaldeviate.wordpress.com/2012/09/17/high-dimensional-undirected-graphical-models/)
