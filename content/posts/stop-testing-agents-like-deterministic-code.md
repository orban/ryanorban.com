---
title: "Stop Testing AI Agents Like Deterministic Code"
date: 2026-03-26
description: "Your AI agent CI is a coin flip and you don't know it. Here's how to test stochastic systems like an adult."
math: true
---

Most teams I work with are trying to retrofit CI/CD pipelines built for deterministic software onto systems that aren't deterministic at all.

They build an agent — it calls an LLM, uses tools, makes decisions — and then test it the same way they'd test a REST endpoint:

`assert(agent(input) === expected_output)`

Green. Ship. Next day it's red. Nobody changed anything. Rerun. Green again.

"Flaky test." Move on.

But it's not flaky. It's stochastic. And the objection I hear most often is: "It's just matrix multiplication — how is it not deterministic?" In practice, batch sizing, floating-point accumulation order, speculative decoding, and tool calls all introduce variation. The same prompt won't produce identical output 100% of the time, even at temperature 0.

So what do you do? You stop asserting and start sampling. You treat the agent as the stochastic process it actually is, apply hypothesis testing, and gate on statistical evidence instead of exact matches. And with SPRT, you can do it without burning your entire trial budget every time.

---

## The problem with `assert`

When you write `assert(f(x) === y)`, you're claiming this function always returns this value for this input. That makes sense for `parseInt("42")`. It does not make sense for a system that queries a language model.

Some things around an agent are still deterministic. "The process didn't crash." "The output is valid JSON." "The schema parsed." Hard-assert those.

The problem is using the same pattern for things that are inherently probabilistic: output quality, task success, rubric adherence, correctness under ambiguity.

For those, each run is basically a Bernoulli trial. The agent either produces a satisfactory result or it doesn't, with some unknown success rate $p$. That rate isn't truly fixed across all tasks and conditions, but it's a useful model.

Now the ugly part. Suppose your agent really does succeed 90% of the time. That sounds good enough to ship. You have 10 tests, each run once. What's the probability CI comes back perfectly clean?

$$P(\text{all 10 pass}) = 0.9^{10} = 0.349$$

So even with a 90% success rate, you still have a **65% chance of at least one failure**.

Not because the agent is broken. Because you ran 10 Bernoulli trials and expected deterministic behavior.

That's the bug. Not the agent. The test harness.

And yes, this assumes independence. Real failures often cluster because tests share failure modes. That changes the shape, not the conclusion. Deterministic assertions on stochastic behavior still give you garbage.

Run those 10 tests twice each and it gets worse. Now you're at 20 trials. Probability of at least one failure jumps to 87%.

The more coverage you add, the more "flaky" your suite becomes. Not because you're testing better. Because you're using the wrong testing model.

<iframe src="/embeds/flaky-ci-probability.html" style="width:100%;height:440px;border:none;overflow:hidden;" loading="lazy"></iframe>

## The reframe: this is hypothesis testing

Once you stop treating agent evals like assertions and start treating them like experiments, the path gets obvious.

The real question is not:

"Did this exact run pass?"

It's:

"Is this agent reliable enough?"

That's a hypothesis test.

You don't accept a batch of parts by testing one and declaring the factory good or bad. You sample, measure a rate, and decide whether the rate meets spec. Agent testing is the same problem.

- **Null hypothesis $H_0$:** the agent meets the target pass rate, say $p \ge 0.90$
- **Alternative $H_1$:** it's materially worse, say $p < 0.80$

That 0.90 to 0.80 gap is your indifference zone. Borderline systems need more evidence.

## Use SPRT, not one-shot CI theater

The dumb but already-better version is fixed-$N$: run the contract 50 times, estimate the rate, do a binomial test, gate on that.

Fine. Already better than `assert`.

But fixed-$N$ wastes money. If the answer is obvious after 10 runs, forcing 50 is just lighting tokens on fire.

That's what SPRT is for.

The Sequential Probability Ratio Test updates evidence after every trial and asks: do we already know enough to decide?

If an agent passes 12/12, you probably don't need 38 more runs to know it's likely above a 90% threshold. If it faceplants immediately, you don't need to keep paying to watch it drown.

After each trial, update the log-likelihood ratio:

$$\text{pass: } \Lambda \mathrel{+}= \log(p_0 / p_1)$$

