---
title: "feat: Publish the trace-divergence essay and resolve the claims that block it"
date: 2026-09-25
type: feat
depth: standard
status: u1-u3 approved for merge; u4 gated on author revision
origin: none (solo invocation, no upstream brainstorm)
decided: 2026-09-25
---

# feat: Publish the trace-divergence essay and resolve the claims that block it

## Summary

`content/posts/agent-trace-divergence-what-the-signal-is-and-isnt.md` is a finished 2,790-word essay that has sat at `draft: true` since its `date:` of 2026-04-08. Publishing it is three lines of mechanical work and one editorial decision that only Ryan can make.

The mechanical part: three finished branches need to land first, because one of them retires a homepage claim the essay contradicts. The editorial part: the essay's central number was subsequently retracted by Ryan himself, in a correction that is itself sitting unmerged on one of those branches.

**This plan cannot be executed end-to-end without a decision from Ryan.** Units U1–U3 are unblocked and can land immediately. U4 (the actual publication) is gated on Open Question OQ1.

---

## Problem Frame

Public `/posts/` contains exactly two essays. The last one published is dated 2026-04-04 — nearly six months stale. The strongest unpublished artifact on disk is the trace-divergence essay: six experiments, four negative results, a pre-registered bar, reproduction commands, and a full appendix.

Three things stand between it and production.

**1. A homepage claim the essay refutes.** `layouts/partials/record/data.html` on `master` describes Moirai as exporting "the survivors as **preference data**" and carries a headline metric `"Preference pairs" "11,006"`. The essay's section 6 concludes: *"Don't extract DPO pairs from agent trace divergence on SWE-bench."* `copy/built-section` fixes the prose but leaves the metric.

