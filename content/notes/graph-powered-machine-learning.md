---
title: Graph-Powered Machine Learning
date: 2022-04-05
categories:
  - graph-neural-networks
  - knowledge-graphs
  - machine-learning
  - book
description: Alessandro Negro's Manning book covers the intersection of graph theory and machine learning, from knowledge graphs and GNNs to fraud detection and recommendations using Neo4j. It's a practical end-to-end treatment that bridges graph databases and ML for practitioners.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/Alessandro Nego - Graph-Powered Machine Learning (2021, _ Manning Publications) - libgen.li.pdf
---

## Summary

Alessandro Negro's 2021 Manning Publications book is a practitioner-oriented treatment of applying machine learning to and with graph-structured data. The book uses Neo4j as the primary graph database throughout, grounding abstract concepts in a system readers can run locally. Topics span knowledge graphs, graph neural networks (GNNs), community detection, and link prediction, forming a progression from graph fundamentals to advanced ML techniques.

A significant portion focuses on applied use cases: fraud detection (where transaction graphs reveal rings invisible to tabular models), recommendation systems (collaborative filtering reframed as link prediction on user-item graphs), and entity resolution (merging duplicate nodes via similarity). These chapters are particularly strong because they show where graph representations offer structural advantages over flat feature vectors — not just aesthetic ones.

The graph neural network chapters cover message passing, GraphSAGE, and Graph Convolutional Networks (GCN), connecting them to the broader deep learning literature. The book bridges the gap between graph theory practitioners (who may know Cypher and Neo4j well) and ML engineers (who may not), making it useful for teams building knowledge graph-backed applications or embedding graph structure into neural pipelines.

## Key points

- Neo4j is used as the primary implementation vehicle, with Cypher queries shown alongside Python ML code.
- Graph Neural Networks chapter covers GCN, GraphSAGE, and message passing frameworks including PyTorch Geometric.
- Fraud detection case study shows how connected-component and community detection algorithms surface criminal rings missed by per-transaction classifiers.
- Knowledge graphs are covered both as standalone data structures and as enrichment layers for downstream NLP and recommendation tasks.
- The book treats both supervised learning on graphs (node classification, link prediction) and unsupervised learning (community detection, graph embeddings).

[Original](file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/Alessandro Nego - Graph-Powered Machine Learning (2021, _ Manning Publications) - libgen.li.pdf)
