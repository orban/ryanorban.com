---
title: "FastUI: Python-Defined React UIs"
date: 2024-03-02
categories:
  - python
  - react
  - web-development
  - pydantic
  - open-source
description: FastUI is a Pydantic framework for building React-based web UIs entirely in Python — no JavaScript required. The backend defines UI structure as Pydantic models, and matching TypeScript interfaces render them. Now inactive.
params:
  source: pinboard
  sourceUrl: https://github.com/pydantic/FastUI
---

![FastUI: Python-Defined React UIs](/images/notes/fastui-python-react-ui.png)

## Summary

FastUI is a framework from the Pydantic team that lets Python developers build React-based web UIs without writing any JavaScript. The backend defines the entire application structure using Pydantic models; matching TypeScript interfaces on the frontend render them into real UI components. Communication happens via JSON over REST — new features only require backend changes.

The approach solves a real friction point for Python backend teams who need frontends but don't want to maintain a full React codebase. Single-location development, type safety via Pydantic's validation, and decoupled deployments are the main selling points. The prebuilt CDN version requires no npm setup at all.

The catch: the repository is now marked as **inactive**. The Pydantic team has moved on. FastUI is worth understanding as a pattern — backends defining UI declaratively — but it's not a foundation for new projects. Similar ideas appear in other frameworks like Reflex (Python → React) and NiceGUI.

## Key points

- Define React UI entirely in Python via Pydantic models — no JavaScript needed.
- RESTful architecture: backend defines application structure, frontend renders it.
- Four components: PyPI package, React TypeScript implementation, Bootstrap layer, prebuilt CDN.
- Type safety via Pydantic (Python) and TypeScript (frontend) in sync.
- **Now inactive** — the Pydantic team has stopped development.
- The declarative UI-from-backend pattern lives on in Reflex and NiceGUI.

[Original](https://github.com/pydantic/FastUI) → GitHub