$$\text{fail: } \Lambda \mathrel{+}= \log((1-p_0)/(1-p_1))$$

Where $p_0$ is your acceptable rate, say 0.90, and $p_1$ is your unacceptable rate, say 0.80.

SPRT formally compares two simple hypotheses, $p = p_0$ vs $p = p_1$, not the full composite claim you actually care about. In practice you pick $p_1$ as a clearly bad rate below your threshold and test between those two points. That's standard and works well.

Think of it like a factory inspection. You can't directly test the claim "this factory produces good parts at least 90% of the time" — that's an infinite family of possibilities. What you can test is: "Does this factory look more like one that produces 90% good parts, or one that produces 80% good parts?" If the factory is actually producing at 96%, it'll look like the 90% factory even faster — the test accepts sooner, and the approximation is conservative in your favor. The only place it gets fuzzy is when the true rate is between the two points (the indifference zone), which is exactly where you'd want more data anyway.

Then compare against two boundaries:

- **Accept:** $\Lambda \ge \log((1-\alpha)/\beta)$
- **Reject:** $\Lambda \le \log(\alpha/(1-\beta))$
- **Otherwise:** keep going

With typical values $\alpha = 0.05$, $\beta = 0.20$, the upper boundary is about 1.56 and the lower is about -2.77.

The nominal error bounds are slightly conservative because the log-likelihood ratio moves in discrete jumps and can overshoot the boundary. Fine. That helps you.

Concrete example. Suppose the true pass rate is 95% and your threshold is 90%:

```text
Trial 1:  pass → logLR = +0.118
Trial 2:  pass → logLR = +0.235
Trial 3:  pass → logLR = +0.353
...
Trial 14: pass → logLR = +1.649 → ACCEPT
```

14 trials instead of 50.

Now suppose the agent actually sucks, say 60% success:

```text
Trial 1:  pass → logLR = +0.118
Trial 2:  fail → logLR = -0.575
Trial 3:  fail → logLR = -1.268
Trial 4:  pass → logLR = -1.150
Trial 5:  fail → logLR = -1.843
Trial 6:  fail → logLR = -2.536
Trial 7:  fail → logLR = -3.229 → REJECT
```

Seven trials. Done.

<iframe src="/embeds/sprt-random-walk.html" style="width:100%;height:400px;border:none;overflow:hidden;" loading="lazy"></iframe>

That's the whole point. SPRT is not just more statistically sane. It's a cost-control mechanism.

For clearly good or clearly bad agents, it often cuts trial count by 60-80%.

Caveat: SPRT assumes the pass rate is stationary during the run. If your eval drags on for hours and the provider updates the model halfway through, your guarantees get mushy. Keep runs short enough that the underlying system is effectively stable.

## Confidence intervals that aren't lying to you

You also want to see uncertainty, not just a pass/fail badge.

A 90% pass rate from 10 runs and a 90% pass rate from 100 runs are not the same thing.

The naive interval, $\hat{p} \pm z\sqrt{\hat{p}(1-\hat{p})/n}$, breaks badly near the edges. If you go 10/10, it gives you [1.0, 1.0], which is obviously nonsense.

Use Wilson intervals instead:

$$\text{center} = \frac{\hat{p} + z^2/2n}{1 + z^2/n}$$

$$\text{spread} = \frac{z \sqrt{\hat{p}(1-\hat{p})/n + z^2/4n^2}}{1 + z^2/n}$$

For 10/10 at 95% confidence, Wilson gives roughly [0.72, 1.00]. That's much more honest. You saw all passes, but the sample is small.

That's exactly the behavior you want: more skepticism when data is thin, convergence as $n$ grows.

<iframe src="/embeds/wilson-vs-naive-ci.html" style="width:100%;height:380px;border:none;overflow:hidden;" loading="lazy"></iframe>

One caveat: if the run stopped early via SPRT, Wilson intervals are descriptive, not strict post-stopping inference. Fine for dashboards. Don't pretend they're something more.

## Multiple testing will quietly wreck you

Now suppose you have 10 contracts, each with false rejection rate $\alpha = 0.05$. Even if each one is individually controlled, the chance of at least one spurious rejection across the suite grows fast:

$$P(\geq 1 \text{ false rejection}) = 1 - (1-0.05)^{10} \approx 0.40$$

