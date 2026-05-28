---
title: "HN: 40 Statistics Interview Problems and Answers"
date: 2020-03-01
categories:
  - statistics
  - interviews
  - data-science
  - career
  - hacker-news
description: A Hacker News thread discussing a list of 40 statistics interview problems — the HN comments add context, caveats, and additional problems to the original post. A snapshot of what statistics knowledge is actually tested in data science interviews.
params:
  source: pinboard
  sourceUrl: https://news.ycombinator.com/item?id=22456977
---

![HN: 40 Statistics Interview Problems and Answers](/images/notes/statistics-interview-questions-hn.png)

## Summary

This Hacker News thread discusses a blog post containing 40 statistics interview problems commonly asked in data science and quant roles. The original post covers problems that appear at tech companies (Google, Netflix, Airbnb) and financial firms in quantitative roles — these span probability theory, combinatorics, distributions, Bayesian inference, and hypothesis testing.

The HN discussion adds substantial value beyond the original post: commenters debate which problems are actually asked in practice vs. which are textbook, identify the trick problems where the naive answer is wrong, and share context about which types of companies emphasize statistics vs. coding vs. ML design questions. The thread also surfaces the distinction between data science interviews at tech companies (more SQL + ML) and at quant finance firms (more rigorous statistics and probability).

Representative problem types: conditional probability (Monty Hall variants, Bayesian updates), expected value calculations for games and bets, distribution questions (when to use Poisson vs. binomial vs. geometric), sampling and estimation, and A/B testing design and analysis. These are the statistics layer that data scientists should know separately from the ML layer — knowing how to train a model doesn't substitute for knowing how to evaluate whether an experiment result is real.

## Key points

- Statistics interview problems: conditional probability, expected value, distributions, hypothesis testing, A/B testing design.
- HN comments add context: which problems are realistic vs. textbook, company-type differences in emphasis.
- Quant finance vs. tech company interviews: finance requires deeper statistics; tech requires more SQL + ML design.
- The Monty Hall-class problems test Bayesian reasoning — correct intuition often requires explicitly conditioning.
- A/B testing questions require both statistical knowledge (p-values, power, MDE) and practical experimental design.
- Related: 160 DS interview questions, [Hiring Without Whiteboards](/notes/hiring-without-whiteboards/), labuladong algorithms in vault.

[Original](https://news.ycombinator.com/item?id=22456977)
