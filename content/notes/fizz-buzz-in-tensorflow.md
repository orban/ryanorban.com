---
title: Fizz Buzz in TensorFlow
date: 2016-05-24
categories:
  - machine-learning
  - tensorflow
  - humor
  - neural-networks
  - programming
description: Joel Grus deliberately solves FizzBuzz using TensorFlow — a satirical demonstration of using a neural network where simple conditional logic would do. A sharp critique of ML overcomplexity disguised as a tutorial.
params:
  source: pinboard
  sourceUrl: http://joelgrus.com/2016/05/23/fizz-buzz-in-tensorflow/
---

## Summary

Joel Grus wrote this post as a wry exercise in applying TensorFlow to a problem that every programmer solves with three lines of conditionals: FizzBuzz. The joke is the point — building a neural network to learn the modular arithmetic rules of FizzBuzz requires encoding the numbers in binary, training a hidden layer, and ultimately doing far more work than a `for` loop ever would. The network learns the pattern rather than following the rule.

The deeper observation is about the relationship between machine learning and rule-based programming. When the mapping is deterministic and the rules are known, ML adds complexity without benefit. TensorFlow — then newly open-sourced by Google — was being applied everywhere, and Grus's post implicitly asked which problems actually benefit from learned models versus explicit logic.

The post captures a genuine tension in data science practice: the seduction of powerful tools leading to their misuse. It became widely shared precisely because practitioners recognized the pattern. It's also a usable tutorial on binary encoding of inputs, softmax output layers, and the basic structure of a TensorFlow training loop.

## Key points

- Deliberately over-engineers FizzBuzz using TensorFlow to satirize ML overcomplexity.
- Input encoding: numbers represented in binary, not decimal — required for the neural network to find patterns.
- Output: softmax over four classes (fizz, buzz, fizzbuzz, number).
- The neural network actually works and achieves high accuracy — making the satire more effective.
- Illustrates when machine learning is the wrong tool: deterministic, rule-based problems with known structure.

[Original](http://joelgrus.com/2016/05/23/fizz-buzz-in-tensorflow/)
