---
title: The Kernel Trick
date: 2014-03-28
categories:
  - machine-learning
  - svm
  - kernel-methods
  - mathematics
description: Eric Kim's explanation of the kernel trick in support vector machines — how kernels enable SVMs to classify non-linearly separable data by implicitly mapping it to a higher-dimensional space. One of the cleaner intuitive explanations of a mathematically dense concept.
params:
  source: pinboard
  sourceUrl: http://www.eric-kim.net/eric-kim-net/posts/1/kernel_trick.html
---

![The Kernel Trick](/images/notes/kernel-trick-svm.png)

## Summary

The kernel trick is one of the more elegant ideas in machine learning: you can classify non-linearly separable data using a support vector machine without ever explicitly computing a high-dimensional feature mapping. Instead, you define a kernel function K(x, z) that computes the dot product in the high-dimensional space directly — which is often much cheaper. The SVM only needs inner products between points, so the trick works.

Eric Kim's explanation walks through the intuition: some datasets can't be separated by a linear boundary in their original feature space, but become separable when mapped to a higher-dimensional space (think the classic XOR problem). The kernel trick makes this computationally tractable by avoiding the explicit mapping — you implicitly compute in the high-dimensional space.

Common kernels include the RBF (radial basis function) kernel, which maps to infinite-dimensional space and is equivalent to measuring Gaussian similarity; the polynomial kernel; and the linear kernel (which is just the standard SVM). The choice of kernel is a form of inductive bias: the RBF kernel is a good default, but gets expensive for large datasets because it requires computing n² pairwise similarities.

## Key points

- The kernel trick avoids explicit high-dimensional feature mapping by computing inner products directly.
- Any positive semi-definite function qualifies as a kernel (Mercer's theorem).
- RBF kernel: equivalent to infinite-dimensional mapping, measures Gaussian similarity between points.
- Kernel choice is inductive bias — RBF is the common default but scales as O(n²) in training.
- SVMs with kernels were state-of-the-art before deep learning — still useful for small datasets.

[Original](http://www.eric-kim.net/eric-kim-net/posts/1/kernel_trick.html)