So now you've got up to a **40% chance of a bogus red build**.

That's not a corner case. That's what happens when you pile multiple tests onto the same stochastic system and ignore family-wise error.

If you care about controlling the probability of any false rejection, use Bonferroni. It's conservative, but simple.

If you care more about overall discovery power and can tolerate a controlled fraction of false rejections, use Benjamini-Hochberg.

<iframe src="/embeds/bh-procedure.html" style="width:100%;height:400px;border:none;overflow:hidden;" loading="lazy"></iframe>

BH is usually the better tradeoff for larger suites, but it assumes independence or certain positive dependence structures. If your contracts are highly correlated, and many are, the guarantees get softer. Then you may want Benjamini-Yekutieli or a more conservative correction.

Point is: if you have one contract, whatever. If you have 15, this matters.

## What agent CI should actually do

A sane CI pipeline for agents should have three outcomes:

| Exit code | Meaning |
|-----------|---------|
| 0 | PASS — enough evidence the agent meets threshold |
| 1 | FAIL — enough evidence it does not |
| 3 | INCONCLUSIVE — max trials hit, evidence still ambiguous |

That last one matters. "Inconclusive" is not weakness. It's the honest answer.

Treating inconclusive as fail is a policy choice. Conservative, but costly. Treating it as pass is reckless.

Your config should specify reliability targets, not fantasy-world exact matches:

```yaml
studies:
  - name: my-agent-quality
    scenario: scenarios/task.yaml
    contracts:
      - name: exits-cleanly
        type: code
        assert: "output.meta.exitCode === 0"
        threshold: 0.95
        confidence: 0.95
        trials: 50

      - name: response-is-valid-json
        type: code
        assert: "output.meta.jsonParsed === true"
        threshold: 0.90
        confidence: 0.95
        trials: 50
```

That says: this behavior needs to succeed often enough, with enough evidence, not literally every single time forever.

And yes, threshold choice depends on product reality, not vibes. Deterministic-ish properties like valid JSON or clean exit can live around 0.95-0.99. Subjective or hard tasks may belong lower. If the product tolerates a 15% miss rate, stop pretending the eval threshold should be 0.99.

Persist every run. Trendlines are more informative than single snapshots. If observed rates drift down or inconclusives rise, that tells you something real.

## The cost math is not subtle

Let's say you have 5 contracts, max 50 trials each.

At &#36;1/trial, fixed-$N$ costs:

$$5 \times 50 \times \$1 = \$250 \text{ per CI run}$$

If SPRT stops around 14 trials on a clearly passing agent:

$$5 \times 14 \times \$1 = \$70 \text{ per CI run}$$

That's a 72% cost reduction.

At &#36;5/trial, the savings are enormous. And real agentic workflows can absolutely get there once you include tool use, code execution, and longer rollouts.

This is not just cleaner stats. It's fewer wasted tokens, faster feedback, and a smaller bill.

## Hard lessons from building eval harnesses

The math helps, but it won't save you from bad experimental design.

### Single runs tell you almost nothing

Early on, we compared baseline vs treatment with one run each and pretended the delta meant something. It didn't.

A task that passed once under baseline would fail the next three times. A treatment that looked worse in one run could easily end up better over five.

Temperature 0 does not magically fix this. API-level nondeterminism still exists. If you are using temperature 0 as an excuse not to repeat runs, you are fooling yourself.

Run repetitions. Report intervals. Use paired tests.

### You need a real failure taxonomy

We initially excluded timeouts from the denominator as "infra errors." That was wrong and inflated success rates.

If the agent was actively working and then ran out of time, that is a real failure under the operational budget you gave it.

We ended up with something like:

| Error tag | Meaning | Count in success rate? |
|-----------|---------|------------------------|
| none | normal pass/fail trial | Yes |
| `[timeout]` with tool calls | agent ran out of time while working | Yes, as failure |
| `[infrastructure]` | Docker crash, network issue | No |
| `[pre-validation]` | broken test before agent acted | No |
| `[empty-run]` | agent returned immediately, did nothing | No |

Timeouts are technically censoring, not pure failure, but in CI they often function as failure because wall-clock budget is part of the product constraint.

Also, report both per-protocol and full-pipeline reliability when you can. Those are different questions.

