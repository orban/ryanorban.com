---
title: Lightweight Architecture Decision Records
date: 2026-01-23
categories:
  - architecture
  - documentation
  - decision-records
  - github
  - templates
description: Peter Evans' lightweight ADR repo is a minimal five-section template for capturing architecture decisions in plain markdown files stored alongside code. The approach lowers the adoption barrier enough that even skeptical teams can accept the overhead, keeping decisions documented at the moment they're made.
params:
  source: pinboard
  sourceUrl: https://github.com/peter-evans/lightweight-architecture-decision-records
---

![Lightweight Architecture Decision Records](/images/notes/lightweight-adr.png)

## Summary

Lightweight Architecture Decision Records (LADRs) are a minimal approach to documenting design choices, popularized by Michael Nygard's 2011 blog post and later featured on the ThoughtWorks Technology Radar. The format proposes just five sections: Title, Context, Decision, Status, and Consequences. That simplicity is the point—it's hard to argue the overhead isn't worth it.

Peter Evans' repo distills practical guidance for teams adopting the practice. The key advice is to write the ADR at the moment of the decision, store it in Markdown next to the code it relates to in version control, and peer-review it like any other code change. The GOV.UK govuk-aws migration to AWS is cited as a real-world example of the format in use at scale.

For cross-cutting decisions that affect multiple components, the recommendation is a separate `architecture` repository. Sequential numeric file naming (0001, 0002…) keeps the log ordered and easy to scan.

## Key points

- Five sections only: Title, Context, Decision, Status (`Proposed` / `Accepted` / `Deprecated` / `Superseded`), Consequences
- Store Markdown ADR files in version control next to the component they describe
- Peer-review ADRs as you would code—this builds shared understanding and catches unclear reasoning
- Write the ADR immediately when the decision is made, not weeks later when context is fuzzy
- See the companion ADR template at `0001-ladr-template.md` for a copy-paste starting point

[Original](https://github.com/peter-evans/lightweight-architecture-decision-records)
