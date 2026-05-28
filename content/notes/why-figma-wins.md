---
title: Why Figma Wins
date: 2020-08-23
categories:
  - strategy
  - product
  - design
  - saas
  - network-effects
description: Kevin Kwok's analysis of why Figma dominates design tools — the browser-first architecture enabled cross-side network effects by pulling non-designers into the design loop, making collaboration both the core product and the distribution mechanism.
params:
  source: pinboard
  sourceUrl: https://kwokchain.com/2020/06/19/why-figma-wins/
---

![Why Figma Wins](/images/notes/why-figma-wins.png)

## Summary

Kevin Kwok's 2020 analysis of Figma argues that the company's success isn't simply about making a better design tool — it's about recognizing that design is fundamentally a collaborative process involving non-designers (PMs, engineers, executives, clients), and then building a product and distribution model around that insight. The result is a virtuous cycle where adopting Figma for design pulls in the rest of the organization.

The browser-first architecture was the enabling technology. Figma used WebGL and CRDTs (conflict-free replicated data types) to make collaborative editing work natively in the browser — not file syncing, but real multiplayer editing. This eliminated the friction that had plagued earlier cloud design tools and made collaboration feel like a first-class experience rather than a workaround.

The strategic insight is what Kwok calls **cross-side network effects**: designers use Figma, which requires them to bring in PMs and engineers to view prototypes or leave comments, who then advocate for Figma to other design teams. This is fundamentally different from within-side network effects (more users = more value for existing users) — it's more expansive because each new design team adoption potentially brings an entire cross-functional team.

The distribution loop: collaborative features solve real friction (handoff, feedback, review) → this causes non-designers to use the product → they become evangelists → they accelerate adoption at other organizations. "The core of Figma's product is the core of its distribution loop."

## Key points

- Browser-first wasn't just a deployment choice — it removed the installation barrier that prevented non-designers from engaging with design artifacts.
- CRDTs are the technical foundation for conflict-free real-time collaboration — the same technology that powers Google Docs, now applied to vector design.
- Cross-side network effects (designers ↔ non-designers) are more powerful than single-side effects because adoption in one function drives adoption in another.
- Plugin ecosystem and community (Figma Community) add another layer: templates, components, and plugins embed Figma deeper into workflows, raising switching costs.
- The 2022 Adobe acquisition attempt ($20B) validated this analysis — Adobe recognized Figma's network effects as a structural threat to its design tool dominance.

[Original](https://kwokchain.com/2020/06/19/why-figma-wins/)
