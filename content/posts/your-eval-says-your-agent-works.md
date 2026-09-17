---
title: "Your eval says your agent works. Production disagrees."
date: 2026-04-16
description: "Single-run evals don't measure reliability. They sample it."
math: false
draft: true
---

**Your agent passed the eval. It shipped. Three days later it started failing in production.**

The eval ran once. It got lucky.

---

## Same task. 30 runs. 18 pass.

I ran one SWE-rebench v2 task 30 times. Same model, same prompt, same environment.

18 passed. 12 failed.

**Single-run evals don't measure reliability. They sample it.**

A 95% single-run score is consistent with two completely different agents:

- **Agent A** solves 95% with near-certainty, fails 5% reliably.
- **Agent B** solves 30% with certainty, coin-flips the other 65%.

Same headline. Different products.

Your users will figure out which one you shipped.

---

## The variance comes from one early decision

Across runs of the same task, outcomes usually collapse to a single early move.

```
Opened test file first    → 94% pass   (17 runs)
Edited source first       →  0% pass   (4 runs)
```

The first move locks in the outcome. Everything after is consequence.

Run it once and you don't know which path the agent took. Your eval gives you the outcome of the die roll, not the bias of the die.

This is common.

<!-- chart goes here: per-task pass-rate histogram — spikes at 0% and 100%, long tail in the middle -->

---

## Your users will hit the failure path

They don't run a task once. They run it repeatedly, or they hit sibling tasks with the same hidden branch. The 0% path lands on someone eventually.

Every team I talk to hits the same wall: eval numbers hold, production reliability tanks. They blame distribution shift. Usually the eval number was never what they thought it was.

---

## What to do

**If you're not doing this, your number is wrong.**

**Run every eval task N times.** N=10 separates 100% from 80%. N=30 tightens the middle.

**Report the distribution, not the mean.** Show how many tasks sit at 100%, at 0%, and in between. The middle is your production risk. Watch it like p99 latency.

**Stratify by task family.** A "73% on SWE-bench" that's 95% on one family and 40% on another lied through aggregation. If production skews toward the 40% family, you shipped the 40% agent.

---

## How I do it

I built [moirai](https://github.com/orban/moirai) to surface these divergence points across runs.

It outputs things like:

---

```
path A → 94% pass
path B →  0% pass
```

---

## If you run it once, you don't know if your agent works.

---
