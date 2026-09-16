---
title: "Kubernetes for MLOps: Scaling Enterprise Machine Learning, Deep Learning, and AI"
date: 2022-04-04
categories:
  - kubernetes
  - mlops
  - infrastructure
  - book
  - enterprise-ai
description: A book/transcript from the This Week in ML podcast by Sam Charrington on using Kubernetes as the operational backbone for enterprise ML workloads. Covers the full spectrum from containerized training jobs to model serving, making the case that Kubernetes is the de facto standard for scaling ML in production.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/[This Week in ML] Sam Charrington - Kubernetes for MLOps - Scaling Enterprise Machine Learning, Deep Learning, and AI - libgen.li.pdf
---

## Summary

Sam Charrington, host of the This Week in ML & AI podcast, presents a comprehensive guide to deploying and scaling machine learning workloads on Kubernetes. The book addresses the central operational challenge enterprise ML teams face: standard DevOps tooling doesn't account for the unique artifacts of ML systems — datasets, model weights, hyperparameter configurations, experiment lineage — and Kubernetes provides the extensible substrate to handle all of them uniformly.

The core argument is that Kubernetes acts as the neutral runtime for the entire MLOps stack. Whether you're running distributed training with PyTorch or TensorFlow, managing GPU allocation across a cluster, orchestrating pipelines with Kubeflow Pipelines, or serving models with KServe, Kubernetes provides the scheduling, networking, and resource management primitives that everything else builds on. Enterprise scale introduces multi-tenancy, cost accounting, and governance requirements that ad hoc compute setups can't satisfy.

The book covers the journey from local experimentation to production-grade infrastructure: packaging workloads as containers, writing Kubernetes manifests for ML jobs, leveraging Custom Resource Definitions (CRDs) to extend Kubernetes for ML-specific primitives like training jobs and model servers, and integrating with cloud-managed Kubernetes services. It sits alongside related works like [Effective Data Science Infrastructure](/notes/effective-data-science-infrastructure/) and the [AI Infrastructure Landscape Map](/notes/ai-infrastructure-landscape-map/) as part of the maturing MLOps engineering canon.

## Key points

- Kubernetes CRDs extend the platform to natively understand ML-specific resources: `TrainingJob`, `ModelServer`, `Pipeline`
- GPU scheduling and resource isolation are first-class concerns at enterprise scale — Kubernetes handles heterogeneous hardware uniformly
- Kubeflow is the primary ML-native layer on top of Kubernetes: covers pipelines, notebooks, hyperparameter tuning, and serving
- KServe provides model inference serving with canary deployments, autoscaling, and multi-framework support
- Multi-tenancy through Kubernetes namespaces and RBAC enables shared clusters without resource contention between teams
- The transition from DevOps to MLOps requires extending CI/CD to cover data versioning and model validation stages

[Original](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/%5BThis%20Week%20in%20ML%5D%20Sam%20Charrington%20-%20Kubernetes%20for%20MLOps%20-%20Scaling%20Enterprise%20Machine%20Learning%2C%20Deep%20Learning%2C%20and%20AI%20-%20libgen.li.pdf)
