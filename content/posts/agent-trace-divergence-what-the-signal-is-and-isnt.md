---
title: "Eleven ways to score an agent trajectory"
date: 2026-09-25
description: "Same agent, same task, different seed, different outcome. I tried eleven ways to find what separates the passing runs from the failing ones, five of them reimplemented from published papers. They all land within five points of each other, and most of what looks like signal turns out to be task difficulty."
math: true
---

You run the same coding agent on the same task twenty times. Same model, same scaffold, same config, same prompt. Eleven pass, nine fail. Nothing differs between those runs except the sampling seed.

So something in the traces separates the winners from the losers. Find it and you get step-level credit assignment out of variance you already paid for: no human labels, no reward model, no extra rollouts. Free preference pairs.

I spent a while testing that on 12,854 OpenHands runs across 1,096 SWE-rebench tasks, and then longer testing whether my way of testing it was any good.

The short version. Eleven ways of representing a trajectory, five of them reimplemented from published papers, all land between 0.528 and 0.581 held-out AUROC on the same corpus under the same protocol. When I dropped the filter that restricts analysis to mixed-outcome tasks, held-out AUROC jumped to 0.690 and the label-permutation control jumped to 0.681. Ninety-eight percent of that apparent signal was a model learning which tasks are hard.

The permutation floor is the part worth stealing. The rest is why I believe it.

## The number that wasn't a result

