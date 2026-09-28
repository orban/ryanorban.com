# Session state — 2026-09-27

Handoff before compaction. Supersedes `SESSION-STATE-2026-09-25.md`, which stays as
history. Everything below was measured, read, or run in-session unless marked recalled.

## Publishing gate — read this first

**Ryan has said explicitly: do not publish the essay until he has reviewed it and given
explicit approval.** Merging PR #26 to `master` deploys to production. Nothing merges
without a fresh "yes" from him in chat. Approval for other work does not carry over.

## Branches and PRs

| repo | branch | head | state |
|---|---|---|---|
| ryanorban.com | `essay/trace-divergence` | `786d766797` | PR #26, CI **build: success / deploy: skipped** (PRs never deploy). Awaiting Ryan's read. |
| ryanorban.com | `design/essay-page` | see PR #27 | Off `master`, independent of #26. Essay body 18px/64ch, booktabs tables, `render-heading.html` override (written heading level + `§` anchors). Audit and validator green. |
| ryanorban.com | `tooling/citation-validator` | `8f331efde2` | pushed, **no PR**. Adds `scripts/validate_citations.py` + CI step + CLAUDE.md section. Its CI is red against `master` until #26 merges (master's draft still carries two fabricated arXiv IDs the rewrite removed). Sequence: #26 first. |
| moirai | `exp/trajectory-representations` | `419da01` | PR #7, stacked on `feat/diagnosability` (PR #6, unmerged). Renamed from `exp/markov-state-abstraction`; old remote branch deleted. |

Check the *job*, not the run: a skipped `deploy` reports the run green.

## The essay (PR #26)

`content/posts/agent-trace-divergence-what-the-signal-is-and-isnt.md`, 5,185 words,
title **"Eleven ways to score an agent trajectory"**, date 2026-09-25, no `draft` flag.
Slug unchanged so `audit_homepage.py`'s `MOIRAI_POST` pin and `MOIRAI_CONTRACT`
regexes still resolve from the appendix line
`**Scale:** 1,096 tasks with mixed-outcome runs, 12,854 total runs, median 11 runs/task`.
**Do not edit that line's phrasing.**

Gates at commit: `audit_homepage.py` pass; `validate_site.py` 7/0; citation validator
28/28 identifiers resolve and match; anti-slop 0/100; zero banned words/constructions.

Two decisions Ryan hasn't made:
1. Two em-dashes remain, both inside the verbatim SWE-Dev quotation on p.2 of that
   paper. His rule is "remove all em-dashes"; I left a direct quote intact. Paraphrase
   if he says so.
2. Commit `dd3f319e88` is titled "close the data-adequacy escape hatch with a measured
   DDU" and that claim is now known false. Offered to squash the branch before merge.

Structure: permutation floor as the lede → M0–M5 ladder (M0 reproduces 0.507 exactly)
→ representation sweep (full-history breaks at 0.504, everything else 0.55–0.58,
hashed buckets 0.578) → Liblit predicates with the stratification bug as a worked
example (0.5483 → 0.5768) → eleven representations incl. five published, 0.528–0.581
→ the floor (unfiltered 0.6897 real / 0.6808 shuffled) → prior art around the
three-questions distinction → "what I'd do differently" → repro block → appendix.

PR #26's description was rewritten 2026-09-27 and names the two open decisions.

## What the prior-art reading found (all applied in the essay)

Read from source: Liblit 2005, Cho et al. 2608.23670, SWE-Gym, Perez ICSE'17, SWE-Dev,
OmegaPRM, FDG (PDFs); Capable but Unreliable, Failure as a Process, OAT, When Evidence
is Sparse, Beyond Resolution Rates, ATLAS, False Success, Agent trajectories as
programs (full HTML). Fourteen more verified at abstract level.

Corrections made to the old map: SWE-Gym was **inverted** (mixing on/off-policy is their
*best* verifier setting); Perez's 0.10–0.42 is before/after an EvoSuite intervention,
not a working band; SBEST's structural signal is crash stack traces, no analogue for
us; FDG's criticism is about using suspiciousness *during* localisation, not
outcome-blindness; OmegaPRM's "75×" figure unverifiable and cut. SWE-Dev's direct quote
is verbatim (p.2). The three-questions frame (between-model / between-task /
within-model sampling) is the essay's central distinction; Capable but Unreliable is
the one paper measuring our quantity (d=0.48 ≈ 0.63 AUROC-eq vs our 0.578).

