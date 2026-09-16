---
title: Designing Cloud Data Platforms
date: 2022-04-04
categories:
  - cloud
  - data-platforms
  - data-engineering
  - book
  - manning
  - architecture
description: Manning textbook on building modern cloud data platforms covering ingestion, storage, processing, and serving layers across major providers. Practical guide for data engineers designing end-to-end pipelines that balance performance, cost, and operational complexity.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/Danil Zburivsky, Lynda Partner - Designing Cloud Data Platforms-Manning Publications (2021).pdf
---

## Summary

*[Designing Cloud Data Platforms](/notes/designing-cloud-data-platforms/)* by Danil Zburivsky and Lynda Partner (Manning, 2021) provides a comprehensive architecture guide for building data platforms on cloud infrastructure. The book takes a layered approach: data ingestion → storage → processing → serving, with each layer examined through the lens of the major providers (AWS, GCP, Azure).

A central theme is the trade-off between managed services and custom orchestration. The authors walk through when to use a fully managed data warehouse like BigQuery or Redshift versus assembling your own pipeline with Apache Spark, Kafka, and object storage. Their framework for evaluating these choices based on team size, latency requirements, and data volume is the most actionable part of the book.

The later chapters address data governance, metadata management, and the operational reality of running a platform at scale — including cost control, lineage tracking, and building for observability. These sections reflect the authors' experience that data platform failures are usually organizational, not technical.

## Key points

- Architecture pattern: every platform needs ingestion, storage, processing, and serving layers — and the book treats each as a separable design decision with multiple valid implementations
- Batch processing vs. stream processing trade-offs are covered in depth, with Apache Kafka and Apache Flink as the streaming exemplars
- Storage layer discussion spans data lakes (raw object storage), data warehouses (columnar analytical stores), and lakehouses (unified schemas over object storage)
- Data governance chapter covers data lineage, access control, and schema evolution — often the hardest part of scaling a platform past a single team
- Cloud provider comparison is honest about lock-in risk and shows how to design for portability where it matters

[Original document](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/Danil%20Zburivsky%2C%20Lynda%20Partner%20-%20Designing%20Cloud%20Data%20Platforms-Manning%20Publications%20(2021).pdf)
