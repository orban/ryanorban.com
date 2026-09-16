---
title: Hypermodern Python
date: 2021-05-12
categories:
  - python
  - tooling
  - packaging
  - best-practices
  - developer-experience
description: Claudio Jolowicz's influential multi-part guide to modern Python project setup — covering pyenv, Poetry, Nox, pre-commit, and automated testing and linting. The 2020 standard for what a well-configured Python project looks like before Ruff and uv simplified things further.
params:
  source: pinboard
  sourceUrl: https://cjolowicz.github.io/posts/hypermodern-python-01-setup/
---

## Summary

Claudio Jolowicz's "[Hypermodern Python](/notes/hypermodern-python/)" is a multi-part guide to setting up a Python project using what was, in 2020-2021, the most modern available tooling. The title is a reference to a 1920s avant-garde movement and signals the intent: opinionated, up-to-date, not the conventional wisdom. The series covers environment management, packaging, testing, linting, and CI.

The specific tools: pyenv for Python version management, Poetry for dependency management and packaging (replacing `setup.py` + `requirements.txt`), Nox for test automation across multiple Python versions, flake8 + Black + isort for code formatting and linting, pytest for testing, and GitHub Actions for CI. Pre-commit hooks run linters before each commit to catch issues early.

From a 2026 perspective, this guide represents a transitional moment in Python tooling. The tools it recommends were the best available then, but the ecosystem has since shifted: Ruff replaced flake8/isort/Black with a single fast Rust-based linter-formatter, and uv largely replaced pyenv + Poetry for environment and dependency management. The conceptual structure Jolowicz describes — separate concerns for env management, dependency pinning, testing, and linting — remains sound even as the specific tools evolved.

## Key points

- Recommended toolchain: pyenv + Poetry + Nox + Black + flake8 + pytest + GitHub Actions.
- Poetry manages dependencies and packaging in a single `pyproject.toml` — replaces `setup.py` and `requirements.txt`.
- Nox runs test suites against multiple Python versions in isolated environments.
- Pre-commit hooks enforce linting before commit — catches issues before CI.
- 2026 context: Ruff and uv have since superseded several of these tools while keeping the same structural philosophy.

[Original](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/) → GitHub
