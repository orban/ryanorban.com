---
title: A Survey on Graph Representation Learning Methods
date: 2022-07-07
categories:
  - graph-neural-networks
  - representation-learning
  - knowledge-graphs
  - survey
  - machine-learning
description: Khoshraftar and An (York University) provide a comprehensive survey of graph representation learning covering node embeddings, GNNs, and knowledge graph methods, with attention to both spectral and spatial approaches. It's the right starting point for anyone orienting to the GRL landscape — methodical coverage from DeepWalk through GAT.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/A Survey of Graph Representation Learning Methods.pdf
---

## Summary

Khoshraftar and An (York University) survey the field of graph representation learning, organizing methods into three broad families: shallow node embeddings, graph neural networks, and knowledge graph embeddings. The goal throughout is to learn low-dimensional vector representations that preserve graph structure — proximity, community membership, relational patterns — so that downstream tasks like node classification, link prediction, and graph classification can be solved with standard ML pipelines.

The shallow embedding section covers random walk-based methods: DeepWalk applies word2vec to random walk sequences to learn node embeddings, and Node2Vec adds biased walks that interpolate between breadth-first and depth-first exploration, allowing the embeddings to capture different structural notions of similarity. These methods are effective but transductive — they don't generalize to unseen nodes. The GNN section covers GCN (Graph Convolutional Network), which defines convolution via spectral methods on the graph Laplacian, and spatial approaches like GraphSAGE (inductive learning by sampling and aggregating neighbor features) and GAT (Graph Attention Networks, which use attention to weight neighbor contributions). Knowledge graph embeddings — TransE, RotatE — are treated separately, as they must model typed relations rather than just proximity.

The survey is organized around the key design choices: spectral vs. spatial convolution, shallow vs. deep architectures, transductive vs. inductive learning. Understanding these distinctions is necessary for choosing the right method for a given task. Spectral methods like GCN are theoretically grounded in signal processing on graphs but require the full graph Laplacian at training time, limiting scalability. Spatial methods like GraphSAGE are more flexible and scale to large graphs via mini-batch training over sampled neighborhoods.

## Key points

- Node embeddings (DeepWalk, Node2Vec): random walk-based, learn proximity in embedding space, transductive only
- GCN: spectral convolution via graph Laplacian — theoretically clean but not inductive; can't generalize to new nodes
- GraphSAGE: inductive by aggregating sampled neighbor features — scales to large graphs via mini-batches
- GAT: attention over neighbors lets the model weight high-information connections more heavily
- Knowledge graph embeddings (TransE, RotatE) model typed relational facts rather than structural proximity

[Source](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/A%20Survey%20of%20Graph%20Representation%20Learning%20Methods.pdf)
