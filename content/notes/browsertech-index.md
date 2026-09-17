---
title: Browsertech Index
date: 2022-12-06
categories:
  - browser-technology
  - collaboration
  - local-first
  - crdt
  - directory
description: The Browsertech Index is a curated directory of companies and projects building browser-native collaboration technology — real-time sync, local-first software, CRDTs, and multiplayer features. A map of the technical ecosystem underlying tools like Figma, Linear, and Notion.
params:
  source: pinboard
  sourceUrl: https://browsertech.com/bt-index
---

## Summary

The [Browsertech Index](/notes/browsertech-index/) (by browsertech.com) is a curated directory of companies and open-source projects building browser-native collaboration technology — the infrastructure for real-time multiplayer, local-first software, CRDTs, WebRTC, WebSocket infrastructure, and related capabilities. It maps the ecosystem that powers collaboration features in tools like Figma, Linear, Notion, and Liveblocks.

The index covers several sub-categories: real-time sync infrastructure (Liveblocks, PartyKit, Yjs, Automerge), local-first databases (ElectricSQL, Replicache, PowerSync), multiplayer cursors and presence, operational transformation and CRDT libraries, and the companies building on top of these primitives. It's a useful map because the how does Figma do multiplayer question has a complex answer involving multiple layers of technology that most people don't see.

The local-first software movement that this directory maps to is defined by Ink & Switch's 2019 paper: applications that store data locally, work offline, and sync peer-to-peer rather than requiring cloud connectivity for every operation. Automerge and Yjs are the main CRDT libraries in this space. The tension between fully local-first (no central server) and practically-collaborative (need some server for discovery and relay) remains unresolved — most products pick a middle ground. The [Browsertech Index](/notes/browsertech-index/) is a good entry point for understanding where that ecosystem currently sits.

## Key points

- Directory of companies and projects building browser-native collaboration infrastructure.
- Covers: real-time sync providers, local-first databases, CRDT libraries, multiplayer presence.
- Maps the technology stack underlying Figma, Linear, Notion, Liveblocks and others.
- Key players: Liveblocks, PartyKit, Yjs, Automerge, ElectricSQL, Replicache.
- Local-first software movement context: Ink & Switch paper, offline-first, peer-to-peer sync.
- Useful entry point for understanding "how do multiplayer web apps work" at the infrastructure level.

[Original](https://browsertech.com/bt-index)
