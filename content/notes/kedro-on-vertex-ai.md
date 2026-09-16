---
title: Migrate Kedro Pipeline to Vertex AI
date: 2022-01-23
categories:
  - kedro
  - vertex-ai
  - mlops
  - data-pipelines
  - gcp
  - data-science
description: A walkthrough by Ivan Nardini on migrating a Kedro data science pipeline to run on Google Vertex AI Pipelines — covering the Kedro-Vertex plugin, pipeline conversion, and deployment. Shows how Kedro's portability story works in practice against a major cloud ML platform.
params:
  source: pinboard
  sourceUrl: https://medium.com/google-cloud/migrate-kedro-pipeline-on-vertex-ai-fa3f2c6f7aad
---

## Summary

This Google Cloud blog post by Ivan Nardini walks through migrating a Kedro data science pipeline to run on Google Vertex AI Pipelines — one of the managed ML workflow execution services that Kedro's portability story targets. It's a practical test of whether the write once, deploy anywhere promise holds up against a real cloud orchestration platform.

The migration path uses the Kedro-Vertex plugin (part of the broader kedro-plugins ecosystem) to translate Kedro pipeline definitions into Kubeflow Pipelines components that Vertex AI can execute. Kedro's pipeline abstraction — nodes as Python functions, data catalog for IO, explicit dependency graph — maps reasonably cleanly to Vertex AI's concept of pipeline components and artifacts.

The post covers: setting up the GCP project and enabling Vertex AI APIs, installing and configuring the Kedro-Vertex plugin, adapting the data catalog to use Google Cloud Storage (GCS) instead of local paths, compiling the pipeline to Kubeflow YAML, and submitting it to Vertex AI Pipelines. The migration is non-trivial but follows a clear pattern, which validates Kedro's design goal of making deployment environment changes require configuration changes rather than code rewrites.

## Key points

- Kedro-Vertex plugin translates Kedro pipelines to Kubeflow Pipelines components for Vertex AI execution.
- Data catalog adapts to cloud storage (GCS) — local paths swapped for GCS URIs, code unchanged.
- Pipeline compiles to Kubeflow YAML and submits to Vertex AI — same pipeline definition runs locally or in the cloud.
- Validates Kedro's portability story: environment change = config change, not code rewrite.
- Related: Ploomber offers similar multi-platform portability with a different configuration approach.

[Original](https://medium.com/google-cloud/migrate-kedro-pipeline-on-vertex-ai-fa3f2c6f7aad)
