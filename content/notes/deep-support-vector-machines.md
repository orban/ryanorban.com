---
title: Deep Support Vector Machines
date: 2013-09-04
categories:
  - machine-learning
  - svm
  - deep-learning
  - neural-networks
  - research
description: A video lecture on Deep Support Vector Machines from ROKS 2013 — hybrid architectures combining deep feature learning with SVM classification. A snapshot of the moment researchers explored whether SVMs and deep learning could coexist before end-to-end networks won out.
params:
  source: pinboard
  sourceUrl: http://videolectures.net/roks2013_wiering_vector/
---

## Summary

This video lecture from ROKS 2013 (Recent Advances in Kernel-based methods) by Marco Wiering covers [Deep Support Vector Machines](/notes/deep-support-vector-machines/) — architectures combining deep neural networks with SVM classification. The core idea: use multiple layers to learn hierarchical feature representations, then feed those into an SVM classifier rather than a softmax layer.

This research direction emerged at a specific inflection point: AlexNet had just won ImageNet in 2012, showing that deep convolutional neural networks could learn features automatically. But SVMs had a stronger theoretical track record (margin maximization, kernel trick) and dominated structured prediction tasks. Deep SVM hybrids attempted to get both: deep feature learning plus margin-based optimization with theoretical guarantees.

The kernel trick is central to SVM theory — you compute inner products in a high-dimensional feature space implicitly via a kernel function. Deep SVMs tried to learn those kernel functions or feature maps end-to-end. This line of work ultimately didn't win: end-to-end training with softmax classifiers proved far simpler to optimize, and deep learning absorbed the field by 2015.

## Key points

- Deep SVM: replaces the final linear layer in a deep network with an SVM — seeks margin maximization on top of learned representations.
- Competing objective: joint training of feature layers and SVM margin is harder than end-to-end cross-entropy training.
- ROKS 2013: a specialized workshop for kernel-based learning methods — the academic community most invested in SVM theory at the moment deep learning was taking over.
- The hybrid approach never broadly landed — the field moved to pure end-to-end deep learning, not deep + SVM hybrids.
- Kernel methods and deep learning briefly competed: SVMs dominated structured prediction until ~2015; deep learning then absorbed those tasks too.
- Historically interesting as a road not taken — understanding why it lost informs how we evaluate hybrid ML approaches today.

[Original](http://videolectures.net/roks2013_wiering_vector/)
