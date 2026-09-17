---
title: React Docs Beta
date: 2022-11-27
categories:
  - react
  - javascript
  - documentation
  - frontend
  - hooks
description: The beta rewrite of the React documentation — hooks-first, with interactive examples and a complete rethinking of how React concepts are taught. This eventually became the official react.dev site.
params:
  source: pinboard
  sourceUrl: https://beta.reactjs.org/
---

## Summary

The React documentation beta was a complete rewrite of the official React docs, initiated around 2021 and released publicly in 2022. The driving motivation: the existing docs were written for class components and had been incrementally patched to mention React Hooks, but never truly reorganized around hooks as the primary mental model. The beta docs started from scratch with hooks as the foundation.

The pedagogical approach changed significantly. Every concept is taught using function components and hooks — `useState`, `useEffect`, `useContext`, etc. The docs introduced the idea of thinking in React with hooks, replacing the older class-based lifecycle model. Interactive sandboxes powered by CodeSandbox are embedded throughout, letting readers run and modify examples without leaving the page. The "Escape Hatches" section is particularly good — it's honest about when you need to reach outside React's model (refs, effects that synchronize with external systems) rather than pretending everything fits into pure declarative patterns.

The beta docs were at beta.reactjs.org during development; they eventually replaced the old docs and became react.dev. This was around the same time as the React Server Components announcement, which added another dimension to the React mental model the new docs needed to accommodate.

## Key points

- Complete rewrite of React docs — hooks-first, starting from function components rather than retrofitting class component patterns.
- Interactive embedded sandboxes let readers experiment without leaving the docs.
- Reorganized around the thinking in React mental model for hooks.
- "Escape Hatches" section handles refs, effects, and external system synchronization honestly.
- Eventually became the official react.dev site, replacing the old docs entirely.
- Part of the broader shift in the React ecosystem toward hooks as the default paradigm.

[Original](https://beta.reactjs.org/)
