# Session state — 2026-09-25

Handoff note written before context compaction. Everything below was measured or
run in-session, not recalled.

## Where things stand

**Two open PRs, both green, neither merged. Both need Ryan to read them.**

| Repo | PR | Branch | Head | State |
|---|---|---|---|---|
| `ryanorban.com` | [#26](https://github.com/orban/ryanorban.com/pull/26) | `essay/trace-divergence` | `dd3f319e88` | CI green, unmerged |
| `moirai` | [#6](https://github.com/orban/moirai/pull/6) | `feat/diagnosability` | `7f30f91` | 440 tests pass, unmerged |

**Already shipped to production earlier in the session** — PRs #22–#25 on
`ryanorban.com`, all merged, `deploy` job verified green at job level on each:
record-thesis (About page), built-section (+ preference-pair metric removal),
ablation-correction (the September retraction), seo/homepage-title.

Live now: zero preference-pair claims on the homepage, Moirai card shows two
metrics, `/advising/` and `/office-hours/` redirect instead of 404, `<title>`
reads `Ryan Orban — Agent evaluation and reliability`.

## PR #26 — the trace-divergence essay

Publishes `content/posts/agent-trace-divergence-what-the-signal-is-and-isnt.md`,
draft since April. Also moves the Moirai homepage pin to this essay and lets
`what-stochastic-variation-reveals` take the Writing slot.

**Coupling to know about:** `scripts/audit_homepage.py`'s `MOIRAI_POST` and
`MOIRAI_CONTRACT` resolve the homepage's Moirai figures against whichever essay
the card pins. They currently match the appendix `Scale:` line
(`([\d,]+) total runs`, `([\d,]+) tasks with mixed-outcome runs`). Editing that
line breaks the audit.

**Gates:** `python3 scripts/audit_homepage.py` (24/24) and
`python3 scripts/validate_site.py --public <build> --url-manifest scripts/baselines/public-urls.txt`
(7 passed / 0 failures). Merging to `master` deploys; PRs never do.

## PR #6 — `moirai diagnosability`

New `moirai/analyze/diagnosability.py` porting DDU (Perez, Abreu & van Deursen,
ICSE 2017) to trajectories. Reads no pass/fail labels. 17 new tests, every
expected value hand-computable. `scripts/run_diagnosability.py` streams the
2.1 GB parquet by row group and reuses `convert_swe_rebench.parse_openhands_trajectory`
so the component alphabet matches the published analysis.

`pyarrow` was installed into `moirai/.venv` for this. It is **not** declared in
`pyproject.toml`; neither is `datasets`, which `convert_swe_rebench.py` imports.
Worth declaring before merge.

Corpus parquet is at `/tmp/rebench/trajectories.parquet` (2.1 GB, 67,074 rows).
Output at `/tmp/rebench/ddu.json` and copied to `scripts/blog_output/diagnosability.json`,
which is **gitignored** — regenerate rather than hunt for it.

## The measurement that changed the essay's argument

Ran over 1,737 mixed-outcome tasks (>=4 runs), 19,592 runs:

| | step-name | step+target |
|---|---:|---:|
| Median DDU | 0.141 | 0.145 |
| Density | 0.358 | 0.501 |
| Diversity | 0.879 | 1.000 |
| Uniqueness | 0.438 | 0.331 |
| Below 0.10 | 25.8% | 23.9% |

Perez et al.'s real-fault Defects4J medians were 0.10 to 0.42, so **this corpus is
diagnosable**. The earlier draft claimed the run set had "very little diagnostic
diversity" — that was false, and diversity turned out to be the strongest of the
three terms. The binding constraint is uniqueness: components get hit together
and sit in ambiguity groups. The negative result is now stronger, because the
data-adequacy escape hatch is closed by measurement.

**Caveat to keep:** my filter yields 1,737 tasks where the published analysis used
1,096, so the corpora are not identical, though mean runs/task is 11.3 against a
published median of 11. Stated in the essay.

## Corrections made to the essay this session

An adversarial workflow review (13 agents, `wf_ddc88716-0cb`) returned PARTIALLY
and surfaced eight factual errors. Five were introduced by me. All fixed and each
verified against source, not against the review:

- "multiple models, multiple harnesses" was false — one agent, one scaffold, one
  config, and that is the identification strategy
- dataset link pointed at `nebius/SWE-rebench` (no trajectories) instead of
  `nebius/SWE-rebench-openhands-trajectories`
- SWE-Dev *did* run KTO and OREO and chose RFT — verified in the PDF; I had
  deleted this true, stronger claim earlier
- SWE-Lego is SFT-only, not contrastive
- low-structure is 827, not 811 (verified: 269 high, 812 zero-divergence, 15
  low-with-divergence)
- "margin shrinks" was one row of four; it is noise in both directions
- moirai is ~10.5k lines not ~7k; the frozen assertion reads `0.593`
- date moved to 2026-09-20; it had predated three citations

The review also confirmed the prior-art section **does** carry mechanism rather
than name-drops — a suspicion I had asserted and which was wrong.

## Style constraints in force on the essay

Zero em-dashes, zero "not just/only/merely", zero "isn't X, it's Y", no
elapsed-time framing. Verified by regex each commit. Anti-slop detector reads
0/100. The `anti-slop@ryo-marketplace` plugin is disabled in settings; its
ruleset and `detect_slop.py` were read off disk at
`~/.claude/plugins/cache/ryo-marketplace/anti-slop/1.0.0/skills/anti-slop/`.

Ryan plans to install `miqdadbadjuber/anti-slop` out of band.
`sam-paech/auto-antislop` was assessed and is not applicable — it is a model
fine-tuning pipeline, not a prose tool.

## Open, not done

1. **Neither PR is merged.** Ryan wants to read #26 before it ships; roughly
   2,000 words of it are agent-written prose under his name.
2. `pyarrow` and `datasets` undeclared in moirai's `pyproject.toml`.
3. The review's remaining structural suggestions were not acted on: stating the
   fixed-state-vs-fixed-position axis as the sort key at the top of the prior-art
   map, and cutting ~140 words of genuine duplication between the two lesson
   sections.
4. Sections 3–5 of the essay still report numbers from the original detector. The
   caveat says so. Re-running them against the rebuilt detectors is unstarted.

## Context on the goal

The post's job is to reward a search by someone at Core Automation, a 16-person
frontier lab (Jerry Tworek, ex-OpenAI VP of RL Research) — Ryan already has a
referral there, so this is not lead generation. The bar he set: "I've read the
papers so you don't have to." Not a post-mortem; an instrumentation story whose
finding happens to be null.
