---
title: "tldraw: Infinite Canvas Drawing App"
date: 2023-01-24
categories:
  - drawing
  - canvas
  - open-source
  - collaboration
  - developer-tools
description: tldraw is a tiny, open-source infinite canvas drawing app with a clean developer SDK — excellent for whiteboarding, diagrams, and embedding collaborative drawing into your own applications. Later gained prominence for its 'make it real' GPT-4V integration demo.
params:
  source: pinboard
  sourceUrl: https://tldraw.com
---

![tldraw: Infinite Canvas Drawing App](/images/notes/tldraw-drawing-app.png)

## Summary

tldraw is an open-source infinite canvas drawing application with an extremely clean developer SDK. The app itself (tldraw.com) is a polished whiteboarding tool — supporting shapes, connectors, text, freehand drawing, and sticky notes — but the more significant aspect is the TypeScript library that lets developers embed the canvas in their own applications.

The tldraw SDK provides the full canvas as a React component with a rich API for reading and writing canvas state, handling events, creating custom shapes and tools, and syncing via any backend. This makes it useful for embedding drawing into other applications — diagram editors, collaborative workspaces, design tools — without building the canvas infrastructure from scratch.

tldraw gained wider attention in late 2023 when Steve Ruiz (the creator) published the make it real demo: users drew UI mockups on the canvas and GPT-4V (Vision) converted them into working React code in real time. This demonstration of multimodal AI + infinite canvas became one of the most widely shared AI demos of 2023 and positioned tldraw as a platform for AI-augmented design tools. The collaboration with Vercel on that demo also introduced it to a wider developer audience.

## Key points

- Open-source infinite canvas app + embeddable TypeScript/React SDK
- SDK API lets developers create custom shapes, tools, and event handlers
- Clean architecture: canvas state is a serializable JSON blob — easy to sync and persist
- Creator: Steve Ruiz; "make it real" GPT-4V demo in 2023 brought mainstream attention
- Foundation for AI-augmented design tools — later used for multimodal prototyping workflows

[Original](https://tldraw.com)
