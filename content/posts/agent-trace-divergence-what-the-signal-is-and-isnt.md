---
title: "What agent trace divergence actually tells you"
date: 2026-04-08
description: "I spent three weeks trying to extract training signal from agent trace divergence. Most of the dreams didn't survive contact with held-out data. Here's what's actually there."
math: true
draft: true
---

You run your agent 30 times on the same task. 18 pass, 12 fail. The traces look different. They branch at different points, pick different tools, choose different files. The hypothesis everyone reaches for is:

*Those branch points are where the decisions matter. Find them, score them, turn them into training data.*

That's the dream. A self-generating preference signal from the variance you already have. Free DPO pairs. A causal handle on agent behavior. No labeling cost.

I spent three weeks testing that hypothesis on [SWE-rebench v2](https://huggingface.co/datasets/nebius/SWE-rebench) — 1,096 tasks, 12,854 runs, multiple models, multiple harnesses — and built a tool called [moirai](https://github.com/orban/moirai) to run the experiments end to end.

Most of it doesn't work the way you'd hope. But the parts that do are narrower and sharper than I expected, and the negative results are more useful than the positive ones. Here's what I found.

---

## The setup

Each task has multiple runs with mixed outcomes. Each run is a sequence of tool calls: `read(source)`, `search(grep_targeted)`, `edit(source)`, `test(pass)`, `bash(python)`, and so on.

To find divergence points, align the runs with [Needleman-Wunsch](https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm). At each column, group runs by the step they took. Test whether the branch predicts outcome with [Fisher's exact](https://en.wikipedia.org/wiki/Fisher%27s_exact_test), correct for multiple comparisons with [Benjamini-Hochberg](https://en.wikipedia.org/wiki/False_discovery_rate#Benjamini%E2%80%93Hochberg_procedure).

That gives you a list of statistically significant divergence points per task. Within-task, the signal looks real. The question is whether it generalizes, whether it's uniform across tasks, and whether you can do anything useful with it.

Six questions, six experiments.

---

## 1. Does divergence correlate with outcome? (Weakly)

Split each task's runs into train/test halves. Find divergence points on train. Use them to score held-out test runs. Measure AUROC.

| Method | Pooled AUROC | Per-task mean AUROC |
|--------|-------------:|--------------------:|
| Behavioral features | 0.562 | 0.556 |
| Step count | 0.537 | 0.535 |
| **Divergence score** | **0.533** | **0.507** |
| Random | 0.488 | 0.486 |

0.507 is a coin flip. Pooled is slightly better because large tasks dominate, but per-task the divergence signal is essentially noise on held-out data.

Features do better — a modest 0.056 above chance. That's "real but weak." Trajectory *shape* matters more than the exact branch choice.

**Takeaway:** The divergence signal that looks strong in-sample collapses on held-out data. If you're training on one task's divergence and applying to another, you've got nothing.

---

## 2. Does reranking with it work? (Slightly)

Second experiment: best-of-K selection. For each task, sample K=3 runs and pick the one with the best score. Compare to random selection and oracle (always pick a passing run if one exists).

| Method | Accuracy | Lift vs random |
|--------|---------:|---------------:|
| Features | 57.2% | +4.4pp |
| Uncertainty (inv) | 56.4% | +3.7pp |
| Divergence | 55.9% | +3.2pp |
| Random | 52.7% | — |
| **Oracle** | **85.9%** | **+33.2pp** |

Features capture 13% of the oracle gap. Divergence captures 10%. Both are real but neither is close to what a reward model or perplexity-based reranker would give you.

The more interesting number is the oracle gap itself. 33 points of potential lift are sitting in the data. Current methods capture a small slice. The rest is locked up in task-specific structure that doesn't generalize across families.

---

## 3. Where does it generalize? (The 25% with structure)

Here's where it gets interesting.

I computed "captured oracle gap" per task family and got a range from **-73% to +100%**. Some families benefit enormously from divergence-based scoring. Others get hurt. The aggregate mean of +10% is hiding the actual story.

So I built a per-task score called **structure** — three components, equal-weight:

- `branch_gap`: mean pass-rate spread at the top divergence points
- `earlyness`: how early in the trajectory those splits occur (early = more decisive)
- `stability`: how reproducible the divergence map is under run resampling

Kendall's tau between structure and divergence reranking lift: **+0.402** (p < 0.0001).

Split tasks at structure ≥ 0.20:

- **High-structure** (269 tasks, 25%): divergence scoring gives +12.5% reranking lift
- **Low-structure** (811 tasks, 75%): divergence scoring gives +0.4% lift

That's the whole story. In one quarter of the tasks, the signal is strong. In three quarters, it's noise-indistinguishable drift. Aggregating across both hides the fact that you have two regimes, not one.

**Takeaway:** Divergence-based analysis works on a minority of tasks with a detectable property: early, reproducible, outcome-correlated branching. For everything else, the runs look like samples from a diffuse distribution over successful paths.

---

## 4. Can you route between scoring methods? (Yes, modestly)

If you know structure per task, you can pick the right scoring strategy per task instead of globally:

| Strategy | Accuracy | Lift |
|----------|---------:|-----:|
| Random | 52.9% | — |
| Divergence (global) | 56.1% | +3.1pp |
| Features (global) | 57.3% | +4.4pp |
| **Conditional (struct ≥ 0.20)** | **59.2%** | **+6.3pp** |
| Oracle | 64.2% | +11.4pp |

Use divergence on high-structure tasks, features on low-structure tasks. Beats both global strategies by +2pp.

That's not a breakthrough. It's a routing rule over two heuristics that gets you closer to oracle. If you're already running features or a reranker, adding structure-based routing is a drop-in that nudges the number up. If you're not, this isn't enough to justify building the infrastructure.

**Takeaway:** Structure score is a **method router**. You use it to decide which existing scoring strategy to apply per task. It is not a standalone scorer.

---

## 5. Can you use structure to allocate eval budget? (No)

This is where the negative result gets interesting.

If some tasks have structure and some don't, intuition says: spend more eval runs on the structured ones. They should need more samples to characterize. Use the rest of your budget uniformly on low-structure tasks.

That's wrong, and it's wrong for a reason that took me a day to see.

Kendall's tau between structure score and [task volatility](https://en.wikipedia.org/wiki/Bernoulli_distribution) (`p(1-p)`): **-0.273** (p < 0.0001).

High-structure tasks *anti-correlate* with volatility. Why? Because structured tasks have decisive branch points — early decisions that lock in the outcome. That means pass rates cluster near 0% or 100%, which means low Bernoulli variance, which means *fewer* runs needed to characterize the rate, not more.

Simulate it. Three policies under fixed compute budget:

| Budget | Policy | MAE | P90 error | False signal rate |
|-------:|--------|----:|----------:|------------------:|
| 1.0 | n=1 | 1.1% | 2.3% | 12.9% |
| 2.0 | uniform | **0.8%** | **1.6%** | **2.4%** |
| 2.0 | structure-aware | 1.0% | 2.0% | 8.2% |
| 3.0 | uniform | **0.6%** | **1.3%** | **1.0%** |
| 3.0 | structure-aware | 1.0% | 2.0% | 8.3% |

Uniform wins at every budget ≥ 2.0. Structure-aware plateaus because it keeps spending compute on high-structure tasks that already have stable estimates.

**Takeaway:** Structure and volatility are orthogonal axes. Structure predicts *which scoring method works*. Volatility predicts *how much sampling you need*. They are not the same latent variable, even when your intuition insists they should be.

---

## 6. Can you extract DPO pairs from divergence? (No, and this one isn't new)

The original dream: at each divergence point, the better-outcome branch is the preferred response and the worse-outcome branch is the rejected response. Feed those pairs into DPO. Train a better agent for free.

There are two problems.

**Problem 1: the signal is too weak to justify the infrastructure.** AUROC 0.556 with features and 0.507 with raw divergence means any preference pair you extract has massive label noise. DPO is already fragile to label noise; pairs from this signal would train the model on mostly random distinctions.

**Problem 2: someone already tried this.** [SWE-Dev](https://arxiv.org/abs/2502.12904) explicitly tested preference learning (KTO, OREO) on SWE-bench trajectories and rejected it in favor of SFT on successful trajectories. All five public SWE-bench fine-tunes I looked at (SWE-Gym, SWE-Fixer, Lingma SWE-GPT, SWE-Smith, SWE-Dev) use SFT. [DeepSWE](https://arxiv.org/abs/2506.08902) is the exception and uses online GRPO, which is a different animal.

The structural reason it doesn't work: preference pairs extracted from trajectory divergence are conditioned on observed actions, not on the latent state of the repository/task. Two runs that took different actions at step 7 might have been in subtly different states (files opened, context accumulated, model hidden state) that the extracted pair completely ignores. You end up training on correlations that are confounded by invisible prefix state.

**Takeaway:** Don't extract DPO pairs from agent trace divergence on SWE-bench. The signal is too weak, the state-aliasing is severe, and the teams with the most resources and the most data have already tried and rejected it. SFT on successful trajectories remains the right move.

---

## What's left that's useful

After all six experiments, here's what survives:

1. **Structure score as a method router.** Useful if you're already running multiple scoring strategies and want to pick per task. +2-6pp over global strategy. Not a standalone product.

2. **Negative results that are actually useful.** "Divergence doesn't generalize" is a thing a lot of people assume without checking. "Structure score is a method router, not a variance router" is a mistake I almost made and several people I talked to independently proposed. Documenting them saves someone else three weeks.

3. **The discipline of held-out validation.** The in-sample results looked great. The held-out results killed most of the pipeline. If I had built the training loop first — as was my original plan — I would have spent weeks debugging an infrastructure problem that was actually a signal problem.

4. **moirai itself as a per-task debugging tool.** If you have traces and want to know where your runs diverge and which path worked, it works. On SWE-rebench v2, 77/1096 tasks surface strong claims like "wrote source → 85% success (13 runs) vs ran a command first → 0% success (3 runs)". That's not a product. It's a personal tool.

---

## Hard lessons from building this

Same section as the [last post](/posts/stop-testing-agents-like-deterministic-code). These are the things I wish someone had told me at the start.

### Prove signal before building infrastructure

My original plan was SFT → ORM → DPO with divergence-mined pairs, running on OpenHands eval infrastructure. Three stages of training, plus eval harness work. Six to eight weeks of build before the first result.

My advisor pushed back: "prove the signal first." I compressed the plan into two validation experiments — held-out prediction and reranking — and ran them in three days. The signal was weak. The entire training pipeline plan evaporated in 72 hours.

If I had skipped that step, I would have built the training loop, run it, gotten noisy results, and then spent weeks debugging "training instability" that was actually a signal-strength problem. Held-out validation is cheap. Training loops are not. Run the cheap experiment first.

### Family-conditional signals look universal in aggregate

The first round of analysis on eval-harness data showed strong behavioral patterns: edit-test alternation, specific motif sequences, etc. Then I stratified by task family. Everything disappeared. The "universal" patterns were family artifacts — certain families have certain shapes, and when those families dominate the dataset the pattern looks global.

This is [Simpson's paradox](https://en.wikipedia.org/wiki/Simpson%27s_paradox) in agent eval, and it's everywhere. Always stratify. If you can't stratify because your dataset is too small per family, you don't have enough data to draw the conclusion you want.

### Don't reuse one latent variable for two jobs

I had structure score working for method routing. I assumed it would also work for eval budget allocation — both "use this variable to make a per-task decision," same shape. Different physics.

Structure score measures *branching sensitivity*, which predicts which scoring function works best. Volatility measures *outcome uncertainty*, which predicts how much sampling you need. These are empirically anti-correlated on SWE-rebench. One latent variable can't do both jobs. Test each application on its own terms before assuming it transfers.

### Don't overclaim

The pull to frame a +2-6pp routing rule as a "control system for stochastic agents" or a "reasoning paradigm" is real, and it's killed every time I tested it against a serious reader. A routing rule is a routing rule. Name it that. The honest framing is easier to defend and easier to iterate on.

### Aggregate metrics hide the regimes

The headline number for divergence-based reranking was +3.2pp. The per-family captured oracle gap ranged from -73% to +100%. The aggregate hid the fact that I had two different problems on different subsets of the data. Once I saw the per-family distribution, everything else followed.

Any time you're computing an aggregate metric over a heterogeneous dataset, look at the distribution. Always. The mean is almost never the story.

---

## The point

Agent trace divergence contains signal. The signal is narrower, weaker, and more task-specific than the in-sample numbers suggest. On held-out data, raw divergence is a coin flip. Behavioral features recover a modest amount. Routing between scoring strategies by structure buys you another two points.

None of that justifies a preference-learning pipeline. SWE-bench teams have converged on SFT for a reason, and the reason is consistent with what I found.

If you're thinking about extracting training signal from multi-run agent traces, run the cheap experiments first. Held-out AUROC. Reranking lift. Per-family captured oracle gap. If those numbers are weak — and they probably will be — the expensive infrastructure won't save you.

Use the signal where it's real: method selection on the minority of tasks where the divergence is strong, decisive, and early. Treat everything else as drift.

---

## Try it yourself

The code for all six experiments is public:

**[github.com/orban/moirai](https://github.com/orban/moirai)** — Python, ~7k lines, 423 tests.

```bash
git clone https://github.com/orban/moirai.git
cd moirai
pip install -e .

# Run branch analysis on your own traces
moirai branch path/to/traces/ --html report.html --json report.json

# Reproduce the held-out study
moirai holdout path/to/traces/

# Reproduce the reranking experiment
moirai rerank path/to/traces/ --k 3

# Reproduce the structure score routing
python -m scripts.run_structure_routing path/to/traces/
```

The last script is locked with frozen parameters and an assertion on the output, so you can verify the headline number (`59.2%` conditional accuracy on SWE-rebench v2) hasn't drifted.

If you run this on your own multi-run data and find something I missed, I want to hear about it.

---

## Appendix: experimental details

### Data

- **Dataset:** [SWE-rebench v2](https://huggingface.co/datasets/nebius/SWE-rebench) from Nebius
- **Scale:** 1,096 tasks with mixed-outcome runs, 12,854 total runs, median 11 runs/task
- **Filter:** tasks with ≥3 runs and both pass and fail outcomes
- **Alignment:** Needleman-Wunsch at step-name granularity (e.g., `read(source)`, `edit(test_file)`)

### Holdout study

For each task with ≥6 runs, randomly split runs 50/50 into train/test (stratified by outcome). Find divergence points on train with `min_branch_size=2, q_threshold=0.5`. Score each test run by the signed sum of its step contributions at known divergence columns. Measure per-task AUROC via Mann-Whitney U. Aggregate as pooled AUROC across all test runs and as per-task mean AUROC.

Reported results are over 1 seed. Spot-checked with 3 seeds and deltas were within 0.01.

### Reranking study

For each task with ≥3 runs, sample K=3 runs without replacement. Score each with the method being evaluated. Pick the top-scored run. Record whether it passes. Repeat 500 times per task. Aggregate accuracy across tasks.

Confidence intervals via [Wilson score](https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval#Wilson_score_interval). Per-family captured oracle gap = (method_accuracy − random_accuracy) / (oracle_accuracy − random_accuracy).

### Structure score

For task `t`:

$$\text{structure}(t) = \frac{\text{branch\_gap} + \text{earlyness} + \text{stability}}{3}$$

- `branch_gap` = mean outcome spread across top-5 divergence points, range [0, 1]
- `earlyness` = 1 − mean position of top divergence points (normalized to trajectory length)
- `stability` = fraction of 20 subsamples (at 70% of runs) that recover at least one top-5 divergence column within 10% position tolerance

Threshold of 0.20 for "high structure" was picked by inspecting the bimodal distribution on a held-out slice, not optimized on the test set.

### Eval reliability simulation

For each task with ≥6 runs, treat the full run set as ground-truth pass rate. Simulate 2,000 evals per policy by sampling `k` runs with replacement from the ground-truth outcomes. Measure absolute error of estimated rate vs ground-truth and false signal rate between pairs of independent simulated evals (disagreement > 3pp).

Budgets tested: 1.0, 1.5, 2.0, 3.0 runs per task. Structure-aware policy spends 1 run on low-structure tasks and distributes the rest uniformly over high-structure tasks.

### Code

All experiments are in `moirai/analyze/` with a `run_*` script per experiment in `scripts/`. Everything is deterministic under fixed seed. Reproducibility assertions are in `scripts/run_structure_routing.py`.
