---
title: Mappers vs Packers
date: 2020-10-07
categories:
  - programming
  - cognitive-styles
  - communication
  - teams
  - patterns
description: Ward Cunningham's wiki pattern distinguishing 'Mappers' (who think in connected concepts and structures) from 'Packers' (who think in discrete lists and procedures). A useful lens for diagnosing communication friction in technical teams.
params:
  source: pinboard
  sourceUrl: http://wiki.c2.com/?MappersVsPackers
---

## Summary

The [Mappers vs Packers](/notes/mappers-vs-packers/) pattern from Ward Cunningham's WikiWikiWeb (the original wiki, where many software patterns were first articulated) describes two cognitive styles that frequently appear in programming teams and cause communication friction when unrecognized.

**Mappers** think in terms of connected concepts, relationships, and structures — they build mental models as graphs, see how pieces relate, and communicate by building up a picture. When a Mapper explains a system, they start with the big picture and work down into specifics. They find lists without relationships unsatisfying.

**Packers** think in terms of discrete items, procedures, and lists — they process information sequentially and communicate by enumerating steps or items. When a Packer explains a system, they start with concrete steps and build up from there. They find open-ended conceptual explanations hard to act on.

Neither style is better — they're complementary. Mappers tend to excel at architecture and system design work; Packers tend to excel at execution and implementation. The friction arises when a Mapper explains and a Packer needs action items, or when a Packer explains and a Mapper needs to understand the relationships.

## Key points

- The pattern is descriptive, not prescriptive — it helps explain communication failures, not prescribe which style to use.
- The same person can be a Mapper in domains where they have deep mental models and a Packer in domains where they're learning.
- In code review: Mappers often leave architectural comments; Packers leave procedural or nitpick comments — both valid, different signal types.
- Understanding the distinction helps in technical communication: when writing docs, you need both the map (overview, relationships) and the packed list (step-by-step instructions).
- Related to Systems Thinking (mapper orientation) vs. procedural thinking (packer orientation).

[Original](http://wiki.c2.com/?MappersVsPackers)