### Separate setup cost from experimental cost

If your treatment adds docs or context before the actual task, don't lump setup token cost into the fix attempt and then act like the treatment is intrinsically worse.

Measure setup separately from the thing you're actually trying to compare.

Same for no-op runs. If the agent does nothing and instantly returns, that should be detected and classified, not silently counted as a normal task attempt.

### Use paired tests when the data is paired

If baseline and treatment are run on the same task under the same conditions, use a paired test. McNemar is often the right choice for binary outcomes.

Looking at raw success rates without a paired test is how people talk themselves into fake conclusions.

CI overlap is not a substitute. It's a visual aid at best.

### At scale, all of this compounds

Once runs cost real time and real money, statistical sloppiness stops being academic. It turns into delayed feedback, bogus regressions, blown budgets, and bad product calls.

## The point

Stop pretending agent evals are deterministic software tests with slightly annoying noise around the edges.

They are not.

They are statistical quality-control problems wrapped around stochastic systems.

If you keep using exact-match assertions for probabilistic behavior, your CI will keep alternating between false confidence and random humiliation.

Use hard assertions for deterministic properties.

Use statistical tests for stochastic ones.

Track rates, not anecdotes. Use sequential testing. Report uncertainty. Correct for multiple contracts. Classify failures properly.

Test the system you actually built, not the fantasy version that only exists in a clean demo run.

## Try it yourself

If you want to put this into practice, the code behind these ideas is a reference implementation you can read end-to-end:

**[github.com/orban/cerberus](https://github.com/orban/cerberus)** — 1,600 lines of TypeScript, 80 tests.

```bash
git clone https://github.com/orban/cerberus.git
cd cerberus
npm install && npm run build

# Initialize a starter config
npx cerberus init

# Run the test suite
npx cerberus run
```

The implementation is deliberately minimal — 9 source files, 4 runtime dependencies — so you can read the code and understand every decision. See the [README](https://github.com/orban/cerberus) for a file-by-file map of which concepts live where.

---

## Appendix: the math

### SPRT

For Bernoulli observations with null $p_0$ and alternative $p_1$:

**Log-likelihood update**

$$\Lambda_n = \Lambda_{n-1} + \begin{cases} \log(p_0/p_1) & \text{if pass} \\ \log((1-p_0)/(1-p_1)) & \text{if fail} \end{cases}$$

**Wald boundaries**

$$A = \frac{1-\alpha}{\beta}, \quad B = \frac{\alpha}{1-\beta}$$

**Decision rule**

$$\begin{cases} \text{Accept } H_0 & \text{if } \Lambda_n \ge \log(A) \\ \text{Reject } H_0 & \text{if } \Lambda_n \le \log(B) \\ \text{Continue} & \text{otherwise} \end{cases}$$

Where $\alpha$ is the false rejection rate and $\beta$ is the false acceptance rate.

The usual practical mapping is:

- $p_0 =$ threshold
- $p_1 =$ a clearly worse rate below threshold
- $\alpha = 1 -$ confidence
- $\beta \approx 0.20$

SPRT is optimal in expected sample size among tests with the same error guarantees. That's the whole reason to use it.

### Wilson interval

For $k$ successes in $n$ trials:

$$\text{center} = \frac{\hat{p} + \frac{z^2}{2n}}{1 + \frac{z^2}{n}}$$

$$\text{spread} = \frac{z \sqrt{\frac{\hat{p}(1-\hat{p})}{n} + \frac{z^2}{4n^2}}}{1 + \frac{z^2}{n}}$$

$$CI = [\text{center} - \text{spread},\; \text{center} + \text{spread}]$$

Where $\hat{p} = k/n$ and $z = \Phi^{-1}(1-\alpha/2)$.

Use Wilson, not the naive normal approximation, especially for small $n$ or edge cases like 0/10 and 10/10.

### Benjamini-Hochberg

Given ordered p-values $p_1 \le p_2 \le \ldots \le p_m$:

1. Find the largest $k$ such that $p_k \le \frac{k}{m}\alpha$
2. Reject all hypotheses up to $k$

Bonferroni controls the chance of any false rejection and is more conservative. BH controls expected false discovery rate and is usually less wasteful.

Pick the correction that matches the actual failure mode you care about.