**Dead, do not resurrect:** DDU as evidence of corpus adequacy. It failed to predict
downstream AUROC three times (win-2 0.523 vs win-1 0.130 DDU → identical 0.554/0.559
AUROC). It survives in the essay only as a cautionary example.

## moirai branch contents

Eight experiment scripts, all reproducible from the corpus, all printing a shuffled arm:
`exp_matching_ablation.py` (M0–M5, `context` param), `exp_predicate_vocabulary.py`
(Liblit, stratified, `--exclude/--only`), `exp_tfidf_baseline.py`,
`exp_per_state_features.py` (`--prefix-frac`, `--protocol trace`, `--all-tasks`,
`--length-only`), `exp_mixed_outcome_filter.py` (reads raw parquet),
`exp_published_representations.py` (bpe/outcome/canon/canon_rich/tfidf2), plus
`moirai/analyze/diagnosability.py` and `scripts/run_diagnosability.py` from PR #6.
Result JSONs were copied to `scripts/blog_output/` which is **gitignored** — regenerate.

Outstanding: `canon_rich` still has ~2pts of leave-one-out asymmetry (shuffled
0.482) — its margin is approximate and the essay says so.

## Data

- Raw parquet: `/tmp/rebench/trajectories.parquet` (2.1 GB, 67,074 rows; 6,225 tasks
  ≥4 runs, 1,737 mixed, 4,488 always-same). `/tmp` may not survive a reboot; source is
  `nebius/SWE-rebench-openhands-trajectories` on HF.
- Converted corpus: `/Volumes/mnemosyne/moirai/swe_rebench_v2/` (NAS). **Pre-filtered to
  mixed-outcome tasks only** (1,096 tasks / 12,854 runs at ≥4). The floor experiment
  has to read the parquet for that reason.

## Design assessment (items 2, 3, 8 built in PR #27; the rest not started)

Ryan likes https://david.alvarezrosa.com (source: github.com/david-alvarez-rosa/
personal-website, cloned at `/tmp/dar-site`). Assessment delivered; his answer pending.

Verdict: our homepage is the stronger page for its purpose, leave it. His **essay page**
wins: sidenotes in a right margin (`processed-content.html` rewrites Goldmark footnotes
into inline `<span class="side">`), ~21px body on ~62ch, booktabs tables, one serif
superfamily with metric-matched fallbacks. Scope any port to `posts/single.html` and
`.record-prose`.

Hard constraint: his CSS uses `:has()` ~12× and `!important` 3×; both banned by our
audit (`!important` is a substring check). Sidenote mobile collapse needs a
template-emitted class, not `p:has(.side)`.

Ranked: (1) sidenotes [medium, new partial + single.html + home.css]; (2) essay body
type ~18–19px/1.7/64ch [low]; (3) booktabs tables [low]; (4) dark mode on existing
`--record-*` tokens, audit needs second-palette contrast checks [low–med]; (5)
metric-matched font fallbacks, generate with a tool [low]; (6) read-next via `.Related`
[low]; (7) post-list entries with subtitle [low]; (8) hover `§` anchors [trivial].
Infra worth taking: `--panicOnWarning`, lychee, html5validator. **Don't take:** drop
caps, ornaments, Alegreya, subscribe form, instantpage.

Open layout question for him: essays have a *left* rail; sidenotes want right. I'd
move date/meta to the right margin and retire the left rail on essays.

Built 2, 3 and 8 on `design/essay-page` (PR #27) after Ryan said "proceed". Found on the
way: the theme's `render-heading.html` emitted `h{{ add .Level 1 }}`, so `##` was an h3
site-wide and `.record-prose h2` never matched content; the override fixes the level.
Also noticed, not touched: the essay nav shows "Writing" twice (section link plus the
"where you are" item), pre-existing on master.

## Pattern for whoever picks this up

Nine claims were asserted and retracted this session. Every one was checkable in
minutes and I stated it in the measured voice first. Separately, I ran a prior-art
search and read the search engine's summaries instead of the papers; four of the map's
claims were wrong and two papers that tested our exact hypothesis sat unopened in my
own results for hours. Read the PDF. Run the shuffled arm before the real one.