**2. Three finished branches never merged.** All four branches (including this session's `seo/homepage-title`) are independent off `master` — none is stacked on another.

| Branch | Base | Real files touched | What it does |
|---|---|---|---|
| `copy/record-thesis` | `6f52677597` | `content/about.md` | States results plainly; adds independent-research row |
| `copy/built-section` | `6f52677597` | `baseof.html`, `home.html`, `index.llms.txt`, `data.html`, `audit_homepage.py` | Renames "Building now" → "Built"; removes the preference-data prose |
| `copy/ablation-correction` | `d0e86908ed` | 10 files incl. `what-stochastic-variation-reveals.md`, both validators | Retires the preference-pair claim; retires `/advising/` + `/office-hours/` |
| `seo/homepage-title` | `d0e86908ed` | `head.html`, `audit_homepage.py` | Homepage `<title>` descriptor (this session) |

**3. The essay's headline number was already retracted.** See OQ1 — this is the blocker.

### Correction to the initiating brief

The brief flagged `copy/built-section` as carrying "hundreds of changed `static/sfevents/**` files" as a merge hazard. **That is wrong and no plan work should be spent on it.** Verified: `git diff <merge-base>..<branch> --name-only -- static/sfevents` returns zero files for all four branches. The churn appears only in `master..branch` diffs because `copy/record-thesis` and `copy/built-section` branch from `6f52677597`, which predates master's two sfevents refresh commits (`d1a5e346ea`, `d0e86908ed`). A three-way merge keeps master's newer snapshot. There is no sfevents hazard.

---

## Requirements

- **R1.** The trace-divergence essay is published at `/posts/agent-trace-divergence-what-the-signal-is-and-isnt/` and reachable from `/posts/`.
- **R2.** No page on the site asserts that preference-pair extraction from divergence works. This includes prose *and* numeric metrics.
- **R3.** The site does not present two mutually inconsistent accounts of the same held-out AUROC result.
- **R4.** `scripts/audit_homepage.py` passes (baseline: 24/24 on `seo/homepage-title`).
- **R5.** `scripts/validate_site.py --public <build> --url-manifest scripts/baselines/public-urls.txt` passes (baseline: 7 passed / 0 failures).
- **R6.** The merge to `master` is an explicit human decision, not a pipeline step.
- **R7.** No word of the essay body is changed by an agent. Wording concerns are reported, never applied.

---

## Open Questions

### OQ1 — BLOCKING. The essay's central number is one Ryan already retracted.

The essay rests its case on per-task held-out AUROC:

- Line 41: `| **Divergence score** | **0.533** | **0.507** |`
- Line 44: *"0.507 is a coin flip … the divergence signal is essentially noise on held-out data."*
- Line 149: *"AUROC 0.556 with features and 0.507 with raw divergence means any preference pair you extract has massive label noise."*
- Line 211: *"On held-out data, raw divergence is a coin flip."*

`copy/ablation-correction` adds this to `what-stochastic-variation-reveals.md`, dated September 2026:

> Held-out per-task AUROC came back at 0.507 — a coin flip. **That number was unfalsifiable as stated**, because the pipeline gates branch points behind Fisher's exact plus Benjamini-Hochberg, and at a median of 11 runs a 2-vs-9 split can't clear significance after correction. 812 of the 1,096 tasks returned no branch points at all, the scorer fell back to a constant, and a constant scorer lands on 0.500 by construction. "No signal" and "no detector" were indistinguishable.

The essay's *conclusion* survives — after three detector rebuilds the best AUROC anywhere was 0.532 against a pre-registered bar of 0.55, with a maximum real-minus-shuffled gap of +0.052 across 28 cells. But the *argument the essay uses to get there* is the one the September note retracts as unfalsifiable.

Publishing the April essay unchanged puts a superseded argument on the site, dated April, one click from a September note saying that argument could not have been falsified. The essay is admired precisely for its epistemic discipline; shipping it in this state undercuts the thing it demonstrates.

**Options for Ryan (pick one; the plan executes whichever):**

| | Option | Consequence |
|---|---|---|
| **A** | Add a September update banner to the essay, mirroring the one already written for the sibling post, and publish | Preserves the April record; lowest prose effort; two accounts still coexist but the relationship is explicit |
| **B** | Revise sections 1 and 6 to lead with the rebuilt-detector numbers (0.532 vs the 0.55 bar, 28 cells, shuffled controls), then publish | Strongest artifact; **requires Ryan to write**, since R7 forbids agent edits |
| **C** | Re-date the essay to September and fold the ablation in as its spine | One authoritative account; largest rewrite |
| **D** | Don't publish separately — the September correction in the existing post already carries the finding | Zero prose work; the six-experiment structure and the appendix stay unpublished |

**Recommendation: A**, then B later if Ryan wants it. A is the smallest move that makes the site internally honest, it reuses a correction pattern he has already established on the sibling post, and it does not block on a writing session. D is a real option and should not be dismissed — the September note is tighter than the essay's section 6 — but it leaves four unpublished experiments and the appendix on the floor.

### OQ2 — Non-blocking. What replaces the `"Preference pairs" "11,006"` metric?

Removing it leaves Moirai with two metrics (`Runs analyzed 12,854`, `Mixed-outcome tasks 1,096`), both corroborated verbatim by the essay. A third slot could carry an essay-supported result: `High-structure tasks 25%` or `Conditional accuracy 59.2%` (the latter is the figure the essay says is locked behind a frozen-parameter assertion in `scripts/run_structure_routing.py`).

**Default if Ryan doesn't weigh in: remove the metric, ship two.** Deleting a refuted claim needs no approval; adding a new headline figure does.

---

## Key Technical Decisions

**KTD1 — Merge the three copy branches to `master` first, as their own PRs, before touching the essay.** They are independently finished, independently reviewable, and `copy/built-section` is a hard prerequisite for R2. Bundling them with the essay would make one PR that is part copy-edit, part retraction, part publication.

**KTD2 — Merge order: `copy/record-thesis` → `copy/built-section` → `copy/ablation-correction` → `seo/homepage-title`.** Ordered by blast radius, smallest first. `record-thesis` touches one content file. `built-section` touches the homepage data and its audit assertions together. `ablation-correction` touches both validators and retires two URLs, so it goes last among the copy branches and needs the alias machinery verified.

**KTD3 — Two file-level overlaps exist; both are comment-only and in disjoint hunks.**
- `layouts/_default/baseof.html`: `built-section` edits a "Building now"→"Built" comment; `ablation-correction` edits a different comment block about nav labels. Different regions.
- `scripts/audit_homepage.py`: `built-section` edits "Building now" label strings; `seo/homepage-title` edits `EXPECTED_TITLE` at line 26. Different lines.

Expect clean merges. If either conflicts, it is a textual comment conflict, not a semantic one.

**KTD4 — `copy/built-section`'s `home.html` and `audit_homepage.py` changes are coupled and must land together.** The branch renames the homepage section "Building now" → "Built" and updates the audit's label assertions in the same commit. Splitting them red-lines the audit.

**KTD5 — Do not re-pin Moirai to the new essay without asking.** Moirai currently pins `what-stochastic-variation-reveals`. The new essay is arguably the better Moirai artifact, but the pinned/unpinned split drives the homepage Writing list and the audit's "writing list is populated exactly when an unpinned post exists" check. Default: leave pins alone, let the new essay land unpinned in the Writing list. Revisit with Ryan after OQ1.

**KTD6 — Validate on a PR, never on `master`.** The `deploy` job is gated `github.ref == 'refs/heads/master' && github.event_name == 'push'` — the dispatch-only hold from the redesign era is gone. PRs run `build` + `validate_site.py` and never deploy. The master merge is the live moment.

---

## Implementation Units

### U1. Land `copy/record-thesis`

**Goal:** Merge the About-page results rewrite.
**Requirements:** Unblocks nothing directly; smallest-blast-radius first per KTD2.
**Dependencies:** none.
**Files:** `content/about.md` (19+/8−).
**Approach:** Open a PR from the existing pushed branch. No rebase needed — it merges cleanly from `6f52677597`.
**Verification:** `audit_homepage.py` passes. Note the audit's `ABOUT_CLAIMS` corroborates homepage figures against `content/about.md`, so an About edit can red-line the homepage audit even though the homepage is untouched — this is the unit most likely to surprise.
**Test scenarios:** `audit_homepage.py` passes 24/24; specifically the `ABOUT_CLAIMS` check still finds `$1M`, `150+`, `$100M+`, `91%` in both `content/about.md` and `home.html`.

### U2. Land `copy/built-section` and resolve the preference-pair metric

**Goal:** Remove every assertion that Moirai produces usable preference data — prose *and* metric. Satisfies R2.
**Requirements:** R2. Hard prerequisite for U4.
**Dependencies:** U1.
**Files:** `layouts/partials/record/data.html`, `layouts/_default/home.html`, `layouts/_default/baseof.html`, `layouts/index.llms.txt`, `scripts/audit_homepage.py`.
**Approach:** Merge the branch as-is, then apply two additional changes the branch does not make:
1. Delete the `(dict "label" "Preference pairs" "value" "11,006")` entry from the Moirai `metrics` slice in `data.html`, per OQ2's default.
2. Delete the matching `"Preference pairs"` entry from `MOIRAI_CONTRACT` in `scripts/audit_homepage.py:61-65`.

Both are required. The audit does not hardcode Moirai's figures — it derives each one by regex from `content/posts/what-stochastic-variation-reveals.md` (`MOIRAI_POST`), so the homepage label is the key and the essay is the only authority for the value. Dropping the rendered metric without dropping its contract entry leaves the audit looking for a metric that no longer exists.

**Note for the record:** the literal `11,006 preference pairs` survives in the ablation-corrected essay inside a fenced code block, so `MOIRAI_CONTRACT` would have continued to pass while the homepage advertised a figure the essay's own update calls unpredictive. The audit checks that the number *agrees* with the essay, not that the claim it encodes is still one we make.

**Patterns to follow:** `metrics` is a `slice` of `dict`s in `data.html`; removing one entry is a line deletion, and `home.html` ranges over whatever is there.
**Test scenarios:**
- Built homepage contains no occurrence of "preference data" or "Preference pairs".
- Moirai renders exactly two metrics without layout breakage.
- `audit_homepage.py` passes, including the renamed "Built" section assertions.
- `layouts/index.llms.txt` output contains no preference-pair claim.

### U3. Land `copy/ablation-correction`, then `seo/homepage-title`

**Goal:** Publish the September retraction and the retired-offer redirects; land the title descriptor.
**Requirements:** R3 (partially — the retraction becomes public), R4, R5.
**Dependencies:** U2.
**Files:** `content/posts/what-stochastic-variation-reveals.md`, `content/_index.md`, `content/advising.md` (delete), `content/office-hours.md` (delete), `layouts/_default/baseof.html`, `layouts/_default/single.html`, `scripts/baselines/approved-aliases.txt`, `scripts/validate_live.py`, `scripts/validate_site.py`, `CLAUDE.md`; then `layouts/partials/head.html`, `scripts/audit_homepage.py`.
**Approach:** Two PRs, `ablation-correction` first. The retirement-by-redirect machinery is already built on the branch (aliases in `content/_index.md`, entries in `approved-aliases.txt`, validator changes) — do not re-derive it.
**Test scenarios:**
- `/advising/` and `/office-hours/` serve meta-refresh stubs, appear in the URL manifest, and are absent from the sitemap.
- `approved-aliases.txt` entries resolve to real redirects in the build (the file re-verifies this, so a typo exempts nothing).
- The September update banner's anchor `#the-preference-pair-hypothesis` resolves to the renamed `## The preference-pair hypothesis` heading in the built HTML.
- `validate_site.py` passes 7/0.
- After `seo/homepage-title`: homepage `<title>` is `Ryan Orban — Agent evaluation and reliability`; `og:title` and the Twitter card still read `Ryan Orban`.

### U4. Publish the essay — **GATED ON OQ1**

**Goal:** The essay goes live. Satisfies R1 and, depending on OQ1's answer, R3.
**Requirements:** R1, R3, R7.
**Dependencies:** U2 (hard — R2 must hold first), U3, and **Ryan's answer to OQ1**.
**Files:** `content/posts/agent-trace-divergence-what-the-signal-is-and-isnt.md`.
**Approach:** Remove `draft: true`. Under OQ1-A, additionally insert the update banner **written by Ryan** — verbatim, not composed by an agent (R7). Under OQ1-B or C, the prose lands from Ryan before this unit runs. Under OQ1-D, this unit is deleted.
**Execution note:** The only agent-authored change permitted in this file is deleting the `draft: true` line.
**Test scenarios:**
- `/posts/agent-trace-divergence-what-the-signal-is-and-isnt/` builds and renders.
- KaTeX renders the `structure(t)` display equation (`math: true` is already set).
- The in-post link `/posts/stop-testing-agents-like-deterministic-code` resolves. It omits a trailing slash where the published URL has one — confirm Hugo serves it rather than 404ing.
- The post appears on `/posts/`, in `sitemap.xml`, in `/llms.txt`, and in the graph feed.
- A `.../index.md` companion is emitted beside the HTML.
- `audit_homepage.py` still passes with a third published post — in particular the "writing list is populated exactly when an unpinned post exists" check.
- `validate_site.py` passes; newly added URLs do not trip the baseline comparison.

### U5. Deploy gate — **human decision, not a pipeline step**

**Goal:** Ryan decides when production changes. Satisfies R6.
**Dependencies:** U4.
**Approach:** Present the merged, green PRs and stop. Merging to `master` triggers build + deploy + `validate_live.py` against the Cloudflare edge.
**Verification:** After merge, check the **`deploy` job**, not the run rollup — a skipped `deploy` still reports the run green, which once held the redesign off production for two days.

---

## Scope Boundaries

**In scope:** publishing one essay; merging four finished branches; deleting one refuted metric; validator gates.

**Out of scope:**
- `content/posts/your-eval-says-your-agent-works.md` — 434 words, a stub. Stays `draft: true`.
- Rewriting any part of the essay body (R7).
- Re-pinning Moirai (KTD5).
- `scripts/baselines/sitemap-urls-2026-08-18.txt` — a dated snapshot; never edited to make a check pass.

**Deferred to follow-up work:**
- OQ2's replacement metric, if Ryan wants a third.
- Whether the new essay should displace `what-stochastic-variation-reveals` as Moirai's pinned post.

---

## Risks & Dependencies

| Risk | Likelihood | Mitigation |
|---|---|---|
| OQ1 goes unanswered and the essay ships with a retracted argument | — | U4 is hard-gated. The pipeline stops at U3. |
| `ABOUT_CLAIMS` red-lines on U1 despite the homepage being untouched | Medium | Run `audit_homepage.py` on the U1 PR before merging. |
| Comment conflicts in `baseof.html` / `audit_homepage.py` | Low | KTD3; both are disjoint hunks. Resolve textually. |
| A third published post changes the Writing-list audit assertion | Medium | Explicit test scenario in U4; verify before the master merge. |
| The moirai README anchor cited by the September banner has drifted | Unverified | External URL. Confirm `#what-the-ablation-found` exists before U3 merges. |

---

## Sources

All findings below were measured in-session against the working tree, not recalled:

- Draft state, word counts, dates — `content/posts/*.md` frontmatter.
- Branch topology, merge-bases, per-branch file lists — `git merge-base`, `git diff <base>..<branch> --name-only`.
- The preference-pair contradiction — `layouts/partials/record/data.html` on `master` vs essay section 6.
- The AUROC retraction — `git show copy/ablation-correction:content/posts/what-stochastic-variation-reveals.md`.
- Deploy gating — `.github/workflows/hugo.yml:124-135`.
- Validator baselines — `audit_homepage.py` 24/24 and `validate_site.py` 7 passed / 0 failures, both run on `seo/homepage-title`.
