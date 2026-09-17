---
title: What Are the Most Important Statistical Ideas of the Past 50 Years?
date: 2022-02-22
categories:
  - statistics
  - bayesian
  - causal-inference
  - survey
  - jasa
description: Andrew Gelman and Aki Vehtari's 2021 JASA paper enumerating 8 ideas that most changed statistics in the past 50 years — from counterfactual causal inference to bootstrapping to overparameterized models. A rare high-level synthesis by two of the field's most credible voices.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/gelman-vehtari-statistical-ideas.pdf
---

## Summary

Andrew Gelman and Aki Vehtari (JASA, 2021) take stock of what actually moved statistics forward over the past half-century. Rather than a textbook survey, this is an opinionated synthesis: eight ideas the authors believe reshaped how statisticians think, not just what methods they use.

The eight ideas:

1. **Counterfactual causal inference** — formalizing causation via potential outcomes (Rubin causal model) and graphical models (DAGs, do-calculus). Before the 1970s, causation was largely avoided in statistics as unscientific. Now it has a rigorous language.

2. **Bootstrapping and simulation-based inference** — Efron's 1979 bootstrap and the broader shift toward using computation (simulation, Monte Carlo) rather than analytic formulas for inference. Freed statistics from the constraints of distributional assumptions.

3. **Overparameterized models** — neural networks, regularization, and the empirical discovery that models with more parameters than data points can generalize well. Challenges the classical bias-variance tradeoff intuition.

4. **Multilevel models** (hierarchical models) — pooling information across groups, units, or time periods via random effects. Ubiquitous in educational testing, epidemiology, and social science.

5. **Generic computation algorithms** — Expectation-Maximization, Gibbs sampling, Hamiltonian Monte Carlo, variational inference. These made Bayesian inference tractable for complex models; you no longer needed analytic posteriors.

6. **Adaptive decision analysis** — clinical trials, sequential testing, and online learning methods that adapt based on accumulating data rather than fixing designs upfront.

7. **Robust inference and nonparametric models** — methods that work without strong distributional assumptions; quantile regression, kernel methods, permutation tests. Building in robustness as a design goal rather than an afterthought.

8. **Exploratory data analysis** — John Tukey's 1977 EDA book and the attitude that visualization and informal exploration are legitimate scientific activities, not just data cleaning.

The paper's framing is notable: the authors argue that computation and simulation underlie many of these advances — the bootstrap, generic algorithms, and overparameterized models all depend on computational power that didn't exist in 1970. The ideas aren't purely mathematical; they're about what became *practical*.

## Key points

- Counterfactual causal inference (Rubin potential outcomes + Pearl DAGs) is listed first — the authors view causal reasoning as statistics' biggest conceptual advance
- Bootstrapping introduced computation as a core statistical tool, not just a numerical aid; resampling freed inference from parametric assumptions
- Overparameterized models (including deep learning) challenge the classical bias-variance tradeoff — the double descent phenomenon is a statistical puzzle that existing theory doesn't explain
- Generic algorithms (EM, MCMC, VI) democratized Bayesian inference — made it possible for practitioners to fit complex models without deriving analytic posteriors
- John Tukey's EDA is explicitly included as a philosophical shift, not just a technique

[Original (JASA 2021)](https://www.tandfonline.com/doi/full/10.1080/01621459.2021.1938081)
