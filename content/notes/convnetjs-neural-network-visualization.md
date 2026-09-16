---
title: "ConvNetJS Demo: Classify Toy 2D Data"
date: 2014-04-19
categories:
  - machine-learning
  - neural-networks
  - visualization
  - javascript
  - deep-learning
description: Andrej Karpathy's ConvNetJS demo for classifying 2D toy datasets — a real-time browser visualization of a neural network training on user-drawn boundaries. One of the first compelling interactive deep learning visualizations.
params:
  source: pinboard
  sourceUrl: http://cs.stanford.edu/people/karpathy/convnetjs/demo/classify2d.html
---

## Summary

ConvNetJS is Andrej Karpathy's JavaScript library for training neural networks entirely in the browser. The 2D classification demo is the most memorable piece: you can draw training data on a canvas, pick a network architecture, and watch the decision boundary update in real time as the network trains. In 2014, this was a genuinely impressive demonstration that deep learning was accessible enough to run interactively in a browser.

The demo works because toy 2D classification is computationally cheap — the network is tiny and the data fits in memory. Karpathy built ConvNetJS while at Stanford to make neural networks more understandable through direct manipulation. The same pedagogical instinct drove his later work at OpenAI and Tesla on making deep learning education accessible.

The significance beyond novelty: this was part of a wave of interactive machine learning visualizations in 2013-2014 (alongside Jason Davies' work with D3.js and Distill-precursor explanations) that began shifting deep learning from academic specialty to something practitioners and curious engineers could engage with directly.

## Key points

- ConvNetJS: JavaScript library by Andrej Karpathy for in-browser neural network training.
- 2D demo shows decision boundaries updating in real-time as network trains — intuition builder.
- Supports fully connected networks, CNNs, and recurrent networks in the browser.
- Pioneering example of interactive deep learning visualization before Tensorflow Playground or Distill.
- Karpathy's pedagogical philosophy: understanding comes from direct manipulation, not passive reading.

[Original](http://cs.stanford.edu/people/karpathy/convnetjs/demo/classify2d.html)
