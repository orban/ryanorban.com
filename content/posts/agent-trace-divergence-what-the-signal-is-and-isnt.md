---
title: "What agent trace divergence actually tells you"
date: 2026-09-20
description: "Same agent, same task, different outcomes. Is there signal in the variability? I borrowed an alignment algorithm from bioinformatics to find out, then went to the literature and found four fields already working on it. Here's the compressed map."
math: true
---

You run your agent 30 times on the same task. 18 pass, 12 fail. The traces look different. They branch at different points, pick different tools, choose different files. The hypothesis everyone reaches for is:

*Those branch points are where the decisions matter. Find them, score them, turn them into training data.*

That's the dream. A self-generating preference signal from the variance you already have. Free DPO pairs. A causal handle on agent behavior. No labeling cost.

It is also, as far as I could find, assumed rather than tested. People reason from it, build on it, and propose it in conversation, but I could not find anyone who had run it end to end against held-out data with a control. That gap is the reason for this work.

I tested that hypothesis on [Nebius's SWE-rebench OpenHands trajectories](https://huggingface.co/datasets/nebius/SWE-rebench-openhands-trajectories): 12,854 runs across 1,096 mixed-outcome tasks, every one of them OpenHands v0.54.0 driving Qwen3-Coder-480B.

One agent, one scaffold, one config. That narrowness is the design rather than a limitation. When every run comes from the same setup, a within-task comparison has no architecture differences and no framework artifacts available to explain the outcome, so the only thing varying is the model's own sampling. I learned that the hard way: an earlier round of this work on a cross-agent corpus concluded that no universal behavioural predictors exist, and that conclusion was an artifact of comparing across 133 agent architectures rather than anything about agents. To run the experiments end to end I built a tool called [moirai](https://github.com/orban/moirai).

Most of it doesn't work the way you'd hope, and the parts that do are narrower than I expected.

The obvious escape hatch is that the data was inadequate, so I closed it. Spectrum-based fault localization has a metric for whether a set of runs can localize anything at all, called DDU, and it reads no outcome labels. I ported it to trajectories and ran it over 19,592 runs. Median 0.14, against 0.10 to 0.42 for the real-fault suites in the paper that introduced it. This corpus sits inside the range where the technique demonstrably works, and the runs are individually distinct rather than collapsed on top of each other. They are diagnosable. The signal still isn't there.

When the rebuilt detectors came back flat I went looking for who else had attacked this. Four fields have been working on versions of the problem, three of them for decades: multiple sequence alignment, spectrum-based fault localization, counterfactual off-policy evaluation, and process reward modelling. They don't cite each other, and none of them are indexed under "agent traces." The last section maps what each one gives you.

---

## The setup

Each task has multiple runs with mixed outcomes. Each run is a sequence of tool calls: `read(source)`, `search(grep_targeted)`, `edit(source)`, `test(pass)`, `bash(python)`, and so on.

To find divergence points, align the runs with [Needleman-Wunsch](https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm). At each column, group runs by the step they took. Test whether the branch predicts outcome with [Fisher's exact](https://en.wikipedia.org/wiki/Fisher%27s_exact_test), correct for multiple comparisons with [Benjamini-Hochberg](https://en.wikipedia.org/wiki/False_discovery_rate#Benjamini%E2%80%93Hochberg_procedure).

That gives you a list of statistically significant divergence points per task. Within-task, the signal looks real. The question is whether it generalizes, whether it's uniform across tasks, and whether you can do anything useful with it.

Six questions, six experiments.

---

## 1. Does divergence correlate with outcome? (No, and my first answer didn't count)

Split each task's runs into train/test halves. Find divergence points on train. Use them to score held-out test runs. Measure AUROC.

The first pass gave the divergence score 0.507 per-task, against 0.556 for behavioral features and 0.486 for random. I called 0.507 a coin flip and moved on. That was wrong, though not because the number was too low. It could not have come out any other way.

The detector gated branch points behind Fisher's exact plus Benjamini-Hochberg. At a median of 11 runs a 2-vs-9 split cannot clear significance after correction, so **812 of the 1,096 tasks returned no branch points at all**. With nothing to score, the scorer fell back to a constant, and a constant scorer lands on 0.500 by construction. "No signal" and "no detector" were emitting the same number and I had no way to tell them apart. The result was unfalsifiable as stated.

So I rebuilt the detector three times, each version changing exactly one thing: Ochiai suspiciousness from spectrum-based fault localization in place of Fisher; prefix-tree matching in place of column alignment; 165,820 content signatures in place of 13 step names. Ochiai is always defined, so the rebuilt matchers fit a model for 72–96% of tasks where the original fit one for none at all below 15 runs. The decision rule was fixed before I read any output.

| Detector | Best held-out AUROC | Verdict |
|---|---:|---|
| Original (Fisher + BH) | 0.507 | Unfalsifiable: 812/1,096 tasks scored by a constant |
| **Best of three rebuilds** | **0.532** | Below the pre-registered 0.55 bar |

Every cell ran a second time with pass/fail labels shuffled within task. The largest real-minus-shuffled gap across all 28 cells was **+0.052**. Finer signatures made things worse, not better: going from 13 step names to 165,820 content signatures shortens the mean shared prefix across a task's runs from 1.68 steps to 1.18, because resolution buys you nothing once runs stop agreeing almost immediately either way.

### Would more runs have fixed it?

The obvious objection is that a median of 11 runs per task is simply too few, and the fix is to collect more. That is testable, so I tested it. Every method was re-run at fixed budgets of 4, 6, 8, 11, 15 and 20 runs per task.

| Runs per task | 4 | 6 | 8 | 11 | 15 | 20 |
|---|---:|---:|---:|---:|---:|---:|
| Tasks in cell | 486 | 714 | 711 | 575 | 162 | 71 |
| Detection rate, original | 0.000 | 0.000 | 0.000 | 0.000 | 0.426 | 0.563 |
| Detection rate, Ochiai rebuild | 0.718 | 0.846 | 0.907 | 0.911 | 0.957 | 0.930 |
| Held-out AUROC, Ochiai rebuild | 0.514 | 0.525 | 0.523 | 0.517 | 0.522 | 0.530 |
| Margin over shuffled labels | +0.052 | +0.032 | +0.017 | +0.031 | +0.020 | +0.015 |

Three things to read off that. The original detector's detection rate is **exactly zero** through 11 runs per task, which turns the constant-scorer diagnosis from an inference into a measurement. The rebuild reaches 96% detection at 15 runs, so past that point there is no detection problem left to solve. And AUROC stays flat across the whole range. The margin over shuffled labels is the row shown here, which declines; the other three rebuilt methods wander in both directions, from -0.025 to +0.045, with no trend. Read across all four, the margin is indistinguishable from noise at every budget. The single best cell anywhere was 0.532, and it sits at the largest budget, which is exactly where the thinnest task counts are.

More runs fixed detection completely and did nothing for prediction. That is the answer to "just collect more data," at least across this range, and the trend gives no reason to expect 50 runs per task to read differently.

Task counts thin toward the right of the table, because fewer tasks have 20 runs to draw from. Treat the last two columns as weaker evidence than the first four.

Behavioral features are a separate measurement, within-task median splits with split-half validation rather than off-policy prediction of a held-out outcome, and the rebuild does not test them. Their 0.556 stands.

**Takeaway:** The detector was the problem. Fixing the detector did not produce a signal. That is a stronger negative result than the one I started with, because this one could have come out the other way.

---

## 2. Does reranking with it work? (Slightly)

Second experiment: best-of-K selection. For each task, sample K=3 runs and pick the one with the best score. Compare to random selection and oracle (always pick a passing run if one exists).

| Method | Accuracy | Lift vs random |
|--------|---------:|---------------:|
| Features | 57.2% | +4.4pp |
| Uncertainty (inv) | 56.4% | +3.7pp |
| Divergence | 55.9% | +3.2pp |
| Random | 52.7% | n/a |
| **Oracle** | **85.9%** | **+33.2pp** |

Features capture 13% of the oracle gap. Divergence captures 10%. Both are real but neither is close to what a reward model or perplexity-based reranker would give you.

The more interesting number is the oracle gap itself. 33 points of potential lift are sitting in the data. Current methods capture a small slice. The rest is locked up in task-specific structure that doesn't generalize across families.

---

## 3. Where does it generalize? (The 25% with structure)

Here's where it gets interesting.

I computed "captured oracle gap" per task family and got a range from **-73% to +100%**. Some families benefit enormously from divergence-based scoring. Others get hurt. The aggregate mean of +10% is hiding the actual story.

So I built a per-task score called **structure**, three components, equal-weight:

- `branch_gap`: mean pass-rate spread at the top divergence points
- `earlyness`: how early in the trajectory those splits occur (early = more decisive)
- `stability`: how reproducible the divergence map is under run resampling

Kendall's tau between structure and divergence reranking lift: **+0.402** (p < 0.0001).

Split tasks at structure ≥ 0.20:

- **High-structure** (269 tasks, 25%): divergence scoring gives +12.5% reranking lift
- **Low-structure** (827 tasks, 75%): divergence scoring gives +0.4% lift

That's the whole story. In one quarter of the tasks, the signal is strong. In three quarters, it's noise-indistinguishable drift. Aggregating across both hides the fact that you have two regimes, not one.

**One caveat.** All three components of the structure score (`branch_gap`, `earlyness`, `stability`) are computed *from* divergence points. The original detector found none for 812 of 1,096 tasks. This section splits the corpus into 269 high-structure and 827 low-structure tasks, and the original detector found no divergence points at all for 812 of them. Those 812 sit entirely inside the low bucket; no high-structure task has zero divergence points, and only 15 low-structure tasks have any. So "low structure" is, to within 15 tasks out of 827, a restatement of "the detector fired on nothing." Read this section as a statement about when the detector produces output, not about a latent property of the task. I have not re-run sections 3 through 5 against the rebuilt detectors, so treat the sign of these results as more reliable than their magnitude.

**Takeaway:** Divergence-based analysis produces output on a minority of tasks with a detectable property: early, reproducible, outcome-correlated branching. For everything else, the runs look like samples from a diffuse distribution over successful paths, or the detector simply had nothing to say, and I cannot fully separate those two cases.

---

## 4. Can you route between scoring methods? (Yes, modestly)

If you know structure per task, you can pick the right scoring strategy per task instead of globally:

| Strategy | Accuracy | Lift |
|----------|---------:|-----:|
| Random | 52.9% | n/a |
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

High-structure tasks *anti-correlate* with volatility. Why? Because structured tasks have decisive branch points: early decisions that lock in the outcome. That means pass rates cluster near 0% or 100%, which means low Bernoulli variance, which means *fewer* runs needed to characterize the rate, not more.

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

**Problem 1: the signal is too weak to justify the infrastructure.** The best detector I could build tops out at 0.532 held-out, under the 0.55 bar, with a largest real-minus-shuffled gap of +0.052. Any preference pair extracted at that level carries enormous label noise. DPO is already fragile to label noise; pairs from this signal would train the model on mostly random distinctions.

**Problem 2: the field already tried it and went the other way.** Every public SWE-bench fine-tune I looked at (SWE-Gym, SWE-Fixer, Lingma SWE-GPT, SWE-Smith, SWE-Dev) ships SFT on successful trajectories. [SWE-Dev](https://arxiv.org/abs/2506.07636) is the useful case, because they did not simply skip preference learning: they ran it. Their paper reports exploring rejection-sampling fine-tuning alongside KTO and OREO, and finds that "RFT brings the most significant performance improvement, while offline reinforcement learning (RL) methods -- KTO and OREO -- deliver marginal or task-specific gains." A team with more data than me tested the contrastive route on these trajectories and shipped the supervised one. [SWE-Gym](https://arxiv.org/abs/2412.21139) is the clearest case: rejection-sampling SFT on runs that passed, and mixing in on-policy self-generated trajectories *hurt* their numbers. Successful and failed rollouts aren't exchangeable training signal in aggregate. The problem is the approach, not the choice of divergence step.

The one prominent exception goes around the problem rather than through it. Agentica and Together AI's [DeepSWE-Preview](https://www.together.ai/blog/deepswe) trains Qwen3-32B with RL only, using a modified GRPO they call GRPO++, and reaches 42.2% Pass@1 on SWE-bench Verified and 59% with test-time scaling. Online RL never needs a preference pair mined from logs, because it generates its own on-policy signal. That's a different animal from what I was attempting, and it's the direction with momentum behind it.

Two 2026 papers show what the alternatives look like, and neither makes the comparison I was making. [SWE-Lego](https://arxiv.org/abs/2601.01426) stays SFT-only and adds step-level error masking: it excludes tokens tied to failing tool calls and failing tests from the loss, using per-step *outcome* as a cheap always-available label instead of trying to locate a decisive step statistically. No preference pairs at all. [Agentic-DPO](https://arxiv.org/abs/2607.10601) does use a contrastive objective, but builds its pairs *within* a single expert trajectory, contrasting the expert action against sampled plausible wrong actions at the same state, rather than pairing across independently sampled runs.

That last distinction is the one that matters, and it's the structural reason this doesn't work. Agentic-DPO holds the state fixed and varies the action, as do the process reward methods further down. I aligned separate runs and compared whatever actions happened to land in the same column, so the pairs are conditioned on observed actions rather than on the latent state of the repository and task. Two runs that diverged at step 7 may have been in quite different states already (files opened, context accumulated, model hidden state), and the extracted pair ignores all of it. You end up training on correlations confounded by invisible prefix state.

**Takeaway:** Don't extract DPO pairs from agent trace divergence on SWE-bench. The signal is too weak, the state-aliasing is severe, and every team with more data than me builds its contrastive pairs at a fixed state rather than across independent runs. SFT on successful trajectories remains the right move.

---


## What's left that's useful

After all six experiments, here's what survives:

1. **Structure score as a method router.** Useful if you're already running multiple scoring strategies and want to pick per task. +2-6pp over global strategy. Not a standalone product.

2. **Two assumptions worth testing before you build on them.** "Divergence generalizes across tasks" is widely assumed and rarely checked. "Structure score is a variance router" is a mistake I nearly made, and several people I described the work to proposed it independently. Both are cheap to test and expensive to assume.

3. **Held-out validation, plus a negative control.** The in-sample results looked great and the held-out results killed most of the pipeline, which is the version of this lesson I wrote down first. It isn't enough. My held-out number was 0.507 and it was unfalsifiable, because a broken detector and a genuinely absent signal both produce 0.500. What made the second answer real was the shuffled-label control: run every cell again with outcomes permuted within task, and see whether the gap survives. Held-out data tells you the signal doesn't transfer. A negative control tells you whether you were ever measuring anything.

4. **moirai itself as a per-task debugging tool.** If you have traces and want to know where your runs diverge and which path worked, it works. On this corpus, 77/1096 tasks surface strong claims like "wrote source → 85% success (13 runs) vs ran a command first → 0% success (3 runs)". That's not a product. It's a personal tool.

---

## Hard lessons from building this

Same section as the [last post](/posts/stop-testing-agents-like-deterministic-code). These are the things I wish someone had told me at the start.

### Prove signal before building infrastructure

My original plan was SFT → ORM → DPO with divergence-mined pairs, running on OpenHands eval infrastructure. Three stages of training, plus eval harness work, all of it before the first result.

My advisor pushed back: "prove the signal first." I compressed the plan into two validation experiments, held-out prediction and reranking. The signal was weak, and the training pipeline plan went with it.

If I had skipped that step, I would have built the training loop, run it, gotten noisy results, and then gone debugging "training instability" that was actually a signal-strength problem. Held-out validation is cheap. Training loops are not. Run the cheap experiment first.

### Family-conditional signals look universal in aggregate

The first round of analysis on eval-harness data showed strong behavioral patterns: edit-test alternation, specific motif sequences, etc. Then I stratified by task family. Everything disappeared. The "universal" patterns were family artifacts: certain families have certain shapes, and when those families dominate the dataset the pattern looks global.

This is [Simpson's paradox](https://en.wikipedia.org/wiki/Simpson%27s_paradox) in agent eval, and it's everywhere. Always stratify. If you can't stratify because your dataset is too small per family, you don't have enough data to draw the conclusion you want.

### Don't reuse one latent variable for two jobs

I had structure score working for method routing. I assumed it would also work for eval budget allocation, since both are "use this variable to make a per-task decision," the same shape. Different physics.

Structure score measures *branching sensitivity*, which predicts which scoring function works best. Volatility measures *outcome uncertainty*, which predicts how much sampling you need. These are empirically anti-correlated on SWE-rebench. One latent variable can't do both jobs. Test each application on its own terms before assuming it transfers.

### Don't overclaim

The pull to frame a +2-6pp routing rule as a "control system for stochastic agents" or a "reasoning paradigm" is real, and it's killed every time I tested it against a serious reader. A routing rule is a routing rule. Name it that. The honest framing is easier to defend and easier to iterate on.

### Aggregate metrics hide the regimes

The headline number for divergence-based reranking was +3.2pp. The per-family captured oracle gap ranged from -73% to +100%. The aggregate hid the fact that I had two different problems on different subsets of the data. Once I saw the per-family distribution, everything else followed.

Any time you're computing an aggregate metric over a heterogeneous dataset, look at the distribution. Always. The mean is almost never the story.

---

## The prior art, compressed

Given many runs of one stochastic agent on one task, some passing and some failing, find the step that made the difference. Several fields have been working on that question under other names. Here is each of them, what it gives you, and where it stops.

### Alignment: partial order, not pairwise

Needleman-Wunsch is pairwise and global. It forces a set of runs into a single linear column structure, which is precisely wrong for trajectories that branch and never reconverge. [Partial order alignment](https://doi.org/10.1093/bioinformatics/18.3.452) (Lee, Grasso & Sharlow, *Bioinformatics* 18(3):452–464, 2002) keeps the alignment as a DAG instead of collapsing it into a linear profile, which is what you want for branching histories. Profile HMMs are the softer version of the same move: assign runs to latent branch states probabilistically instead of committing to one discrete column.

I owe you my own counterevidence here, because I already tested a version of this. Rung 2 of the rebuild replaced column alignment with a prefix tree for exactly the reason POA exists. My note in the script at the time: "Global alignment aliases states. NW can align step i of run A to step j of run B when their histories differ entirely, so a 'divergence column' pools runs that are in different states. A prefix tree cannot do this: at a node every run shares a byte-identical history." That is the same structural move, a strict one, and it bought nothing. The prefix-tree rungs reached 0.532 and 0.524 against 0.530 for plain alignment.

There is a reason to think POA would not rescue it either. A DAG helps when runs share substantial structure and diverge at identifiable points. On this corpus the mean shared prefix is between one and two steps, so there is almost no agreement for a graph to represent before the runs scatter. Better alignment cannot manufacture structure that the runs do not have.

I could not find anyone who has applied multiple sequence alignment to LLM agent trajectories, and the bioinformatics methods are twenty-plus years old and well understood, so the application does look open. Go in knowing that the obvious first version of it has been tried here and did not work.

### Detection: diagnosability, not significance

I reached for Ochiai on instinct once Fisher failed. The instinct was right and the literature is well ahead of it. Spectrum-based fault localization has spent twenty years on exactly "which component is implicated when some runs pass and some fail," through Tarantula, Ochiai, DStar and Barinel.

The result that reframes my failure is Perez, Abreu & van Deursen's [test-suite diagnosability metric](https://doi.org/10.1109/ICSE.2017.66) (ICSE 2017, 654–664). Their argument is that coverage is the wrong thing to optimize for diagnosis. What matters is the structure of the coverage matrix: how densely runs touch components, how many distinct activity patterns appear across runs, and how many components are distinguishable from one another at all. They combine those three into a metric called DDU, computable from the matrix alone with no pass/fail labels. Generating suites to maximize DDU instead of branch coverage cut diagnosis effort by an average of 34% across 186 real faults in Defects4J.

It is worth knowing this is contested ground rather than settled: [FDG](https://arxiv.org/abs/2104.06641) argues that scoring a suite without using the outcomes a test would produce leaves value on the table, and [RLFDC](https://arxiv.org/abs/2501.02216) reports beating DDU on the same benchmarks.

So I ran it on my own data. `moirai diagnosability` builds the activity matrix from traces instead of coverage, with runs as rows and step signatures as components, and computes the three terms. Over 1,737 mixed-outcome tasks with at least four runs each, 19,592 runs in total:

| | step-name alphabet | step+target alphabet |
|---|---:|---:|
| Median DDU | 0.141 | 0.145 |
| Density | 0.358 | 0.501 |
| Diversity | 0.879 | 1.000 |
| Uniqueness | 0.438 | 0.331 |
| Tasks below 0.10 | 25.8% | 23.9% |

I expected this to come back low and explain everything. It didn't. A median of 0.14 is inside the band their Defects4J suites occupied, and diversity, the term I assumed had collapsed, is the strongest of the three: at the finer alphabet every single run has a distinct activity pattern. Whatever is wrong here, it isn't that the runs are too few or too alike.

The weak term is uniqueness, at 0.33 to 0.44. Components keep getting touched together, so a large share of them sit in ambiguity groups where nothing distinguishes one from another. That is a real limit, and it is a limit on telling *components* apart rather than on telling *runs* apart. Two caveats worth carrying: my filter takes every mixed-outcome task with four or more runs and yields 1,737 tasks where the published analysis used 1,096, so the corpora are not identical even though mean runs per task lands at 11.3 against a published median of 11. And DDU was validated as a test-suite generation objective, not as a go/no-go gate, so treat 0.14 as "comparable to suites that localize successfully" and not as a passing grade.

[SBEST](https://arxiv.org/abs/2405.00565) is the precedent for what to do instead: when the failing signal is too scarce for statistics to mean anything, stop doing statistics on it and substitute a structural signal.

The instinct is in the air, too. [Who is Introducing the Failure?](https://arxiv.org/abs/2509.13782) applies SBFL-style spectrum analysis to attributing failures in multi-agent systems. It does not solve my problem, since attributing a failure across *agents within one system* is a different question from predicting an outcome across *independent runs of one agent*, but it is a sign that fault localization is the frame this family of questions keeps converging on.

### Causality: the prefix-state problem

This is the deepest of the four.

Comparing the action taken at aligned step *k* across two runs assumes those runs were in equivalent states at step *k*. Nothing in the alignment checks that. [Namkoong et al.](https://arxiv.org/abs/2003.05623) put it directly: off-policy evaluation for sequential decisions routinely assumes no unobserved confounding, that assumption is usually false, and it is usually unstated. Mine was unstated.

The formal tool is [Oberst & Sontag's Gumbel-Max structural causal models](https://arxiv.org/abs/1905.05824), which construct counterfactual trajectories in a POMDP and identify which episodes would genuinely have gone differently. [COMA](https://arxiv.org/abs/1705.08926) is the same idea in multi-agent RL: marginalize one action while holding the others fixed, against a learned counterfactual baseline. My column-wise Fisher test was a crude approximation of that baseline with no state model behind it.

Honest caveat: none of these is a drop-in fix. They need a POMDP or SCM model of agent state that OpenHands logs don't give you. You'd have to build a state abstraction first. That's a real obstacle, not a citation I can hand you.

### Budget: sequential, not fixed

Experiment 5 asked how to spend a fixed number of eval runs across tasks, and found that uniform allocation beat my structure-aware policy at every budget. That's the right conclusion from the wrong frame: I was choosing between two *fixed* allocations decided up front.

The better framing is sequential. [Knowing When to Stop](https://arxiv.org/abs/2608.14425) (Pilditch, August 2026) treats it as Bayesian optimal stopping, with a hierarchical model that allocates sampling budget dynamically from current uncertainty and stops per task when the estimate is good enough, rather than committing to a per-task count in advance. That is the correct shape for "how many times should I run this," and it subsumes the uniform-vs-weighted question I was actually asking.

This one postdates the work here by four months, so I could not have missed it. It is where I would start now.

### Credit assignment: roll forward, don't align back

[Math-Shepherd](https://arxiv.org/abs/2312.08935) is the one to reach for. Rather than asking which of two observed actions was better, it resumes many rollouts from each intermediate state and scores that state by the fraction of completions that succeed. Step-level labels from outcome-only supervision, no human annotation. [OmegaPRM](https://arxiv.org/abs/2406.06592) is the MCTS version, roughly 75× more label-efficient. Both descend from [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050), which established that process supervision beats outcome supervision when you can get it.

[RTMC](https://arxiv.org/abs/2604.11037) is the cheapest version of the idea: aggregate return statistics across rollouts that share a common state to get per-step advantages, with no learned critic at all. That's much closer to something you could run over existing data, provided the runs genuinely share states, which is the assumption my whole approach needed and never checked.

The catch is the part that matters if you're planning this work. Math-Shepherd needs to *resume execution from an intermediate agent state and sample forward*. My 12,854 runs are post-hoc logs, not resumable checkpoints. So this is a different data collection design rather than a better analysis of the data I had, and a more expensive one.

Which puts the real lesson upstream of the analysis: if you want step-level signal, build for resumable rollouts *before* you collect anything. Aligning logs afterwards is trying to recover information the collection design already threw away.

---

## The point

Agent trace divergence, detected this way, does not predict outcome. Three rebuilt detectors topped out at 0.532 against a pre-registered bar of 0.55, with a largest real-minus-shuffled gap of +0.052 across 28 cells. Behavioral features are a different measurement and recover a modest amount. Routing between scoring strategies by structure buys another two points, on the subset where the detector produces output at all.

None of that justifies a preference-learning pipeline. SWE-bench teams have converged on SFT for a reason, and the reason is consistent with what I found.

The deeper problem wasn't the detector, though rebuilding it three times is how I learned that. Comparing actions at an aligned column across independently sampled runs assumes those runs were in the same state, and nothing in the method establishes that. Every team getting contrastive signal out of agent trajectories holds state fixed and varies the action instead.

So if you're thinking about extracting training signal from multi-run agent traces: run the cheap experiments first, and run a negative control alongside them, because a broken detector and an absent signal return the same number.

And start from the map above rather than from an aligner. The alignment people don't cite the fault-localization people, and neither cite the off-policy-evaluation people, so the useful version of this problem sits spread across fields that don't read each other.

And before committing compute, measure whether your run set can answer the question at all. `moirai diagnosability` does it over traces without reading a single outcome label. A low score means you have a data problem and none of the log-mining methods here will rescue you. A score in range, which is what I got, means the question was fair and the answer is genuinely no. That second outcome is the more valuable one, and it is the one a negative result cannot give you on its own.

---

## Try it yourself

The code for all six experiments is public:

**[github.com/orban/moirai](https://github.com/orban/moirai)**: Python, ~10.5k lines, 423 tests.

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

# Score whether your own runs can support any of this. Reads no outcome labels.
moirai diagnosability path/to/traces/ --min-runs 4
```

The last script is locked with frozen parameters and an assertion on the output, so you can verify the headline number hasn't drifted. The measured value is 59.19% conditional accuracy; the assertion in the script is written against `0.593` with a tolerance of 0.01.

If you run this on your own multi-run data and find something I missed, I want to hear about it.

---

## Appendix: experimental details

### Data

- **Dataset:** [nebius/SWE-rebench-openhands-trajectories](https://huggingface.co/datasets/nebius/SWE-rebench-openhands-trajectories) (CC-BY-4.0)
- **Agent:** OpenHands v0.54.0 with Qwen3-Coder-480B, single scaffold and config throughout
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
