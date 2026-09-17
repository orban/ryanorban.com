---
title: How to Make an Awesome Python Package in 2021
date: 2021-04-08
categories:
  - python
  - packaging
  - pypi
  - tooling
  - open-source
description: Anton Zhiyanov's practical guide to creating a well-structured Python package in 2021 — covering pyproject.toml, setup.cfg, versioning, testing, and publishing to PyPI. A concise alternative to piecing together the official documentation.
params:
  source: pinboard
  sourceUrl: https://antonz.org/python-packaging/
---

## Summary

Anton Zhiyanov wrote this as a concise, opinionated guide to the then-current best practices for creating Python packages — covering the toolchain and configuration that the official PyPI documentation spreads across multiple pages. The 2021 context matters: this was during the transition from `setup.py` to `pyproject.toml` as the standard configuration format.

The guide covers: `pyproject.toml` with PEP 517/PEP 518 build system declarations, `setup.cfg` for package metadata (name, version, dependencies, classifiers), pytest configuration, tox for testing across Python versions, and publishing to PyPI via twine. It also covers semantic versioning, CHANGELOG maintenance, and configuring pre-commit hooks.

From a 2026 perspective, this captures a transitional moment. The tools have since consolidated: Poetry simplified the `pyproject.toml` + build backend story, and uv has since become the dominant packaging tool, replacing pip, pip-tools, pyenv, and virtualenv with a single fast Rust implementation. The core concepts remain — how packaging works, what metadata PyPI expects — but the specific tool recommendations have evolved.

## Key points

- Covers the `pyproject.toml` + `setup.cfg` pattern for Python package configuration.
- PEP 517/PEP 518: standardized build system interface that decoupled tools from `setup.py`.
- Publish via twine to PyPI; TestPyPI for testing the release pipeline.
- 2026 context: Poetry and uv have since simplified this considerably.
- By Anton Zhiyanov — concise and practical, good reference for understanding the plumbing.

[Original](https://antonz.org/python-packaging/)
