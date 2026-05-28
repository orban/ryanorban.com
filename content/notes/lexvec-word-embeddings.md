---
title: LexVec
date: 2016-07-27
categories:
  - machine-learning
  - nlp
  - word-embeddings
  - golang
  - open-source
description: LexVec is a Go implementation of a word embedding model that factorizes the PPMI matrix with position-dependent weighting, outperforming Word2Vec on several NLP benchmarks at the time. An interesting mid-2010s data point in the race to improve on Word2Vec before attention-based models took over.
params:
  source: pinboard
  sourceUrl: https://github.com/alexandres/lexvec
---

![LexVec](/images/notes/lexvec-word-embeddings.png)

## Summary

LexVec is a word embedding model implemented in Go by Alexandre Salle, Aline Villavicencio, and Marco Idiart. It was published in 2016 as part of a wave of methods trying to improve on Word2Vec and GloVe by more carefully modeling the PPMI (Positive Pointwise Mutual Information) matrix that encodes word co-occurrence statistics. The key idea: rather than simply factorizing the PPMI matrix (like GloVe), LexVec minimizes a weighted loss that penalizes errors on frequently co-occurring pairs more heavily — giving the model better signal on the relationships that matter most.

The model was written in Go rather than Python or C, which was somewhat unusual and positioned it as a high-performance alternative. The paper reported better performance than Word2Vec's skip-gram and CBOW variants on several word similarity and analogy benchmarks, though the improvements were incremental rather than transformative. This was characteristic of the 2015-2017 era of NLP: lots of careful matrix factorization variants competing for small gains on fixed benchmarks before Transformer-based models like BERT reshaped the evaluation landscape entirely.

LexVec sits in an interesting historical position. It represents the mature end of the first generation of distributional semantics methods — the class of models that treat meaning as derived from context distributions. By 2018, contextual embeddings from ELMo and then BERT demonstrated that static embeddings (where a word has one vector regardless of context) were fundamentally limited, and the research frontier moved on. Tools like LexVec are now mainly of historical interest as examples of how far classical distributional methods could be pushed.

## Key points

- Factorizes PPMI matrix with position-dependent weighting rather than simple co-occurrence counts — the key innovation over GloVe.
- Written in Go, making it faster and easier to deploy than Python implementations at the time.
- Benchmarked against Word2Vec skip-gram and CBOW; outperformed both on several word similarity and analogy tasks.
- Part of the 2015-2017 wave of Word2Vec improvements that was superseded by contextual embeddings (ELMo, BERT).
- Open-source on GitHub under MIT license.

[Original](https://github.com/alexandres/lexvec)
