---
title: Speeding up scikit-learn Workflow Using a High-Performance Go Proxy
date: 2016-12-19
categories:
  - machine-learning
  - testing
  - scikit-learn
  - golang
  - developer-tools
description: A 2016 blog post on using HoverPy — a Go-based HTTP recording/replay proxy — to speed up scikit-learn workflows that make external HTTP calls. An early example of applying API mocking techniques to ML pipelines for faster, deterministic testing.
params:
  source: pinboard
  sourceUrl: http://ioloop.io/blog/hoverpy-scikitlearn/
---

## Summary

This post from ioloop.io covers HoverPy, a Go-based HTTP proxy that records and replays HTTP interactions. The application: scikit-learn pipelines that fetch data or features from external APIs can be slow and non-deterministic in tests because they depend on network calls. HoverPy intercepts those calls, records the responses on first run, and replays them on subsequent runs — making tests fast and deterministic without mocking at the code level.

The technique is a variant of VCR (video cassette recorder) testing, a pattern originally popularized in Ruby for HTTP interaction recording and common in API testing. What makes this interesting for machine learning is that ML pipelines often involve fetching features from external services (feature stores, data APIs) that are tedious to mock by hand and change over time. A transparent proxy-level recorder handles this at the HTTP level, meaning the application code doesn't need to be modified and the recorded responses reflect real-world data shapes.

HoverPy being written in Go made it fast as a subprocess proxy — low overhead compared to a Python-native approach. This was a niche but practically useful technique in 2016 for teams that had scikit-learn workflows making external API calls. The underlying problem — that ML test suites are slow and non-deterministic because they depend on external data — remains relevant and has been addressed by later tools (DVC for dataset versioning, feature store abstractions for mocking, pytest-recording for HTTP interaction capture in Python).

## Key points

- HoverPy: a Go HTTP proxy that records API calls on first run and replays them in subsequent test runs — VCR pattern for HTTP.
- Applied to scikit-learn pipelines that fetch features from external services — eliminates network calls from test suite runs.
- Transparent proxy approach: no application code changes needed, works at the HTTP level.
- Related to VCR testing pattern from Ruby/Rails; similar tools: pytest-recording, responses, httpretty for Python.
- Problem remains relevant: ML pipeline testing with external data dependencies is a persistent pain point addressed later by feature stores and dataset versioning tools like DVC.

[Original](http://ioloop.io/blog/hoverpy-scikitlearn/)
