---
title: "Machine Learning: Genetic Algorithms in JavaScript"
date: 2012-09-05
categories:
  - machine-learning
  - genetic-algorithms
  - javascript
  - evolutionary-computation
  - optimization
description: Burak Kanber's accessible tutorial implementing genetic algorithms in JavaScript from scratch — part of a machine learning series aimed at web developers. One of the early 'ML for JS devs' resources that predated the current wave of browser-based ML by several years.
params:
  source: pinboard
  sourceUrl: http://burakkanber.com/blog/machine-learning-genetic-algorithms-part-1-javascript/
---

## Summary

Burak Kanber's blog post implemented a genetic algorithm in JavaScript as part of a machine learning series for web developers. In 2012, JavaScript was not an obvious choice for machine learning — Python had scikit-learn, NumPy, and SciPy; R had a comprehensive stats ecosystem. The choice of JS was pedagogical: it's the language most web developers know, and the algorithm could run visually in the browser.

Genetic algorithms are a class of evolutionary computation inspired by biological natural selection. The core loop: maintain a population of candidate solutions (each encoded as a chromosome), evaluate each on a fitness function, select the fittest, then create a new generation through crossover (combining parts of two parent solutions) and mutation (randomly altering parts). Over generations, the population evolves toward better solutions. The algorithm doesn't guarantee finding the global optimum but is often effective on problems where the search space is too large for exhaustive search and gradients aren't available.

The tutorial's canonical example was typically a simple optimization problem — minimizing a function or evolving a string toward a target — designed to make the mechanics visible. The educational approach: show the actual code, run it, see the population evolve in the browser. This see it work approach was characteristic of the early-2010s wave of accessible ML tutorials that preceded the current era of notebooks and Jupyter. The connection to Boids (saved the same month) is structural — both use decentralized rules to produce useful aggregate behavior.

## Key points

- Genetic algorithm components: population, fitness function, selection, crossover, mutation, generation loop
- No gradient required: works on discrete, combinatorial, or non-differentiable search spaces where gradient descent fails
- JavaScript ML pedagogy: 2012 version of the ML for web developers genre — browser execution made results immediately visual
- Connects to evolutionary computation more broadly: genetic programming, particle swarm optimization, ant colony optimization
- Weakness: slow convergence, sensitive to fitness function design, prone to premature convergence — works well on problems where good enough solutions are acceptable

[Original](http://burakkanber.com/blog/machine-learning-genetic-algorithms-part-1-javascript/)