The first detector aligned runs with [Needleman-Wunsch](https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm) over a 13-symbol alphabet of step names, grouped runs by what they did at each column, and tested whether the branch predicted outcome with [Fisher's exact](https://en.wikipedia.org/wiki/Fisher%27s_exact_test), corrected across columns by [Benjamini-Hochberg](https://en.wikipedia.org/wiki/False_discovery_rate#Benjamini%E2%80%93Hochberg_procedure).

Held-out AUROC: 0.507.

I read that as a negative result for months. It isn't one. At a median of 11 runs per task, a 2-versus-9 split can't clear significance after correcting across every column, so **812 of the 1,096 tasks returned no branch points at all**. With nothing to score, the scorer falls back to a constant, and a constant scorer lands on exactly 0.500 because ties contribute 0.5 to the Mann-Whitney statistic.

"No signal" and "no detector" were emitting the same number. That's the first thing worth carrying: if your pipeline can produce a degenerate scorer, measure how often it does before interpreting the aggregate.

## Rebuilding the detector

Spectrum-based fault localization has used Ochiai as a *ranking* statistic since the mid-2000s, and a ranking statistic is always defined. So I built a ladder, each rung changing exactly one thing, with a decision rule written down before I looked at any output.

| rung | change | held-out AUROC |
|---|---|---:|
| M0 | NW on step names, Fisher + BH | 0.507 |
| M1 | same matching, Ochiai instead of the gate | 0.523 |
| M2 | prefix tree on names, Ochiai | 0.504 |
| M3 | prefix tree on content signatures, shrinkage | 0.501 |
| M4 | Markov-2 state, Ochiai | 0.554 |
| M5 | Markov-2 on content, shrinkage | 0.545 |

Every cell ran twice, once real and once with pass/fail labels shuffled within task. The shuffled arms sit between 0.487 and 0.502 at full budget, so the estimator isn't leaking. M0 reproduces 0.507 exactly, which is the regression check that the harness measures the same thing the original did. The pre-registered threshold was 0.60 and nothing reached it.

The interesting rung is M2. Replacing column alignment with a prefix tree was supposed to be the principled fix, because global alignment aliases states: Needleman-Wunsch will happily align step *i* of run A to step *j* of run B when their histories differ completely, so a "divergence column" pools runs that are in different situations. A prefix tree can't do that, since every run at a node shares a byte-identical history.

It scored 0.504, worse than the crude column model it was meant to repair.

## It was never the statistic

That sent me to look at the representation instead of the scoring, and the sweep is where the real finding lives. Corpus, protocol and control held fixed, varying only how a trajectory gets encoded:

| encoding | components | held-out AUROC |
|---|---:|---:|
| step name, last action only | 12 | 0.559 |
| step name, last two actions | 56 | 0.554 |
| step name, last three actions | 134 | 0.554 |
| step name, full history | 332 | 0.504 |
| name + file target, last action | 106 | 0.571 |
| name + file target, full history | 337 | 0.502 |
| **file paths hashed into 26 arbitrary buckets** | 26 | **0.578** |

Two things fall out. Full history is broken and everything else is equivalent, which kills the Markov-2 story I'd been building since M4 scored highest. And hashing file paths into 26 meaningless buckets beats every alphabet I designed on purpose.

When a random coarsening outperforms deliberate design, the design was contributing nothing. That's a useful thing to learn about your own feature engineering, and you don't learn it by staring at the features.

## Generating a vocabulary instead of choosing one

Statistical debugging solved this in 2005 and I'd been reinventing the problem badly. Liblit, Naik, Zheng, Aiken and Jordan's [Scalable Statistical Bug Isolation](https://doi.org/10.1145/1065010.1065014) stops picking predicates. Templates emit everything the program admits, and the outcome labels prune the set. On Rhythmbox: **857,384 predicates, cut to 537 by keeping only those whose 95% confidence interval on Increase(P) sits above zero, then to 15 by redundancy elimination.**

Their statistic is what transfers:

$$\text{Context}(P) = \frac{F(P\ \text{observed})}{S(P\ \text{observed}) + F(P\ \text{observed})}$$

$$\text{Increase}(P) = \text{Failure}(P) - \text{Context}(P)$$

Context is a counterfactual baseline. A run that has thrown five tracebacks by step 30 is doomed whatever it does next, so every predicate true at that point scores high on raw failure rate. Liblit calls those innocent bystanders. Subtracting the failure probability of merely *reaching* the state removes them.

This matters here specifically, because the prefix-state problem is the deepest objection to the whole approach: comparing what two runs did at aligned step *k* assumes they were in equivalent states at *k*, and nothing in the alignment checks that. The causal literature says fixing it properly needs a state model. It turns out you can approximate it with subtraction, and the approximation is twenty years old.

So I generated instead of choosing: command head tokens, path tokens, file extensions, action counts at five thresholds, adjacent action pairs, ordered before-and-after pairs, step and file and error count thresholds, re-read and edit-without-read. 3,596 predicates over the corpus, 93 surviving the confidence interval, scored on entirely held-out tasks.

**0.5768**, against a shuffled arm at 0.4922.

### The bug that made it look better than it was

The first version scored 0.5483, and these were the top predicates:

```
+0.474  tok:executionresult     +0.461  tok:python__gql__
+0.487  tok:basehttpmiddleware  +0.440  tok:apsw
```

Those are repository names. `apsw` and `python__gql__` identify *which task* the run belongs to, not anything the agent did. The shuffled arm selected the same token families, which is the tell: shuffling permutes labels within task, so a task-constant predicate has an identical failure rate in both arms and sails through the test untouched.

Worse, they contribute nothing to the evaluation. AUROC is computed within each held-out task, and a predicate true for every run of that task adds the same constant to every score and cancels. Roughly 190 of my 200 selected predicates were inert padding.

I'd selected on corpus-level variance and evaluated on within-task variance. Liblit doesn't hit this because his setting is one program, with no between-task dimension to confound. Stratifying the selection so a predicate only accumulates evidence from tasks where it actually varies moved the number to 0.5768 and left behavioral predicates on top.

That's Simpson's paradox inside a pipeline whose author had already written "always stratify" in his own notes.

## Five published representations, one protocol

At that point I'd tried six encodings I made up. The obvious missing comparison is against encodings somebody else published and validated. Four are specified precisely enough to reimplement and need nothing my logs lack:

- **Bigram TF-IDF**, 30k features, min_df 2, sublinear term frequency, L2 logistic regression with class-balanced weights. The configuration that reaches task-disjoint AUROC 0.83 on tau2-bench in [From Confident Closing to Silent Failure](https://arxiv.org/abs/2606.09863).
- **Byte-pair encoding over action sequences** at K=192, where [Agent trajectories as programs](https://arxiv.org/abs/2606.16988) reports its V-measure plateauing at 0.644.
- **Action crossed with environment response**, the enriched encoding from [Beyond Resolution Rates](https://arxiv.org/abs/2604.02547) that distinguishes a clean edit from a syntax error from a re-patch.
- **Canonical-path Jaccard**, where the reference is the set of steps appearing in more than half of a task's successful runs, from [Capable but Unreliable](https://arxiv.org/abs/2602.19008).

All under one protocol: tasks split in half, everything fit on the train half, AUROC computed within each held-out task and averaged, shuffled arm permuting outcomes within task.

| representation | origin | real | shuffled | margin |
|---|---|---:|---:|---:|
| bigram TF-IDF, class-balanced | arXiv:2606.09863 | **0.5813** | 0.5146 | +0.067 |
| per-state FSM features | arXiv:2608.23670 | 0.5783 | 0.5044 | +0.074 |
| hashed path buckets, k=26 | this work | 0.5780 | 0.4820 | +0.096 |
| generated predicates, Increase(P) | Liblit 2005 | 0.5768 | 0.4922 | +0.085 |
| unigram TF-IDF | this work | 0.5727 | 0.5070 | +0.066 |
| canonical Jaccard, rich alphabet | arXiv:2602.19008 | 0.5632 | 0.4822 | +0.081 |
| BPE vocabulary, K=192 | arXiv:2606.16988 | 0.5607 | 0.5018 | +0.059 |
| action × outcome bigrams | arXiv:2604.02547 | 0.5603 | 0.5125 | +0.048 |
| step name, last-action state | this work | 0.5590 | 0.5040 | +0.055 |
| canonical Jaccard, 13 symbols | arXiv:2602.19008 | 0.5280 | 0.5079 | +0.020 |
| full-history prefix tree | this work | 0.5040 | 0.4960 | +0.008 |

Learned vocabularies, bags of words, spectrum statistics, counterfactual baselines, finite state machines. A span of five points, and the winner is a bag of bigrams over raw trajectory text.

Two caveats I'd want if I were reading this. The canonical-Jaccard rows are approximate: their shuffled arm sits below chance because leave-one-out is asymmetric across labels, and equalizing the reference size fixed most of that but not all. And canonical adherence reads the outcomes of a task's *other* runs, so it isn't a deployable predictor the way the rest are.

Canonical Jaccard also shows why cardinality matters. On the 13-symbol alphabet it scores 0.528; on name-plus-target it scores 0.563. Every run touches about eleven of the thirteen step names, so a set comparison over that alphabet has nothing to vary over. Their benchmark has a rich tool vocabulary. Mine doesn't.

## The floor

Every experiment above restricts to mixed-outcome tasks, where the same agent both passes and fails. That's deliberate: if a task always passes or always fails, there's no within-task contrast to find a divergence point in.

I wanted to know what the filter was worth, so I rebuilt the corpus from the raw parquet, which holds 6,225 tasks with at least four runs, of which 1,737 are mixed-outcome and 4,488 always produce the same outcome. Then I scored both populations under an 80/20 split over runs with pooled AUROC, which is the shape most published evaluations use.

| population | features | real | shuffled | margin |
|---|---|---:|---:|---:|
| all 6,225 tasks | structural | 0.6897 | **0.6808** | +0.009 |
| all 6,225 tasks | trace length only | 0.6629 | 0.6616 | +0.001 |
| 1,737 mixed-outcome | structural | 0.6229 | 0.5619 | +0.061 |
| 1,737 mixed-outcome | trace length only | 0.5826 | 0.5633 | +0.019 |

Drop the filter and AUROC climbs from 0.58 to 0.690. The permutation control climbs to 0.681. With 4,488 always-same-outcome tasks in the pool, a model learns "this task always fails," and permuting labels *within* task leaves that untouched because each task's success count is preserved.

So: report your permutation floor. Raw held-out AUROC on an agent-trajectory corpus is dominated by task difficulty, and the gap between a method that works and a method that memorizes which repositories are hard is invisible in the headline number and obvious in the control. It costs one extra run of the same pipeline.

## The prior art, compressed

While I was doing this, several groups published on versions of the same question. Here's what each gives you and where it stops. The most useful thing I can hand over is a distinction that took me far too long to see.

### Three different questions get reported as one

**Between-model variation.** Why does one agent beat another? [Beyond Resolution Rates](https://arxiv.org/abs/2604.02547) covers 9,374 trajectories across 19 agents, 8 frameworks and 14 LLMs on 500 tasks. Agents delaying their first edit succeed more (ρ = +0.68), agents front-loading patches in the first ten steps succeed less (ρ = −0.78), validation effort correlates with resolution (ρ = +0.50). Those are correlations across 19 agents, not run-level predictions. The paper also reports that agents sharing an LLM agree on 85–93% of tasks regardless of framework, while agents sharing a framework but not an LLM agree on 47–88%. Behavior is mostly the model.

**Between-task variation.** Why is this task harder? Large, and it contaminates any pooled metric, as measured above: 0.690 against a 0.681 floor.

**Within-model, within-task sampling variation.** Same agent, same task, same config, different seed. This is the question everyone means, and it's the small residual left after the other two. The paper that isolates it cleanly is [Capable but Unreliable](https://arxiv.org/abs/2602.19008): 22 models on 108 tasks at 3 runs each, restricted to the 22.5% of model-task units with mixed outcomes, measuring Jaccard adherence to a canonical tool set defined by successful runs. They report +0.060 Jaccard (p < 0.0001, 95% CI [+0.043, +0.077]), worth +5.3 percentage points of success probability, Cohen's *d* = 0.48. That's roughly 0.63 AUROC-equivalent against my 0.578.

They also ship an intervention, which is the strongest practical result in this literature: a monitor flagging bottom-tercile adherence at 75% completion lifts success by +8.8 points among intervened runs.

Once you separate those three, most of the impressive numbers in this space are measuring the first two. If you're planning to mine step-level signal from sampling variance specifically, budget for an effect around *d* = 0.5 and design accordingly.

### The methods that work best need data your logs don't have

[OAT](https://arxiv.org/abs/2607.12747) trains neural controlled differential equations on successful trajectories only and scores each step of a failure by reconstruction error. Its step vector is "the aggregated token representations produced by layer ℓ when generating action a_t," mean-pooled and projected to 64 dimensions. That's an LLM hidden state, which post-hoc logs don't contain. The absolute numbers are modest too: in-domain F1 0.435 against 0.181 for a GPT-5 judge, out-of-distribution F1 0.211. The win is cost, 16ms against 38 seconds.

[Math-Shepherd](https://arxiv.org/abs/2312.08935) and [OmegaPRM](https://arxiv.org/abs/2406.06592) are the right answer to credit assignment and need something logs don't have either. Rather than asking which of two observed actions was better, they resume many rollouts from each intermediate state and score that state by the fraction of completions that succeed. OmegaPRM is the MCTS version, using binary search to find the first error in a chain of thought, and collected over 1.5 million process annotations with no human in the loop, lifting Gemini Pro from 51% to 69.4% on MATH500. Both descend from [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050), which established that process supervision beats outcome supervision and released 800,000 human step labels to prove it.

The catch is resumability. My runs are post-hoc logs, not checkpoints you can fork from. That makes this a different data collection design rather than a better analysis of data I already had.

[RTMC](https://arxiv.org/abs/2604.11037) is the cheapest version and the closest to runnable on existing data: aggregate return statistics across rollouts sharing a common state to produce per-step Q-values and advantages with no learned critic at all, for +3.2 points of pass@1 over GRPO on SWE-bench Verified. It needs runs that genuinely share states, which is the assumption this whole approach rests on and the one I never checked.

### Order doesn't help, found twice independently

Capable but Unreliable's limitations section reports that their sequence metrics performed worse than set-based Jaccard. Independently, my full-history prefix trees score 0.504 against 0.55 to 0.58 for every order-insensitive or bounded-history encoding.

Two corpora, two methods, same conclusion: the sequence structure of an agent trajectory carries less than the multiset of things it did. Worth knowing before you build an alignment algorithm.

### There's a blind window between cause and evidence

[Failure as a Process](https://arxiv.org/abs/2607.09510) hand-annotated 63,000 execution steps across 3,843 trajectories from seven models and three scaffolds on Terminal-Bench. Failures are epistemic 57.9% of the time, competence 32.8%, environment 9.4%. The decisive error lands at a **median of step 7** in runs whose median length is 27, and observable failure signals emerge about **10 steps later**.

[When Evidence is Sparse](https://arxiv.org/abs/2606.05414) arrives from the other direction, learning turn-level failure signal from trajectory-level labels via attention. High-relevance turns are 4.7–11.3% of turns, and most failure-indicating evidence appears after 59–84% of the trajectory has elapsed.

So the cause lands around a quarter of the way in and becomes visible around three quarters of the way in. That predicts what I measured: truncating traces to their first 25% moves AUROC from 0.578 to 0.558, barely at all, because the decisive error has already happened and hasn't left a mark yet. It also explains why every spectrum method underperforms here. They weight all steps equally when one step in ten carries anything.

### Alignment: partial order, not pairwise

Needleman-Wunsch reduces a multiple alignment to a linear profile at each step, losing information and introducing gap-scoring artifacts. [Partial order alignment](https://doi.org/10.1093/bioinformatics/18.3.452) (Lee, Grasso & Sharlow, *Bioinformatics* 18(3):452–464, 2002) keeps the alignment as a directed acyclic graph instead, which is the right shape for histories that branch and never reconverge.

I owe you counterevidence, because the prefix-tree rungs above are a strict version of the same move and they bought nothing. Given the order result, I'd now expect POA to underperform a bag of actions on this data too.

### Detection: diagnosability, and why I wouldn't lead with it

Perez, Abreu and van Deursen's [test-suite diagnosability metric](https://doi.org/10.1109/ICSE.2017.66) (ICSE 2017) argues that coverage is the wrong thing to optimize for diagnosis. What matters is the structure of the coverage matrix: how densely runs touch components, how many distinct activity patterns appear, how many components are distinguishable at all. DDU multiplies those three terms, needs no pass/fail labels, and runs before you spend any compute. Generating suites to maximize DDU instead of branch coverage cut diagnosis effort by 34% on average across 186 real Defects4J faults.

I ported it, ran it over 19,592 runs, got a median of 0.14, and spent a day drawing conclusions from that number. Three things went wrong, and all three are instructive.

First, I read their Table III as a range that real-fault suites occupy. It isn't. **0.10 is the median DDU of suites generated without optimizing for diagnosability, and 0.42 is the median when EvoSuite optimizes for it.** Those are the before and after of an intervention. Sitting at 0.14 means sitting next to the arm they measured as diagnostically worse in 77% of scenarios.

Second, DDU is a function of the component alphabet, and I fed it the alphabets I already suspected were bad. Over the same runs it reads 0.008 for full-history prefix nodes, 0.130 for last-action states, and 0.523 for a two-step context. A 65-fold swing from changing nothing but the definition of "same state."

Third, and worst: those differences don't predict downstream performance. The 0.523 encoding and the 0.130 encoding deliver 0.554 and 0.559 AUROC. Identical. DDU told me one was four times more diagnosable than the other and it made no difference at all.

DDU also can't tell you whether a signal exists, by construction. It reads no outcome labels, which is what makes it cheap and what makes it blind to whether the outcome depends on the trajectory at all. A run set can be beautifully structured for localizing a fault that isn't there.

This is contested ground, which is worth knowing. [FDG](https://arxiv.org/abs/2104.06641) argues that no existing metric uses the suspiciousness scores of individual program elements *during* localization, even though those scores say where more information is needed, and reports 11.6× acc@1 and 2.2× acc@10 from augmenting suites its way. [RLFDC](https://arxiv.org/abs/2501.02216) goes further and learns the measurement rather than designing it, treating fault localization results as reward signals. Given that DDU predicted nothing downstream for me, learning the metric from downstream feedback looks like the right instinct.

Two more from this family. [SBEST](https://arxiv.org/abs/2405.00565) handles the case where the failing signal is too scarce for statistics by substituting a structural one, and it's worth being precise about which: stack traces from crash reports. Only 3.33% of their 60 Defects4J crash bugs had fault-triggering tests, but 98.3% of fixes addressed the exception in the trace, for +32.22% MAP. A failing coding-agent run has no exception pointing at the fault, so this doesn't transfer. [Who is Introducing the Failure?](https://arxiv.org/abs/2509.13782) is the first spectrum-based failure attribution for multi-agent systems, which is a different question: attributing failure across agents within one system rather than across independent runs of one agent.

### Causality: the prefix-state problem

Comparing the action at aligned step *k* across two runs assumes those runs were in equivalent states. [Namkoong et al.](https://arxiv.org/abs/2003.05623) put it directly: off-policy evaluation for sequential decisions routinely assumes no unobserved confounding, that assumption is usually false, and it's usually unstated. Mine was unstated. They derive worst-case bounds and show that even minimal per-decision confounding creates substantial bias.

The formal tools are [Oberst & Sontag's Gumbel-Max structural causal models](https://arxiv.org/abs/1905.05824), which construct counterfactual trajectories in a POMDP and identify which episodes would genuinely have gone differently, and [COMA](https://arxiv.org/abs/1705.08926), which does the same in multi-agent RL by marginalizing out a single agent's action while holding the others fixed against a learned counterfactual baseline.

Both need a state model you'd have to build. Liblit's Increase(P) is the cheap approximation that needs nothing, and the agent-trace literature isn't using it. If you take one implementable idea from this section, take that one.

### Vocabulary: the axis nobody varies

Every experiment here except the last few holds the alphabet fixed without saying so, and so does most of the agent-trace literature. [Automata from Agent Traces](https://arxiv.org/abs/2608.23670) collapses a trace corpus into a finite state machine of 7 to 43 states over alphabets of 6 to 42 symbols, replays held-out data at ≥0.997 fitness, and reports failure-prediction AUROC up to 0.94 across twelve datasets, with 0.80 on SWE-agent against 0.659 for trace length alone. Its state, by their Theorem 3, is the last activity performed. Its abstraction step is manual activity typing. [ATLAS](https://arxiv.org/abs/2608.14352) uses an LLM to generate semantic labels and learns labelled Markov chains with Alergia, lifting a 14B model from 1.7% to 38.3% on a penetration-testing benchmark through knowledge transfer.

The exception is [Agent trajectories as programs](https://arxiv.org/abs/2606.16988), which induces the vocabulary with byte-pair encoding over action sequences, merging frequently co-occurring adjacent actions and stopping by V-measure at K=192. It identifies which of ten agents produced an unseen trajectory at 85.7% accuracy against an 11.1% random baseline.

Learning the abstraction alphabet and the model together is where the hole is. On this corpus it may not matter, since BPE at the size its authors validated scores 0.5607 and arbitrary hash buckets score 0.5780. But that's one corpus with a 13-symbol base alphabet, and the answer could differ where the action space is richer.

### What the field did about preference pairs

The specific version of the dream in my opening, mining DPO pairs from divergence points, has been tried by people with more data than me.

[SWE-Dev](https://arxiv.org/abs/2506.07636) is the clearest case because they ran the comparison rather than skipping it: "We observe that RFT brings the most significant performance improvement, while offline reinforcement learning (RL) methods—KTO and OREO—deliver marginal or task-specific gains." With 2,300 rejection-sampling trajectories they reach a 21.2% resolve rate, against 17.2% for KTO and 17.0% for OREO at 1,800.

[SWE-Gym](https://arxiv.org/abs/2412.21139) is more nuanced than I'd assumed, and I had it backwards for a while. Their verifier ablation finds that "training with a mixture of off-policy and on-policy data yields the best results," reaching 27@8, while off-policy alone plateaus around 22%. Mixing helps. What's modest is self-improvement: two rounds of rejection-sampling fine-tuning moved their 7B from 7.0% to 10.0% and their 32B from 19.0% to 19.7% with no further gains.

[Agentic-DPO](https://arxiv.org/abs/2607.10601) shows what the preference-pair idea looks like done correctly, and the difference is the one that matters. At each expert action state it samples a one-step action from *that state*, treats plausible wrong actions as negatives, and contrasts them with the expert action. State fixed, action varied. A 9B model goes from 21.7% to 41.4% on τ-bench retail. I aligned separate runs and compared whatever actions happened to land in the same column, so my pairs were conditioned on observed actions rather than on shared state. That's the structural reason it doesn't work, and it sits upstream of every detector choice in this piece.

[SWE-Lego](https://arxiv.org/abs/2601.01426) takes the cheap route: stay supervised and mask tokens tied to failing tool calls and failing tests out of the loss, using per-step outcome as an always-available label instead of locating a decisive step statistically. [DeepSWE](https://www.together.ai/blog/deepswe) goes around the problem entirely, training Qwen3-32B with a modified GRPO and reaching 42.2% Pass@1 on SWE-bench Verified averaged over 16 runs, 59% with test-time scaling. Online RL never needs a preference pair mined from logs, because it generates its own on policy.

### Budget: sequential, not fixed

One more, because it subsumes a question I'd asked badly. I'd been choosing between fixed allocations of eval budget decided up front. [Knowing When to Stop](https://arxiv.org/abs/2608.14425) treats it as Bayesian optimal stopping with a hierarchical model, sampling where uncertainty is high and stopping where estimates are stable, and removes 57% to 97% of planned trials across nine validation settings with conclusions equivalent to the full run.

## What I'd do differently

**Run the permutation control first.** It costs one extra pass and it invalidated a result I'd otherwise have published. If your held-out metric and your label-permuted metric move together, you're measuring the data's structure rather than your method.

**Stratify selection at the level you evaluate at.** Choosing features on pooled data and scoring within task puts repository names in your model and hides them behind a plausible number.

**Check whether a degenerate scorer is possible.** A constant predictor scores exactly 0.500, which looks like a finding.

**Don't infer adequacy from a label-free metric.** DDU is cheap and worth running. It told me three different things this week and none of them predicted downstream performance.

**Design for resumability before you collect.** Every method that genuinely assigns step-level credit needs to fork execution from an intermediate state. Aligning logs afterward tries to recover information the collection design already discarded.

The honest summary: on one agent, one scaffold and one config, what a coding agent's trajectory tells you about whether it will resolve the issue tops out around 0.58 AUROC, and eleven ways of asking agree. That ceiling is a property of pure sampling variance. Between-model and between-task variation are much larger, which is why the literature's numbers look better than mine, and why they're answering a different question than the one you're probably asking.

## Try it yourself

```bash
git clone https://github.com/orban/moirai.git && cd moirai
uv sync

# the ablation ladder, M0 through M5, with shuffled controls
python scripts/exp_matching_ablation.py <traces>/ --out ablation.json

# generated predicate vocabulary with Liblit's Increase(P)
python scripts/exp_predicate_vocabulary.py <traces>/ --out predicates.json

# the four published representations, head to head
python scripts/exp_published_representations.py <traces>/ --out published.json

# how much of your AUROC survives label permutation
python scripts/exp_mixed_outcome_filter.py trajectories.parquet --out floor.json
```

Every script prints a shuffled arm beside every real number. If they move together, stop.

## Appendix: experimental details

### Data

- **Dataset:** [nebius/SWE-rebench-openhands-trajectories](https://huggingface.co/datasets/nebius/SWE-rebench-openhands-trajectories) (CC-BY-4.0)
- **Agent:** OpenHands with Qwen3-Coder-480B, one scaffold and one config throughout. Variation across runs is sampling only.
- **Scale:** 1,096 tasks with mixed-outcome runs, 12,854 total runs, median 11 runs/task
- **Filter:** tasks with at least 4 runs and both outcomes present
- **Unfiltered population:** 6,225 tasks with at least 4 runs, of which 1,737 are mixed-outcome and 4,488 always produce the same outcome

### Protocol

Tasks are split in half. Vocabularies, feature selection and model fitting happen on the train tasks only. AUROC is computed within each held-out task via Mann-Whitney U and averaged across tasks, which keeps task difficulty out of the ranking. Ties contribute 0.5, so a constant scorer lands on exactly 0.500.

Every configuration runs twice, once with real outcomes and once with outcomes permuted within task. Within-task permutation preserves each task's success count, so it removes label dependence while leaving task difficulty intact. That's what makes it the right null here.

### The ablation ladder

Budgets of 4, 6, 8, 11, 15 and 20 runs per task plus "all," sampled without replacement. Within each task, runs split 50/50 into train and test, the model fits on train, and held-out runs are scored. Pre-registered decision rule, fixed before any output: every rung at or below 0.55 at every budget means the negative result stands; any rung rising with budget and clearing 0.60 at n ≥ 15 means the original conclusion was a power artifact. M4 peaked at 0.585 with 15 runs per task over 162 tasks, which didn't clear it.

### Predicate generation

Templates emit predicates as (site, condition) pairs so Context(P) stays a counterfactual baseline rather than collapsing to the global failure rate. A predicate is retained when its support is at least 20 train runs and the lower bound of the 95% normal-approximation interval on Increase(P) is strictly above zero. Importance is the harmonic mean of Increase(P) and a log-scaled failure count, per Liblit. Redundancy elimination then ranks by importance, removes the top predicate along with every run where it holds, and repeats.

Counts accumulate only from tasks where the predicate varies. Without that stratification the selection fills with repository names, as described above.

### Diagnosability

DDU over trajectories with runs as rows and step signatures as components, following Perez et al.:

$$\text{DDU} = \rho' \times G \times U, \qquad \rho' = 1 - |1 - 2\rho|$$

where ρ is matrix density with an ideal of 0.5, *G* is Gini-Simpson diversity over distinct activity rows, and *U* is distinct columns over total components. No outcome labels are read. Measured over 1,737 tasks and 19,592 runs from the raw parquet: median 0.141 at step-name granularity, 0.145 at step-plus-target.

### Reproduction notes

`pyarrow` and `datasets` are needed for the parquet path and aren't yet declared in the project's dependencies. The converted corpus on disk was pre-filtered to mixed-outcome tasks before any of this work started, which is why the floor experiment reads the raw parquet directly.
