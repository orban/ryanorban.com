---
title: Some Useful Machine Learning Libraries
date: 2014-03-10
categories:
  - machine-learning
  - python
  - libraries
  - reference
  - tools
description: A 2013-era survey of machine learning libraries across Python, R, Java, and C++ — a snapshot of the fragmented ML tooling landscape before scikit-learn and deep learning frameworks consolidated the field.
params:
  source: pinboard
  sourceUrl: http://www.erogol.com/broad-view-machine-learning-libraries/
---

## Summary

This survey from Ero Gol in 2013-2014 maps the machine learning library landscape at a time when it was genuinely fragmented. Unlike today, where Python + scikit-learn + PyTorch/TensorFlow is the default stack, practitioners in 2013 chose differently based on their background: R users had R's extensive statistical packages, Java users had Weka and Mahout, C++ users had LIBSVM, and Python was still consolidating around scikit-learn and Theano.

The Python libraries covered likely include scikit-learn (the emerging consensus for classical ML), Theano (the first widely-used deep learning framework for Python), PyML, and utilities like NumPy/SciPy. Weka gets attention as the accessible GUI-based ML tool — valuable for exploratory work without coding. LIBSVM remains the reference implementation for support vector machines, and Vowpal Wabbit handles online learning at very large scale.

The historical value here is seeing what alternatives existed before scikit-learn became canonical. Theano predated TensorFlow (2015) and PyTorch (2016) as the practical deep learning framework. Many libraries in this survey either got absorbed into mainstream tools or faded — MLlib for Apache Spark hadn't launched yet, and none of the GPU-accelerated frameworks were production-ready.

## Key points

- 2013-2014: scikit-learn was gaining but not yet canonical — Weka, LIBSVM, and per-language alternatives were viable choices.
- Theano: the first Python library to compile mathematical expressions to CUDA GPU code — predecessor to TensorFlow and PyTorch.
- Weka: Java-based GUI tool for ML experimentation — useful for non-programmers and algorithm comparison without writing code.
- Vowpal Wabbit: online learning at massive scale (billions of features) — still used for large-scale logistic regression.
- The consolidation that followed (2015-2018) was driven by deep learning's rise making GPU-accelerated frameworks essential.

[Original](http://www.erogol.com/broad-view-machine-learning-libraries/)
