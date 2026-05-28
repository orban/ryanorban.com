---
title: "BERTopic: The Future of Topic Modeling"
date: 2022-05-11
categories:
  - nlp
  - topic-modeling
  - bert
  - machine-learning
  - pinecone
description: A Pinecone explainer on BERTopic — a topic modeling library that uses transformer embeddings instead of bag-of-words statistics, producing semantically coherent topics. BERTopic largely made LDA obsolete for practitioners who have access to modern embeddings.
params:
  source: pinboard
  sourceUrl: https://www.pinecone.io/learn/bertopic/
---

![BERTopic: The Future of Topic Modeling](/images/notes/bertopic.png)

## Summary

[BERTopic](/notes/bertopic/) is a topic modeling library that replaces the bag-of-words statistics of LDA (Latent Dirichlet Allocation) with transformer-based document embeddings. The core pipeline: embed documents using a sentence transformer (e.g. `all-MiniLM-L6-v2`), reduce dimensions with UMAP, cluster with HDBSCAN, then extract representative terms per cluster using c-TF-IDF (a class-based variant of TF-IDF). The result is semantically coherent topics where documents in the same cluster are genuinely about the same thing rather than just sharing common words.

Traditional topic modeling with LDA struggles with short texts and polysemous words — a document about Apple (the company) and "apple" (the fruit) could end up in the same topic because the word is identical. BERT-based embeddings encode context, so these are placed in entirely different neighborhoods of embedding space before clustering even starts. [BERTopic](/notes/bertopic/) inherits this disambiguation for free.

The Pinecone tutorial covers the full workflow and explains why each component was chosen. UMAP over PCA for dimensionality reduction: UMAP preserves local structure (nearby documents stay nearby) better than PCA's global variance approach. HDBSCAN over k-means: HDBSCAN is density-based and handles noise/outliers gracefully, doesn't require specifying k in advance, and produces variable-density clusters that match how topics actually distribute in practice.

## Key points

- [BERTopic](/notes/bertopic/) pipeline: embed with sentence transformers → reduce with UMAP → cluster with HDBSCAN → label with c-TF-IDF
- Handles short texts well (tweets, titles) where LDA fails — embeddings encode meaning regardless of length
- UMAP preserves local neighborhood structure; HDBSCAN finds clusters of varying density without requiring k
- c-TF-IDF: term frequency reweighted at the cluster level — identifies terms that are distinctive *within* a topic vs. the whole corpus
- Dynamic topic modeling variant tracks how topics evolve over time — useful for analyzing news corpora or long-running discussions
- Pinecone hosts the tutorial as a practical entry point; [BERTopic](/notes/bertopic/) itself is by Maarten Grootendorst

[Original](https://www.pinecone.io/learn/bertopic/)
