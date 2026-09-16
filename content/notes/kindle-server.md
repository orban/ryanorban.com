---
title: "kindleServer: Serve Local Files to Kindle"
date: 2022-03-15
categories:
  - kindle
  - self-hosting
  - reading
  - tools
  - open-source
description: kindleServer serves local HTML files with a Kindle-friendly UI and a Read Mode powered by ReadabiliPy — a simple self-hosted solution for reading long-form web content on a Kindle without relying on Pocket or Send to Kindle.
params:
  source: pinboard
  sourceUrl: https://github.com/edgartaor/kindleServer
---

## Summary

kindleServer is a small open-source project that runs a local web server optimized for the Kindle browser — serving HTML files stored on your computer with a UI designed for e-ink display reading. It includes a Read Mode powered by ReadabiliPy (a Python port of Firefox's Readability algorithm) that strips navigation, ads, and clutter from web pages and presents clean readable text.

The use case: you want to read long-form web content (articles, documentation, essays) on your Kindle without relying on Amazon's Send to Kindle service, Pocket, or Instapaper. Those services send content to Amazon's servers; kindleServer keeps everything local. You run the server on your home network, connect your Kindle's browser to it, and read your saved content in the Kindle's own browser with appropriate formatting.

The Kindle browser is limited but functional — it renders basic HTML and CSS, handles scrolling, and supports bookmarking. The key challenge is that most web pages are designed for desktop browsers and render poorly on e-ink displays with their low refresh rates and small screens. kindleServer's Read Mode extraction and simple CSS produce content that's actually comfortable to read.

This is a small, practical project that solves a specific pain point: reading long-form web content on the device optimized for long-form reading, without cloud intermediaries.

## Key points

- Local web server for Kindle browser — serves saved HTML files with e-ink-friendly formatting.
- Read Mode via ReadabiliPy (Firefox Readability algorithm) strips clutter for clean text.
- Privacy argument: no cloud intermediary like Amazon Send to Kindle, Pocket, or Instapaper.
- Kindle browser is underused but functional — basic HTML/CSS works fine for reading.
- Simple Python project — low maintenance, runs on any machine on your local network.

[Original](https://github.com/edgartaor/kindleServer) → GitHub
